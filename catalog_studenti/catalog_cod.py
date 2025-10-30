from flask import Flask,render_template, request,redirect
import functii

app = Flask(__name__)

'''
COD BEGINNER
CATALOG DE STUDENTI
1. Input de la user cu : nume, prenume, materii, note
2.Adaugam intr-o b.d. SQLITE (fisier local)
3.Functii: Afisare studenti, cauta dupa nume, calculeaza media studentului/clasei,stergere student, manipulare b.d.
4.Web User Interface
5.Executabil + installer, PLUG AND PLAY!
'''

@app.route("/")
def home():
    return render_template('baza.html')

@app.route("/pagina/<nume_pagina>")
def pagina(nume_pagina):
    try:
        return render_template(f"{nume_pagina}.html")
    except Exception as e:
        return f"{e}Pagina nu exista",404

@app.route("/submit", methods=["POST"])
def submit():
    pagina=request.form.get("pagina")
    if pagina:
        return redirect(f"/pagina/{pagina}")
    return "Nu ai selectat nimic!"

@app.route("/adauga_student",methods=["POST"])
def adauga_student():
    id_student = request.form.get("id_student")
    nume = request.form.get("nume")
    prenume = request.form.get("prenume")
    try:
        if len(id_student) == 7:
            corectitudine = functii.validare_nume(nume, prenume)
            if corectitudine:
                functii.creare_student(id_student, nume, prenume)
                return redirect("/")
            else:
                return render_template("introducere_student.html", eroare="Eroare: Introduceti nume/prenume valid")
        else:
            return render_template("introducere_student.html", eroare="Eroare: Introduceti ID VALID!")
    except Exception as e:
            return render_template("introducere_student.html",eroare=f"Eroare:{e}")

@app.route("/adauga_nota", methods=["POST"])
def introducere_nota():
    id_student = request.form.get("id_student")
    materie = request.form.get("materie").upper()
    if materie in ["M1","M2","M3"]:
        try:
            nota = float(request.form.get("nota"))
        except ValueError:
            return render_template("introducere_nota.html", eroare="Error: Introduceti valoare valida")
        if not (1 <= nota <= 10):
            return render_template("introducere_nota.html", eroare="Error: Introduceti nota 1-10")
        functii.introducere_nota(id_student, materie, nota)
        return render_template("introducere_nota.html", nota="Nota introdusa cu succes")
    else:
        return render_template("introducere_nota.html", eroare="Error: Introduceti MATERIE valida")



@app.route("/afisare_info", methods=["POST"])
def afisareinfo():
    id_student = request.form.get("id_student")
    try:
        id_student=int(id_student)
    except:
        return render_template("afisare_info.html", eroare="Error: ID-ul introdus este gresit!")
    nota_totala = functii.calcul_nota_totala(id_student)
    student_list, note_list = functii.afisare_student(id_student)
    if student_list and note_list:
        student = student_list[0]
        student_dict = {
            "id_student": student[0],
            "Nume": student[1],
            "Prenume": student[2],
            "Nota_Generala": nota_totala
        }
        note = note_list[0]
        note_dict = {}
        materii = ["M1", "M2", "M3"]
        for materie, nota in enumerate(note[1:]):
            if materie < len(materii):
                note_dict[materii[materie]] = nota if nota is not None else "-"

        student_dict["note"] = note_dict
        return render_template("afisare_info.html", student=student_dict)
    else:
        return render_template("afisare_info.html", eroare="Error: Studentul NU exista!")



@app.route("/nota_generala", methods=["POST"])
def calculnote():
    try:
        id_student = int(request.form.get("id_student"))
    except Exception as e:
        return render_template("calcul_note.html", eroare=f"Error: {e}")
    nota_generala = functii.calcul_nota_totala(id_student)
    if nota_generala:
        return render_template("calcul_note.html", nota=nota_generala)
    else:
        return render_template("calcul_note.html", eroare="Error: Studentul NU exista!")


@app.route("/stergere_student", methods=["POST"])
def stergerestudent():
    id_student=request.form.get("id_student")
    if len(id_student) == 7:
        functii.stergere_student(id_student)
        return render_template("stergere_student.html", mesaj="Student șters cu succes!")
    else:
        return render_template("stergere_student.html", eroare="Error: ID-ul introdus este gresit!")

