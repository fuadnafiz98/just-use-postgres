import psycopg
from psycopg.rows import dict_row
import logging

logging.basicConfig(level=logging.DEBUG)

logging.getLogger("psycopg").setLevel(logging.DEBUG)


POSTGRESQL_CONN_STR = "postgresql://postgres:secure_password@localhost:5432/local_db"

with psycopg.connect(conninfo=POSTGRESQL_CONN_STR, row_factory=dict_row) as conn:
    cur = conn.execute("""
            CREATE TABLE IF NOT EXISTS test (
                id serial PRIMARY KEY, 
                counter integer
            )
        """)

    record = conn.execute("""
            SELECT * from test
        """).fetchone()
    print(record)
    conn.commit()
