# Flask README - Dein Projekt

## App starten

```bash
python run.py
```

Oder mit Flask CLI:
```bash
flask run
```

Die App ist dann unter http://127.0.0.1:5000 erreichbar.

---

## Projekt-Struktur

```
SQL_Uebung_V2/
├── run.py                  # Startdatei - hier startest du die App
├── app/
│   ├── __init__.py         # Flask-App Erstellung (nicht ändern)
│   ├── routes/             # Deine Routen/Seiten
│   │   └── __init__.py      # Blueprint-Definition
│   ├── templates/          # HTML-Dateien
│   │   └── index.html
│   └── static/             # CSS, JS, Bilder
│       └── style.css
```

---

## Eigene Seiten erstellen

### 1. Neue Route in `app/routes/__init__.py`

```python
from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

# NEUE SEITE - Beispiel: /about
@bp.route('/about')
def about():
    return render_template('about.html')
```

### 2. HTML-Template erstellen in `app/templates/`

Erstelle z.B. `about.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Über uns</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Über uns</h1>
    <p>Willkommen!</p>
    <a href="{{ url_for('main.index') }}">Zurück zur Startseite</a>
</body>
</html>
```

---

## Daten an Template übergeben

### Aus Python an HTML übergeben:

```python
@bp.route('/test')
def test():
    name = "Max"
    alter = 25
    return render_template('test.html', name=name, alter=alter)
```

### In HTML verwenden:

```html
<h1>Hallo {{ name }}!</h1>
<p>Du bist {{ alter }} Jahre alt.</p>
```

---

## Statische Dateien (CSS/JS/Bilder)

### CSS in `app/static/style.css` schreiben

### Im HTML einbinden:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

### JavaScript:

```html
<script src="{{ url_for('static', filename='script.js') }}"></script>
```

### Bilder:

```html
<img src="{{ url_for('static', filename='bild.png') }}">
```

---

## Datenbank (SQLite) - Optional

Falls du eine Datenbank brauchst:

```python
from flask import Flask
import sqlite3

def create_app():
    app = Flask(__name__)
    
    # Datenbank-Verbindung
    def get_db():
        conn = sqlite3.connect('datenbank.db')
        conn.row_factory = sqlite3.Row
        return conn
    
    # Route mit Datenbank-Abfrage
    @app.route('/benutzer')
    def benutzer():
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM benutzer")
        daten = cur.fetchall()
        conn.close()
        return render_template('benutzer.html', daten=daten)
    
    return app
```

---

## Formulare verarbeiten

### HTML-Formular:

```html
<form method="POST" action="/submit">
    <input type="text" name="name" required>
    <button type="submit">Absenden</button>
</form>
```

### Python-Route:

```python
from flask import request

@bp.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    return f"Hallo {name}!"
```

---

## Wichtig zu wissen

1. **Immer im Hauptverzeichnis arbeiten** (`SQL_Uebung_V2/`), nicht in `app/` Dateien ändern die du selbst schreibst
2. **Nach Änderungen:** Server startet neu (debug=True in run.py)
3. **Templates:** Heißen `*.html` und kommen in `app/templates/`
4. **CSS/JS/Bilder:** kommen in `app/static/`
5. **Neue Seiten:** Routen in `app/routes/__init__.py` hinzufügen

---

## Troubleshooting

**Fehler: "Module not found"**
```bash
pip install flask
```

**Fehler: "Template not found"**
- Prüfe ob die .html Datei in `app/templates/` liegt
- Prüfe den Namen genau (Groß-/Kleinschreibung)

**App startet nicht:**
- Prüfe ob du im richtigen Verzeichnis bist
- Prüfe ob das Virtual Environment aktiviert ist
