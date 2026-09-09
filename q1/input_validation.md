# Input Validation and Output Verification
**Activity:** PSHS Workshop Registration Validator
**Name:** Shiery Nicole L. Aranel
**Section:** 8-Dahlia
**Quarter:** 1
---
## Activity Overview
In this activity, I created a program that validates information entered into a PSHS workshop registration
system.
The program checks whether user input satisfies specific requirements before accepting the registration.
The program validates:
- student name
- age
- grade level
- email address and
- registration code.

---
# Part A - Validation Requirements
| Data Captured | Expected Input | Validation Type | Invalid Input Example | Validation Rule | Error
Message |
|---|---|---|---|---|---|
| Student Name | text | Presence check | (blank) | The input must not be blank or empty | "REGISTRATION NOT ACCEPTED" "Student name is required." |
| Age | Integer from 11 to 18 | Range check| 23 | The input must be an integer from 11 to 18 | "REGISTRATION NOT ACCEPTED" "Age must be from 11 to 18" |
| Grade Level | (7, 8, 9, 10, 11, 12) | Range check | 5 | The input must be either 7, 8, 9, 10, 11, or 12 | "REGISTRATION NOT ACCEPTED" "Invalid Grade Level" |
| Email Address | Standard email format containing “@” and “.” | Format check | Zizibrc.pshs/Zizi@brcpshs | The input must include both “@” and “.” | "REGISTRATION NOT ACCEPTED" "Invalid email" |
| Registration Code | 6 Characters | Length check | ZZ4 | The input must be exactly 6 characters | "REGISTRATION NOT ACCEPTED" "The registration code must contain exactly 6 characters." |
---
## Validation Questions
### 1. Why should the student name not be blank?
> The student name should not be blank because the name is needed for proper identification of the user.
### 2. Why should age be checked for both data type and range?
> 
### 3. Why should grade level only accept specific values?
> Write your answer here.
### 4. What format requirements did you use for the email address?
> Write your answer here.
### 5. What length requirement did you use for the registration code?
> Write your answer here.
---
# Part B - Program Design
## Flowchart
![Workshop Validator Flowchart](workshop_validator_flowchart.png)

``
Your design should show:
- user input
- validation decisions
- error messages
- accepted registration
- rejected registration.
---
# Part C - Program Implementatio
## Programming Language
> Write the programming language used.
## Source Code File
[`workshop_validator.py`](workshop_validator.py)
## Final Code
```python
# Paste your final code here.
```

---
## Validation Techniques Used
### Presence Validation
Explain where you used presence validation.
> Write your answer here.
### Data Type Validation
Explain where you used data type validation.
> Write your answer here.
### Range Validation
Explain where you used range validation.
> Write your answer here.

### Acceptable Value Validation
Explain where you used acceptable value validation.
> Write your answer here.
### Pattern Validation
Explain the simple pattern rule you used.
> Write your answer here.
### Length Validation
Explain the length rule you used.
> Write your answer here.
---
# Part D - Testing
Test your program using both valid and invalid inputs.
| Test | Input / Condition | Validation Being Tested | Expected Output | Actual Output | Result |
|---:|---|---|---|---|---|
| 1 | All inputs valid | Normal case | | | |
| 2 | Blank student name | Presence | | | |
| 3 | Age = `fourteen` | Data type | | | |
| 4 | Age = `11` | Minimum boundary | | | |
| 5 | Age = `18` | Maximum boundary | | | |
| 6 | Age = `10` | Range | | | |
| 7 | Grade Level = `13` | Acceptable value | | | |
| 8 | Email = `studentpshs.edu.ph` | Pattern | | | |
| 9 | Registration Code = `ABC` | Length | | | |
| 10 | Registration Code = `CS2026` | Valid length | | | |
Write **PASS** when the actual output matches the expected output.
Write **FAIL** when it does not.
---
# Part E - Output Verification
Choose any **three tests** from Part D.
## Verification Test 1
**Input:**
```text
Write the input here.

```
**Expected Output:**
```text
Write the expected output here.
```
**Actual Output:**
```text
Write the actual output here.
```
**Result:** PASS / FAIL
**Explanation:**
> Explain why the output is correct or incorrect.
---
## Verification Test 2
**Input:**
```text
Write the input here.
```
**Expected Output:**
```text
Write the expected output here.
```
**Actual Output:**
```text
Write the actual output here.
```
**Result:** PASS / FAIL
**Explanation:**
> Explain why the output is correct or incorrect.
---
## Verification Test 3
**Input:**
```text
Write the input here.
```
**Expected Output:**
```text
Write the expected output here.
```
**Actual Output:**

```text
Write the actual output here.
```
**Result:** PASS / FAIL
**Explanation:**
> Explain why the output is correct or incorrect.
---
# Reflection
### 1. Why should a program validate input before processing it?
> Write your answer here.
### 2. What is the difference between input validation and output verification?
> Write your answer here.
### 3. Which validation technique was easiest for you to implement? Why?
> Write your answer here.
### 4. Which validation technique was most challenging? Why?
> Write your answer here.
### 5. How did testing invalid inputs help you improve your program?
> Write your answer here.
---
# Files for This Activity
- [`workshop_validator.py`](workshop_validator.py)
- `input_validation.md`
- `workshop_validator_flowchart.png` if a flowchart was used
---

>[README.md](README.md)
