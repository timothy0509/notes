---
name: obsidian-tikz
description: "Drawing TikZ diagrams in Obsidian notes (.md files) using the ```tikz code block and the TikZJax plugin. Use whenever the user wants a diagram — flowchart, graph, plot, supply/demand curve, timeline, state machine, geometric figure — in an Obsidian note."
---

# TikZ diagrams in Obsidian (TikZJax plugin)

This vault renders TikZ with the **obsidian-tikzjax** plugin (v0.5.2), which compiles a
bundled WASM build of TeX inside Obsidian. No local LaTeX installation is involved, and
the bundled format **preloads the `standalone` document class internally**.

## The one true block template

Always emit this skeleton (fenced with "tikz"):

````latex
```tikz
\begin{document}
\begin{tikzpicture}[scale=0.8]
  % content here
\end{tikzpicture}
\end{document}
```
````

## Hard rules (violation = broken image icon in the note)

| Rule | Why |
|------|-----|
| **NEVER write `\documentclass{}...`** | The WASM core cannot load class files; it crashes and the plugin swaps in a broken `<img src='//invalid.site/img-not-found.png'/>`. |
| **Always include `\begin{document}` and `\end{document}`** | The input is fed to a full LaTeX run; without them it fails. |
| Packages come from a fixed list only | Supported: `chemfig`, `tikz-cd`, `circuitikz`, `pgfplots`, `array`, `amsmath`/`amstext`, `amsfonts`/`amssymb`, `tikz-3dplot`. Anything else fails to compile. |
| `\usetikzlibrary{...}` inside the block is fine | TikZ libraries (arrows.meta, positioning, calc, shapes.geometric, decorations, patterns, automata, trees, mindmap, ...) are bundled. |
| **No external files** | No `\input`, `\include`, `\includegraphics`, no data-file reading (`\addplot table {file.csv}`), no `\tikzexternalize`/`--shell-escape`. Inline all data. |
| Inline all define-and-use | Every diagram is compiled independently; each block needs its own `\usepackage` / `\usetikzlibrary` / `\tikzset`. |

## Failure mode & debugging

- Compile failure ⇒ plugin replaces the diagram with a broken-image icon (or shows the
  raw loader spinner stuck). It does **not** show the error inline.
- Successful renders are cached (keyed on the source hash), so **edit the source or add a
  whitespace/comment change to force a re-render** of a previously failed block.
- For real diagnostics: Ctrl+Shift+I (developer console) — the plugin logs
  `TikZJax: Rendering input:` followed by the exact LaTeX and the TeX error.

## Colors & dark mode

The plugin's *Invert colors in dark mode* setting (on by default) rewrites `"black"`/`"#000"`
→ `currentColor` and `"white"`/`"#fff"` → the theme background at render time. So:

- Default black strokes/labels adapt automatically to dark theme. Prefer leaving commonly
  used lines black and using explicit colors (blue, red, ...) only where the color is pedagogically meaningful.
- Named colors like `red`, `blue`, `gray` render as-is in both themes.

---

## Quick reference (works inside ```tikz blocks)

### Path operations

| Operation | Syntax | Example |
|-----------|--------|---------|
| Line | `--` | `(0,0) -- (1,1)` |
| Right then up | `-|` | `(0,0) -| (1,1)` |
| Up then right | `|-` | `(0,0) |- (1,1)` |
| Curve | `.. controls ..` | `(0,0) .. controls (0.5,1) .. (1,0)` |
| Smooth | `to[out=..,in=..]` | `(0,0) to[out=90,in=180] (2,1)` |
| Arc | `arc` | `(0,0) arc (0:90:1)` |
| Circle | `circle` | `\draw (0,0) circle (1);` |
| Rectangle | `rectangle` | `(0,0) rectangle (2,1)` |
| Plot | `plot` | `\draw plot[domain=0:3] (\x, {\x^2});` |
| Close | `cycle` | `-- cycle` |

### Actions & options

- `\draw` stroke, `\fill` fill, `\filldraw` both, `\node`, `\coordinate`, `\clip`, `\shade`.
- Line style: `thick`, `very thick`, `dashed`, `dotted`, `rounded corners=5pt`, `opacity=0.5`, `->`, `-Stealth`.
- Fill: `fill=blue!20` (20% blue), `pattern=north east lines` (needs `patterns` library).

### Coordinates

```latex
(2,3)                      % cartesian
(45:2)                     % polar: angle:radius
\coordinate (A) at (1,2);  % named
($(A)!0.5!(B)$)            % midpoint (needs calc)
($(A)!1cm!(B)$)            % 1cm from A toward B
(A |- B)                   % (x of A, y of B) — great for axis guides
++(1,0)                    % relative, moves reference point
```

### Nodes

```latex
\node[draw, circle, fill=blue!20, minimum size=8mm] (a) at (0,2) {A};
\draw[->] (a) -- node[above] {label} (b);              % label on path
\draw[dashed] (5,5) -- (5,0) node[below] {$Q^*$};      % math positions
```
Anchors: `north west|north|north east|west|east|south west|south|south east`, plus pos along path (`node[pos=0.3, below]`).

### Arrows

```latex
\usetikzlibrary{arrows.meta}
\draw[->] (0,0) -- (1,0);         % default
\draw[-Stealth] ...;              % filled triangle
\draw[-{Stealth[length=4pt]}] ...;
% >=Stealth (or arrows.meta) in picture options sets the default tip
```

### Styles

```latex
\begin{tikzpicture}[
  block/.style={draw, rectangle, fill=blue!10, minimum width=2cm},
  arrow/.style={thick, -Stealth},
  every node/.style={font=\small},
]
```

### foreach

```latex
\foreach \x/\label in {1/Long-run, 2/Short-run}
  \node at (\x,0) {\label};
\foreach \x [count=\i] in {a,b,c} ...
```

### positioning library

```latex
\usetikzlibrary{positioning}
\node[right=of A] (B) {B};
\node[above right=1cm and 2cm of A] (C) {C};  % never hardcode layout coords
```

---

## Pattern library

### Supply & demand / econ diagram (matches vault Economics notes)

````latex
```tikz
\begin{document}
\begin{tikzpicture}[scale=0.8]
  \draw[->] (0,0) -- (10,0) node[below right] {$Q$ (Quantity)};
  \draw[->] (0,0) -- (0,10) node[above] {$P$ (Price)};
  \draw[thick,blue]  (1,9) -- (9,1) node[below left]  {Demand};
  \draw[thick,red]   (1,1) -- (9,9) node[above right] {Supply};
  \draw[dashed] (5,5) -- (5,0) node[below] {$Q^*$};
  \draw[dashed] (5,5) -- (0,5) node[left]  {$P^*$};
  \fill (5,5) circle (2.5pt) node[above right] {$E$};
\end{tikzpicture}
\end{document}
```
````

(To show a shift, add e.g. `\draw[thick,red!60,dashed] (2,1) -- (10,9) node[above right] {Supply$_2$};` and a second equilibrium point.)

### Flowchart

````latex
```tikz
\begin{document}
\usetikzlibrary{arrows.meta, shapes.geometric, positioning}
\begin{tikzpicture}[node distance=1.5cm,
  startstop/.style={rectangle, rounded corners, draw, fill=red!20, minimum width=2.5cm},
  process/.style={rectangle, draw, fill=blue!20, minimum width=2.5cm},
  decision/.style={diamond, draw, fill=green!20, aspect=1.5},
  arrow/.style={thick, -Stealth}]
  \node[startstop] (start) {Start};
  \node[process, below=of start] (a) {Step 1};
  \node[decision, below=of a] (dec) {Condition?};
  \node[process, below right=of dec] (yes) {Yes branch};
  \draw[arrow] (start) -- (a);
  \draw[arrow] (a) -- (dec);
  \draw[arrow] (dec.east) -| node[above, near start] {Yes} (yes);
\end{tikzpicture}
\end{document}
```
````

### Graph / network

````latex
```tikz
\begin{document}
\begin{tikzpicture}[vertex/.style={draw, circle, fill=blue!20, minimum size=8mm}, thick]
  \node[vertex] (a) at (0,2) {A};
  \node[vertex] (b) at (2,3) {B};
  \node[vertex] (c) at (4,2) {C};
  \draw (a) -- node[above] {3} (b) -- node[above right] {2} (c);
\end{tikzpicture}
\end{document}
```
````

### Timeline

````latex
```tikz
\begin{document}
\begin{tikzpicture}
  \draw[thick, -Stealth] (0,0) -- (10,0);
  \foreach \x/\year/\event in {1/Event A, 4/Event B, 7/Event C}{
    \draw (\x,-0.15) -- (\x,0.15);
    \node[below=3pt] at (\x,-0.15) {\footnotesize \event};
  }
\end{tikzpicture}
\end{document}
```
````

### State machine

````latex
```tikz
\begin{document}
\usetikzlibrary{automata, positioning}
\begin{tikzpicture}[shorten >=1pt, node distance=2.5cm, every state/.style={draw}]
  \node[state, initial] (q0) {$q_0$};
  \node[state, right=of q0] (q1) {$q_1$};
  \path[->] (q0) edge node {a} (q1)
            (q1) edge [loop above] node {b} ();
\end{tikzpicture}
\end{document}
```
````

### Plain plot (no pgfplots)

````latex
```tikz
\begin{document}
\begin{tikzpicture}[scale=0.9]
  \draw[->] (-0.5,0) -- (4.5,0) node[below] {$x$};
  \draw[->] (0,-0.5) -- (0,3.5) node[left] {$y$};
  \draw[blue, thick, domain=0:4, samples=50] plot (\x, {sqrt(\x)});
\end{tikzpicture}
\end{document}
```
````

For anything with axes + legends + bar charts, prefer pgfplots — see the **obsidian-pgfplots** skill.

---

## Pitfalls

| Problem | Cause | Fix |
|---------|-------|-----|
| Broken image icon | `\documentclass` in the block, unsupported package, or any TeX error | Remove `\documentclass`; check the package list; read the console error |
| Still broken after edit | Cached failure or identical content | Verify source differs from the failing version; restart Obsidian if it persists |
| Withdrawn/shifted curve invisible in dark mode | Light-gray colors | Use pure colors (blue, red) or default black — black auto-inverts |
| Unsupported package error | e.g. `! LaTeX Error: File 'foo.sty' not found` | Stick to the package allowlist |
| "Dimension too large" | Coordinates too big / huge function values | Use `scale`, smaller coords, or `restrict y to domain` (pgfplots) |
| Missing arrow tips | Forgot `arrows.meta` | `\usetikzlibrary{arrows.meta}` |
| Nodes overlap | Hardcoded coordinates | Use `positioning` library, `right=of ...` |
| foreach errors | Special characters in body | Wrap body in `{}` |

## Tips

- Keep diagrams simple for the WASM engine: a diagram a local pdfLaTeX compiles in 0.1s
  may take noticeably longer here. Keep `samples` ≤ 100 on plots.
- One `\tikzpicture` per block; multiple pictures in one block render but bloat the note editor.
- Titles/captions: no `\begin{figure}`/`\caption` support — put them in plain markdown text
  above or below the block.
- Verify: after writing a ```tikz block, confirm the note shows the rendered
  diagram — not the broken-image icon — before considering the task done.
