import sqlite3

# Conecta ao arquivo (ele vai criar se não existir)
conn = sqlite3.connect("musicas.sqlite")
cur = conn.cursor()

# 1. Limpa tudo para não dar erro de "já existe"
cur.executescript(
    """
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT
);

CREATE TABLE Album (
    id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id   INTEGER,
    title       TEXT
);

CREATE TABLE Track (
    id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title       TEXT,
    album_id    INTEGER,
    genre_id    INTEGER,
    len         INTEGER, rating INTEGER, count INTEGER
);
"""
)

# 2. Insere os Dados (Seguindo a ordem hierárquica)
cur.execute("INSERT INTO Artist (name) VALUES (?)", ("Led Zeppelin",))
artist_id = cur.lastrowid  # Pega o ID 1 automaticamente

cur.execute("INSERT INTO Genre (name) VALUES (?)", ("Rock",))
genre_id = cur.lastrowid

cur.execute("INSERT INTO Album (artist_id, title) VALUES (?, ?)", (artist_id, "IV"))
album_id = cur.lastrowid

cur.execute(
    """INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
    VALUES (?, ?, ?, ?, ?, ?)""",
    ("Black Dog", 5, 297, 0, album_id, genre_id),
)

conn.commit()
print("✅ Banco de Dados Criado e Dados Inseridos com Sucesso!")

# 3. Fazendo o JOIN (A mágica que junta as tabelas)
print("\n--- Resultado do JOIN ---")
sqlstr = """
SELECT Track.title, Artist.name, Album.title, Genre.name 
FROM Track 
JOIN Artist JOIN Album JOIN Genre 
    ON Track.album_id = Album.id 
    AND Album.artist_id = Artist.id 
    AND Track.genre_id = Genre.id
"""

for row in cur.execute(sqlstr):
    print(f"Música: {row[0]} | Artista: {row[1]} | Álbum: {row[2]} | Gênero: {row[3]}")

cur.close()







import json
import sqlite3

# Conecta ao banco (cria o arquivo se não existir) [cite: 11, 19]
conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor() # O cursor funciona como um "file handle" [cite: 12, 15]

# Configuração inicial: Apaga e cria as tabelas do zero [cite: 21, 22, 24]
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

# Lendo os dados do arquivo JSON [cite: 34, 35]
fname = 'roster_data_sample.json'
str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:
    name = entry[0]
    title = entry[1]
    role = entry[2]

    print((name, title, role))

    # O "Truque ": INSERT OR IGNORE [cite: 41, 45, 50]
    # Se o nome já existir (UNIQUE), ele apenas ignora e não dá erro [cite: 42, 47]
    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0] # Pega o ID (novo ou antigo) [cite: 67, 68]

    # Mesma lógica para o Curso [cite: 73]
    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    # INSERT OR REPLACE: Se a combinação aluno/curso já existir, ele atualiza [cite: 75, 77]
    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''',
        ( user_id, course_id, role ) )

    # Salva no disco (commit) [cite: 81]
    conn.commit()

print("\nSucesso! O arquivo 'rosterdb.sqlite' foi gerado.")
cur.close()