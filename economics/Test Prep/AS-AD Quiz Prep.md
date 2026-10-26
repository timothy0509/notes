---
tags:
  - economics
  - macroeconomics
  - test-prep
  - as-ad
  - fiscal-policy
  - monetary-policy
---

# AS-AD Quiz Prep

Quiz topics: AS-AD model in the short run and long run, plus government intervention in the AS-AD framework.

## One-page mental model

The three curves:

- **AD** slopes down. Reasons (in this order, all three needed): wealth effect, interest rate effect, exchange rate effect. Lower $P$ means higher $C$, higher $I$, higher $NX$.
- **SRAS** slopes up. Reasons: sticky wages, sticky prices, imperfect information.
- **LRAS** is vertical at $Y_f$. In the long run, wages and prices are fully flexible, so output depends only on real factors: labour, capital, technology.

Equilibrium: short run is where AD crosses SRAS ($Y_e$, $P_e$). Long run requires AD = SRAS = LRAS, so $Y_e = Y_f$.

Frequent trap: mixing up shift and slide. "SRAS $\leftarrow$" means the whole curve shifts up and left, giving higher $P$ at any $Y$; it does not mean movement along the curve.

## Short-run vs long-run for every AD shift

| Shock | Short run | Long run (self-correction) |
|-------|-----------|---------------------------|
| AD $\rightarrow$ (e.g. $G\uparrow$, exports boom) | $Y\uparrow$, $P\uparrow$ | Wages rise $\Rightarrow$ SRAS $\leftarrow$; $Y$ back to $Y_f$ at a permanently higher $P$ |
| AD $\leftarrow$ (e.g. $T\uparrow$ overseas recession) | $Y\downarrow$, $P\downarrow$ | Wages fall $\Rightarrow$ SRAS $\rightarrow$; $Y$ back to $Y_f$ at a permanently lower $P$ |

The key exam point: in the long run, AD shifts change only the price level, not real output. Real output changes only when LRAS moves. Write the adjustment in two steps: (1) nominal wages adjust because unemployment differs from the natural rate, (2) that shifts SRAS until it crosses both AD and LRAS at $Y_f$.

## Supply shocks and the two gaps

- Negative supply shock (oil price spike): SRAS $\leftarrow$, giving stagflation: $Y\downarrow$ and $P\uparrow$ at the same time. The long-run fix is a fall in expected prices or nominal wages, which restores SRAS, but the process is slow.
- Positive supply shock (technology): SRAS and LRAS both $\rightarrow$, $Y\uparrow$, $P\downarrow$. This is the only shock that gives sustained $Y\uparrow$ with $P$ stable or lower.

- **Recessionary (deflationary) gap**: $Y_e < Y_f$. High unemployment puts downward pressure on wages; SRAS $\rightarrow$ over time.
- **Inflationary gap**: $Y_e > Y_f$. Overheating pushes wages up; SRAS $\leftarrow$ over time.

Quick takeaway: whichever way the gap points, SRAS is what moves to close it if the government does nothing. Because that wage adjustment is slow, the government often steps in and shifts AD instead.

## Government intervention in the AS-AD model

Both policies work through AD in the short run.

| Policy | Direction | Chain of effects | Short-run result |
|--------|-----------|------------------|------------------|
| Expansionary fiscal ($G\uparrow$, $T\downarrow$) | AD $\rightarrow$ | Direct injection into AD (or via disposable income $\Rightarrow C\uparrow$) | $Y\uparrow$, $P\uparrow$; closes a recessionary gap |
| Contractionary fiscal ($G\downarrow$, $T\uparrow$) | AD $\leftarrow$ | Withdraws demand | $Y\downarrow$, $P\downarrow$; closes an inflationary gap |
| Expansionary monetary ($M_s\uparrow$) | AD $\rightarrow$ | $i\downarrow \Rightarrow I\uparrow, C\uparrow$ | $Y\uparrow$, $P\uparrow$ |
| Contractionary monetary ($M_s\downarrow$) | AD $\leftarrow$ | $i\uparrow \Rightarrow I\downarrow, C\downarrow$ | $Y\downarrow$, $P\downarrow$ |

Comparison lines worth memorising:

- Discretionary fiscal policy changes $G$ or $T$ deliberately; automatic stabilisers (progressive taxes, welfare payments) do the same job with no decision needed.
- Monetary policy works with only an interest rate channel and has a shorter implementation lag than fiscal policy (no budget approval needed).
- Crowding out: expansionary fiscal policy raises $i$, cutting private $I$, so some stimulus is offset. Monetary expansion does not have this problem; arguably it does the opposite.
- In Hong Kong, fiscal policy is the real tool: the currency board pegs the HKD to USD, so the HKMA has no independent monetary policy and HK rates follow US rates (see [[Money and Banking]]).

One judgment call exam questions like: intervention trades a faster return to $Y_f$ for a permanently different $P$. Closing a recessionary gap by expansionary policy keeps $P$ higher than it would have been after pure self-correction (which would restore $Y$ via SRAS $\rightarrow$ and a lower $P$ instead).

## Diagrams to be able to draw from memory

Every point marked with a dot sits exactly on its curves; dashed grey lines drop to the axes so you can read off $Y$ and $P$ labels. If a rendering fails to load, sketch by hand from the description under each figure.

**1. Long-run equilibrium.** AD, SRAS and LRAS all intersect at one point, so $Y_e = Y_f$.

```tikz
\begin{document}
\tikzset{every picture/.style={line width=0.6pt}}
\begin{tikzpicture}[scale=0.9]
  \draw[->] (0,0) -- (6,0) node[right] {$Y$};
  \draw[->] (0,0) -- (0,5) node[above] {$P$};
  \draw[dashed,black] (3.0,0) -- (3.0,4.8) node[above] {LRAS};
  \draw[thick,blue] (0.5,4.85) -- (5.5,0.35) node[right] {AD};
  \draw[thick,red] (0.7,0.3) -- (5.2,4.8) node[right] {SRAS};
  \fill (3.0,2.6) circle (2pt);
  \draw[dashed,gray] (0,2.6) -- (3.0,2.6) node[midway,left] {$P_e$};
  \draw (3.0,0) node[below] {$Y_f$};
\end{tikzpicture}
\end{document}
```

**2. Recessionary gap and self-correction.** AD and SRAS$_1$ cross left of LRAS ($Y_e < Y_f$). Unemployment above the natural rate pushes wages down, so SRAS shifts right until AD crosses both SRAS$_2$ and LRAS at $Y_f$, with a lower $P$ than before.

```tikz
\begin{document}
\begin{tikzpicture}[scale=0.9]
  \draw[->] (0,0) -- (6,0) node[right] {$Y$};
  \draw[->] (0,0) -- (0,4.5) node[above] {$P$};
  \draw[dashed,black] (3.6,0) -- (3.6,4.3) node[above] {LRAS};
  \draw[thick,blue] (0.3,3.63) -- (5.5,1.38) node[right] {AD};
  \draw[thick,red] (0.5,0.08) -- (4.4,5.02) node[right] {SRAS$_1$};
  \draw[thick,purple] (2.0,0.12) -- (4.6,3.5) node[right] {SRAS$_2$};
  \draw[->,red,thick] (3.25,3.4) -- node[above,black] {wages $\downarrow$} (4.45,3.4);
  \fill (2.54,2.66) circle (2pt) node[below left] {A};
  \fill (3.6,2.2) circle (2pt) node[below right] {B};
  \draw[dashed,gray] (0,2.66) -- node[midway,left] {$P_1$} (2.54,2.66);
  \draw[dashed,gray] (0,2.2) -- node[midway,left] {$P_2$} (3.6,2.2);
  \draw[dashed,gray] (2.54,0) -- (2.54,2.66);
  \draw (2.54,0) node[below] {$Y_e$};
  \draw (3.6,0) node[below] {$Y_f$};
\end{tikzpicture}
\end{document}
```

At A: $Y_e < Y_f$, recessionary gap. Falling wages move SRAS$_1$ to SRAS$_2$; at B the economy is back at $Y_f$ with a lower price level $P_2 < P_1$.

**3. Inflationary gap and self-correction.** Equilibrium right of LRAS ($Y_e > Y_f$). Overheating pushes wages up, so SRAS shifts left back to $Y_f$ at a higher $P$.

```tikz
\begin{document}
\begin{tikzpicture}[scale=0.9]
  \draw[->] (0,0) -- (6,0) node[right] {$Y$};
  \draw[->] (0,0) -- (0,5) node[above] {$P$};
  \draw[dashed,black] (2.4,0) -- (2.4,4.9) node[above] {LRAS};
  \draw[thick,blue] (0.6,4.7) -- (5.8,0.1) node[right] {AD};
  \draw[thick,red] (1.6,0.12) -- (5.0,4.38) node[right] {SRAS$_1$};
  \draw[thick,purple] (0.7,0.98) -- (4.3,5.02) node[left] {SRAS$_2$};
  \draw[->,red,thick] (4.3,3.7) -- node[above,black] {wages $\uparrow$} (3.0,3.7);
  \fill (3.33,2.29) circle (2pt) node[below right] {A};
  \fill (2.51,3.01) circle (2pt) node[below left] {B};
  \draw[dashed,gray] (0,2.29) -- node[midway,left] {$P_1$} (3.33,2.29);
  \draw[dashed,gray] (0,3.01) -- node[midway,left] {$P_2$} (2.51,3.01);
  \draw[dashed,gray] (3.33,0) -- (3.33,2.29);
  \draw (3.33,0) node[below] {$Y_e$};
  \draw (2.51,0) node[below] {$Y_f$};
\end{tikzpicture}
\end{document}
```

**4. Negative supply shock (stagflation).** SRAS alone shifts left: $Y$ falls while $P$ rises at the same time. LRAS does not move, so this is a short-run phenomenon until wages and expected prices adjust.

```tikz
\begin{document}
\begin{tikzpicture}[scale=0.9]
  \draw[->] (0,0) -- (6,0) node[right] {$Y$};
  \draw[->] (0,0) -- (0,5.5) node[above] {$P$};
  \draw[dashed,black] (3.2,0) -- (3.2,5.2) node[above] {LRAS};
  \draw[thick,blue] (0.5,4.89) -- (5.5,1.0) node[right] {AD};
  \draw[thick,red] (1.55,0.71) -- (4.8,4.92) node[right] {SRAS$_1$};
  \draw[thick,purple] (1.15,0.8) -- (3.62,4.82) node[right] {SRAS$_2$};
  \draw[->,red,thick] (3.6,3.2) -- node[above,black] {oil price $\uparrow$} (2.5,3.2);
  \fill (3.17,2.81) circle (2pt) node[below left] {A};
  \fill (2.64,3.23) circle (2pt) node[below right] {B};
  \draw[dashed,gray] (0,2.81) -- node[midway,left] {$P_1$} (3.17,2.81);
  \draw[dashed,gray] (0,3.23) -- node[midway,left] {$P_2$} (2.64,3.23);
  \draw[dashed,gray] (3.17,0) node[below] {$Y_1$} -- (3.17,2.81);
  \draw[dashed,gray] (2.64,0) node[below] {$Y_2$} -- (2.64,3.23);
\end{tikzpicture}
\end{document}
```

At A: long-run equilibrium. The oil spike moves SRAS$_1$ to SRAS$_2$; at B, $Y_2 < Y_1$ but $P_2 > P_1$ at the same time: stagflation. Self-correction needs wages and expected prices to fall, which is slow; SRAS$_2$ drifts back right over time.

**5. Expansionary intervention vs doing nothing.** Closing a recessionary gap with fiscal or monetary expansion shifts AD right: the short run lands directly on $Y_f$ at B. Pure self-correction would instead have shifted SRAS right and landed at C, also on $Y_f$ but at a lower price level.

```tikz
\begin{document}
\begin{tikzpicture}[scale=0.9]
  \draw[->] (0,0) -- (6,0) node[right] {$Y$};
  \draw[->] (0,0) -- (0,5.5) node[above] {$P$};
  \draw[dashed,black] (3.6,0) -- (3.6,5.2) node[above] {LRAS};
  \draw[thick,blue] (0.2,3.97) -- (4.6,1.05) node[right] {AD$_1$};
  \draw[thick,teal] (2.1,5.44) -- (5.6,3.13) node[right] {AD$_2$};
  \draw[thick,red] (0.9,0.94) -- (3.95,4.9) node[left] {SRAS};
  \draw[->,teal,thick] (1.0,3.5) -- node[above,black] {$G\uparrow$ or $M_s\uparrow$} (4.9,3.5);
  \fill (2.21,2.64) circle (2pt) node[below left] {A};
  \fill (3.6,4.45) circle (2pt) node[above] {B};
  \fill (3.6,1.71) circle (2pt) node[right] {C};
  \draw[thick,purple!70] (2.4,0.15) -- (4.4,2.75) node[right] {SRAS$_2$};
  \draw[dashed,gray] (0,2.64) -- node[midway,left] {$P_1$} (2.21,2.64);
  \draw[dashed,gray] (0,4.45) -- node[midway,left] {$P_2$} (3.6,4.45);
  \draw[dashed,gray] (0,1.71) -- node[midway,left] {$P_3$} (3.6,1.71);
  \draw[dashed,gray] (2.21,0) -- (2.21,2.64);
  \draw (2.21,0) node[below] {$Y_e$};
  \draw (3.6,0) node[below] {$Y_f$};
\end{tikzpicture}
\end{document}
```

A: recessionary gap. The policy shift to AD$_2$ reaches $Y_f$ at B, price $P_2$. Doing nothing would instead shift SRAS right and land at C, price $P_3 < P_2$. Same $Y_f$, permanently different price level: that is the trade in one picture and the core judgment in Q1c.

## Practice questions

**Q1.** The economy is at long-run equilibrium. A sudden rise in oil prices hits the country.
a) State the short-run effects on $Y$ and $P$, with a diagram.
b) Explain how the economy returns to $Y_f$ if the government does nothing.
c) Why might the government prefer to act instead of waiting?

**A1.**
a) SRAS shifts left. $Y\downarrow$, $P\uparrow$: stagflation. Diagram: LRAS vertical at $Y_f$; SRAS shifts left through it; new equilibrium left of $Y_f$ with higher $P$.
b) Unemployment above the natural rate puts downward pressure on nominal wages and expected prices. Lower wages shift SRAS right until it passes through AD and LRAS at $Y_f$, at a lower $P$ than before.
c) The self-correction requires nominal wages to fall, which takes a long time and hurts workers. Expansionary AD policy (fiscal $G\uparrow$ or monetary $M_s\uparrow$) restores $Y$ much faster, at the price of a permanently higher $P$. It also avoids prolonged unemployment's output losses.

**Q2.** Expansionary fiscal policy restores full employment "permanently". Criticise this claim using the long run.

**A2.** It only works if the gap existed to begin with. If the economy is already at $Y_f$, the AD increase creates an inflationary gap: $Y\uparrow$ to above $Y_f$ in the short run only. Wages then rise, SRAS shifts left, and $Y$ returns to $Y_f$ at a higher $P$. Long-run output is unchanged; only prices changed. Crowding out weakens the short-run gain too.

**Q3.** Why is the AD curve downward sloping, and why is its micro demand-curve explanation wrong?

**A3.** Three aggregate channels: lower $P$ raises real money holdings (wealth effect), lowers money demand and interest rates (interest rate effect), and lowers $i$, depreciating the currency and raising $NX$ (exchange rate effect). The micro explanation fails because when $P$ falls, all prices fall, so no single firm gains relative demand shifts; the substitution logic only works for one good's price, not the whole price level.

**Q4.** For each, decide: does it shift AD, SRAS, LRAS, or several?
a) a cut in the profits tax
b) a rise in the minimum wage
c) a fall in the money supply
d) an improvement in technology
e) expectations of higher future prices forming now

**A4.**
a) LRAS and SRAS right (more incentive to invest, capital stock grows); higher $I$ also shifts AD right in the short run.
b) SRAS left only. A statutory wage floor is a labour cost change that hits any $P$; it does not change potential output directly.
c) AD left. Money supply is a shift factor of the interest rate channel, not of supply.
d) Both SRAS and LRAS right.
e) SRAS left only. Expectations are long-run-neutral; nothing real changes until they come true.

**Q5.** Hong Kong case: exports collapse in a global recession.
a) Which curve moves, and which way?
b) Name the type of gap created.
c) Which government intervention fits here, fiscal or monetary, and why?

**A5.**
a) AD shifts left: lower $NX$.
b) Recessionary (deflationary) gap: $Y_e < Y_f$.
c) Fiscal policy is the practical choice. Under the linked exchange rate, expansionary monetary policy is off the table: HKMA rates must shadow the Fed's rates even in a global recession (when the rule would call for easing), so fiscal expansion is the tool that works on $Y$ without breaking the peg.

## Final pre-quiz checklist

- Can I state all three reasons AD slopes down and all three reasons SRAS slopes up?
- Can I explain why LRAS is vertical at $Y_f$?
- Can I trace an AD shift through short run, wage adjustment, long run, without skipping a step?
- Can I draw all five diagrams above in under a minute each?
- Do I know which curve each shock hits, including the "expectations of prices" case?
- Can I argue fiscal vs monetary with a Hong Kong-specific point?

Related notes: [[National Income Determination and Price Level]], [[Macroeconomic Problems and Policies]], [[Microeconomics Test Prep]], [[Economics Index]]
