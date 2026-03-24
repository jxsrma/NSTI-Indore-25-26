# 🟦 **Python Practice Questions — File Handling + Exception Handling**

---

## **📄 Question 1: File Read & Count Words**

Write a Python program that:

1. Opens the file **`notes.txt`** (assume it already exists).
2. Reads its content.
3. Counts how many words are in the file.
4. Handles exceptions if the file is **missing** using `try-except`.

---

## **📄 Question 2: Write Student Marks to a File**

You are given a list:

```python
marks = [78, 85, 92, 66, 89]
```

Write a program that:

1. Creates a file **`marks.txt`**
2. Writes each mark on a new line
3. Uses a `try-except` block to catch file writing errors
4. Uses `finally` to print:
   `"File operation completed"`

---

## **📄 Question 3: Append Log Entries**

Create a program that:

1. Opens **`log.txt`** in append mode
2. Adds 5 log entries like:
   `"Log entry 1"`
   `"Log entry 2"`
3. Use `try-except` to handle any error
4. Ensure the file is closed using `finally`

---

## **📄 Question 4: Read Numbers & Handle Conversion Error**

Create a file named **`numbers.txt`** containing:

```
10
20
abc
30
```

Write a program that:

1. Reads lines from the file
2. Converts each line into an integer
3. Handles **ValueError** when “abc” is encountered
4. Skips invalid data and continues processing

Expected output example:

```
Valid number: 10
Valid number: 20
Invalid line: abc
Valid number: 30
```

---

## **📄 Question 5: Copy File Content**

Write a program that:

1. Reads content from **`source.txt`**
2. Writes it into **`backup.txt`**
3. If the source file is missing, catch the exception and print:
   `"Source file not found!"`

---

# 🟥 **Custom Exception Question**

## **📝 Question 6 (Custom Exception): Age Validation**

Create a custom exception class named **`InvalidAgeError`**.

Write a program that:

1. Has a list of ages:

   ```python
   ages = [21, 15, 34, 10, 28]
   ```
2. For each age, check if it is **18 or above**.
3. If not, **raise your custom exception** with message:
   `"Age below 18 is not allowed: <age>"`
4. Catch the custom exception and print the message.
5. Continue checking the rest of the ages.

Expected output example:

```
Valid age: 21
InvalidAgeError: Age below 18 is not allowed: 15
Valid age: 34
InvalidAgeError: Age below 18 is not allowed: 10
Valid age: 28
```

---