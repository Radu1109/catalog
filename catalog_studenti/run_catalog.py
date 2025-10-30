import os
import webbrowser
from catalog_cod import app
import catalog_db


os.chdir(os.path.dirname(os.path.abspath(__file__)))

def open_browser():
    webbrowser.open("http://127.0.0.1:5000/")

if __name__ == "__main__":
    catalog_db.init_db()
    open_browser()
    app.run(debug=False)