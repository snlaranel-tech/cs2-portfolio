# Clean Decision Code Makeover: Student Score Checker
**Name:** Shiery Nicole L. Aranel
**Section:** 8-Dahlia
---
## Activity Overview

In this activity, I learned how to improve a Student Score Checker program by applying proper coding standards and
selection structures.
The program only accepts a student score from 0 to 100 and determines the appropriate classification.

The classifications are:
| Score | Classification |
|---:|---|
| 90–100 | Outstanding |
| 80 – 89 | Very Satisfactory |
| 75 – 79 | Satisfactory |
| 0–74 | Needs Improvement |

Scores below 0 or above 100 are considered invalid.

Part 1: Analyze the logic
Input: The program needs the user to input their numerical score as an integer.
Boundary: The minimum valid score is 0.
Boundary: The maximum valid score is 100.
Possible Outputs: The possible outputs the program can print based on the inputs are; 
  1. "Invalid score"
  2. "Outstanding"
  3. "Very Satisfactory"
  4. "Satisfactory"
  5. "Needs Improvement"
Selection Pattern: The number validation part (while score < 0 or score > 100:) and the score classification section, both use boundary conditions.
Selection Pattern: The if-elif part during classification uses multiple decision paths.

Part 2: Flowchart
<img width="1933" height="2003" alt="scorezz - Main" src="https://github.com/user-attachments/assets/7157ca18-d7f0-4bc1-a9a2-827f7e07ddbf" />


Part 3: Pseudocode
START
INPUT score

WHILE score < 0 OR score > 100
DISPLAY "Invalid score"
DISPLAY "Please enter a valid score: "
INPUT score

IF score >= 90 AND score <= 100 THEN
  DISPLAY "Outstanding"
ELSE IF score >= 80 AND score < 90 THEN
  DISPLAY "Very Satisfactory"
ELSE IF score >= 75 AND score < 80 THEN
  DISPLAY "Satisfactory"
ELSE IF score >= 0 AND score < 75 THEN
  DISPLAY "Needs Improvement"
  
END

Part 4: [Clean_Code](score_checker.py)

Part 5:
<img width="890" height="251" alt="comscciii" src="https://github.com/user-attachments/assets/ec0260a7-1922-44da-bafb-fa8edd97b266" />

Testing Reflection:
1. It is important to test the values 0 and 100 because they are the exact boundaries of the valid score range and it must be confirmed that the edge values are included accordingly.
3. I tested -1 and 101 because they are the closest values outside of the valid score range and testing them ensures that the loop condition correctly catches invalid inputs and forces the user to enter a valid input.
5. Testing 75, 80, and 90 helped me understand boundary conditions the most, because these are the internal split points where the performance classification changes and highlights how a single number can change the output of the program.
7. Yes, my initial tests failed due to syntax errors in the input and conditional statements. For the input() it lacked a fully closed parenthesis (Ex: (input("Please enter a valid score: ") ). To fix it, a closed parenthesis was added. For the conditional statements, the greater than symbol and less than symbol were switched around (Ex: score > 0 or score < 100). To fix it the symbols were switched around.

Reflection: 
1. The selection structures (if, elif, and else), helped the program make decisions and execute specific code blocks with their right conditions, therefore aiding the score categorization by evaluating the entered scores numerical value and its proper output.
2. The comments, proper formatting, and use of meaningful variables improved the previous code by making it easier to understand, maintain, and debug if anything were to go wrong.
3. Planning using flow charts and pseudocode before proceeding to code writing helps the user visually map out the code logic and structure in simpler form without having to worry about any special missing characters and syntax rules that come with proper coding.
