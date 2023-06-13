import random as rd
import mysql.connector

class Question:
    def __init__(self, id, materia, enunciation, alternative1, alternative2, alternative3, alternative4, resposta_correta, feedback):
        self.id = id
        self.enunciation = str(enunciation)
        self.alternatives = [alternative1, alternative2, alternative3, alternative4]
        rd.shuffle(self.alternatives)
        if self.alternatives[0] == resposta_correta:
            self.answer = 0
        elif self.alternatives[1] == resposta_correta:
            self.answer = 1
        elif self.alternatives[2] == resposta_correta:
            self.answer = 2
        elif self.alternatives[3] == resposta_correta:
            self.answer = 3
        self.feedback = feedback
        self.materia = materia

questao_exemplo = Question(0, 'Matemática', 'Quanto é 1 + 1?', '2', '11', '3', '5', '2', 'Matematicamente, 1 + 1 é igual a dois.')

questoes = [questao_exemplo, questao_exemplo, questao_exemplo, questao_exemplo, questao_exemplo, questao_exemplo, questao_exemplo, questao_exemplo, questao_exemplo, questao_exemplo, questao_exemplo, questao_exemplo, questao_exemplo, questao_exemplo, questao_exemplo, questao_exemplo, questao_exemplo, questao_exemplo]

import mysql.connector

# Conexão com o banco de dados
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='dungeonQuest'
)

# Cria um cursor para executar comandos SQL
cursor = mydb.cursor()

# Executa a consulta SQL para recuperar as questões
sql = "SELECT * FROM Questoes"
cursor.execute(sql)

# Recupera os resultados da consulta
resultados = cursor.fetchall()

# Cria uma lista para armazenar as questões recuperadas
questoes_recuperadas = []

# Percorre os resultados e cria objetos Question
for resultado in resultados:
    id_questao = resultado[0]
    materia = resultado[1]
    enunciado = resultado[2]
    alternativa_a = resultado[3]
    alternativa_b = resultado[4]
    alternativa_c = resultado[5]
    alternativa_d = resultado[6]
    resposta_correta = resultado[7]
    justificativa = resultado[8]

    # Cria o objeto Question e adiciona à lista
    questao = Question(id_questao, materia, enunciado, alternativa_a, alternativa_b, alternativa_c, alternativa_d, resposta_correta, justificativa)
    questoes_recuperadas.append(questao)

# Fecha a conexão
mydb.close()