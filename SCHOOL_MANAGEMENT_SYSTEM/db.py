import psycopg2
import PyQt5

databaseName = 'OKUL YONETIM SISTEMI'
userName = 'postgres'
password = '967272'
hostIp = '127.0.0.1'
hostIpPort = '5432'

# Veritabanına bağlantı
connect = psycopg2.connect(database=databaseName,
                           user=userName,
                           password=password,
                           host=hostIp,
                           port=hostIpPort)

connect.autocommit = True
cursor = connect.cursor()
