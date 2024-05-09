import psycopg2
import settings

def connect():
    try:
        conn = psycopg2.connect(
            user=settings.USER,
            password=settings.PASSWORD,
            host=settings.HOST,
            port=settings.PORT,
            dbname=settings.DATABASE,
            sslmode="disable"
        )
        
        return conn
    except Exception as e:
        print(e)
        print("\nErro ao conectar com banco de dados.")
