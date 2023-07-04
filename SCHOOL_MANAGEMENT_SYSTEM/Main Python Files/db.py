import psycopg2
from psycopg2 import Error

# Veritabanı bağlantı bilgileri
databaseName = 'postgres'
userName = 'postgres'
password = '12345'
hostIp = '127.0.0.1'
hostIpPort = '5432'

try:
    # Yeni veritabanı oluşturma bağlantısı
    create_db_connection = psycopg2.connect(
        host=hostIp,
        database=databaseName,
        user=userName,
        password=password
    )

    # Veritabanı oluşturma işlemi
    create_db_connection.autocommit = True
    create_db_cursor = create_db_connection.cursor()
    create_db_cursor.execute("CREATE DATABASE schoolmanagement")

    # Yeni veritabanı bağlantısı
    connection = psycopg2.connect(
        host=hostIp,
        database="schoolmanagement",
        user=userName,
        password=password
    )

    # Veritabanı işlemleri burada gerçekleştirilir
    cursor = connection.cursor()

    connection.commit()

    # Bağlantıyı kapatın
    cursor.close()
    connection.close()
    create_db_cursor.close()
    create_db_connection.close()

    print("Veritabani oluşturuldu ve bağlanti yapildi.")

except (Exception, psycopg2.Error) as error:
    print("Veritabanina bağlanirken veya oluştururken hata oluştu:", error)
