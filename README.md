# Company Attendance System

A complete **Employee Attendance Management System** developed with Python. The system helps companies manage employee information, track daily attendance, and monitor employee work schedules through a simple and beginner-friendly desktop application.

The project focuses on employee attendance management using **Clock In** and **Clock Out** functionality while also providing additional tools for managing employees, checking attendance records, generating reports, and viewing attendance statistics.

---

## Features

### Employee Management

The system allows administrators to manage employee information.

* Add new employees
* View employee list
* Search for employees
* Update employee information
* Remove employees
* View individual employee details
* Organize employees using employee IDs
* Store employee names and other basic information

### Clock In

Employees can clock in when they start their workday.

The system records:

* Employee ID
* Employee name
* Clock-in date
* Clock-in time
* Attendance status

The system also prevents an employee from clocking in multiple times without first clocking out.

### Clock Out

Employees can clock out when they finish their workday.

The system records:

* Clock-out date
* Clock-out time
* Total working time
* Attendance record

The system checks whether the employee is currently clocked in before allowing them to clock out.

### Attendance Records

The system keeps track of employee attendance records.

Users can:

* View attendance records
* Search attendance records
* Check employee attendance history
* View clock-in and clock-out times
* Check working hours
* Identify employees who are currently working
* Review previous attendance records

### Today's Attendance

A dedicated attendance view allows users to see the attendance activity for the current day.

It can display:

* Employees who clocked in
* Employees who clocked out
* Employees currently working
* Clock-in times
* Clock-out times
* Total working hours

### Attendance Status

The system can determine different attendance statuses based on employee activity.

Examples include:

* Present
* Currently Working
* Completed Shift
* Absent
* Late

This makes it easier for administrators to understand the current attendance situation.

### Late Employee Tracking

The system can identify employees who clocked in after the expected work start time.

Late records can include:

* Employee name
* Employee ID
* Clock-in time
* Expected start time
* Late status

This provides a simple way to monitor employee punctuality.

### Working Hours Calculation

The system automatically calculates the amount of time an employee worked.

For example:

```text
Clock In: 08:00 AM
Clock Out: 05:00 PM

Working Hours: 9 hours
```

The system calculates the difference between the clock-in and clock-out times.

### Employee Attendance History

Administrators can view the attendance history of individual employees.

This can be useful for checking:

* Previous clock-ins
* Previous clock-outs
* Working hours
* Attendance dates
* Late records
* Attendance patterns

### Attendance Search

The system includes search functionality for quickly finding attendance information.

Users can search using information such as:

* Employee ID
* Employee name
* Date
* Attendance status

This makes it easier to find specific records without manually checking every entry.

### Attendance Statistics

The system provides basic attendance statistics to help summarize employee attendance.

Statistics may include:

* Total employees
* Employees present
* Employees absent
* Employees currently working
* Number of completed shifts
* Number of late employees
* Total attendance records

### Daily Attendance Summary

The system can generate a summary of attendance for a selected day.

Example:

```text
Daily Attendance Summary
------------------------
Total Employees: 20
Present: 17
Absent: 3
Currently Working: 8
Completed Shifts: 9
Late Employees: 4
```

### Employee Performance Summary

The system can provide basic attendance information for individual employees.

It can show:

* Number of attendance records
* Number of late arrivals
* Total working hours
* Average working hours
* Attendance history

This provides a simple overview of an employee's attendance behavior.

### Attendance Reports

The system includes attendance reporting functionality.

Reports can be used to review:

* Daily attendance
* Employee attendance
* Working hours
* Late employees
* Attendance statistics

Reports help administrators review attendance information without checking each transaction individually.

### Data Validation

The program checks user input before processing information.

Examples include:

* Checking if an employee ID exists
* Checking if required information is entered
* Preventing duplicate employee IDs
* Preventing invalid clock-in actions
* Preventing invalid clock-out actions
* Checking whether an employee is already clocked in
* Checking whether an employee has an active attendance record

This helps prevent common input errors.

### Duplicate Clock-In Prevention

An employee cannot clock in again while they already have an active clock-in record.

For example:

```text
Employee 1001 is already clocked in.
Please clock out first.
```

This prevents duplicate attendance records.

### Clock-Out Validation

Employees can only clock out if they have an active clock-in record.

If an employee has not clocked in, the system will display an appropriate message instead of creating an invalid clock-out record.

### Employee Removal

Administrators can remove employees from the employee list.

Before removing an employee, the system can verify that the employee exists.

This helps prevent accidental deletion of unknown employee records.

### Employee Information Editing

Existing employee information can be updated when necessary.

This allows administrators to correct or change employee details without creating a completely new employee record.

### Menu-Based System

The Python application uses a menu-based interface to make the system easy to navigate.

Example:

```text
=================================
     COMPANY ATTENDANCE SYSTEM
=================================

1. Employee Management
2. Clock In
3. Clock Out
4. Today's Attendance
5. Attendance Records
6. Search Attendance
7. Attendance Statistics
8. Attendance Reports
9. Exit
```

The user can select an option by entering its corresponding number.

---

## How the System Works

### 1. Start the Program

Run the Python program from your Python IDE or terminal.

The main menu will appear.

### 2. Manage Employees

Administrators can add, view, search, edit, or remove employees.

Each employee is assigned an employee ID.

### 3. Clock In

When an employee begins work, their employee ID is entered into the system.

The system records the current date and time.

### 4. Work During the Shift

The employee remains marked as currently working until they clock out.

### 5. Clock Out

When the employee finishes work, they enter their employee ID again.

The system records the clock-out time and calculates their working hours.

### 6. Review Attendance

Administrators can view attendance records and check employee attendance information.

### 7. Generate Reports

Attendance statistics and reports can be viewed to summarize employee attendance.

---

## Example Attendance Record

```text
Employee ID: 1001
Employee Name: Juan Dela Cruz
Date: 2026-09-24
Clock In: 08:03 AM
Clock Out: 05:02 PM
Working Hours: 8 hours 59 minutes
Status: Present
```

---

## Example Late Record

```text
Employee ID: 1002
Employee Name: Maria Santos
Expected Time: 08:00 AM
Clock In: 08:17 AM
Status: Late
```

---

## Example Employee List

```text
----------------------------------------
Employee ID    Name
----------------------------------------
1001           Juan Dela Cruz
1002           Maria Santos
1003           Pedro Reyes
1004           Ana Garcia
----------------------------------------
```

---

## Project Structure

```text
Clock In Clock Out/
│
├── main.py
├── employee.py
├── attendance.py
├── reports.py
└── README.md
```

> The exact files may vary depending on the current version of the project.

---

## Technologies Used

* **Python**
* **Python DateTime**
* **Lists**
* **Dictionaries**
* **Functions**
* **Loops**
* **Conditional Statements**
* **Input Validation**
* **File Handling / Data Storage** depending on the project version

---

## Python Concepts Demonstrated

This project was created to practice important Python programming concepts.

### Variables

Used to store information such as employee names, IDs, dates, and times.

### Lists

Used to store multiple employee or attendance records.

Example:

```python
employees = []
attendance_records = []
```

### Dictionaries

Used to organize information about individual employees.

Example:

```python
employee = {
    "id": "1001",
    "name": "Juan Dela Cruz"
}
```

### Functions

The program is separated into different functions to make the code easier to understand and maintain.

Examples:

```python
add_employee()
clock_in()
clock_out()
view_attendance()
search_employee()
generate_report()
```

### If / Else Statements

Used to make decisions based on employee and attendance information.

Example:

```python
if employee_exists:
    print("Employee found.")
else:
    print("Employee not found.")
```

### For Loops

Used to go through employee and attendance records.

### While Loops

Used for menus and repeated user input.

### Date and Time

Python's `datetime` functionality is used to record clock-in and clock-out times.

Example:

```python
from datetime import datetime
```

---

## Attendance Workflow

```text
Employee
   |
   v
Enter Employee ID
   |
   v
Employee Found?
   |
   +------ No ------> Display Error
   |
  Yes
   |
   v
Clock In
   |
   v
Employee Works
   |
   v
Clock Out
   |
   v
Calculate Working Hours
   |
   v
Save Attendance Record
```

---

## Attendance Management Workflow

```text
Employee Management
        |
        v
   Add Employee
        |
        v
   Employee List
        |
        v
     Clock In
        |
        v
    Work Shift
        |
        v
     Clock Out
        |
        v
Working Hours Calculated
        |
        v
 Attendance Record
        |
        v
Reports and Statistics
```

---

## Input Validation

The program includes validation to make the system more reliable.

The system checks for situations such as:

```text
Invalid Employee ID
Employee Already Exists
Employee Not Found
Already Clocked In
Not Clocked In
Invalid Menu Option
Empty Input
Invalid Attendance Record
```

---

## Benefits of the System

The system provides a simple way for a company to:

* Manage employees
* Record employee attendance
* Track clock-in times
* Track clock-out times
* Calculate working hours
* Monitor late employees
* Search attendance records
* View employee history
* Generate attendance summaries
* Review attendance statistics

---

## Future Improvements

Possible future features include:

* SQLite database integration
* MySQL database integration
* Login and administrator accounts
* Employee profile pictures
* Employee departments
* Employee positions
* Different work schedules
* Overtime tracking
* Break time tracking
* Leave management
* Holiday management
* Payroll integration
* Export reports to CSV
* Export reports to Excel
* PDF attendance reports
* Graphs and charts
* Monthly attendance reports
* Weekly attendance reports
* Web application version
* GUI version using Tkinter or CustomTkinter
* Automatic backup
* Cloud database support

---

## Purpose of the Project

This project was created as a **Python programming project** to practice building a practical application using basic and intermediate programming concepts.

Instead of creating a simple example program, the project demonstrates how Python can be used to create a real-world style **Employee Attendance Management System**.

The project also helps demonstrate how different Python concepts can work together in one application, including functions, lists, dictionaries, loops, conditional statements, date and time handling, validation, and data management.

---

## Learning Goals

Through this project, I practiced:

* Creating Python functions
* Using lists and dictionaries
* Working with loops
* Using conditional statements
* Handling user input
* Validating data
* Working with dates and times
* Managing multiple records
* Calculating time differences
* Creating menu-driven programs
* Organizing Python code
* Building a larger Python project
* Designing a practical real-world application

---

## Version

**Current Version:** Python Attendance Management System

The project may continue to receive new features and improvements as I continue learning Python and software development.

---

## Author

**Jose Manuel Navoa**

Aspiring Information Technology Student

This project was created as part of my learning journey in Python and Information Technology.

---

## License

This project is available for educational and learning purposes.
