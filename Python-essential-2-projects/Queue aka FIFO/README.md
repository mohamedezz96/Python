# 3.2.9 LAB – Queue aka FIFO

## Lab Objective
This lab introduces the **Queue** data structure, which implements the **FIFO (First In – First Out)** model. Unlike a stack (LIFO), the first element added to the queue is the first one to be removed. This behavior is common in **lines at stores, print jobs, and task scheduling**.

You will implement a `Queue` class in Python with two main operations:

1. `put(element)` – adds an element to the end of the queue.
2. `get()` – removes and returns an element from the front of the queue.

You will also implement **exception handling** to prevent getting elements from an empty queue.

---

## Instructions
1. Use a **list** as the underlying storage for the queue.
2. Define the following methods:
   - `put(element)` – append elements to the **beginning** of the list.
   - `get()` – remove elements from the **end** of the list and return them.
3. Define a **custom exception** called `QueueError` that inherits from a built-in exception (e.g., `Exception` or `RuntimeError`).
4. Raise the `QueueError` if `get()` is called on an empty queue.
5. Test your queue by adding and removing elements, and verify proper behavior.

---

## Hints
- The queue is like a line in a store: the **first element added** is the **first element removed**.
- Use **list operations**:
  - `list.insert(0, value)` → insert at the **beginning**.
  - `list.pop()` → remove from the **end**.
- Implementing `QueueError` ensures that the program fails gracefully when trying to `get()` from an empty queue.

---
