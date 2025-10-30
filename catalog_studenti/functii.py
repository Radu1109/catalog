import catalog_db
import re


def get_cursor():
    db, cursor = catalog_db.init_db()
    return db,cursor
def creare_student(id_student,nume, prenume):
    db, cursor = get_cursor()
    try:
        query = "INSERT INTO studenti (id_student, nume, prenume) VALUES (?, ?, ?)"
        values = (id_student,nume,prenume)
        cursor.execute(query,values)
        print("Student adaugat cu succes")
        cursor.execute("INSERT INTO note_studenti (id_student) VALUES (?)", (id_student,))
        db.commit()
    except Exception as e:
        print("Something went wrong",e)
    cursor.close()
    db.close()

def validare_nume(nume,prenume):
    pattern = r"^[A-Za-z\- ]+$"
    if re.match(pattern,nume) and re.match(pattern,prenume):
        return True
    else:
        return False

def stergere_student(id_student):
    db,cursor = get_cursor()
    query = "SELECT * FROM studenti where id_student = ?"
    values=(id_student,)
    cursor.execute(query,values)
    exista=cursor.fetchone()
    if exista:
        cursor.execute("DELETE FROM studenti where id_student = ?",values)
        cursor.execute("DELETE FROM note_studenti where id_student = ?",values)
        db.commit()
    else:
        return("Studentul nu exista!")
    cursor.close()
    db.close()

def afisare_student(id_student):
    db, cursor = get_cursor()
    query1 = ("SELECT * FROM studenti WHERE id_student=?")
    values = (id_student,)
    cursor.execute(query1,values)
    student = cursor.fetchall()
    print(student)
    query2 = ("SELECT * FROM note_studenti WHERE id_student=?")
    cursor.execute(query2,values)
    note= cursor.fetchall()
    cursor.close()
    db.close()
    return student,note

def introducere_nota(id_student,materie,nota):
    db, cursor = get_cursor()
    query = f"UPDATE note_studenti SET {materie} = ? WHERE id_student = ?"
    cursor.execute(query,(nota,id_student))
    db.commit()
    cursor.close()
    db.close()

def calcul_nota_totala(id_student):
    db, cursor = get_cursor()
    query=("SELECT * FROM note_studenti WHERE id_student=?")
    values=(id_student,)
    cursor.execute(query,values)
    note=cursor.fetchall()
    if not note:
        cursor.close()
        db.close()
        return("Studentul nu exista")
    note=note[0][1:]
    if None in note:
        cursor.close()
        db.close()
        return("Studentul nu are note suficiente!")
    else:
        nota_generala = sum(note) / len(note)
        cursor.execute("UPDATE studenti SET Nota_Generala = ? WHERE id_student = ?",(nota_generala,id_student))
        cursor.close()
        db.close()
        return nota_generala