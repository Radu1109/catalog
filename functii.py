import mysql.connector
from dotenv import load_dotenv
load_dotenv(r"/.env")
import os
import re

host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASS")
database = os.getenv("DB_NAME")

db = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor=db.cursor()


def creare_student(nume, prenume):
    try:
        query = "INSERT INTO studenti (nume, prenume) VALUES (%s, %s)"
        values = (nume,prenume)
        cursor.execute(query,values)
        db.commit()
        print("Student adaugat cu succes")
        id_student = cursor.lastrowid
        cursor.execute("INSERT INTO note_studenti (id_student) VALUES (%s)", (id_student,))
        db.commit()
    except ValueError:
        print("Input only string")
    except Exception as e:
        print("Something went wrong",e)

def validare_nume(nume,prenume):
    pattern = r"^[A-Za-z\- ]+$"
    if re.match(pattern,nume) and re.match(pattern,prenume):
        return True
    else:
        return False

def stergere_student(id_student):
    query = "DELETE FROM studenti WHERE id_student = %s"
    values = (id_student,)
    cursor.execute(query,values)
    db.commit()

def afisare_student(id_student):
    query = ("SELECT * FROM studenti WHERE id_student=%s")
    values = (id_student,)
    cursor.execute(query,values)
    student = cursor.fetchall()
    for i in student:
        print(f"ID:{i[0]},Nume:{i[1]},Prenume:{i[2]},Nota:{i[3]}")

def preia_nume_prenume(id_student):
    query = "SELECT nume, prenume FROM studenti WHERE id_student = %s"
    cursor.execute(query, (id_student,))
    return cursor.fetchone()

def introducere_nota(id_student,materie,nota):
    query = f"UPDATE note_studenti SET {materie} = %s WHERE id_student = %s"
    cursor.execute(query,(nota,id_student))
    db.commit()

def preia_note_student(id_student):
    query = "SELECT M1, M2, M3, M4, M5 FROM note_studenti WHERE id_student = %s"
    cursor.execute(query, (id_student,))
    rezultat = cursor.fetchone()
    return rezultat

def calcul_nota_totala(note):
    if None in note:
        print("Studentul nu are note suficiente!")
    else:
        nota_generala = sum(note) / len(note)
        return nota_generala

def introducere_nota_generala(id_student, nota_generala):
    query = "UPDATE studenti SET nota = %s WHERE id_student = %s"
    cursor.execute(query, (nota_generala,id_student))
    db.commit()

def Meniu():
    while True:
        try:
            print("Ce actiune doriti sa folositi?: \n"
                  "1.Introducere student \n"
                  "2.Introducere nota \n"
                  "3.Afisare informatii \n"
                  "4.Calcul nota generala \n"
                  "5.Stergere student \n"
                  "6.Exit\n")
            user_input = int(input())
            if user_input == 1:
                print("Introduceti numele si prenumele studentului\n")
                nume = input("Nume: \n")
                prenume = input("Prenume: \n")
                if validare_nume(nume,prenume) is True:
                    creare_student(nume,prenume)
                else:
                    print("Introduceti nume si prenume valabil!")
            elif user_input == 2:
                id_student = int(input("Id student:\n"))
                materie = input("Introduceti materia dorita M1-M5: \n").upper()
                if materie in ["M1", "M2", "M3", "M4", "M5"]:
                    nota = float(input("Introduceti nota: \n"))
                    if nota <= 10:
                        introducere_nota(id_student, materie, nota)
                        print("Nota introdusa cu succes!")
                    else:
                        print("Nota trebuie sa fie intre 0-10")
                else:
                    print("Materia nu exista!")
            elif user_input == 3:
                id_student = int(input("Id student:\n"))
                afisare_student(id_student)
                print(f"{preia_note_student(id_student)}")
            elif user_input == 4:
                id_student = int(input("Id student:\n"))
                note = preia_note_student(id_student)
                nota_generala = calcul_nota_totala(note)
                print(f"Nota generala: {nota_generala}")
                introducere_nota_generala(id_student,nota_generala)
            elif user_input == 5:
                id_student = int(input("Id student:\n"))
                student = preia_nume_prenume(id_student)
                if student is None:
                    print("Nu exista acel student")
                else:
                    nume_prenume = preia_nume_prenume(id_student)
                    stergere_student(id_student)
                    print(f"Studentul {nume_prenume[0]},{nume_prenume[1]} a fost sters!")
            elif user_input == 6:
                print("Exitting")
                break
            else:
                print("Alegeti un numar de la 1-6")
        except ValueError:
            print("Introduceti un numar de la 1-6")
            continue
        except Exception as e:
            print("This command went wrong",e)