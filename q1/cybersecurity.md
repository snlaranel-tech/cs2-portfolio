# Fundamentals of Cybersecurity and Data Privacy
**Activity:** PSHS Secure Club Registration System

**Name:** Shiery Nicole L. Aranel

**Section:** 8 - Dahlia

**Quarter:** 1
---
## Activity Overview
In this activity, I analyzed a cybersecurity threat and developed secure data-capture rules for a simple
PSHS Club Registration System.
The goal is to create a program that collects only necessary information and accepts only correct,
expected, and appropriate input.
---
# Part A - Cybersecurity Threat Analysis
## Assigned Case

**Case Number: 2**

**Case Title: Fake Prize**
> A student supposedly wins a prize but must provide personal and payment information.
---
### 1. What cybersecurity threat is shown?
> The cybersecurity threat being shown is Phishing.
### 2. What warning signs make the situation suspicious?
> One of the biggest warning signs is the fact the student supposedly won a prize, yet has to input payment information to claim it, another similar warning sign is the need for personal information which would not usually be necessary when being given a prize, the final warning sign is the abruptness as there might be no reason for the student to win a prize in the first place. 
### 3. What may be affected?
Check or describe all that apply:
- Data: yes
- Account: yes
- Application
- Device
- Network
- Financial information: yes
> Only the data, account, and financial information would be affected because the student is being asked about their personal information and payment information which would give the scammer access to their accounts.
### 4. What information could be exposed or misused?
> The information that could be exposed or misused are the students full name, address or contact information, basic student information, email address, account usernames and passwords, bank account/s, and credit/debit card information
### 5. What should the user do to reduce the risk?
> The student should not click on just any link they see without double checking, not provide personal information on unverified websites, delete or report any suspicious messages, and if anything similar to this happens again they should verify the prize through official organizations and such.
---
# Part B - Data Privacy and Secure Data Capture
A proposed Club Registration System wants to collect the following information.
Determine whether each item is really necessary.
| Data | Collect / Do Not Collect | Reason |
|---|---|---|
| Student Name | Collect | The club organization needs to identify you |
| Section | Collect | So the organizations know where to commonly find you and know your class adviser |
| Club Choice | Collect | So you can register into your desired club |
| School Email | Collect | The club can easily contact you for any announcements |
| Attendance Status | Collect | So the club can mark your absence or presence during club meetings and determine your activeness |
| Password | Do not collect | This is a personal piece of information that is unnecessary and should not be used in a basic club organization |
| OTP | Do not collect | This is a personal piece of information that is unnecessary and should not be used in a basic club organization |
| Home Address | Do not collect | This is a personal piece of information that is unnecessary and should not be needed in a basic club organization that will take place on school grounds |
| Parent Bank Account | Do not collect | This is a personal piece of information that is unnecessary because the club does not need to access your parents bank account |
---
## Privacy Question
Why is it safer to collect only information that the program actually needs?
> It is safer to collect only needed information because it allows you to be easily identifiable and easy to contact while not violating any privacy laws or unnecessary intrusion.
---
# Part C - Security-Focused Validation Rules
Complete the table before writing your program.
| Data Captured | Expected Input | Possible Risk | Invalid Input Example | Validation Rule | Error
Message |

|---|---|---|---|---|---|

| Student Name | Student name | blank input | (blank) | Student name must not be blank | Student name is required. |

| Section | Dahlia, Sampaguita, Rosal, Ilang-Ilang | invalid/other input | Lily | Input must come from the list of valid sections | Please enter a valid section. |

| Club Choice | Robotics, Science, Mathematics, Programming | invalid/other input | Baking | Input must come from the list of valid club choices | Please choose a valid club. |

| School Email | email containing both "@" and a "." | invalid/other input without a "@" and a "." | Zii.royall.high | Input must contain both an "@" and a "." | Please enter a valid email. |

| Attendance Status | Present, Late, Absent | invalid/other input | On vacation | Input must either be Present, Late, or Absent | Please enter attendance status. |
---
## Secure Data Capture Questions
### 1. What should your program accept?
> My program should only accept Student Name, Section, Club Choice, School Email and Attendance Status
### 2. What should your program reject?
> My program should reject Password, OTP, Home Address, Banking Information
### 3. How do your validation rules help reduce incorrect or unsafe input?
> The validation rules help reduce incorrect or unsafe input by ensuring that all the entered information is correct and complete. First of all, the program checks the presence of a student name, then, the section and club choices are included in the list of valid options to enter, next, the email is checked to contain an "@" and a ".", finally, the attendance status is checked if it is a valid input, If any input is to be incorrect, the program will display an error message and the registration will not be accepted. This all reduces the possibility of invalid data being accepted, and will protect a students privacy and personal information.
---
# Part D - Secure Program Implementation
## Program

>[secure_registration.py](secure_registration.py)

## Source Code File
[`secure_registration.py`](secure_registration.py)
---
## Final Code
```python
is_valid = True 

def print_error(message):
  global is_valid
  is_valid = False
  print ("\n----------------------------")
  print ("REJECTED")
  print (f"{message}")
  print ("------------------------------")
  return

# Name Validation
name = str(input("Enter student name: ").strip())
if not name:
  print_error("Error: Student name is required.")

# Section Validation
valid_sec = ["Dahlia", "Sampaguita", "Rosal", "Ilang-ilang"]
section = input("List of sections: (Dahlia, Sampaguita, Rosal, Ilang-ilang)\n" "Enter a section from the list: ").strip()
if section not in valid_sec:
  print_error("Error: Please enter a valid section.")

# Club Choice Validation
valid_club = ["Robotics", "Science", "Mathematics", "Programming"]
club = input("List of clubs: (Robotics, Science, Mathematics, Programming)\n" "Enter a chosen club from the list: ").strip()
if club not in valid_club:
  print_error("Error: Please choose a valid club.")

# Email validation
email = input("Enter student email: ").strip()
if "@" in email and "." in email:
    pass
else:
  print_error ("Error: Please enter a valid email.")

# Attendance status
attendance = str(input("Enter student attendance status: ").strip())
# List of different attendance statuses
valid_att = ["Present", "Late", "Absent"]
if attendance not in valid_att:
  print_error("Error: Please enter a valid attendance status.")

if is_valid:
  print ("\n------------------------------")
  print ("REGISTRATION ACCEPTED!!")
  print ("------------------------------")
  print (f"Student: {name}")
  print (f"Section: {section}")
  print (f"Club: {club}")
  print (f"Email: {email}")
  print (f"Attendance: {attendance}")

```
---
## Security Practices Applied
### Required Input
> I handled blank input by checking if a student name was even entered or not using "if not". If the name is blank, the program displays an error message saying, "Student name is required." This stops the program from accepting a registration without a student name.
### Allowed Values
> The only fields that use a list of predefined values to accept inputs are the section, club choice, and attendance. Each of these can only accept fixed inputs, if the user decides to enter an input outside the list of given choices, the program displays an error message and will not accept the registration.
### Format Check
> My simple email validation rule checks if the email input contains both "@" and a ".", if either of the symbols are missing, the program displays an error message and will not accept the registration.
### Error Messages
> The error messages I added are useful for informing the user about why the data they inputted may not have been accepted and can overall help people understand the process of entering valid information into a program.
### Data Minimization
> The passwords, OTPs, home addresses, or banking information were intentionally not collected because they are not necessary for school club registration. The program is only required to collect appropriate information, in doing so, it protects students' privacy, reduces the risk of exposing personal data, and makes the program overall safer to use.
---
# Part E - Testing and Reflection
## Testing
| Test | Input Situation | Expected Output | Actual Output | Result |
|---:|---|---|---|---|
| 1 | All data valid | REGISTRATION ACCEPTED!! |REGISTRATION ACCEPTED!! | PASS |
| 2 | Blank student name | REJECTED Error: Student name is required. | REJECTED Error: Student name is required. | PASS |
| 3 | Invalid section | REJECTED Error: Please enter a valid section. | REJECTED Error: Please enter a valid section. | PASS |
| 4 | Invalid club choice | REJECTED Error: Please choose a valid club. | REJECTED Error: Please choose a valid club. | PASS |
| 5 | Email missing `@` | REJECTED Error: Please enter a valid email. | REJECTED Error: Please enter a valid email. | PASS |
| 6 | Email missing `.` | REJECTED Error: Please enter a valid email. | REJECTED Error: Please enter a valid email. | PASS |
| 7 | Invalid attendance status | REJECTED Error: Please enter a valid attendance status. | REJECTED Error: Please enter a valid attendance status. | PASS |
| 8 | Different valid inputs | REGISTRATION ACCEPTED!! | REGISTRATION ACCEPTED!! | PASS |
---
# Reflection
### 1. What is one cybersecurity threat that can affect an application or user?
> One cybersecurity threat that can affect an application or user is phishing. Phishing is where attackers send fake messages or websites to look like trusted companies or organizations to trick users into giving away their personal information such as passwords or banking information.
### 2. How can users reduce the risk of phishing or suspicious messages?
> Users can reduce the risk of phishing by not clicking suspicious links, checking the sender, and avoiding sharing personal information with unknown or untrusted sources on the website without a proper background check and the use of logical explanations.
### 3. How can validation rules improve the security of user input?
> Validation rules can improve the security of user inputs by helping make sure that users enter correct and appropriate information, and rejecting incorrect information inputs.
### 4. Why should a program avoid collecting unnecessary personal information?
> A program should avoid collecting unnecessary personal information because if it has no unnecessary information in the first place, there would barely be any data to misuse or invade the privacy of the user.
### 5. How did SG7's input validation concepts become security practices in SG8?
> SG7's input validation concepts became security practices in SG8 by using validation rules that will check user inputs before accepting them. For example, the program presented today validates the presence of student names, proper sections, proper club choices, proper email formats, and attendance statuses, while also collecting only the information needed for registration, nothing more.
---

# AI Prompt used
> How to fix this code so the list of predetermined values for sections and club choices are displayed along with the line of code asking for it.


# Files for This Activity
- [`secure_registration.py`](secure_registration.py)
- `cybersecurity.md`
---
[← Back to Main Portfolio](../README.md)
