from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)# Conexão com o banco de dados

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="escola"
    )

# 🔹 LISTAR ALUNOS
@app.route("/")
def index():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM aluno")
    alunos = cursor.fetchall()

    conexao.close()
    return render_template("index.html", alunos=alunos)

# 🔹 CADASTRAR ALUNO
@app.route("/cadastrar_aluno", methods=["POST"])
def cadastrar_aluno():
    nome = request.form["nome"]
    idade = request.form["idade"]
    email = request.form["email"]

    conexao = conectar()
    cursor = conexao.cursor()

    sql = "INSERT INTO aluno (nome, idade, email) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nome, idade, email))

    conexao.commit()
    conexao.close()

    return redirect("/")

# 🔹 LISTAR CURSOS
@app.route("/cursos")
def cursos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM curso")
    cursos = cursor.fetchall()

    conexao.close()
    return render_template("cursos.html", cursos=cursos)

# 🔹 CADASTRAR CURSO
@app.route("/cadastrar_curso", methods=["POST"])
def cadastrar_curso():
    nome = request.form["nome"]
    descricao = request.form["descricao"]

    conexao = conectar()
    cursor = conexao.cursor()

    sql = "INSERT INTO curso (nome, descricao) VALUES (%s, %s)"
    cursor.execute(sql, (nome, descricao))

    conexao.commit()
    conexao.close()

    return redirect("/cursos")

# 🔹 MATRÍCULA
@app.route("/matricular", methods=["GET", "POST"])
def matricular():
    conexao = conectar()
    cursor = conexao.cursor()

    if request.method == "POST":
        aluno_id = request.form["aluno_id"]
        curso_id = request.form["curso_id"]

        sql = """
        INSERT INTO matricula (aluno_id, curso_id, data_matricula)
        VALUES (%s, %s, CURDATE())
        """
        cursor.execute(sql, (aluno_id, curso_id))
        conexao.commit()

        return redirect("/matricular")

    # GET → mostrar dados
    cursor.execute("SELECT * FROM aluno")
    alunos = cursor.fetchall()

    cursor.execute("SELECT * FROM curso")
    cursos = cursor.fetchall()

    conexao.close()

    return render_template("matricula.html", alunos=alunos, cursos=cursos)

if __name__ == "__main__":
    app.run(debug=True)