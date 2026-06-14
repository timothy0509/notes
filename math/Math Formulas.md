---
tags:
  - math
  - reference
  - formulas
---

# Math Formulas

> [!abstract] Comprehensive categorized list of formulas from the HKDSE Mathematics curriculum.

---

## Compulsory Part

### Number and Algebra

#### Number Systems

$$i^1 = i, \quad i^2 = -1, \quad i^3 = -i, \quad i^4 = 1$$

$$\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}$$

#### Quadratic Equations

For $ax^2 + bx + c = 0$ ($a \neq 0$):

**Quadratic Formula**

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

**Discriminant**

$$\Delta = b^2 - 4ac$$

| $\Delta$ | Roots |
|----------|-------|
| $> 0$ | 2 distinct real roots |
| $= 0$ | 1 real root (repeated) |
| $< 0$ | 2 complex conjugate roots |

**Sum and Product of Roots** (roots $\alpha, \beta$):

$$\alpha + \beta = -\frac{b}{a}, \qquad \alpha\beta = \frac{c}{a}$$

**Forming equation from roots:**

$$(x-\alpha)(x-\beta) = 0 \implies x^2 - (\alpha+\beta)x + \alpha\beta = 0$$

#### Functions and Graphs

**Quadratic function:** $f(x) = ax^2 + bx + c$

- Axis of symmetry: $x = -\dfrac{b}{2a}$
- Vertex form: $y = a(x-h)^2 + k$, vertex at $(h,k)$
- $a > 0$: opens upward (minimum); $a < 0$: opens downward (maximum)

#### Exponential and Logarithmic Functions

**Laws of Indices:**

$$a^p \cdot a^q = a^{p+q}, \qquad \frac{a^p}{a^q} = a^{p-q}, \qquad (a^p)^q = a^{pq}$$

$$a^{\frac{m}{n}} = \sqrt[n]{a^m}, \qquad a^{-\frac{m}{n}} = \frac{1}{a^{m/n}}$$

$$a^p b^p = (ab)^p, \qquad \frac{a^p}{b^p} = \left(\frac{a}{b}\right)^p$$

**Logarithms:** $y = \log_a x \iff a^y = x \quad (a>0,\, a\neq1,\, x>0)$

$$\log_a MN = \log_a M + \log_a N, \qquad \log_a \frac{M}{N} = \log_a M - \log_a N$$

$$\log_a M^k = k\log_a M, \qquad \log_b N = \frac{\log_a N}{\log_a b}$$

**Applications:**

- Richter scale: $M = \log_{10}\dfrac{I}{I_0}$
- Decibels: $L = 10\log_{10}\dfrac{I}{I_0}$

#### More about Polynomials

**Division Algorithm:**

$$\text{Dividend} = \text{Divisor} \times \text{Quotient} + \text{Remainder}$$

**Remainder Theorem:** Remainder of $f(x) \div (mx - n)$ is $f\!\left(\dfrac{n}{m}\right)$

**Factor Theorem:** $f(a)=0 \iff (x-a)$ is a factor of $f(x)$

#### Variations

| Type | Formula |
|------|---------|
| Direct | $y = kx$ |
| Inverse | $y = \dfrac{k}{x}$ |
| Joint | $y = kxz$ |
| Partial | $y = a + bx$ |

#### Arithmetic and Geometric Sequences

**Arithmetic:**

$$T_n = a + (n-1)d, \qquad S_n = \frac{n}{2}[2a + (n-1)d] = \frac{n}{2}(a + \ell)$$

**Geometric:**

$$T_n = ar^{n-1}, \qquad S_n = \frac{a(1-r^n)}{1-r} \;\; (r \neq 1), \qquad S_\infty = \frac{a}{1-r} \;\; (|r|<1)$$

#### Inequalities

- Quadratic: $(x-\alpha)(x-\beta)$ positive outside roots, negative between
- Linear programming: Maximise/minimise $P = ax + by$ subject to constraints

#### Graphs of Functions — Transformations of $y=f(x)$

| Transformation | Formula |
|----------------|---------|
| Vertical shift (up $k$) | $f(x) + k$ |
| Horizontal shift (left $k$) | $f(x+k)$ |
| Vertical scale (factor $k$) | $kf(x)$ |
| Horizontal scale (factor $1/k$) | $f(kx)$ |

---

### Measures, Shape and Space

#### Equations of Straight Lines

$$y - y_1 = m(x - x_1) \qquad \text{(point-slope)}$$

$$y = mx + c \qquad \text{(slope-intercept)}$$

$$\frac{y - y_1}{y_2 - y_1} = \frac{x - x_1}{x_2 - x_1} \qquad \text{(two-point)}$$

$$Ax + By + C = 0 \qquad \text{(general form)}$$

From general form: $\;m = -\dfrac{A}{B}$, $\;\text{x-intercept} = -\dfrac{C}{A}$, $\;\text{y-intercept} = -\dfrac{C}{B}$, $\;m = \tan\theta$

#### Basic Properties of Circles

- Centre–chord: perpendicular from centre bisects the chord
- Angle at centre = $2 \times$ angle at circumference (same arc)
- Angle in semicircle = $90^\circ$
- Cyclic quadrilateral: opposite angles sum to $180^\circ$
- Tangent $\perp$ radius at point of contact
- Two tangents from external point are equal in length
- Alternate segment theorem: angle between tangent and chord = angle in alternate segment

#### Equations of Circles

$$(x-h)^2 + (y-k)^2 = r^2 \qquad \text{(standard form)}$$

$$x^2 + y^2 + Dx + Ey + F = 0 \qquad \text{(general form)}$$

From general form: $\;\text{centre} = \left(-\dfrac{D}{2}, -\dfrac{E}{2}\right)$, $\;r = \sqrt{\left(\dfrac{D}{2}\right)^2 + \left(\dfrac{E}{2}\right)^2 - F}$

#### Loci

| Condition | Locus |
|-----------|-------|
| Distance $r$ from point $P$ | Circle, centre $P$, radius $r$ |
| Equidistant from $A$ and $B$ | Perpendicular bisector of $AB$ |
| Distance $d$ from line $L$ | Two lines parallel to $L$ at distance $d$ |
| Equidistant from two intersecting lines | Two angle bisectors |

#### More about Trigonometry

**Identities:**

$$\sin(-\theta) = -\sin\theta, \quad \cos(-\theta) = \cos\theta, \quad \tan(-\theta) = -\tan\theta$$

$$\sin(90^\circ - \theta) = \cos\theta, \quad \cos(90^\circ - \theta) = \sin\theta$$

$$\sin(180^\circ - \theta) = \sin\theta, \quad \cos(180^\circ - \theta) = -\cos\theta$$

**Sine Rule:**

$$\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} = 2R$$

**Cosine Rule:**

$$a^2 = b^2 + c^2 - 2bc\cos A, \qquad \cos A = \frac{b^2 + c^2 - a^2}{2bc}$$

**Area of Triangle:**

$$\text{Area} = \frac{1}{2}ab\sin C$$

**Heron's Formula:**

$$\text{Area} = \sqrt{s(s-a)(s-b)(s-c)}, \quad s = \frac{a+b+c}{2}$$

---

### Data Handling

#### Permutations and Combinations

$$P^n_r = \frac{n!}{(n-r)!}, \qquad C^n_r = \binom{n}{r} = \frac{n!}{r!(n-r)!}$$

$$P^n_r = r! \times C^n_r$$

#### Probability

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

$$P(A') = 1 - P(A), \qquad P(A \cap B) = P(A) \times P(B) \;\;\text{(independent)}$$

$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$

#### Measures of Dispersion

$$\sigma = \sqrt{\frac{\sum f_i(x_i - \mu)^2}{\sum f_i}}, \qquad z = \frac{x - \mu}{\sigma}$$

**Empirical rule (normal):** $\approx 68\%$ within $\mu \pm \sigma$, $\approx 95\%$ within $\mu \pm 2\sigma$, $\approx 99.7\%$ within $\mu \pm 3\sigma$

#### Further Applications

- Ptolemy's theorem (cyclic quad $ABCD$): $AC \cdot BD = AB \cdot CD + AD \cdot BC$
- Fibonacci sequence: $1, 1, 2, 3, 5, 8, 13, \ldots$
- Golden ratio: $\phi = \dfrac{1+\sqrt{5}}{2} \approx 1.618$
- Ceva's theorem: $\dfrac{AF}{FB}\cdot\dfrac{BD}{DC}\cdot\dfrac{CE}{EA} = 1$ (concurrent cevians)

---

## Extended Part

### Module 1 — Calculus and Statistics

#### Binomial Expansion

$$(a+b)^n = \sum_{k=0}^n \binom{n}{k} a^{n-k} b^k, \qquad \binom{n}{k} = \frac{n!}{k!(n-k)!}$$

$$(1+x)^n = \sum_{k=0}^n \binom{n}{k} x^k$$

#### Exponential Functions

$$e = \lim_{n\to\infty}\left(1+\frac{1}{n}\right)^n \approx 2.71828$$

$$e^x = \sum_{n=0}^\infty \frac{x^n}{n!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots$$

**Growth/decay:** $N(t) = N_0 e^{kt}$; **Half-life:** $t_{1/2} = \dfrac{\ln 2}{|k|}$

#### Differentiation

**Definition:**

$$f'(x) = \lim_{h\to 0}\frac{f(x+h)-f(x)}{h}$$

**Rules:**

| Function | Derivative |
|----------|------------|
| $C$ | $0$ |
| $x^n$ | $nx^{n-1}$ |
| $e^x$ | $e^x$ |
| $a^x$ | $a^x \ln a$ |
| $\ln x$ | $\dfrac{1}{x}$ |
| $\sin x$ | $\cos x$ |
| $\cos x$ | $-\sin x$ |
| $\tan x$ | $\sec^2 x$ |

**Product rule:** $(uv)' = u'v + uv'$

**Quotient rule:** $\left(\dfrac{u}{v}\right)' = \dfrac{u'v - uv'}{v^2}$

**Chain rule:** $\dfrac{dy}{dx} = \dfrac{dy}{du}\cdot\dfrac{du}{dx}$

#### Integration

$$\int x^n\,dx = \frac{x^{n+1}}{n+1}+C \;\;(n\neq-1), \qquad \int \frac{1}{x}\,dx = \ln|x|+C, \qquad \int e^x\,dx = e^x+C$$

$$\int \sin x\,dx = -\cos x+C, \qquad \int \cos x\,dx = \sin x+C, \qquad \int \sec^2 x\,dx = \tan x+C$$

**Substitution:** $\int f(g(x))\,g'(x)\,dx = \int f(u)\,du$

**Inverse trig results:**

$$\int \frac{1}{\sqrt{a^2-x^2}}\,dx = \sin^{-1}\frac{x}{a}+C, \qquad \int \frac{1}{x^2+a^2}\,dx = \frac{1}{a}\tan^{-1}\frac{x}{a}+C$$

**Integration by parts:** $\int u\,dv = uv - \int v\,du$

#### Definite Integration

$$\int_a^b f(x)\,dx = F(b)-F(a)$$

**Properties:** $\int_a^a = 0$; $\int_a^b = -\int_b^a$; $\int_{-a}^a = 0$ (odd) or $2\int_0^a$ (even)

#### Trapezoidal Rule

$$\int_a^b f(x)\,dx \approx \frac{h}{2}\big[f(x_0) + 2f(x_1) + \cdots + 2f(x_{n-1}) + f(x_n)\big], \quad h=\frac{b-a}{n}$$

#### Probability Distributions

**Binomial:** $X \sim B(n,p)$

$$P(X=k) = \binom{n}{k}p^k(1-p)^{n-k}, \quad E[X]=np, \quad \text{Var}(X)=np(1-p)$$

**Poisson:** $X \sim \text{Poisson}(\lambda)$

$$P(X=k) = \frac{e^{-\lambda}\lambda^k}{k!}, \quad E[X]=\lambda, \quad \text{Var}(X)=\lambda$$

**Poisson approximation:** $B(n,p) \approx \text{Poisson}(\lambda=np)$ when $n\ge50$, $p\le0.1$

#### Normal Distribution

$$X \sim N(\mu,\sigma^2), \qquad Z = \frac{X-\mu}{\sigma} \sim N(0,1)$$

**Confidence intervals** (95%): $\bar{x} \pm 1.96\dfrac{\sigma}{\sqrt{n}}$

#### Conditional Probability & Bayes

$$P(A|B) = \frac{P(A\cap B)}{P(B)}, \qquad P(B_i|A) = \frac{P(A|B_i)\,P(B_i)}{\sum_j P(A|B_j)\,P(B_j)}$$

#### Expectation and Variance

$$E[X] = \sum x\,P(X=x), \qquad \text{Var}(X) = E[X^2]-(E[X])^2$$

$$E[aX+b] = aE[X]+b, \qquad \text{Var}(aX+b) = a^2\text{Var}(X)$$

---

## Related

- [[Math References]] — External references and further reading
- [[Math Index]] — Mathematics Map of Content
