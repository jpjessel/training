# Python Training Modules

Welcome to the Python training repository! These modules are designed to help you write cleaner, more maintainable, and more Pythonic code.

---

## Session 1: Core Principles & Code Structure

### 1. Single Responsibility Principle (SRP)

> "A class should have one, and only one, reason to change." – SOLID Principle

Each class or module should focus on a single task. Keeping responsibilities separate improves maintainability and testability.

---

### 2. DRY Code – *Don't Repeat Yourself*

> Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.

Avoid code duplication. Reuse logic through functions, classes, or shared modules to reduce errors and improve consistency.

---

### 3. KISS – *Keep It Simple, Stupid*

> Simpler is better than complex. Complex is better than complicated. – Zen of Python

Don't over-engineer. Solve problems with the simplest, cleanest solution that works.

---

### 4. Decorators

Decorators let you dynamically extend or modify the behavior of functions without changing their actual code.

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
def greet(name):
    print(f"Hello, {name}!")
```

### 5. Types 

Python is dynamically typed, but using type hints improves clarity and reduces bugs.
```python
def add(a: int, b: int) -> int:
    return a + b
```

Type annotations also help tools like linters and IDEs give better suggestions.

You can also annotate variables:
```python
age: int = 30
name: str = "Alice"
```

Use the typing module for more complex types:

```python
from typing import List, Dict

def process_items(items: List[str]) -> Dict[str, int]:
    return {item: len(item) for item in items}
```
## 6. Modules and Classes
Split your codebase into smaller modules and classes to:

- Improve readability

- Enable reusability

- Make testing easier

Example Project Structure:
```cs
project/
├── main.py
├── utils/
│   └── string_helpers.py
├── models/
│   └── user.py
```
**Example Class**:
```python
class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def greet(self) -> str:
        return f"Hi, I'm {self.name}!"
```