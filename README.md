# Company Attendance System

A complete **Employee Attendance Management System** developed using Python. This project helps companies manage employee information, track daily attendance, monitor work schedules, and review attendance records through a simple and beginner-friendly desktop application.

The system focuses on **Clock In** and **Clock Out** functionality while providing additional tools for employee management, attendance tracking, working-hours calculation, record searching, and attendance reporting.

The project demonstrates how Python can be used to build a practical application by combining functions, loops, conditional statements, data management, date and time handling, and input validation.

---

## Features

### Employee Management
- Add new employees
- View the employee list
- Search for employees
- Update employee information
- Remove employees
- View individual employee details
- Organize employee information using employee IDs
- Validate employee information
- Prevent duplicate employee IDs

### Clock In
Employees can clock in when they begin their workday.

The system records:
- Employee ID
- Employee name
- Attendance date
- Clock-in time
- Attendance status

The system also prevents employees from clocking in multiple times without first clocking out.

### Clock Out
Employees can clock out when they finish their workday.

The system records:
- Clock-out date
- Clock-out time
- Total working time
- Attendance record

Employees must have an active clock-in record before they can clock out.

### Today's Attendance
View attendance activity for the current day, including:
- Employees who have clocked in
- Employees who have clocked out
- Employees currently working
- Clock-in times
- Clock-out times
- Total working hours

### Attendance Records
The system maintains attendance information for reviewing employee activity.

Users can:
- View attendance records
- Search attendance records
- Check individual attendance history
- Review clock-in and clock-out times
- Check calculated working hours
- Identify employees who are currently working
- Review previous attendance records

### Attendance Status
The system can use attendance information to identify different employee statuses, depending on the implemented rules.

Examples include:
- Present
- Currently Working
- Completed Shift
- Absent
- Late

### Late Employee Tracking
The system can identify employees who clock in after their expected work start time, provided that a scheduled start time is configured.

Late attendance information may include:
- Employee ID
- Employee name
- Expected start time
- Actual clock-in time
- Late status

### Working Hours Calculation
The system calculates the time between clock-in and clock-out.

Example:

```text
Clock In: 08:00 AM
Clock Out: 05:00 PM

Working Hours: 9 hours
```

The actual calculation depends on the recorded timestamps. Break deductions and overtime rules require additional implementation.

### Employee Attendance History
Review individual attendance records to check:
- Previous clock-ins
- Previous clock-outs
- Attendance dates
- Working hours
- Late arrivals, when supported
- Attendance patterns

### Attendance Search
Search for attendance information using available employee and attendance details, such as:
- Employee ID
- Employee name
- Attendance date
- Attendance status

### Attendance Statistics
The system can summarize attendance information using available records.

Possible statistics include:
- Total employees
- Employees present
- Employees absent
- Employees currently working
- Completed shifts
- Late employees
- Total attendance records

### Daily Attendance Summary
Generate an overview of employee attendance for a particular day.

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

*The figures above are examples only.*

### Employee Attendance Summary
Review an employee's attendance information, including:
- Number of attendance records
- Total working hours
- Average working hours
- Attendance history
- Late arrivals, when supported

### Attendance Reports
The reporting features help administrators review attendance information without manually checking every record.

Depending on the implemented version, reports may include:
- Daily attendance
- Individual employee attendance
- Working-hours summaries
- Late employee records
- Attendance statistics

### Data Validation
The system validates user input to help prevent common errors.

Examples include:
- Checking whether an employee ID exists
- Checking required information
- Preventing duplicate employee IDs
- Preventing duplicate clock-ins
- Preventing clock-outs without an active attendance record
- Handling invalid menu selections
- Checking for missing or invalid information

### Employee Information Editing
Administrators can update existing employee information without creating a completely new employee record.

### Employee Removal
Administrators can remove employees after checking whether the specified employee exists.

### Menu-Based Navigation
The Python application uses a menu-based interface that allows users to select available operations.

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

*The actual menu options depend on the current version of the source code.*

---

## How the System Works

### 1. Start the Program
Run the Python application using PyCharm, another Python IDE, or a terminal.

### 2. Manage Employees
Add employees and manage their information using their employee IDs.

### 3. Clock In
Enter the employee ID to record the employee's clock-in date and time.

### 4. Work During the Shift
The employee remains marked as currently working until a valid clock-out is recorded.

### 5. Clock Out
Enter the employee ID again to record the clock-out time and calculate the working duration.

### 6. Review Attendance
View daily attendance, search records, and review individual employee histories.

### 7. Check Statistics and Reports
Use the available reporting features to review attendance information and summarize employee activity.

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

## Example Late Record

```text
Employee ID: 1002
Employee Name: Maria Santos
Expected Time: 08:00 AM
Clock In: 08:17 AM
Status: Late
```

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

*These examples illustrate the expected output format and are not actual records from the program.*

---

## Project Structure

The project may be organized into separate Python files to make the code easier to maintain.

```text
Company Attendance System/
│
├── main.py
├── database.py
├── dashboard.py
├── employees.py
├── attendance.py
├── README.md
└── company_attnce.db
```

The exact structure depends on the version being used. Files such as `dashboard.py` and `database.py` may be present in the desktop version, while a web version may use HTML, CSS, and JavaScript instead.

---

## Technologies Used

- **Python** — Main programming language
- **CustomTkinter** — Desktop interface
- **SQLite** — Local database storage
- **datetime** — Date and time handling
- **Tkinter Treeview** — Tabular record display, where implemented
- **Lists and Dictionaries** — Organizing information
- **Functions** — Separating program operations
- **Loops and Conditional Statements** — Managing program flow
- **Input Validation** — Checking user entries

---

## Python Concepts Demonstrated

### Variables
Store employee information, IDs, attendance dates, times, and calculated working durations.

### Lists and Dictionaries
Organize employee and attendance information in memory or prepare records for database operations.

### Functions
Separate the program into smaller operations, such as employee management, clock-in processing, clock-out processing, and attendance reporting.

### Conditional Statements
Use `if`, `elif`, and `else` to validate information and determine which actions the system should perform.

### Loops
Use loops to display menus, process records, and allow users to perform multiple operations.

### Date and Time Handling
Use Python's `datetime` functionality to record timestamps and calculate working durations.

```python
from datetime import datetime
```

### Database Operations
Where SQLite is implemented, database operations allow the system to save, retrieve, update, and delete employee and attendance records.

### Input Validation
Check user entries before processing them to reduce invalid operations and incorrect records.

### GUI Development
The desktop version uses a graphical interface to organize employee management, attendance records, and dashboard information.

---

## Attendance Workflow

```text
        Start
          |
          v
   Enter Employee ID
          |
          v
    Employee Found?
       /       \
     No         Yes
     |           |
     v           v
Display Error  Check Attendance
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
       Calculate Working Hours
                  |
                  v
        Save Attendance Record
                  |
                  v
       View Reports and Statistics
```

## Attendance Management Workflow

```text
Employee Management
        |
        v
   Add Employee
        |
        v
  Manage Employee Data
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
Calculate Working Hours
        |
        v
Save Attendance Record
        |
        v
Attendance History
        |
        v
Reports and Statistics
```

---

## Benefits of the System

The project provides a practical way to:
- Manage employee information
- Record employee attendance
- Track clock-in and clock-out times
- Calculate working hours
- Monitor employee attendance status
- Search attendance records
- Review individual attendance histories
- View daily attendance activity
- Generate attendance summaries
- Organize records in a structured application

---

## Future Improvements

Possible enhancements include:
- Administrator login and account permissions
- Employee profile pictures
- Employee departments and positions
- Configurable work schedules
- More advanced late-arrival rules
- Overtime calculation
- Break-time tracking
- Leave and holiday management
- Payroll integration
- CSV and Excel report exports
- PDF attendance reports
- Attendance graphs and charts
- Weekly and monthly reports
- Automatic database backups
- Cloud database integration
- Web-based employee portal
- Improved dashboard analytics
- More advanced employee search and filtering

---

## Purpose of the Project

The Company Attendance System was developed as a Python programming project to practice building a practical, real-world-style application.

It demonstrates how programming concepts can be combined to manage employee information, record attendance, calculate working hours, validate user actions, and present useful attendance information.

The project also provides experience in organizing code, working with databases, and developing a desktop application.

## Learning Goals

Through this project, I practiced:
- Creating and organizing Python functions
- Using variables, lists, and dictionaries
- Working with loops and conditional statements
- Handling and validating user input
- Working with dates and times
- Calculating working durations
- Managing employee and attendance records
- Using database operations
- Building a graphical user interface
- Organizing a multi-file Python project
- Developing a practical application

---

## Version

**Project:** Company Attendance System  
**Platform:** Python desktop application  
**Storage:** SQLite, where implemented

The project may continue to receive new features and improvements as I continue learning Python and Information Technology.

---

## Author

**Jose Manuel Navoa**

Aspiring Information Technology Student

This project was created as part of my learning journey in Python and Information Technology.

---

## License

This project is available for educational and learning purposes.
