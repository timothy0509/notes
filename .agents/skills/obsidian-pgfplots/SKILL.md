---
name: obsidian-pgfplots
description: "Plotting data and functions in Obsidian notes with pgfplots inside ```tikz code blocks (TikZJax plugin). Use when the user wants line plots, bar charts, scatter plots, histograms, 3D surfaces, or any scientific/data plot in a .md note."
---

# pgfplots in Obsidian (TikZJax plugin)

This vault renders `pgfplots` with the **obsidian-tikzjax** plugin (WASM TeX, `standalone`
class preloaded) inside ```tikz code blocks. See the **obsidian-tikz** skill for the
general block rules; read the hard rules below before writing any block.

## Block template

````latex
```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{document}
\begin{tikzpicture}
\begin{axis}[
  xlabel={$x$}, ylabel={$f(x)$}, title={My Plot},
  grid=major, samples=60,
]
  \addplot[blue, thick, domain=-3:3] {x^2};
  \addlegendentry{$x^2$}
\end{axis}
\end{tikzpicture}
\end{document}
```
````

## Obsidian-specific rules

| Rule | Why |
|------|-----|
| `\usepackage{pgfplots}` + `\pgfplotsset{compat=1.16}` at the top, before `\begin{document}` | pgfplots is on the plugin's supported-package list; always declare `compat` |
| **NEVER write `\documentclass`** | The block crashes (broken image icon) |
| `\begin{document}` and `\end{document}` required | Full LaTeX run inside WASM |
| **Inline all data** | No filesystem access — `\addplot table {data.csv}` and any external file fails. Use inline `coordinates` or a row-separated inline `table`. |
| Keep `samples` modest (≤ 100; 3D ≤ 30) | The WASM engine is much slower than local pdfLaTeX |
| `\addplot table {data.csv}` | |
| pgfplots libraries (`fillbetween`, `statistics`, `groupplots`, `polar`) are part of pgfplots and loadable via `\usepgfplotslibrary{...}` | |
| Verify the render | A broken-image icon means a compile error; change nothing blind — check the developer console (`TikZJax: Rendering input:`) for the TeX error |

Inline data without a file:

```latex
\addplot coordinates {(1,2) (2,4) (3,9)};
% or table syntax with row separator:
\addplot table[row sep=\\, x=Time, y=Temp] { Time Temp \\ 1 20 \\ 2 40 \\ };
```

## Axis environments

| Environment | Description |
|-------------|-------------|
| `axis` | Standard linear axes |
| `semilogxaxis` / `semilogyaxis` | Log scale on one axis |
| `loglogaxis` | Log on both |
| `polaraxis` | Polar (needs `\usepgfplotslibrary{polar}`) |
| `groupplot` | Grid of plots (needs `groupplots`) |

## Key axis options

`xlabel`/`ylabel`, `title`, `xmin/xmax/ymin/ymax`, `domain`, `samples`, `grid=major`,
`legend pos`, `axis lines=middle|box|left|none`, `enlargelimits`, `xtick={0,1,...,5}`,
`xticklabels={A,B,C}`, `width`/`height`, `nodes near coords`, `restrict y to domain=-10:10`.

## Plot types (inline data)

### Line plot

```latex
\begin{axis}[domain=0:2*pi, samples=60, grid=major, legend pos=south west]
  \addplot[blue, thick] {sin(deg(x))};
  \addplot[red, thick, dashed] {cos(deg(x))};
  \legend{$\sin(x)$, $\cos(x)$}
\end{axis}
```

### Coordinates plot

```latex
\begin{axis}[xlabel=Year, ylabel=Value]
  \addplot coordinates {(2018,10) (2019,15) (2020,12) (2021,20)};
\end{axis}
```

### Scatter

```latex
\begin{axis}[only marks]
  \addplot[mark=*, blue] coordinates {(1,2) (2,3.5) (3,2.8) (4,5.1)};
\end{axis}
```

### Bar chart

```latex
\begin{axis}[ybar, symbolic x coords={A,B,C,D}, xtick=data,
  ylabel={Count}, nodes near coords, bar width=15pt]
  \addplot coordinates {(A,20) (B,35) (C,30) (D,15)};
  \addplot coordinates {(A,25) (B,20) (C,40) (D,10)};
\end{axis}
```

### Histogram / box plot (statistics library)

```latex
\usepgfplotslibrary{statistics}
\begin{axis}[ybar interval]
  \addplot+[hist={bins=10, data min=0, data max=100}]
    coordinates {(0,3) (10,7) (20,5) ...};  % inline values
\end{axis}
```

### Fill between

```latex
\usepgfplotslibrary{fillbetween}
\begin{axis}
  \addplot[name path=upper, blue, thick, domain=0:4] {x^2};
  \addplot[name path=lower, red, thick, domain=0:4] {x};
  \addplot[fill=blue!10] fill between[of=upper and lower];
\end{axis}
```
This is also the VAT/supply-shift "surplus area" trick for Economics diagrams.

### 3D surface

```latex
\begin{axis}[view={45}{30}, colormap/viridis]
  \addplot3[surf, domain=-2:2, domain y=-2:2, samples=25] {exp(-x^2-y^2)};
\end{axis}
```

### Polar

```latex
\usepgfplotslibrary{polar}
\begin{polaraxis}
  \addplot[domain=0:360, samples=60, thick] {1 + cos(x)};
\end{polaraxis}
```

## Annotations

```latex
\begin{axis}
  \addplot[blue, thick, domain=0:5] {x^2};
  \node[pin=60:{Maximum}] at (axis cs:4,16) {};
  \draw[->, thick] (axis cs:2,10) -- (axis cs:3,9) node[above] {Note};
  \draw[dashed, gray] (axis cs:2.5,0) -- (axis cs:2.5,25);
\end{axis}
```

## Marks

`*`, `o`, `square`, `square*`, `triangle`, `triangle*`, `diamond*`, `x`, `+`, `star`, `none` —
e.g. `\addplot+[mark=triangle*, mark size=3pt] ...;`

## Pitfalls

| Problem | Cause | Fix |
|---------|-------|-----|
| Broken image icon | `\documentclass`, missing `\begin{document}`, unsupported feature | Check console error; follow the block template |
| `\addlegend` errors | Wrong command name | It is **`\addlegendentry{...}`**, must directly follow its `\addplot` |
| "Dimension too large" | Large values/domain | Reduce domain, `restrict y to domain` |
| Trig wrong | pgfplots trig is in degrees | `sin(deg(x))` for radians |
| Bars overlap | Multiple bar plots same x | `ybar` handles offset automatically; ensure `xtick=data` |
| Legend misplaced | Default top-right | `legend pos=north west` (or south east, ...) |
| External-file plot fails | No filesystem in WASM | Inline the data instead |
| Very slow/frozen render | Too many samples or huge inline datasets | Cut `samples`, trim data points |
| Stale diagram after edit | Cached SVG keyed on source | Blocks re-render when content changes; if stuck, reload the note |
