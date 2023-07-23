import psycopg2
from psycopg2 import Error

# # Veritabanı bağlantı bilgileri
# databaseName = 'postgres'
# userName = 'postgres'
# password = '12345'
# hostIp = '127.0.0.1'
# hostIpPort = '5432'

try:
    # Yeni veritabanı oluşturma bağlantısı
    # create_db_connection = psycopg2.connect(
    #     host=hostIp,
    #     database=databaseName,
    #     user=userName,
    #     password=password,
    #     port=hostIpPort
    # )

    # # Veritabanı oluşturma işlemi
    # create_db_connection.autocommit = True
    # create_db_cursor = create_db_connection.cursor()
    # # create_db_cursor.execute("CREATE DATABASE schoolmanagement")
    host = "localhost"  # PostgreSQL sunucu adresi
    port = "5432"  # PostgreSQL bağlantı noktası
    database = "schoolmanagement"  # Veritabanı adı
    username = "postgres"  # PostgreSQL kullanıcı adı
    password = "12345"  # PostgreSQL kullanıcı parolası
    # Yeni veritabanı bağlantısı
    connection = psycopg2.connect(
        host=host,
        port=port,
        database="schoolmanagement",
        user=username,
        password=password
    )

    # Veritabanı işlemleri burada gerçekleştirilir
    cursor = connection.cursor()
    connection.commit()
    sql_query = """
            SELECT s."studentID", s.student_name, s.student_surname, s.gender, s.dateofbirth,
                ls.midterm, ls.final,
                l."lessonID", l.lesson_name
            FROM students s
            JOIN lesson_student ls ON s."studentID" = ls."studentID"
            JOIN lessons l ON ls."lessonID" = l."lessonID";
        """

    # SQL sorgusunu çalıştırma
    cursor.execute(sql_query)
    connection.commit()
    # Sonuçları almak
    results = cursor.fetchall()
    print("sonuc: ", results)
    for row in results:
        print("tumu: ", row)

    # Sonuçları işleme
    for row in results:
        # Her bir satırdaki verileri al
        studentID, student_name, student_surname, gender, dateofbirth, midterm, final, lessonID, lesson_name = row

        # İşlem yapmak veya sonuçları kullanmak için burada kodunuzu yazın
        print(
            f"Student ID: {studentID}, Name: {student_name}, Surname: {student_surname}, Gender: {gender}, Date of Birth: {dateofbirth}")
        print(f"Midterm: {midterm}, Final: {final}")
        print(f"Lesson ID: {lessonID}, Lesson Name: {lesson_name}")
        print("-------------------------------------------")
    # Bağlantıyı kapatın
    cursor.close()
    connection.close()
    # create_db_cursor.close()
    # create_db_connection.close()

    print("Veritabani oluşturuldu ve bağlanti yapildi.")

except (Exception, psycopg2.Error) as error:
    print("Veritabanina bağlanirken veya oluştururken hata oluştu:", error)
