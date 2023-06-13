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
from game import *
from user import *
from bd_conn import *

run_game = False

#ERROS E SUCESSOS----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#erro de usuario ja existente
def error_existe():
    CTkMessagebox(title="Error", message="Esse nome de usuário já existe", icon="cancel")

#erro de não preencher todos os campos
def error_campos():
    CTkMessagebox(title="Error", message="Preencha todos os campos obrigatórios", icon="cancel")

#mensagem de cadastro concluído
def cadastro_sucesso():
    CTkMessagebox(title="Sucesso", message="Cadastro concluído com sucesso",
                  icon="check", option_1="Ok")

#Mensagem de bem-vindo após login concluído   
def login_sucesso():
    CTkMessagebox(title="Sucesso",message="Bem-vindo a Dungeon Quest",
                  icon="check", option_1="OK")

#Login errado    
def falha_login():
    CTkMessagebox(title="Error", message="Login ou usuário incorretos", icon="cancel")


#funcao para limpar caixas de texto após submit
def delete_text():
    entry1c.delete(first_index=0, last_index=100)
    entry2c.delete(first_index=0, last_index=100)
    entry3c.delete(first_index=0, last_index=100)

def delete_textl():
    entry1.delete(first_index=0, last_index=100)
    entry2.delete(first_index=0, last_index=100)


def mesma_senha():
    CTkMessagebox(title="Error", message="Senhas diferentes", icon="cancel")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Verificações de cadastro
def cadastro():
    # x = cursor.execute("SELECT * FROM usuario where loginUsuario = (%s)")
    usuario_info = usuario.get()
    senha_info = senha.get()
    confsenha = confirm_senha.get()
    if usuario_info == "":
        error_campos()
    elif senha_info == "":
        error_campos()
    elif senha_info != confsenha:
        mesma_senha()
    # elif int(x) > 0:
    #     error_existe()
    else:
        sql = "insert into Usuario (loginUsuario, senhaUsuario) values (%s,%s)"
        t = (usuario_info, senha_info)
        cursor.execute(sql, t)
        conexao.commit()
        time.sleep(0.50)
        delete_text()
        cadastro_sucesso()

#coloca o pathing dentro do os.system
def open_ex():
    global run_game
    run_game = True


#Verificações de login
def login():

    global usu
    usu = usuario_varify.get()
    sen = senha_varify.get()
    sql = "SELECT * FROM Usuario WHERE loginUsuario = %s and senhaUsuario = %s"
    cursor.execute(sql,[(usu),(sen)])
    resultados = cursor.fetchall()
    if resultados:
        for i in resultados:
            delete_textl()
            login_sucesso()
            time.sleep(0.5)
            app.destroy()
            open_ex()
            break
    else:
        delete_textl()
        falha_login()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#MAIN
def principal():

    pygame.init()

    # musica_fundo = pygame.mixer.Sound("dungeon_quest-main/game/assets/audio/music/soundtrack.mp3")
    # musica_fundo.play(loops=-1)

    global app
    app = customtkinter.CTk()
    app.title('DungeonQuest')
    app.geometry("960x864")
    customtkinter.set_default_color_theme(color_string="blue")

    global tabview
    tabview = customtkinter.CTkTabview(app, width=900, height=830)
    tabview.pack()


    tabview.add("Login")  
    tabview.add("Cadastro")  
    tabview.set("Login")  


    global usuario
    global senha
    global confirm_senha
    usuario = StringVar()
    senha = StringVar()
    confirm_senha = StringVar()

    global usuario_varify
    global senha_varify
    usuario_varify = StringVar()
    senha_varify = StringVar()

    #LOGIN
    img1=ImageTk.PhotoImage(Image.open("assets/sprites/backgrounds/fundo.png"))
    global l1
    l1=customtkinter.CTkLabel(master=tabview.tab("Login"),image=img1)
    l1.pack()

    global frame
    frame=customtkinter.CTkFrame(l1, width=320, height=360, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l2=customtkinter.CTkLabel(master=frame, text="LOGIN",font=('Century Gothic',20))
    l2.place(x=130, y=45)
    
    global entry1
    entry1=customtkinter.CTkEntry(frame, width=220, textvariable=usuario_varify)
    entry1.place(x=50, y=110)

    global entry2
    entry2=customtkinter.CTkEntry(frame, width=220, show="*", textvariable=senha_varify)
    entry2.place(x=50, y=165)

    l3=customtkinter.CTkLabel(frame, text="",font=('Century Gothic',12))
    l3.place(x=155,y=195)

    l4=customtkinter.CTkLabel(frame, text="Usuário",font=('Century Gothic',12))
    l4.place(x=50,y=80)

    l5=customtkinter.CTkLabel(frame, text="Senha",font=('Century Gothic',12), height=10)
    l5.place(x=50,y=144)

    combobox = customtkinter.CTkComboBox(frame,width=220,
                                            values=["Aluno", "Professor", "Admin"])
    combobox.place(x=50, y=220)
    combobox.set("Aluno") 

    button1 = customtkinter.CTkButton(frame, width=220, text="Entrar", command=login, corner_radius=6)
    button1.place(x=50, y=280)

    #Cadastro

    img2=ImageTk.PhotoImage(Image.open("assets/sprites/backgrounds/fundo2.jpg"))
    l2=customtkinter.CTkLabel(master=tabview.tab("Cadastro"),image=img2)
    l2.pack()

    global framec
    framec=customtkinter.CTkFrame(l2, width=320, height=360, corner_radius=15)
    framec.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l2c=customtkinter.CTkLabel(master=framec, text="CADASTRO",font=('Century Gothic',20))
    l2c.place(x=107, y=45)

    global entry1c
    entry1c=customtkinter.CTkEntry(framec, width=220, placeholder_text= "Usuário", textvariable=usuario)
    entry1c.place(x=50, y=110)

    global entry2c
    entry2c=customtkinter.CTkEntry(framec, width=220, textvariable=senha, placeholder_text= "Senha", show="*")
    entry2c.place(x=50, y=165)

    global entry3c
    entry3c = customtkinter.CTkEntry(framec, width=220, show="*", textvariable=confirm_senha)
    entry3c.place(x=50, y = 216)

    l3c=customtkinter.CTkLabel(framec, text="Usuário",font=('Century Gothic',12))
    l3c.place(x=50,y=80)

    l4c=customtkinter.CTkLabel(framec, text="Senha",font=('Century Gothic',12), height=10)
    l4c.place(x=50,y=144)

    l5c=customtkinter.CTkLabel(framec, text="Confirme sua senha",font=('Century Gothic',12), height=8)
    l5c.place(x=50,y=195)

    comboboxc = customtkinter.CTkComboBox(framec,width=220,
                                            values=["Aluno", "Professor", "Admin"])

    comboboxc.place(x=50, y=263)
    comboboxc.set("Aluno") 

    button1c = customtkinter.CTkButton(framec, width=220, text="Cadastrar-se", command=cadastro,  corner_radius=6)
    button1c.place(x=50, y=310)

    app.mainloop()
principal()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Estabelecer conexão com o banco de dados
query_usuario = "SELECT idUsuario, loginUsuario, idSala FROM Usuario WHERE loginUsuario = %s"
cursor.execute(query_usuario, (usu,))
resultado_usuario = cursor.fetchone()


if resultado_usuario:
    id_usuario = (resultado_usuario[0])
    name_usuario = (resultado_usuario[1])

    usuario = User(id_usuario, name_usuario)

#Loop para iniciar game
while run_game == True:
    if __name__ == '__main__':
        game = Game(usuario)
        game.run()  

