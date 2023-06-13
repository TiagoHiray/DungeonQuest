import mysql.connector

# conexao com o banco
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="dungeonQuest"
)

cursor = conexao.cursor()

class User:
    def __init__(self, id, name):
        self.id = int(id)
        self.name = str(name)
        self.connected_room = 0
        self.curr_score = 0
    
    def update_score(self, score):
        self.curr_score = score

    def update_user_room(self, room):
        self.connected_room = room.room_id
        query = 'UPDATE Usuario SET idSala = %s WHERE idUsuario = %s'
        cursor.execute(query, (self.connected_room, self.id))
        conexao.commit()

    def exit_room(self):
        if self.connected_room != 0:
            query = 'UPDATE Usuario SET idSala = NULL WHERE idUsuario = %s'
            cursor.execute(query, (self.id,))
            conexao.commit()
            self.decrease_capacity()

    def decrease_capacity(self):
            query = "UPDATE Sala SET qntdJogadores = qntdJogadores - 1 WHERE idSala = %s"
            cursor.execute(query, (self.connected_room,))
            conexao.commit()