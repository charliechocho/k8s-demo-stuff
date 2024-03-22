import psycopg2
from dotenv import load_dotenv
from os import getenv

load_dotenv()

con = psycopg2.connect(database=getenv('PG_DB_NAME'),
                        host=getenv('PG_HOST'),
                        user=getenv('PG_USER'),
                        password=getenv('PG_PASSWORD'),
                        port=getenv('PG_PORT'))


def table_check(con):
    cursor = con.cursor()
    cursor.execute("select exists(select relname from pg_class where relname = 'users')")
    status = cursor.fetchone()[0]
    cursor.close()
    return status

def table_create(con):
    cursor = con.cursor()
    cursor.execute("""CREATE TABLE users(
        uuid_no uuid PRIMARY KEY,
        user_name VARCHAR (50) UNIQUE NOT NULL,
        user_last_name VARCHAR (50) NOT NULL,
        gender VARCHAR (20) NOT NULL);
        """)
    con.commit()
    

table_exists = table_check(con)

    


con.close()

