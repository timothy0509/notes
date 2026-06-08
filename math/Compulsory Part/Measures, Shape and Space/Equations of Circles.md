---
tags:
  - math
  - compulsory-part
  - measures-shape-space
  - coordinate-geometry
---

# Equations of Circles

## Standard Form

$$
(x - h)^2 + (y - k)^2 = r^2
$$

where $(h, k)$ is the centre and $r$ is the radius.

## General Form

$$
x^2 + y^2 + Dx + Ey + F = 0
$$

Complete the square to find centre and radius:
$$
\text{centre} = \left(-\frac{D}{2}, -\frac{E}{2}\right), \quad
r = \sqrt{\left(\frac{D}{2}\right)^2 + \left(\frac{E}{2}\right)^2 - F}
$$

## Features from Equation

Given a point $P(x_1, y_1)$ and a circle centre $C(h, k)$, radius $r$:

- $P$ is **inside** if $PC < r$
- $P$ is **on** the circle if $PC = r$
- $P$ is **outside** if $PC > r$

## Finding the Equation

| Given | Method |
| ----- | ------ |
| Centre $(h, k)$ and radius $r$ | Direct substitution into $(x-h)^2 + (y-k)^2 = r^2$ |
| Three points on the circle | Substitute each into general form, solve system of 3 equations |

## Intersection of Line and Circle

Solve the line equation and circle equation simultaneously. The discriminant $\Delta$ of the resulting quadratic determines:

- $\Delta > 0$ — two distinct intersection points (secant)
- $\Delta = 0$ — one intersection point (tangent)
- $\Delta < 0$ — no intersection

## Tangents to a Circle

To find the equation of a tangent:
- At a given point on the circle: use radius-tangent perpendicular property
- From an external point: solve using discriminant $\Delta = 0$

See also [[Basic Properties of Circles#Tangents to a Circle]].
