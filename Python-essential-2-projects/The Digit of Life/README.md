# The Digit of Life Calculator

## Lab 2.5.9

This project calculates the **Digit of Life** from a user's birthday.  
The Digit of Life is obtained by summing all the digits of the birth date repeatedly until only a single digit remains.  

**Example:**
- Birthday: 1 January 2017 → 20170101  
- Step 1: 2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12  
- Step 2: 1 + 2 = 3  
- The Digit of Life: 3

---

## Problem Description

The program should:

1. Ask the user to enter their birthday as a numeric string (examples: YYYYMMDD, YYYYDDMM, MMDDYYYY – the order does not matter)
2. Sum all digits of the entered date
3. If the sum has more than one digit, repeat the sum until a **single-digit number** is obtained
4. Output the Digit of Life

**Notes:**
- Input must contain only digits
- The program should work for any valid birthday input length

---

## Input and Output

### Input
- A numeric string representing a birth date

### Output
- The single-digit Digit of Life

---

## Test Cases

### Sample Input 1
19991229

### Sample Output 1
6
