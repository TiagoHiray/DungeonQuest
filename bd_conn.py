import mysql.connector

from settings import *

conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password=SENHA_BD,
        database='dungeonQuest'
    )

# Cria um cursor para executar comandos SQL
cursor = conexao.cursor()
