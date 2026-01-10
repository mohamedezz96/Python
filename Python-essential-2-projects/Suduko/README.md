# 🧩 Sudoku Validator (LAB 2.5.11)

## 📌 Description

Sudoku is a number-placement puzzle played on a **9×9 grid**.  
A completed Sudoku board is considered **valid** if:

- Each **row** contains all digits from **1 to 9** exactly once.
- Each **column** contains all digits from **1 to 9** exactly once.
- Each **3×3 sub-square** contains all digits from **1 to 9** exactly once.

The order of digits does **not** matter — only uniqueness.

---

## 🎯 Objective

Write a Python program that:

1. Reads **9 rows**, each containing **9 digits**.
2. Validates the Sudoku board according to the rules above.
3. Prints:
   - `Yes` → if the Sudoku is valid
   - `No` → if the Sudoku is invalid

---

## 🧠 Solution Approach

The program works as follows:

1. **Read input rows** into a list.
2. **Generate columns** by collecting characters at the same index from each row.
3. **Generate 3×3 sub-squares** by iterating in steps of 3.
4. **Validate** each row, column, and sub-square by:
   - Sorting the digits
   - Comparing them to `"123456789"`

---

## 🧪 Test Data

### ✅ Valid Sudoku

**Input:**
295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672

**Output:**
Yes


---

### ❌ Invalid Sudoku

**Input:**

195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671

**Output:**
No
