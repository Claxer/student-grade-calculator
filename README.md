# Student Grade Calculator

A beginner-friendly Python project that calculates a student's average grade based on multiple subjects. The project was expanded to provide more detailed information about a student's academic performance while still keeping the original grading system.

## Features

### Student Information

* Enter student name
* Enter student ID
* Calculate grades for multiple students without restarting the program

### Subject Grades

* Input grades for multiple subjects
* Supports Math
* Supports English
* Supports Science
* Supports Filipino
* Supports Computer
* Supports Programming
* Supports Database
* Easily calculate the average of all subjects
* Display each subject and its grade

### Grade Validation

* Only accepts grades from 0 to 100
* Prevents grades below 0
* Prevents grades above 100
* Detects invalid text or non-numeric grade input
* Asks the user to enter the grade again when invalid input is provided
* Uses a `while` loop to keep asking until a valid grade is entered

### Grade Calculation

* Calculate average grade
* Display letter grade
* Display pass/fail remarks
* Support detailed letter grades (A+, A, A-, B+, B, B-, C+, C, and F)
* Automatically displays remarks based on the student's average
* Round the final average to two decimal places
* Display the final grade as a percentage

### Academic Performance

* Display the highest grade
* Display the subject with the highest grade
* Display the lowest grade
* Display the subject with the lowest grade
* Count how many subjects were passed
* Count how many subjects were failed
* Display the student's overall academic status
* Display an academic performance recognition level
* Display a performance level based on the student's average

### Recognition Levels

The program can identify different levels of academic performance based on the student's average:

* High Honors
* Honors
* Good Academic Performance
* Passed
* Needs Improvement

### Performance Levels

The program also provides a more detailed performance level:

* Outstanding
* Excellent
* Very Good
* Good
* Satisfactory
* Needs Improvement

### Subject Performance

* Display all subjects using a loop
* Show the grade for each subject
* Identify passed subjects
* Identify failed subjects
* Count the number of passed subjects
* Count the number of failed subjects
* Give the student a quick overview of their subject performance

### Grade Summary

* Display every subject and its grade
* Classify each subject as Excellent, Very Good, Good, Passed, or Failed
* Use the student's grade to determine individual subject performance
* Provide a simple summary of the student's grades

### Attendance Tracking

* Enter the student's attendance percentage
* Validate attendance from 0 to 100
* Prevent invalid attendance values
* Display the student's attendance percentage
* Identify attendance status
* Classify attendance as Excellent, Good, Satisfactory, or Poor

### Scholarship Eligibility

The program checks whether the student meets the basic scholarship requirements.

A student is considered eligible when:

* The overall average is 90 or higher
* Attendance is 90% or higher
* No subjects are failed

The program displays either:

* Scholarship Eligibility: Eligible
* Scholarship Eligibility: Not Eligible

### Overall Status

The program determines the student's overall academic status.

If all subjects are passed and the average is at least 75:

* Overall Status: PASSED
* All subjects passed

If the student has one or more failed subjects:

* Overall Status: FAILED
* Warning that the student has failed subject(s)

If the overall average is below 75:

* Overall Status: FAILED
* Warning that the overall average is below passing

### Program Loop

* Repeat calculations using a `while` loop
* Calculate grades for multiple students
* Ask the user if they want to calculate another student
* End the program when the user chooses `no`

## Technologies Used

* Python 3
* Variables
* Input and Output
* Lists
* `try` and `except`
* `if`, `elif`, and `else` statements
* `for` loops
* `while` loops
* `range()` function
* `sum()` function
* `max()` function
* `min()` function
* `.index()` method
* `round()` function
* `.lower()` method

## Python Concepts Practiced

This project helps practice several basic Python programming concepts:

### Variables

Used to store student information, subject names, grades, attendance, averages, and results.

### Lists

Used to store multiple subjects and their corresponding grades.

### Conditional Statements

`if`, `elif`, and `else` statements are used to determine letter grades, remarks, performance levels, attendance status, scholarship eligibility, and overall academic status.

### For Loops

A `for` loop is used to go through the subjects and display each subject with its corresponding grade.

It is also used to create the grade summary for every subject.

### While Loops

`while` loops are used to:

* Keep the program running
* Allow multiple student calculations
* Validate grade input
* Validate attendance input
* Continue asking the user until valid information is entered

### Range Function

The `range()` function is used together with the `for` loop to access each subject and grade in the list.

### Try and Except

`try` and `except` are used to prevent the program from crashing when the user enters text instead of a number for grades or attendance.

### Built-in Functions

The project uses Python functions such as:

* `sum()` to calculate the total grades
* `max()` to find the highest grade
* `min()` to find the lowest grade
* `round()` to make the average easier to read
* `.index()` to identify the subject connected to the highest or lowest grade

## Grading System

|  Average | Grade | Remarks      |
| -------: | :---: | ------------ |
|   97–100 |   A+  | Outstanding! |
|    93–96 |   A   | Excellent!   |
|    90–92 |   A-  | Excellent!   |
|    87–89 |   B+  | Very Good!   |
|    83–86 |   B   | Very Good!   |
|    80–82 |   B-  | Good!        |
|    77–79 |   C+  | Passed!      |
|    75–76 |   C   | Passed!      |
| Below 75 |   F   | Failed       |

## Performance Level System

|  Average | Performance Level |
| -------: | ----------------- |
|   95–100 | Outstanding       |
|    90–94 | Excellent         |
|    85–89 | Very Good         |
|    80–84 | Good              |
|    75–79 | Satisfactory      |
| Below 75 | Needs Improvement |

## Attendance System

| Attendance | Status       |
| ---------: | ------------ |
|    90–100% | Excellent    |
|     80–89% | Good         |
|     75–79% | Satisfactory |
|  Below 75% | Poor         |

## Scholarship Eligibility

The program checks three conditions before considering a student eligible for a scholarship:

| Requirement     | Minimum |
| --------------- | ------- |
| Average         | 90%     |
| Attendance      | 90%     |
| Failed Subjects | 0       |

If all requirements are met:

```text
Scholarship Eligibility: Eligible
```

Otherwise:

```text
Scholarship Eligibility: Not Eligible
```

## How It Works

1. Enter the student's name.
2. Enter the student's ID.
3. Enter the grades for each subject.
4. The program checks if each grade is between 0 and 100.
5. The program calculates the overall average.
6. The program determines the student's letter grade.
7. The program displays the appropriate remarks.
8. The program displays every subject and its grade.
9. The program identifies the highest and lowest grades.
10. The program counts the number of passed and failed subjects.
11. The program determines the student's performance level.
12. The program determines the student's academic recognition.
13. Enter the student's attendance percentage.
14. The program determines the attendance status.
15. The program checks scholarship eligibility.
16. The program displays the student's overall status.
17. The program creates a grade summary for every subject.
18. The program asks if another student's grades should be calculated.

## How to Run

1. Download or clone this repository.
2. Open the project in your preferred Python editor.
3. Run the Python file.
4. Enter the student's name and student ID.
5. Enter the grades for each subject.
6. Correct any invalid grade input if requested.
7. Enter the student's attendance percentage.
8. View the calculated average, letter grade, and remarks.
9. Review the subject performance and academic results.
10. Check the attendance and scholarship eligibility results.
11. Choose whether to calculate another student's grades.

## Example Output

```text
== Student Grade Calculator ==

Enter student name: Jose Navoa
Enter student ID: 20260001

Enter grades from 0 to 100.
Enter Math grade: 95
Enter English grade: 92
Enter Science grade: 94
Enter Filipino grade: 90
Enter Computer grade: 98
Enter Programming grade: 96
Enter Database grade: 91

Enter attendance percentage: 95

==============================
STUDENT INFORMATION
==============================
Student: Jose Navoa
Student ID: 20260001

==============================
SUBJECT GRADES
==============================
Math: 95.0
English: 92.0
Science: 94.0
Filipino: 90.0
Computer: 98.0
Programming: 96.0
Database: 91.0

Average: 93.71
Grade Percentage: 93.71 %

==============================
FINAL GRADE
==============================
Letter Grade: A
Remarks: Excellent!

==============================
SUBJECT PERFORMANCE
==============================
Math: 95.0 - Passed
English: 92.0 - Passed
Science: 94.0 - Passed
Filipino: 90.0 - Passed
Computer: 98.0 - Passed
Programming: 96.0 - Passed
Database: 91.0 - Passed

Passed Subjects: 7
Failed Subjects: 0

==============================
GRADE ANALYSIS
==============================
Highest Grade: 98.0
Highest Subject: Computer
Lowest Grade: 90.0
Lowest Subject: Filipino

==============================
PERFORMANCE LEVEL
==============================
Performance Level: Excellent

==============================
RECOGNITION
==============================
Recognition: With Honors

==============================
ATTENDANCE
==============================
Attendance: 95.0 %
Attendance Status: Excellent

==============================
SCHOLARSHIP CHECK
==============================
Scholarship Eligibility: Eligible

==============================
OVERALL STATUS
==============================
Overall Status: PASSED
All subjects passed.

==============================
GRADE SUMMARY
==============================
Math: 95.0 - Excellent
English: 92.0 - Excellent
Science: 94.0 - Excellent
Filipino: 90.0 - Excellent
Computer: 98.0 - Excellent
Programming: 96.0 - Excellent
Database: 91.0 - Excellent

==============================
CALCULATION COMPLETE
==============================
```

## Project Purpose

This project was created as a beginner Python programming project to practice calculating grades and working with basic programming concepts.

It was later expanded with additional student information, more subjects, grade validation, attendance tracking, subject analysis, performance recognition, scholarship eligibility, and more detailed academic results.

The goal is to make a simple grade calculator while practicing important Python fundamentals such as **variables, lists, conditional statements, loops, input validation, and built-in functions**.

## Future Improvements

Possible future improvements include:

* Save student records to a file
* Search for students by student ID
* Add more subjects
* Add GPA/GWA calculation
* Add multiple student records
* Generate a student report
* Export grades to a text or CSV file
* Add a class summary
* Add a graphical user interface
* Create a web version of the calculator
* Add a database for storing student records
* Add editing and deleting of student records

## Project Status

**Completed and continuously improving**

This project started as a simple student grade calculator and was expanded with additional academic performance features while keeping the original grading system.

The current version includes multiple subjects, grade validation, attendance tracking, performance analysis, scholarship eligibility, subject summaries, and overall academic status.

## Author

Jose Navoa
