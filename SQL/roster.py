import json
import sqlite3

# Conexão com o banco de dados e criação do cursor (file handle) [cite: 28, 29]
conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Configuração das tabelas: Drop e Create [cite: 34, 49]
# Usamos executescript para rodar múltiplos comandos de uma vez [cite: 34, 35]
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

# Solicita o nome do arquivo ao usuário
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data.json'

# Lendo e parseando o arquivo JSON [cite: 68, 69]
try:
    str_data = open(fname).read()
    json_data = json.loads(str_data)
except:
    print(f"Erro: Não foi possível encontrar o arquivo {fname}")
    quit()

for entry in json_data:
    name = entry[0]   # Nome do usuário [cite: 74]
    title = entry[1]  # Título do curso [cite: 74]
    role = entry[2]   # Função (0 ou 1) [cite: 25, 71]

    print((name, title, role))

    # Inserindo Usuário (ignora se já existir devido ao UNIQUE) [cite: 41, 45, 47]
    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0] # Recupera o ID gerado ou existente

    # Inserindo Curso (ignora se já existir devido ao UNIQUE) [cite: 73]
    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    # Inserindo na tabela conectora Member
    # INSERT OR REPLACE lida com a chave primária composta (user_id + course_id) [cite: 27]
    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''',
        ( user_id, course_id, role ) )

# Salva todas as alterações no disco [cite: 81]
conn.commit()

# --- PARTE FINAL: GERAR O CÓDIGO DE VERIFICAÇÃO PARA O SITE ---
print("\n" + "="*40)
print("GERANDO CÓDIGO DE VERIFICAÇÃO")

sql_verificacao = '''
SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X 
FROM User JOIN Member JOIN Course 
ON User.id = Member.user_id AND Member.course_id = Course.id
ORDER BY X LIMIT 1
'''

cur.execute(sql_verificacao)
resultado = cur.fetchone()

if resultado:
    print("COPIE O CÓDIGO ABAIXO E COLE NO SITE:")
    print(resultado[0])
print("="*40)

cur.close()
conn.close()