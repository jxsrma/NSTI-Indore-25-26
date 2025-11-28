# 🟦 **SET – 1 (Python Practical Question – Medium Logic)**

## **📝 Q1. Filter, Group, and Count Names**

You are given a list of names:

```python
names = ["Aditi", "Aman", "Simran", "Saurabh", "Riya", "Rohan", "Isha", "Ishaan", "Reema"]
```

### **Task**

Write a Python program to:

1. Create a new list containing only names that **start with the same first letter** as their last letter.
   Example: "Aditi" → starts with A, ends with i → **does not match**
   But "Ishi" → starts with I, ends with i → **match**

2. From the filtered list, create a dictionary where:

   * The **key** is the starting letter
   * The **value** is the **count of names** starting with that letter

3. Print the dictionary.

### **Expected Output Example**

```
{'I': 2, 'R': 1}
```

### **Logic Hints**

* Use indexing: `name[0]` and `name[-1]`
* You must check matching letters (case-insensitive)
* Build a dictionary dynamically

---

[🔗Upload Here](https://edunetfoundationorg-my.sharepoint.com/:f:/g/personal/mala_edunetfoundation_org/IgCo4UVPMrg_TLWbBZq8i8m0AYlx7KYjYNihU1Ah-Eq_WrI?e=WyiyBb)