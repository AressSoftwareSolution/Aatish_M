import sqlite3


conn = sqlite3.connect("school_activity.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS courses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS enrollments(
    student_id INTEGER,
    course_id INTEGER
)
""")

conn.commit()

def add_student():
    name = input("Enter student name: ")
    cursor.execute("INSERT INTO students(name) VALUES(?)", (name,))
    conn.commit()

def add_course():
    title = input("Enter course title: ")
    cursor.execute("INSERT INTO courses(title) VALUES(?)", (title,))
    conn.commit()

def enroll():
    student_id = int(input("Student ID: "))
    course_id = int(input("Course ID: "))
    cursor.execute("INSERT INTO enrollments VALUES(?,?)", (student_id, course_id))
    conn.commit()

def show_enrollments():
    cursor.execute("""
    SELECT students.name, courses.title
    FROM enrollments
    JOIN students ON students.id = enrollments.student_id
    JOIN courses ON courses.id = enrollments.course_id
    """)
    for row in cursor.fetchall():
        print(row)


while True:
    print("\n1 Add Student")
    print("2 Add Course")
    print("3 Enroll Student")
    print("4 Show Enrollments")
   
    print("5 Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        add_course()
    elif choice == "3":
        enroll()
    elif choice == "4":
        show_enrollments()
    elif choice == "5":
        break

conn.close()
