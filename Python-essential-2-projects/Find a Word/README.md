# LAB 2.5.10 – Find a Word!

## 📌 Description

In this lab, you will write a program that checks whether a given word is hidden inside another string.  
The letters of the word must appear **in the same order**, but they do **not** need to be consecutive.

---

## 🎯 Task Requirements

Your program should:

- Ask the user to enter a **word**
- Ask the user to enter a **string of characters**
- Check whether the characters of the word appear inside the second string **in order**
- Print **Yes** if the word is found
- Print **No** if the word is not found

---

## 🧠 Rules & Notes

- The comparison is **case-insensitive**
- Characters must appear **in sequence**
- Characters do **not** have to be adjacent
- Spaces and extra characters in the second string are allowed
- Use string search methods such as `find()` or `pos()` with a starting index
- An empty word should be treated as **not found**

---

## 🧪 Test Data

### Sample Input 1
Yes

### Explanation  
The letters **d → o → n → o → r** appear in the second string in the same order.

---

### Sample Input 2
No

### Explanation  
The letters **d → o → n → u → t** do not appear in the correct order in the second string.

---

## ✅ Expected Output

- Print **Yes** if the word is hidden in the string
- Print **No** otherwise

---

## 🏁 Conclusion

This task helps practice:

- String traversal
- Case-insensitive comparison
- Sequential character searching
- Logical problem solving

Good luck 🚀
