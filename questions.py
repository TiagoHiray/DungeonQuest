import random as rd
from settings import *
import mysql.connector

from bd_conn import *

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

# Cria uma lista para armazenar as questões recuperadas
questoes = []

try:
        # Executa a consulta SQL para recuperar as questões
        sql = "SELECT * FROM Questoes"
        cursor.execute(sql)

        # Recupera os resultados da consulta
        resultados = cursor.fetchall()
        print(resultados)

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
            questoes.append(questao)
        questoes = questoes * 20
except:
        questao_exemplo = Question(0, '', 'Questão não pode ser obtida.', '', '', '', '*', '*', 'Não existe explicação para essa questão.')

        questoes = [questao_exemplo, questao_exemplo, questao_exemplo, questao_exemplo, questao_exemplo, questao_exemplo, questao_exemplo, questao_exemplo, questao_exemplo, questao_exemplo, questao_exemplo, questao_exemplo, questao_exemplo, questao_exemplo, questao_exemplo, questao_exemplo, questao_exemplo, questao_exemplo]