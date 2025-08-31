# Catalog Studenți - Python + MySQL

Acest proiect este un **catalog de studenți simplu**, realizat în Python cu MySQL. 
A fost creat ca exercițiu de **refamiliarizare cu Python și manipularea bazelor de date**, nu este un produs final sau complex.

## Funcționalități
- Adăugarea unui student
- Introducerea notelor pe materii
- Afișarea informațiilor despre studenți
- Calcularea mediei generale
- Ștergerea unui student

## Scop
Proiectul a fost realizat ca un cod **ultra basic**, menit să ajute la învățarea conceptelor de bază: 
- interacțiunea cu baza de date MySQL
- manipularea datelor cu Python
- separarea logicii de meniul principal

## Cerințe
- Python 3.10+
- MySQL
- Pachet `mysql-connector-python`
- Pachet `python-dotenv`

## Instalare
1. Clonează repository-ul:
   ```bash
   git clone https://github.com/Radu1109/catalog.git

2. Crează un mediu virtual (opțional):

python -m venv .venv

3. Instalează dependențele:

pip install -r requirements.txt


4. Crează fișierul .env cu datele bazei tale MySQL:

DB_HOST=localhost
DB_USER=catalog_user
DB_PASS=parola_ta
DB_NAME=catalog


Rulează aplicația:

python main.py
