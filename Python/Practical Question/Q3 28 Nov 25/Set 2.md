# 🟦 **SET – 2 (Python Practical Question – Medium Logic)**

## **📝 Q1. Transform Product Prices (Filtering + Logic + Dictionary Work)**

You are given a dictionary of products and their prices:

```python
products = {
    "Pen": 12,
    "Notebook": 55,
    "Bag": 480,
    "Bottle": 150,
    "File": 35,
    "Pouch": 90
}
```

### **Task**

Write a Python program to:

1. Create a new dictionary containing only those products whose price is:

   * **Greater than 40**, and
   * **A multiple of 5**
2. For each selected product, **increase its price by 10%** (multiply by 1.10).
3. Store the updated rounded value (no decimals) in the new dictionary.
4. Print this final dictionary.

### **Expected Output Example**

```
{'Notebook': 61, 'Bag': 528, 'Bottle': 165, 'Pouch': 99}
```

### **Logic Hints**

* Use modulus (`%`) to check multiples of 5
* Multiply by 1.10 for increase
* Use `round()` to avoid decimals
* Build a new dictionary, don't modify the old one

---
[🔗Upload Here](https://edunetfoundationorg-my.sharepoint.com/:f:/g/personal/mala_edunetfoundation_org/IgCo4UVPMrg_TLWbBZq8i8m0AYlx7KYjYNihU1Ah-Eq_WrI?e=WyiyBb)