# 3.2.8 LAB – Counting Stack

## Lab Objective
The goal of this lab is to extend the functionality of a **Stack** class by creating a subclass that counts the number of `pop` operations performed. This will help you practice **inheritance**, **encapsulation**, and **method overriding** in Python's object-oriented programming (OOP) approach.

---

## Instructions
1. Use the `Stack` class provided as a base class.
2. Create a new subclass named `CountingStack`.
3. Introduce a **private property** to count the number of times `pop()` is called.
4. Initialize this counter to `0` in the constructor (`__init__`).
5. Provide a method `get_counter()` that **returns the current value** of the counter.
6. Override the `pop()` method so that each pop increments the counter.

---

## Hints
- Use **double underscores** before the counter name to make it private (e.g., `self.__counter`).
- Remember to call the superclass constructor to initialize the stack list.
- Don’t forget to **return the popped value** from your overridden `pop()` method.
- Test your class by pushing and popping values to see if the counter works correctly.

---

## Example Python Code

```python
# Base Stack class
class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


# Subclass CountingStack
class CountingStack(Stack):
    def __init__(self):
        super().__init__()   # Call superclass constructor
        self.__counter = 0   # Private counter for pop operations

    def pop(self):
        val = super().pop()  # Call the original pop method
        self.__counter += 1  # Increment the counter
        return val            # Return the popped value

    def get_counter(self):
        return self.__counter  # Return current pop count


# Testing the CountingStack
stk = CountingStack()

# Push and pop 100 elements
for i in range(100):
    stk.push(i)
    stk.pop()

# Display the number of pop operations
print(stk.get_counter())  # Output: 100
