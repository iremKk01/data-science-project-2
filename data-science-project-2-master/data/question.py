import psycopg2

## Bu değeri localinde çalışırken kendi passwordün yap. Ama kodu pushlarken 'postgres' olarak bırak.
password = 'postgres'


def connect_db():
    conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",
    user="postgres",
    password=1234)
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="postgres",
        user="postgres",
        password=1234
    )
    conn.set_client_encoding('UTF8')  # <--- TAM BURAYA, 14. SATIR OLARAK
    return conn



def question_1_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students WHERE age > 22 ORDER BY student_id;")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_2_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT course_id, course_name, category FROM courses WHERE category LIKE 'Veritaban%' ORDER BY course_id;")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data



def question_3_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students WHERE student_id IN (1, 2) ORDER BY student_id;")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_4_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT course_id, course_name, category FROM courses WHERE category LIKE 'Veritaban%' ORDER BY course_id;")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_5_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students WHERE age BETWEEN 22 AND 24 ORDER BY student_id;")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_6_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT DISTINCT s.first_name, s.last_name FROM students s JOIN enrollments e ON s.student_id = e.student_id;")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_7_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT c.course_name, COUNT(e.student_id) 
        FROM courses c 
        LEFT JOIN enrollments e ON c.course_id = e.course_id 
        WHERE c.category LIKE 'Veritaban%' 
        GROUP BY c.course_id, c.course_name;
    """)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_8_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT c.course_name, i.name 
        FROM courses c 
        JOIN course_instructors ci ON c.course_id = ci.course_id 
        JOIN instructors i ON ci.instructor_id = i.instructor_id 
        ORDER BY c.course_id;
    """)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_9_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT s.* FROM students s LEFT JOIN enrollments e ON s.student_id = e.student_id WHERE e.student_id IS NULL;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_10_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT c.course_name, AVG(s.age) AS avg_age FROM courses c JOIN enrollments e ON c.course_id = e.course_id JOIN students s ON e.student_id = s.student_id GROUP BY c.course_id, c.course_name ORDER BY c.course_name ASC;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_11_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT DISTINCT category FROM courses;")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_12_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT i.name, COUNT(ci.course_id) FROM instructors i JOIN course_instructors ci ON i.instructor_id = ci.instructor_id GROUP BY i.instructor_id, i.name;")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_13_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM enrollments;")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_14_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT course_id, COUNT(*) FROM enrollments GROUP BY course_id;")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_15_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT student_id, COUNT(*) FROM enrollments GROUP BY student_id;")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data