import sqlite3


conn = sqlite3.connect("school.db")
cursor = conn.cursor()  # Cursor is used to execute the SQL commands


cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY,
    title TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS enrollments (
    student_id INTEGER,
    course_id INTEGER
)
""")

conn.commit()  # this is to save changes permamnently


cursor.execute("INSERT INTO students (name) VALUES (?)", ("Rahul",))
cursor.execute("INSERT INTO students (name) VALUES (?)", ("Priya",))

cursor.execute("INSERT INTO courses (title) VALUES (?)", ("Math",))
cursor.execute("INSERT INTO courses (title) VALUES (?)", ("Science",))

cursor.execute("INSERT INTO enrollments VALUES (?, ?)", (1, 1))
cursor.execute("INSERT INTO enrollments VALUES (?, ?)", (1, 2))
cursor.execute("INSERT INTO enrollments VALUES (?, ?)", (2, 2))

conn.commit()


print("\nAll Students:")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)


cursor.execute(
    "UPDATE students SET name = ? WHERE id = ?",
    ("Rahul Sharma", 1)
)
conn.commit()

print("\nAfter Update:")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

cursor.execute("DELETE FROM students WHERE id = ?", (2,))
conn.commit()

print("\nAfter Delete:")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)


print("\nStudent Enrollments (JOIN):")
cursor.execute("""
SELECT students.name, courses.title
FROM enrollments
JOIN students ON students.id = enrollments.student_id
JOIN courses ON courses.id = enrollments.course_id
""")

for row in cursor.fetchall():
    print(row)


print("\nCourses per Student (Aggregation):")
cursor.execute("""
SELECT students.name, COUNT(enrollments.course_id)
FROM students
LEFT JOIN enrollments
ON students.id = enrollments.student_id
GROUP BY students.name
""")

for row in cursor.fetchall():
    print(row)


conn.close()
