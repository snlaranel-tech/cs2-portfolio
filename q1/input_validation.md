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
<img width="434" height="273" alt="image" src="https://github.com/user-attachments/assets/090915f2-f2dc-4e04-8233-d6295e0c1ae9" />

---
## Validation Questions
### 1. Why should the student name not be blank?
> The student name should not be blank because the program needs to identify the student registering. A blank name means required information is missing.
### 2. Why should age be checked for both data type and range?
> Age should be checked for data type to make sure that the input is a valid integer. It should also be checked for range to make sure the age is from 11 to 18, which is the allowed age for the registration.
### 3. Why should grade level only accept specific values?
> Grade level should only accept specific values because entire program is intended for students in Grades 7 to 12. If the program accepted any other values, it could potentially allow students who do not meet the requirements to register.
### 4. What format requirements did you use for the email address?
> The format requirement for the email address must contain both an "@" symbol and a period "."
### 5. What length requirement did you use for the registration code?
> The registration code must contain exactly 6 characters.
---
# Part B - Program Design
## Pseudocode
START

SET is_valid to TRUE

DEFINE print_error(message)
    SET is_valid to FALSE
    DISPLAY "REGISTRATION NOT ACCEPTED"
    DISPLAY error message
END Define

Ask user to enter student name
Remove extra entered spaces
IF student name is blank 
THEN
    DISPLAY error message
END IF

Ask user to enter an age
TRY to convert age to an integer
    IF age is less than 11 OR greater than 18 
    THEN
        DISPLAY error message
    END IF
IF age is not a valid number 
THEN
    Display error message
END TRY

Ask user to enter a grade level
TRY to convert grade level to an integer
    IF grade level is less than 7 OR greater than 12 THEN
        DISPLAY error message
    END IF
IF grade level is not a valid number THEN
    DISPLAY error message
END TRY

Ask user to enter an email address
IF email does not contain "@" OR "." 
THEN
    DISPLAY error message
END IF

Ask user to enter a registration code
IF registration code does not contain exactly 6 characters 
THEN
    DISPLAY error message
END IF

IF is_valid is TRUE 
THEN
    DISPLAY "REGISTRATION ACCEPTED"
    DISPLAY student information
ELSE
    Registration is rejected
END IF

END

# Part C - Program Implementatio
## Programming Language
> Python
## Source Code File
[`workshop_validator.py`](workshop_validator.py)
## Final Code
```python

is_valid = True 

# Error message declaration
def print_error(message):
  global is_valid
  is_valid = False
  print ("\n----------------------------")
  print ("REGISTRATION NOT ACCEPTED")
  print (f"{message}")
  print ("------------------------------")
  return

# Name validation
name = (input("Enter student name: ").strip())
if not name:
  print_error ("Student name is required.")

# Age validation
age_input = input("Enter student age: ").strip()
age = int(age_input)
if not (11 <= age <= 18):
  print_error ("Age must be from 11 to 18")

# Grade level (gl) validation
try:
  grade_level = int(input("Enter student grade level: ").strip())
  if not grade_level >= 7 and grade_level <= 12:
    print_error ("Invalid Grade Level")
except ValueError:
  print_error("Grade level must be a valid number.")

# Email validation
email = input("Enter student email: ")
if "@" in email and "." in email:
    pass
else:
  print_error ("Invalid email")

# Registration code validation

if is_valid:
  print ("\n------------------------------")
  print ("REGISTRATION ACCEPTED!!")
  print ("------------------------------")
  print (f"Student: {name}")
  print (f"Age: {age}")
  print (f"Grade Level: {grade_level}")
  print (f"Email: {email}")
  print (f"Registration Code: {regis_code}")
```

---
## Validation Techniques Used
### Presence Validation
> The Presence Validator was used to validate the student name input.
### Data Type Validation
> The Data Type Validation was used to validate if the age input is an integer.
### Range Validation
> The Range Validation was used for the age input to see if it is from 11 to 18.
### Acceptable Value Validation
> The Acceptable Value Validation was used for the grade level and make sure the program only accepts grade levels from 7 to 12.
### Pattern Validation
Explain the simple pattern rule you used.
> The Pattern Validation was used for the email address. The program checks that the email contains both @ and . as basic format requirements.
### Length Validation
Explain the length rule you used.
> The Length Validation was used for the workshop registration code. The program uses len(regis_code) != 6 to make sure the registration code only accepts exactly 6 characters.
---
# Part D - Testing

| Test | Input / Condition | Validation Being Tested | Expected Output | Actual Output | Result |
|---:|---|---|---|---|---|
| 1 | All inputs valid | Normal case | Registration accepted student information | Registration accepted student information | PASS |
| 2 | Blank student name | Presence | Registration not accepted, Student name is required | Registration not accepted, Student name is required | PASS |
| 3 | Age = `fourteen` | Data type | Registration not accepted, Age must be a valid number | Registration not accepted, Age must be a valid number | PASS |
| 4 | Age = `11` | Minimum boundary | Age accepted and registration continues| Age accepted and registration continues | PASS |
| 5 | Age = `18` | Maximum boundary | Age accepted and registration continues | Age accepted and registration continues | PASS |
| 6 | Age = `10` | Range | Registration not accepted, Age must be from 11 to 18 | Registration not accepted, Age must be from 11 to 18 | PASS |
| 7 | Grade Level = `13` | Acceptable value | Grade level accepted and registration continues | Grade level accepted and registration continues | PASS |
| 8 | Email = `studentpshs.edu.ph` | Pattern | Registration not accepted, Invalid email | Registration not accepted, Invalid email | PASS |
| 9 | Registration Code = `ABC` | Length | Registration not accepted, Code must contain exactly 6 characters | Registration not accepted, Code must contain exactly 6 characters | PASS |
| 10 | Registration Code = `CS2026` | Valid length | Registration accepted if all previous inputs are valid | Registration accepted if all previous inputs are valid | PASS |

---
# Part E - Output Verification
Choose any **three tests** from Part D.
## Verification Test 1
**Input:**
```text
Student name: Bianca Di Angelo
Student age: 15
Grade level: 10
Email: maria@gmail.com
Registration code: CS2026

```
**Expected Output:**
```text
REGISTRATION ACCEPTED!!
Student: Bianca Di Angelo
Age: 15
Grade Level: 10
Email: maria@gmail.com
Registration Code: CS2026
```
**Actual Output:**
```text
REGISTRATION ACCEPTED!!
Student: Bianca Di Angelo
Age: 15
Grade Level: 10
Email: maria@gmail.com
Registration Code: CS2026
```
**Result:** PASS
**Explanation:**
> The output is accepted by the program because all of the inputs satisfy the program's validation requirements. The student has a valid name, age, grade level, email format, and an exactly 6-character registration code.
## Verification Test 2
**Input:**
```text
Student name: Bianca Di Angelo
Student age: fourteen
Grade level: 10
Email: maria@gmail.com
Registration code: CS2026
```
**Expected Output:**
```text
REGISTRATION NOT ACCEPTED
Age must be a valid number.
```
**Actual Output:**
```text
REGISTRATION NOT ACCEPTED
Age must be a valid number.
```
**Result:** PASS
**Explanation:**
> This is test passed because "fourteen" cannot be converted into an integer. The ValueError exception catches the invalid input and does not accept the registration.
---
## Verification Test 3
**Input:**
```text
Student name: Bianca Di Angelo
Student age: 15
Grade level: 10
Email: Bianca.gmail.com
Registration code: CS2026
```
**Expected Output:**
```text
REGISTRATION NOT ACCEPTED
Invalid email
```
**Actual Output:**
```text
REGISTRATION NOT ACCEPTED
Invalid email
```
**Result:** PASS
**Explanation:**
> The test passed because the entered email does not contain the required @ symbol. Therefore, it fails the program's email pattern validation.
---
# Reflection
### 1. Why should a program validate input before processing it?
> A program should validate the input before processing it to prevent incorrect or code crashes. It also ensures that the information follows the program's requirements
### 2. What is the difference between input validation and output verification?
> Input validation checks whether the user's input is acceptable before the program processes it to the final stage. Output verification checks whether the program produces the expected result after processing the input.
### 3. Which validation technique was easiest for you to implement? Why?
> For me, the easiest validation technique was the Length validation because I only needed to use the len() function to count the characters in the registration code which is super simple.
### 4. Which validation technique was most challenging? Why?
> For me, the most challenging validation technique was the data type validation because the program needed to handle inputs that cannot be converted into numbers. Using try and except helped prevent the program from crashing but I still struggled to make it work at first.
### 5. How did testing invalid inputs help you improve your program?
> Testing invalid inputs helped me find errors in the program and modify the existing code and validations. It also showed me how the program should respond when users enter incorrect information into it.
---

- [`workshop_validator.py`](workshop_validator.py)

GO BACKK!!
>[README.md](README.md)
