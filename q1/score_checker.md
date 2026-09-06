Part 1: Questions
Input: The program needs the user to input their numerical score as an integer.
Boundary: The minimum valid score is 0.
Boundary: The maximum valid score is 100.
Possible Outputs: The possible outputs the program can print based on the inputs are; "Outstanding", "Very Satisfactory", "Satisfactory", and "Needs Improvement"
Selection Pattern: Which part uses a boundary condition?
Selection Pattern: Which part uses multiple decision paths?

Part 2: Flowchart
<img width="1933" height="2003" alt="Flowchart P2" src="https://github.com/user-attachments/assets/4038924f-edaf-48c2-a424-6df1e89f98c7" />

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

Part 4: [Clean_Code](q1/score_checker.py)
