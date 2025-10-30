import sqlite3
import os
import sys

if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.join(os.environ["LOCALAPPDATA"], "CatalogStudenti")
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_PATH = os.path.join(BASE_DIR, "catalog.db")


def init_db():
    create_new = not os.path.exists(DB_PATH)

    conn=sqlite3.connect(DB_PATH)
    cursor=conn.cursor()

    if create_new:
        print("Cream baza de date...")
        cursor.execute("""
            CREATE TABLE studenti (
                id_student INTEGER PRIMARY KEY,
                nume TEXT,
                prenume TEXT,
                Nota_Generala TEXT
            )
        """)
        cursor.execute("""
                    CREATE TABLE note_studenti (
                        id_student INTEGER,
                        M1 REAL,
                        M2 REAL,
                        M3 REAL,
                        FOREIGN KEY (id_student) REFERENCES studenti(id_student) ON DELETE CASCADE
                    )
                """)
        conn.commit()
        print("Baza de date SQLite creată cu tabelele!")

    return conn, cursor