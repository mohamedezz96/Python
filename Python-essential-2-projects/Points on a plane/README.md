# Cartesian Plane – Point Distance Calculator

## 📘 Lab Overview

This lab introduces **object-oriented programming** concepts by working with points on a **Cartesian coordinate plane**.  
Each point is represented by two coordinates `(x, y)`, and the goal is to calculate distances between points.

---

## 🎯 Objective

Create a `Point` class that:

- Stores Cartesian coordinates (`x`, `y`)
- Keeps all attributes **private**
- Allows distance calculation between points
- Uses object methods to access private data

---

## 📐 Mathematical Background

The distance between two points on a plane is calculated using the Euclidean distance formula:

\[
\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
\]

Python provides `math.hypot(dx, dy)` to compute this efficiently.

---

## 🧩 Requirements

### Class Design

- Class name: `Point`
- Constructor arguments:
  - `x` (default `0.0`)
  - `y` (default `0.0`)
- All properties must be **private**
- Provide accessor methods:
  - `getx()`
  - `gety()`

---

### Distance Methods

- `distance_from_xy(x, y)`
  - Calculates the distance from the current point to a coordinate pair
- `distance_from_point(point)`
  - Calculates the distance to another `Point` object

---
