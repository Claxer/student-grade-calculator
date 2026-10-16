        print("15. Failed Subject Report")
        print("16. Attendance Report")
        print("17. Grade Distribution")
        print("18. Class Performance")
        print("19. Compare Two Students")
        print("20. Sort Students")
        print("21. Filter Students")
        print("22. Improvement Calculator")
        print("23. Export Student Report")
        print("24. Export Class Report")
        print("25. Clear All Records")
        print("26. Exit")
        print("27. Export Class Records to CSV")

        print("===================================")

        choice = input("Choose an option: ")

        if choice == "1":
            calculate_student()

        elif choice == "2":
            add_student_record()

        elif choice == "3":
            view_student_records()

        elif choice == "4":
            search_student()

        elif choice == "5":
            display_dashboard()

        elif choice == "6":
            display_class_summary()

        elif choice == "7":
            view_student_details()

        elif choice == "8":
            edit_student_record()

        elif choice == "9":
            delete_student_record()

        elif choice == "10":
            rank_students()

        elif choice == "11":
            display_honor_students()

        elif choice == "12":
            display_students_needing_improvement()

        elif choice == "13":
            display_scholarship_students()

        elif choice == "14":
            display_subject_statistics()

        elif choice == "15":
            display_failed_subject_report()

        elif choice == "16":
            display_attendance_report()

        elif choice == "17":
            display_grade_distribution()

        elif choice == "18":
            display_class_performance()

        elif choice == "19":
            compare_students()

        elif choice == "20":
            sort_students()

        elif choice == "21":
            filter_students()

        elif choice == "22":
            improvement_calculator()

        elif choice == "23":
            export_student_report()

        elif choice == "24":
            export_class_report()

        elif choice == "25":
            clear_all_records()

        elif choice == "26":
            print("\nProgram Ended.")
            break

        elif choice == "27":
            export_class_csv()

        else:
            print("\nInvalid choice. Please choose 1 to 27.")


load_records_from_file()
main()
