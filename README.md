# Student Grade Calculator

A beginner-friendly Python project that calculates a student's average grade based on multiple subjects. The project was expanded to provide more detailed information about a student's academic performance while still keeping the original grading system.

The program now works as a simple **Student Grade Management and Performance Analyzer**, allowing users to calculate grades, manage student records, analyze class performance, rank students, and identify students who may need academic improvement.

## Features

### Student Information

* Enter student name
* Enter student ID
* Calculate grades for multiple students without restarting the program
* Store student records while the program is running
* View previously calculated student records
* Search for a student using their name or student ID
* View detailed student reports
* Edit student information
* Delete student records

### Subject Grades

* Input grades for multiple subjects
* Supports Math
* Supports English
* Supports Science
* Supports Filipino
* Supports Computer
* Supports Programming
* Supports Database
* Calculate the average of all subjects
* Display each subject and its grade
* Store individual subject grades inside each student record

### Grade Validation

* Only accepts grades from 0 to 100
* Prevents grades below 0
* Prevents grades above 100
* Detects invalid text or non-numeric grade input
* Asks the user to enter the grade again when invalid input is provided
* Uses a `while` loop to keep asking until a valid grade is entered

### Attendance Validation

* Accept attendance from 0 to 100 percent
* Prevent invalid attendance values
* Detect non-numeric attendance input
* Continue asking until valid attendance is entered

### Grade Calculation

* Calculate average grade
* Display letter grade
* Display pass/fail remarks
* Support detailed letter grades:

  * A+
  * A
  * A-
  * B+
  * B
  * B-
  * C+
  * C
  * F
* Automatically display remarks based on the student's average
* Round the final average to two decimal places
* Display the final grade as a percentage

## Academic Performance

* Display the highest grade
* Display the subject with the highest grade
* Display the lowest grade
* Display the subject with the lowest grade
* Count how many subjects were passed
* Count how many subjects were failed
* Display the student's overall academic status
* Display an academic performance recognition level
* Display a performance level based on the student's average
* Display the student's academic standing
* Display an estimated GPA equivalent
* Calculate the number of points needed to pass a failed subject
* Provide study recommendations

## Recognition Levels

The program can identify different levels of academic performance based on the student's average:

* High Honors
* Honors
* Good Academic Performance
* Passed
* Needs Improvement

## Performance Levels

The program also provides a more detailed performance level:

* Outstanding
* Excellent
* Very Good
* Good
* Satisfactory
* Needs Improvement

## Subject Performance

* Display all subjects using a loop
* Show the grade for each subject
* Identify passed subjects
* Identify failed subjects
* Count the number of passed subjects
* Count the number of failed subjects
* Give the student a quick overview of their subject performance

## Grade Summary

* Display every subject and its grade
* Classify each subject as Excellent, Very Good, Good, Passed, or Failed
* Use the student's grade to determine individual subject performance
* Provide a simple summary of the student's grades
* Display the number of subjects in each performance category

## Attendance Tracking

* Enter the student's attendance percentage
* Validate attendance from 0 to 100
* Prevent invalid attendance values
* Display the student's attendance percentage
* Identify attendance status
* Classify attendance as Excellent, Good, Satisfactory, or Poor
* Display warnings when attendance needs improvement

## Scholarship Eligibility

The program checks whether the student meets the basic scholarship requirements.

A student is considered eligible when:

* The overall average is 90 or higher
* Attendance is 90% or higher
* No subjects are failed

The program displays either:

```text
Scholarship Eligibility: Eligible
```

or:

```text
Scholarship Eligibility: Not Eligible
```

## Overall Status

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

## GPA Equivalent

The program provides an estimated GPA equivalent based on the student's average.

The GPA system includes:

* 1.00 for very high grades
* 1.25
* 1.50
* 1.75
* 2.00
* 2.25
* 2.50
* 3.00 for passing grades
* 5.00 for failing grades

The program also provides a description of the GPA result.

## Academic Standing

The program provides an additional academic standing based on the student's average, failed subjects, and attendance.

Possible results include:

* Excellent Standing
* Good Standing
* Satisfactory Standing
* Academic Improvement Needed

## Subject Improvement

The program identifies subjects that are below the passing grade.

For every failed subject, it calculates how many additional points are needed to reach the passing grade of 75.

Example:

```text
==============================
SUBJECT IMPROVEMENT NEEDED
==============================

Math needs 8.5 more points to reach the passing grade.
```

If all subjects are already passing:

```text
No subject needs improvement to reach the passing grade.
```

## Study Recommendations

The program provides simple recommendations based on the student's results.

Examples include:

* Focus on subjects that are currently failing
* Spend more study time on subjects below 80
* Improve attendance
* Create a regular study schedule
* Continue studying consistently
* Maintain current study habits when performance is already good

## Student Records

The program temporarily stores student information while it is running.

Each student record includes:

* Student name
* Student ID
* Subjects
* Individual subject grades
* Average
* Letter grade
* Attendance
* Number of failed subjects
* GPA
* Performance level
* Academic standing

Student records are stored using a Python list containing dictionaries.

> Student records are currently stored only while the program is running. Records are not permanently saved after the program is closed.

## View Student Records

The **View Student Records** option displays all students currently stored in the program.

Information includes:

* Name
* Student ID
* Average
* Letter grade
* Attendance
* Failed subjects
* GPA
* Performance
* Academic standing

## Search Student

The program allows the user to search for a saved student record.

Students can be searched using:

* Student name
* Student ID
* Partial names
* Partial student IDs

The search displays the student's academic information and results.

## Detailed Student Report

The program can generate a more complete report for a selected student.

The detailed report includes:

* Student name
* Student ID
* Every subject
* Individual grades
* Overall average
* Letter grade
* GPA
* Performance level
* Academic standing
* Attendance
* Attendance status
* Number of failed subjects

Example:

```text
===================================
STUDENT REPORT
===================================

Name: Jose Navoa
Student ID: 20260001

SUBJECTS
Math : 95
English : 92
Science : 94
Programming : 96

ACADEMIC INFORMATION
Average: 94.25
Letter Grade: A
GPA: 1.25
Performance: Excellent
Academic Standing: Excellent Standing

ATTENDANCE
Attendance: 95 %
Attendance Status: Excellent

FAILED SUBJECTS: 0
```

## Edit Student Record

The program allows existing student records to be modified.

The user can edit:

* Student name
* Student ID
* Subject grades
* Attendance

When grades or attendance are changed, the program recalculates:

* Average
* Letter grade
* Failed subjects
* GPA
* Performance level
* Academic standing

This keeps the student's record updated after an edit.

## Delete Student Record

The program allows the user to remove an individual student record.

Before deleting the record, the program asks for confirmation:

```text
Are you sure you want to delete this record? (yes/no):
```

This helps prevent accidental deletion.

## Class Summary

The program can create a summary of all students currently stored in the program.

The class summary displays:

* Number of students
* Class average
* Highest student average
* Student with the highest average
* Lowest student average
* Student with the lowest average
* Number of students who passed
* Number of students who failed
* Class pass rate

Example:

```text
==============================
CLASS SUMMARY
==============================

Number of Students: 5
Class Average: 87.42
Highest Student Average: 94.25
Highest Student: Jose Navoa
Lowest Student Average: 72.50
Lowest Student: Student 5
Students Passed: 4
Students Failed: 1
Class Pass Rate: 80.0 %
```

## Student Ranking

The program can rank all stored students according to their average grade.

Students are displayed from the highest average to the lowest average.

Example:

```text
==============================
STUDENT RANKING
==============================

1 . Jose Navoa - Average: 94.25 - GPA: 1.25
2 . Maria Santos - Average: 91.50 - GPA: 1.50
3 . John Cruz - Average: 87.75 - GPA: 1.75
```

This feature uses Python's sorting functionality to organize student records.

## Honor Students

The program can identify students who meet the current honors condition.

A student is included when:

* Average is 90 or higher
* No subjects are failed

Example:

```text
==============================
HONOR STUDENTS
==============================

Jose Navoa - Average: 94.25 - With Honors
Maria Santos - Average: 91.50 - With Honors
```

If no students qualify:

```text
No students currently qualify for honors.
```

## Students Needing Improvement

The program can identify students who may need additional academic improvement.

A student is included when:

* Their average is below 75
* Or they have one or more failed subjects

Example:

```text
==============================
STUDENTS NEEDING IMPROVEMENT
==============================

John Cruz - Average: 72.50 - Failed Subjects: 2
```

## Subject Statistics

The program can analyze individual subjects across all stored students.

For each subject, it calculates:

* Subject average
* Highest grade
* Lowest grade

Example:

```text
==============================
SUBJECT STATISTICS
==============================

Subject: Math
Average: 88.50
Highest Grade: 98
Lowest Grade: 72

Subject: Programming
Average: 91.25
Highest Grade: 100
Lowest Grade: 80
```

This allows the user to see which subjects are performing well and which subjects may need more attention.

## Class Performance

The program groups students according to their overall average.

The categories are:

* Excellent
* Good
* Satisfactory
* Needs Improvement

Example:

```text
==============================
CLASS PERFORMANCE
==============================

Excellent: 2
Good: 3
Satisfactory: 1
Needs Improvement: 1
```

## Clear All Records

The program includes an option to remove all student records currently stored in memory.

The program asks for confirmation before deleting everything.

Example:

```text
==============================
CLEAR ALL RECORDS
==============================

Number of records: 5

Are you sure you want to delete ALL records? (yes/no):
```

If the user enters `yes`, all current records are removed.

## Program Menu

The expanded version uses a menu system:

```text
===================================
     STUDENT GRADE CALCULATOR
===================================
1. Calculate Student Grade
2. View Student Records
3. Search Student
4. View Class Summary
5. View Detailed Student Report
6. Edit Student Record
7. Delete Student Record
8. Rank Students
9. View Honor Students
10. Students Needing Improvement
11. Subject Statistics
12. Class Performance
13. Clear All Records
14. Exit
===================================
```

### Menu Options

**1. Calculate Student Grade**

Allows the user to enter a student's information, grades, and attendance and then displays the complete academic analysis.

**2. View Student Records**

Displays all student records currently stored during the program session.

**3. Search Student**

Searches for a student by name or student ID.

**4. View Class Summary**

Displays overall class statistics, including the class average and pass rate.

**5. View Detailed Student Report**

Displays a complete academic report for a selected student.

**6. Edit Student Record**

Allows the user to change a student's name, ID, grades, or attendance.

**7. Delete Student Record**

Removes a selected student record after confirmation.

**8. Rank Students**

Displays students from the highest average to the lowest average.

**9. View Honor Students**

Displays students with an average of 90 or higher and no failed subjects.

**10. Students Needing Improvement**

Displays students who have a failing average or one or more failed subjects.

**11. Subject Statistics**

Shows the average, highest grade, and lowest grade for each subject.

**12. Class Performance**

Shows how many students belong to each overall performance category.

**13. Clear All Records**

Deletes all student records after confirmation.

**14. Exit**

Ends the program.

## Technologies Used

* Python 3
* Variables
* Input and Output
* Lists
* Dictionaries
* Functions
* `try` and `except`
* `if`, `elif`, and `else` statements
* `for` loops
* `while` loops
* `range()` function
* `sum()` function
* `max()` function
* `min()` function
* `sorted()` function
* `lambda`
* `.index()` method
* `.append()` method
* `.remove()` method
* `.clear()` method
* `round()` function
* `.lower()` method

## Python Concepts Practiced

This project helps practice several basic Python programming concepts.

### Variables

Used to store student information, subject names, grades, attendance, averages, and results.

### Lists

Used to store:

* Subjects
* Grades
* Recommendations
* Student records

### Dictionaries

Dictionaries are used to organize information for each student record.

Example information stored includes:

* Name
* Student ID
* Subjects
* Grades
* Average
* Letter grade
* Attendance
* Failed subjects
* GPA
* Performance
* Academic standing

### Functions

The expanded version uses functions to divide the program into smaller sections.

Some of the functions include:

* `get_grade()`
* `get_attendance()`
* `get_letter_grade()`
* `get_performance_level()`
* `get_gpa()`
* `get_attendance_status()`
* `display_subject_grades()`
* `display_subject_performance()`
* `display_grade_analysis()`
* `display_grade_summary()`
* `display_recognition()`
* `display_scholarship()`
* `display_overall_status()`
* `display_gpa()`
* `display_academic_standing()`
* `display_attendance()`
* `display_recommendations()`
* `display_subject_improvement()`
* `save_student_record()`
* `view_student_records()`
* `search_student()`
* `display_class_summary()`
* `view_student_details()`
* `edit_student_record()`
* `update_student_calculation()`
* `delete_student_record()`
* `rank_students()`
* `display_honor_students()`
* `display_students_needing_improvement()`
* `display_subject_statistics()`
* `display_class_performance()`
* `clear_all_records()`
* `calculate_student()`
* `main()`

Using functions makes the program easier to organize, read, debug, and maintain.

### Conditional Statements

`if`, `elif`, and `else` statements are used to determine:

* Letter grades
* Remarks
* Performance levels
* Attendance status
* Scholarship eligibility
* Academic standing
* Overall academic status
* Honor eligibility
* Students needing improvement
* Menu selections

### For Loops

A `for` loop is used to:

* Go through subjects
* Display each subject with its corresponding grade
* Check the performance of each subject
* Generate grade summaries
* Generate study recommendations
* Search through student records
* Calculate class statistics
* Display student rankings
* Calculate subject statistics

### While Loops

`while` loops are used to:

* Keep the program running
* Display the main menu repeatedly
* Allow multiple student calculations
* Validate grade input
* Validate attendance input
* Continue asking the user until valid information is entered

### Range Function

The `range()` function is used together with `for` loops to access each subject and grade in the lists.

### Try and Except

`try` and `except` are used to prevent the program from crashing when the user enters text instead of a number for grades or attendance.

### Sorting

The `sorted()` function is used to arrange students based on their average grade.

The ranking system sorts students from the highest average to the lowest average.

### Lambda

A `lambda` function is used with `sorted()` to tell Python which value should be used when ranking students.

### Built-in Functions

The project uses Python functions and methods such as:

* `sum()` to calculate total grades
* `max()` to find the highest grade
* `min()` to find the lowest grade
* `sorted()` to rank students
* `round()` to make averages easier to read
* `.index()` to identify the subject connected to a grade
* `.lower()` to make text searches easier
* `.append()` to add information to lists
* `.remove()` to remove a selected record
* `.clear()` to remove all records

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

## GPA Equivalent System

The program provides an estimated GPA equivalent based on the student's average.

|  Average |  GPA |
| -------: | ---: |
|   97–100 | 1.00 |
|    93–96 | 1.25 |
|    90–92 | 1.50 |
|    87–89 | 1.75 |
|    83–86 | 2.00 |
|    80–82 | 2.25 |
|    77–79 | 2.50 |
|    75–76 | 3.00 |
| Below 75 | 5.00 |

## How It Works

1. Start the program.
2. Select an option from the main menu.
3. Enter the student's name.
4. Enter the student's ID.
5. Enter the grades for each subject.
6. The program checks if each grade is between 0 and 100.
7. The program calculates the overall average.
8. The program determines the student's letter grade.
9. The program displays the appropriate remarks.
10. The program displays every subject and its grade.
11. The program identifies the highest and lowest grades.
12. The program counts the number of passed and failed subjects.
13. The program determines the student's performance level.
14. The program determines the student's academic recognition.
15. Enter the student's attendance percentage.
16. The program determines the attendance status.
17. The program checks scholarship eligibility.
18. The program displays the student's overall status.
19. The program creates a grade summary for every subject.
20. The program calculates the estimated GPA.
21. The program determines the student's academic standing.
22. The program identifies subjects that need improvement.
23. The program provides study recommendations.
24. The student's complete record is stored temporarily.
25. The user can view saved student records.
26. The user can search for a student.
27. The user can view a detailed student report.
28. The user can edit a student record.
29. The user can delete a student record.
30. The user can rank all students.
31. The user can view honor students.
32. The user can view students needing improvement.
33. The user can view subject statistics.
34. The user can view class performance.
35. The user can view the class summary and pass rate.
36. The user can clear all records.
37. The user can calculate another student's grades or exit the program.

## How to Run

1. Download or clone this repository.
2. Open the project in your preferred Python editor.
3. Run the Python file.
4. Select an option from the main menu.
5. Enter the student's name and student ID.
6. Enter the grades for each subject.
7. Correct any invalid grade input if requested.
8. Enter the student's attendance percentage.
9. View the calculated average, letter grade, and remarks.
10. Review the subject performance and academic results.
11. Check the attendance and scholarship eligibility results.
12. Review the GPA and academic standing.
13. Read the subject improvement suggestions and study recommendations.
14. Save and review the student's temporary record.
15. Search for students or view detailed reports.
16. Edit or delete records when needed.
17. View rankings, honors, subject statistics, and class performance.
18. View the class summary and pass rate.
19. Clear records when needed.
20. Choose whether to calculate another student's grades or exit.

## Example Output

```text
===================================
     STUDENT GRADE CALCULATOR
===================================
1. Calculate Student Grade
2. View Student Records
3. Search Student
4. View Class Summary
5. View Detailed Student Report
6. Edit Student Record
7. Delete Student Record
8. Rank Students
9. View Honor Students
10. Students Needing Improvement
11. Subject Statistics
12. Class Performance
13. Clear All Records
14. Exit
===================================

Choose an option: 1

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
GPA EQUIVALENT
==============================
Estimated GPA: 1.25
GPA Description: Excellent Academic Performance

==============================
ACADEMIC STANDING
==============================
Academic Standing: Excellent Standing

==============================
SUBJECT IMPROVEMENT NEEDED
==============================
No subject needs improvement to reach the passing grade.

==============================
STUDY RECOMMENDATIONS
==============================
- Maintain your current study habits and performance.

==============================
CALCULATION COMPLETE
==============================
```

## Project Purpose

This project was created as a beginner Python programming project to practice calculating grades and working with basic programming concepts.

It was later expanded into a more complete **Student Grade Management and Performance Analyzer** with additional student management and class analysis features.

The project now includes:

* Multiple subject grade calculation
* Grade validation
* Attendance tracking
* Performance analysis
* Scholarship eligibility
* GPA calculation
* Academic standing
* Study recommendations
* Subject improvement analysis
* Temporary student records
* Student searching
* Detailed student reports
* Student record editing
* Student record deletion
* Student ranking
* Honor student identification
* Students needing improvement
* Subject statistics
* Class performance analysis
* Class summary
* Class pass rate
* Record clearing

The goal is to make a simple but useful grade management system while practicing important Python fundamentals such as **variables, lists, dictionaries, functions, conditional statements, loops, input validation, sorting, and built-in functions**.

## Future Improvements

Possible future improvements include:

* Save student records permanently to a file
* Export grades to a text or CSV file
* Add a database for permanent student records
* Add more subjects
* Add more detailed GPA/GWA calculations
* Add semester and school year information
* Add class sections
* Add teacher or administrator accounts
* Add a graphical user interface
* Create a web version of the calculator
* Generate printable student reports
* Add charts and graphs for class performance
* Add attendance history
* Add multiple grading periods
* Add login functionality
* Add student profile pictures
* Add automatic report generation

## Project Status

**Completed and continuously improving**

This project started as a simple student grade calculator and was expanded into a student grade management and academic performance analysis system while keeping the original grading system.

The current version includes multiple subjects, grade validation, attendance tracking, performance analysis, scholarship eligibility, GPA calculation, academic standing, study recommendations, subject improvement analysis, temporary student records, student search, detailed student reports, record editing, record deletion, student ranking, honor student identification, subject statistics, class performance, class summaries, and class pass rates.

## Author

Jose Navoa
