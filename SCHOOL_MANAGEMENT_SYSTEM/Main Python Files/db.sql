-- Öğretmenler tablosuna örnek veriler ekleme

INSERT INTO teacher ("teacherID", "teacher_name", "password")
VALUES (1,
        'John Doe',
        1234), (2,
                'Jane Smith',
                5678);

-- Öğrenciler tablosuna örnek veriler ekleme

INSERT INTO students ("studentID", "student_name", "student_surname", "password", "gender", "dateofbirth")
VALUES (1,
        'Alice',
        'Smith',
        1111,
        'Female',
        '2000-01-01'), (2,
                        'Bob',
                        'Johnson',
                        2222,
                        'Male',
                        '2001-02-02');

-- Sınıflar tablosuna örnek veriler ekleme

INSERT INTO classroom ("classID", "class_name", "capacity")
VALUES (1,
        'Class A',
        30), (2,
              'Class B',
              25);

-- Dersler tablosuna örnek veriler ekleme

INSERT INTO lessons ("lessonID", "classID", "teacherID", "lesson_name", "class_name")
VALUES (1,
        1,
        1,
        'Math',
        'Class A'), (2,
                     2,
                     2,
                     'English',
                     'Class B');

-- Ders-Öğretmen ilişkisi tablosuna örnek veriler ekleme

INSERT INTO lesson_teacher ("lessonID", "teacherID")
VALUES (1,
        1), (2,
             2);

-- Ders-Öğrenci ilişkisi tablosuna örnek veriler ekleme

INSERT INTO lesson_student ("lessonID", "studentID", "midterm", "final", "attendance")
VALUES (1,
        1,
        80,
        90,
        100), (1,
               2,
               75,
               85,
               95), (2,
                     3,
                     55,
                     89,
                     40);

