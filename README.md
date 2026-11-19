# Python Programming Assignment 01

Solutions to Assignment 01 of *Fundamentals of Python Programming*. The programs apply data types, string operations, Boolean logic, comparison operators, conditional statements, lists and tuples.

## Files

| File | Topic |
|------|-------|
| `Q1.py` | Username validation (strings and conditions) |
| `Q2.py` | Student marks analysis (lists, tuples, data types) |
| `Q3.py` | Online shopping discount eligibility (Boolean logic and conditions) |

## Requirements

- Python 3.6 or later
- No external libraries

## How to run

Open a terminal in the project folder and run any file:

```bash
python Q1.py
python Q2.py
python Q3.py
```

On some systems the command is `python3` instead of `python`.

---

## Q1: Username Validation System

Reads a username with `input()` and checks it against three rules:

1. It must contain at least 5 characters.
2. It must not contain only spaces.
3. It must not be `admin`, ignoring uppercase and lowercase.

If a rule fails, the program prints "Invalid username" with the reason. Otherwise it prints "Valid username".

**Test results**

| Input | Output |
|-------|--------|
| `Anjali123` | Valid username |
| `abc` | Invalid: fewer than 5 characters |
| `" "` (a space) | Invalid: only spaces |
| `ADMIN` | Invalid: reserved name |

## Q2: Student Marks Analysis

Uses the sample data `[78, 35, 92, 40, 61]` and:

- converts the list to a tuple and prints both with their data types
- finds the highest and lowest marks with `max()` and `min()`
- counts students who scored at least 40 by adding Boolean comparisons (no loops)
- checks that all marks are within 0 to 100 and prints the Boolean result
- shows that a list is mutable while a tuple is immutable (explained in a comment in the code)

**Output**

```
Highest mark: 92
Lowest mark : 35
Students who scored at least 40: 4
All marks within 0-100: True
```

## Q3: Online Shopping Discount Eligibility

Reads the order amount and membership status (`yes` or `no`, any case) and applies these rules:

- An amount below ₹0 or above ₹1,00,000 is invalid.
- An amount of ₹5,000 or more gets a 15% discount.
- A member with an amount of ₹2,000 or more but below ₹5,000 gets a 10% discount.
- All other orders get no discount.

The program prints the original amount, discount amount, final payable amount and eligibility status.

**Test results**

| Amount | Member | Discount | Final payable |
|--------|--------|----------|---------------|
| ₹6,000 | no | 15% | ₹5,100.00 |
| ₹3,000 | yes | 10% | ₹2,700.00 |
| ₹1,500 | no | 0% | ₹1,500.00 |
| ₹1,00,001 | yes | Invalid amount | n/a |

## Concepts used

- `input()`, `print()`, `len()`, `max()`, `min()`, `type()`
- String methods: `strip()`, `lower()`
- Comparison operators and Boolean expressions (`and`, `or`, `not`)
- `if / elif / else` statements
- Lists, tuples, and mutable vs immutable behavior
