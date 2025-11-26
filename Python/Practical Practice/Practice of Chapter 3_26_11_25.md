# 🟦 **OOP Practice Questions for Python**

---

## **📝 Q1: Create a Simple Class**

Create a class **`Car`** with attributes:

* `brand`
* `model`
* `year`

Create an object and print all details.

---

## **📝 Q2: Class with Methods**

Create a class **`Rectangle`** that has:

* Attributes: `length`, `width`
* Methods:

  * `area()` → returns area
  * `perimeter()` → returns perimeter

Create an object and display area and perimeter.

---

## **📝 Q3: Using Constructor**

Create a class **`Student`** with:

* Constructor accepting `name`, `age`, `marks`
* Method `display()` to print details

Create two objects and call the method.

---

## **📝 Q4: Inheritance (Single Level)**

Create a class **`Animal`** with method:

* `sound()`: prints `"Animals make sounds"`

Create a child class **`Dog`** that overrides `sound()` to print `"Bark"`.

Create objects of both classes and call the `sound()` method.

---

## **📝 Q5: Multilevel Inheritance**

Create three classes:

* `LivingBeing`
* `Animal` (child of LivingBeing)
* `Dog` (child of Animal)

Each should have a method that prints something.
Create an object of `Dog` and call all inherited methods.

---

## **📝 Q6: Encapsulation (Private Attributes)**

Create a class **`BankAccount`** with:

* Private attribute `__balance`
* Constructor to initialize balance
* Method `deposit(amount)`
* Method `withdraw(amount)`
* Method `show_balance()`

Demonstrate access control.

---

## **📝 Q7: Polymorphism (Method Overriding)**

Create two classes:

* `Shape` → method `area()` (prints generic message)
* `Circle` → overrides `area()` to compute πr²

Create objects and call `area()` on both.

---

## **📝 Q8: Polymorphism (Duck Typing)**

Create two classes:

* `Cat` with method `sound()` printing `"Meow"`
* `Cow` with method `sound()` printing `"Moo"`

Write a function that takes any object and calls `sound()`.

---

## **📝 Q9: Class with Class Variable**

Create a class **`Employee`** with:

* Class variable `company = "ABC Ltd"`
* Instance attributes: name, salary
* Method `details()` that prints everything

Create objects and show that the company name is shared.

---

## **📝 Q10: Static Method**

Create a class **`MathOps`** with:

* Static method `add(a, b)` that returns a + b
* Static method `multiply(a, b)` that returns a × b

Call these methods without creating objects.

---

## **📝 Q11: Operator Overloading**

Create a class **`Book`** that stores:

* `pages`

Overload the `+` operator so:

```python
b1 + b2
```

returns total pages.

---

## **📝 Q12: Multiple Objects Interaction**

Create two classes:

* `Product` with attributes name and price
* `Cart` with method `add_product(product)` and `total_price()`

Add 3 products to cart and print total price.

Here are **3 additional OOP practice questions** — simple, clear, and perfect for trainees.

---


## **📝 Q13: Using Property Decorators (Getters & Setters)**

Create a class **`Temperature`** with:

* Private attribute `__celsius`
* Getter method to return Celsius
* Setter method to update Celsius (but raise ValueError if less than -273)

Also add a method:
`to_fahrenheit()` → returns temperature in Fahrenheit.

Create an object and test all methods.

---

## **📝 Q14: Composition (HAS–A relationship)**

Create two classes:

**Class:** `Engine`

* Method: `start()` prints `"Engine started"`

**Class:** `Car`

* Has an `Engine` object inside it
* Method: `run()` calls the engine's start method and prints `"Car is running"`

Create a Car object and call `run()`.

---

## **📝 Q15: Abstract Class (Using abc Module)**

Using the `abc` module:

1. Create an abstract class **`Shape`** with an abstract method `area()`.
2. Create two subclasses:

   * `Rectangle` (length, width)
   * `Circle` (radius)
3. Implement the area method for both.

Create objects and print their areas.

---