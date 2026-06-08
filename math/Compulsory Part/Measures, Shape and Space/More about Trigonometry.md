---
tags:
  - math
  - compulsory-part
  - measures-shape-space
  - trigonometry
---

# More about Trigonometry

## Trigonometric Functions

For any angle $\theta$ ($0^\circ \leq \theta \leq 360^\circ$), $\sin\theta$, $\cos\theta$, $\tan\theta$ are defined using the unit circle or right-angled triangle ratios extended by reference angles.

### Simplification Identities

| Identity |
| -------- |
| $\sin(-\theta) = -\sin\theta$ |
| $\cos(-\theta) = \cos\theta$ |
| $\tan(-\theta) = -\tan\theta$ |
| $\sin(90^\circ - \theta) = \cos\theta$ |
| $\sin(90^\circ + \theta) = \cos\theta$ |
| $\cos(90^\circ - \theta) = \sin\theta$ |
| $\sin(180^\circ - \theta) = \sin\theta$ |
| $\cos(180^\circ - \theta) = -\cos\theta$ |

### Graphs and Properties

| Function | Domain | Range | Period | Max | Min |
| -------- | ------ | ----- | ------ | --- | --- |
| $y = \sin x$ | $\mathbb{R}$ | $[-1, 1]$ | $360^\circ$ | $1$ | $-1$ |
| $y = \cos x$ | $\mathbb{R}$ | $[-1, 1]$ | $360^\circ$ | $1$ | $-1$ |
| $y = \tan x$ | $x \neq 90^\circ + n \cdot 180^\circ$ | $\mathbb{R}$ | $180^\circ$ | — | — |

## Trigonometric Equations

Solve $a\sin\theta = b$, $a\cos\theta = b$, $a\tan\theta = b$ for $0^\circ \leq \theta \leq 360^\circ$.

1. Find the **reference angle** $\alpha$
2. Determine the quadrants based on the sign of the trigonometric ratio
3. Write all solutions in $[0^\circ, 360^\circ]$

Equations that can be transformed into quadratics are dealt with in [[Book 4A notes#Chapter 3: Quadratic Equations in One Unknown]].

## Area of Triangle

$$
\text{Area} = \frac{1}{2} ab \sin C
$$

where $a$ and $b$ are two sides and $C$ is the included angle.

## Sine Rule

$$
\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} = 2R
$$

where $R$ is the circumradius.

## Cosine Rule

$$
a^2 = b^2 + c^2 - 2bc \cos A
$$

or

$$
\cos A = \frac{b^2 + c^2 - a^2}{2bc}
$$

## Heron's Formula

$$
\text{Area} = \sqrt{s(s-a)(s-b)(s-c)}
$$

where $s = \frac{a+b+c}{2}$ (semi-perimeter).

## Projection

The projection of a point onto a plane or line is the foot of the perpendicular.

## Three-Dimensional Geometry

### Angle Between a Line and a Plane

The angle between a line and a plane is the angle between the line and its **projection** onto the plane.

### Angle Between Two Planes

The angle between two intersecting planes is the angle between their **lines of intersection** with a plane perpendicular to their line of intersection (the dihedral angle).

### Theorem of Three Perpendiculars

If a line $l$ in a plane is perpendicular to the projection of another line onto that plane, then $l$ is perpendicular to that line.

### 3D Problems

Finding in 3D contexts:
- Angle between two lines
- Angle between a line and a plane
- Angle between two planes
- Distance between two points
- Distance from a point to a line
- Distance from a point to a plane
