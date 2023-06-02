#importing required modules
import tkinter
from tkinter import *
from tkinter import messagebox
import customtkinter
from PIL import ImageTk,Image
import pygame
import mysql.connector
import os
import time
from CTkMessagebox import CTkMessagebox
from tkinter import messagebox
import mysql.connector

#Conexão com o banco
db = mysql.connector.connect(host="localhost", user="root", passwd="", database="")
cursor = db.cursor()

def botão_envia():
    #variaveis de get
    alt = alt_correta.get()
    materias = materia_var.get()
    text1 = entry1.get("0.0", "end")
    text2 = entry2.get("0.0", "end")
    text3 = entry3.get("0.0", "end")
    text4 = entry4.get("0.0", "end")
    text5 = entry5.get("0.0", "end")
    text6 = entry6.get("0.0", "end")
    if materias == "" or text1 == "" or text2 == "" or text3 == "" or text4 == "" or text5 == "" or text6 == "":
        error_campos()
    else:
        query_correta = "INSERT INTO Questoes (materia, enunciado, alternativa_a, alternativa_b, alternativa_c, alternativa_d, resposta_correta, justificativa) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        valor = materias, text1, text2, text3, text4, text5, alt, text6
        cursor.execute(query_correta, valor)
        db.commit()
        cadastro_sucesso()
        delete_text()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Restrições e pop-ups
def error_campos():
    CTkMessagebox(title="Error", message="Preencha todos os campos obrigatórios", icon="cancel")

def cadastro_sucesso():
    CTkMessagebox(title="Sucesso", message="Cadastro de questão concluído com sucesso",
                  icon="check", option_1="OK")
def delete_text():
    entry1.delete("0.0", "end")
    entry2.delete("0.0", "end")
    entry3.delete("0.0", "end")
    entry4.delete("0.0", "end")
    entry5.delete("0.0", "end")
    entry6.delete("0.0", "end")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def principal():
    #Cria a janela de fundo
    app = customtkinter.CTk()
    app.title('DungeonQuest')
    app.geometry("960x864")
    customtkinter.set_default_color_theme(color_string="blue")

    #Background
    img1=ImageTk.PhotoImage(Image.open("backquest.jpg"))
    l1=customtkinter.CTkLabel(master=app,image=img1)
    l1.pack()

    global alt_correta
    alt_correta = StringVar()

    global frame
    frame=customtkinter.CTkFrame(master = l1, width=600, height=850, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l2=customtkinter.CTkLabel(frame, text="CADASTRO DE QUESTÕES",font=('Century Gothic',20))
    l2.place(x=180, y=45)

    #Entrys de enunciado e alternativas
    l4 = customtkinter.CTkLabel(frame, text="Enunciado: ",font=('Century Gothic',15))
    l4.place(x=50, y =100)

    global entry1
    global text1
    text1 = StringVar
    entry1=customtkinter.CTkTextbox(frame, width=500, height=80)
    entry1.place(x=50, y=135)

    l5 = customtkinter.CTkLabel(frame, text="Alternativas: ",font=('Century Gothic',15))
    l5.place(x=50, y = 240)
    
    l6 = customtkinter.CTkLabel(frame, text="a) ",font=('Century Gothic',15))
    l6.place(x=30, y = 295)

    global entry2
    global text2
    text2 = StringVar()
    entry2=customtkinter.CTkTextbox(frame, width=500, height=80)
    entry2.place(x=50, y=275)

    l6 = customtkinter.CTkLabel(frame, text="b) ",font=('Century Gothic',15))
    l6.place(x=30, y = 390)

    global entry3
    global text3
    text3 = StringVar
    entry3=customtkinter.CTkTextbox(frame, width=500, height=80)
    entry3.place(x=50, y=370)

    l7 = customtkinter.CTkLabel(frame, text="c) ",font=('Century Gothic',15))
    l7.place(x=30, y = 485)

    global entry4
    global text4
    text4 = StringVar()
    entry4=customtkinter.CTkTextbox(frame, width=500, height=80)
    entry4.place(x=50, y=465)

    l8 = customtkinter.CTkLabel(frame, text="d) ",font=('Century Gothic',15))
    l8.place(x=30, y = 580)

    global entry5
    global text5
    text5 = StringVar()
    entry5=customtkinter.CTkTextbox(frame, width=500, height=80)
    entry5.place(x=50, y=560)

    #Alternativa correta
    global radiobutton_1
    radiobutton_1 = customtkinter.CTkRadioButton(master=frame, text="", value="A", variable=alt_correta)
    radiobutton_1.place(x=560, y = 300)
    
    radiobutton_2 = customtkinter.CTkRadioButton(master=frame, text="",
                                               value="B", variable=alt_correta)
    radiobutton_2.place(x=560, y = 395)

    radiobutton_3 = customtkinter.CTkRadioButton(master=frame, text="",
                                               value="C", variable=alt_correta)
    radiobutton_3.place(x=560, y = 490)

    radiobutton_4 = customtkinter.CTkRadioButton(master=frame, text="",
                                               value="D", variable=alt_correta)
    radiobutton_4.place(x=560, y = 580)

    #Entry
    global entry6
    global text6
    text6 = StringVar()
    entry6=customtkinter.CTkTextbox(frame, width=500, height=50)
    entry6.place(x=50, y=685)

    l10=customtkinter.CTkLabel(frame, text="Justificativa: ",font=('Century Gothic',15))
    l10.place(x=50, y=650)

    #Materias
    materias = ["Banco de Dados", "Modelagem Orientada a Objetos", "Programação Orientada a Objetos", "Lógica de Programação"]
    global materia_var
    materia_var = StringVar()
    materia_var.set(materias[0])
    materia_dropdown = customtkinter.CTkOptionMenu(frame, values = materias, variable=materia_var, width=500, font=('Century Gothic',15))
    materia_dropdown.place(x=50, y=750)
    
    botao3 = customtkinter.CTkButton(frame, width=500, height=30, text="Enviar", command=botão_envia)
    botao3.place(x=50, y=800)

    app.mainloop()

principal()
