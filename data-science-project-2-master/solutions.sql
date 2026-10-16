-- Soru 7:# Veritabanı kategorisindeki kurslara kayıtlı öğrenci sayısını bul. ('student_count' — 'course_id'ye göre sıralı)
SELECT c.course_id, c.course_name, COUNT(e.student_id) AS student_count
FROM courses c
JOIN categories cat ON c.category_id = cat.category_id
LEFT JOIN enrollments e ON c.course_id = e.course_id
WHERE cat.category_name = 'Veritabanı'
GROUP BY c.course_id, c.course_name
ORDER BY c.course_id;
-- Soru 8: #  Her kursun adını ve bu kursu veren öğretmenin adını getir. ('course_name', 'instructor_name' — 'course_id'ye göre sıralı)
SELECT c.course_id, c.course_name, i.name AS instructor_name
FROM courses c
JOIN course_instructors ci ON c.course_id = ci.course_id
JOIN instructors i ON ci.instructor_id = i.instructor_id
ORDER BY c.course_id;
-- Soru 9:  # Hiçbir kursa kayıtlı olmayan öğrencileri listele. (Tüm sütunlar)
SELECT s.*
FROM students s
LEFT JOIN enrollments e ON s.student_id = e.student_id
WHERE e.course_id IS NULL;
-- Soru 10: n# Kurslara göre ortalama öğrenci yaşı nedir? ('course_name', 'avg_age' — 'course_name'e göre alfabetik sıralı)
SELECT c.course_name, AVG(s.age) AS avg_age
FROM courses c
JOIN enrollments e ON c.course_id = e.course_id
JOIN students s ON e.student_id = s.student_id
GROUP BY c.course_name
ORDER BY c.course_name ASC;