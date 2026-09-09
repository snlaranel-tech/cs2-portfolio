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
<img width="523" height="326" alt="Screenshot 2026-09-09 210700" src="https://github.com/user-attachments/assets/a81c219c-cae1-4f5b-b006-313126274693" />

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
## Pseudocode
// Global variable
is_valid = True

FUNCTION print_error(message)
    is_valid = False
    PRINT "\n----------------------------"
    PRINT "REGISTRATION NOT ACCEPTED"
    PRINT message
    PRINT "------------------------------"
END FUNCTION

// Name validation

name = TRIM(INPUT("Enter student name: "))

IF name == "" THEN
    print_error("Student name is required.")
    
END IF

// Age validation

age_input = TRIM(INPUT("Enter student age: "))

age = TO_INTEGER(age_input)

IF age < 11 OR age > 18 THEN
    print_error("Age must be from 11 to 18")
    
END IF

// Grade level validation
TRY
    grade_level = TO_INTEGER(TRIM(INPUT("Enter student grade level: ")))
    IF grade_level < 7 OR grade_level > 12 THEN
        print_error("Invalid Grade Level")
    END IF
CATCH ValueError
    print_error("Grade level must be a valid number.")
END TRY

// Email validation
email = INPUT("Enter student email:")
IF NOT ("@" IN email AND "." IN email) THEN
    print_error("Invalid email")
END IF

// Registration code validation
regis_code = TRIM(INPUT("Enter workshop registration code: "))
IF LENGTH(regis_code) != 6 THEN
    print_error("The registration code must contain exactly 6 characters.")
END IF

// Final status check
IF is_valid == True THEN
    PRINT "\n------------------------------"
    PRINT "REGISTRATION ACCEPTED!!"
    PRINT "------------------------------"
    PRINT "Student: " + name
    PRINT "Age: " + age
    PRINT "Grade Level: " + grade_level
    PRINT "Email: " + email
    PRINT "Registration Code: " + regis_code
END IF

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
