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
* Easily calculate the average of all subjects
* Display each subject and its grade

### Grade Calculation

* Calculate average grade
* Display letter grade
* Display pass/fail remarks
* Support detailed letter grades (A+, A, A-, B+, B, B-, C+, C, and F)
* Automatically displays remarks based on the student's average
* Round the final average to two decimal places

### Academic Performance

* Display the highest grade
* Display the subject with the highest grade
* Display the lowest grade
* Display the subject with the lowest grade
* Count how many subjects were passed
* Count how many subjects were failed
* Display the student's overall academic status
* Display an academic performance recognition level

### Recognition Levels

The program can identify different levels of academic performance based on the student's average:

* High Honors
* Honors
* Good Academic Performance
* Passed
* Needs Improvement

### Subject Performance

* Display all subjects using a loop
* Show the grade for each subject
* Identify passed subjects
* Identify failed subjects
* Give the student a quick overview of their subject performance

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
* `if`, `elif`, and `else` statements
* `for` loops
* `while` loops
* `range()` function
* `sum()` function
* `max()` function
* `min()` function
* `.index()` method
* `round()` function

## Python Concepts Practiced

This project helps practice several basic Python programming concepts:

### Variables

Used to store student information, subject names, grades, averages, and results.

### Lists

Used to store multiple subjects and their corresponding grades.

### Conditional Statements

`if`, `elif`, and `else` statements are used to determine letter grades, remarks, and academic performance.

### For Loops

A `for` loop is used to go through the subjects and display each subject with its corresponding grade.

### While Loops

A `while` loop keeps the program running so the user can calculate grades for multiple students.

### Range Function

The `range()` function is used together with the `for` loop to access each subject and grade in the list.

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

## How It Works

1. Enter the student's name.
2. Enter the student's ID.
3. Enter the grades for each subject.
4. The program calculates the overall average.
5. The program determines the student's letter grade.
6. The program displays the appropriate remarks.
7. The program displays every subject and its grade.
8. The program identifies the highest and lowest grades.
9. The program counts the number of passed and failed subjects.
10. The program displays the student's academic performance.
11. The program asks if another student's grades should be calculated.

## How to Run

1. Download or clone this repository.
2. Open the project in your preferred Python editor.
3. Run the Python file.
4. Enter the student's name and student ID.
5. Enter the grades for each subject.
6. View the calculated average, letter grade, and remarks.
7. Review the subject performance and academic results.
8. Choose whether to calculate another student's grades.

## Example Output

```text
== Student Grade Calculator ==

Enter student name: Jose Navoa
Enter student ID: 20260001

Enter Math grade: 95
Enter English grade: 92
Enter Science grade: 94
Enter Filipino grade: 90
Enter Computer grade: 98

Student: Jose Navoa
Student ID: 20260001

Math: 95
English: 92
Science: 94
Filipino: 90
Computer: 98

Average: 93.8
Grade: A
Remarks: Excellent!

Highest Grade: 98
Highest Subject: Computer

Lowest Grade: 90
Lowest Subject: Filipino

Passed Subjects: 5
Failed Subjects: 0

Academic Performance: Honors
Overall Status: Passed
```

## Project Purpose

This project was created as a beginner Python programming project to practice calculating grades and working with basic programming concepts.

It was later expanded with additional student information, multiple subjects, subject analysis, performance recognition, and more detailed academic results.

The goal is to make a simple grade calculator while practicing important Python fundamentals such as **variables, lists, conditional statements, loops, functions, and built-in functions**.

## Future Improvements

Possible future improvements include:

* Save student records to a file
* Search for students by student ID
* Add more subjects
* Add attendance tracking
* Add GPA/GWA calculation
* Create a class summary
* Add multiple student records
* Generate a student report
* Add a graphical user interface
* Create a web version of the calculator

## Project Status

**Completed and continuously improving**

This project started as a simple student grade calculator and was expanded with additional academic performance features while keeping the original grading system.

## Author

Jose Navoa
