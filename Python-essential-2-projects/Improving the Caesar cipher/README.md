# Improving the Caesar Cipher

## Lab 2.5.6

This project implements an improved version of the classic **Caesar cipher** encryption technique.  
Unlike the original Caesar cipher which shifts characters by only one position, this version allows the user to specify a **shift value between 1 and 25**.

The program preserves the case of letters and leaves all non-alphabetic characters unchanged.

---

## Problem Description

The Caesar cipher is a simple encryption method where each letter in the plaintext is replaced by a letter a fixed number of positions down the alphabet.

This lab enhances the original Caesar cipher by:
- Allowing a variable shift value
- Preserving uppercase and lowercase letters
- Ignoring non-alphabetic characters such as spaces, numbers, and symbols

---

## Program Requirements

The program must:

1. Ask the user to enter one line of text to encrypt
2. Ask the user to enter a shift value (integer between 1 and 25)
3. Validate the shift value and force correct input
4. Encrypt the text using the Caesar cipher rules
5. Display the encrypted text

---

## Encryption Rules

- Lowercase letters (`a–z`) remain lowercase after encryption
- Uppercase letters (`A–Z`) remain uppercase after encryption
- Alphabet wrap-around is handled correctly (`z → a`, `Z → A`)
- Non-alphabetic characters remain unchanged

---

## Input and Output

### Input
- A string containing the text to encrypt
- An integer shift value between 1 and 25

### Output
- The encrypted version of the input text

---
