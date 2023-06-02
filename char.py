import pygame

class Shadow:
    def __init__(self, enemy):
        self.image = pygame.transform.scale_by(pygame.image.load('dungeon_quest-main/game/assets/sprites/effects/shadow/shadow.png').convert_alpha(), 6)
        self.enemy = bool(enemy)
        if self.enemy == False:
            self.x_pos = 150
        else:
            self.x_pos = 600
        self.rect = self.image.get_rect(bottomleft = (self.x_pos, 440))

class Slash:
    def __init__(self, enemy):
        self.slash_anim = [pygame.transform.scale_by(pygame.image.load('dungeon_quest-main/game/assets/sprites/effects/slash_1.png').convert_alpha(), 6),pygame.transform.scale_by(pygame.image.load('dungeon_quest-main/game/assets/sprites/effects/slash_2.png').convert_alpha(), 6),pygame.transform.scale_by(pygame.image.load('dungeon_quest-main/game/assets/sprites/effects/slash_3.png').convert_alpha(), 6)]
        self.enemy = bool(enemy)
        self.slash_index = 0
        if self.enemy == False:
            self.x_pos = 150
        else:
            self.x_pos = 600
        self.image = self.slash_anim[self.slash_index]
        self.rect = self.image.get_rect(bottomleft = (self.x_pos, 415))

    def slash(self):
        self.slash_timer = 0
        self.slash_return = False
        self.slash_count = 0
        self.slash_timer += 2
        if self.slash_count < 2:
            if self.slash_timer == 30:
                if self.slash_return == False:
                    self.slash_index += 1
                    self.slash_timer = 0
                elif self.slash_return == True:
                    self.slash_index -= 1
                    self.slash_timer = 0
                if self.slash_index == 2 and self.slash_count == 0:
                    self.slash_return = True
                    self.slash_count += 1
                if self.slash_index == 0 and self.slash_count == 1:
                    self.slash_return = False
                    self.slash_count += 1
        self.image = self.slash_anim[self.slash_index]



class HealthBar:
    def __init__(self, hp, side, name, screename):
        # atributos da barra de hp
        self.font = pygame.font.Font('dungeon_quest-main/game/assets/fonts/ArKkos_Gmimi.ttf', 25)
        self.screename = screename
        self.name = name
        self.hp = hp
        self.hp_max = hp
        self.width = 100
        if side == 0:
            self.start_x = 125
        else:
            self.start_x = 625
        # cores
        self.color_main = (255,255,255)
        self.color_bg = (0,0,0)
        # gerar rects da barra de vida
        self.border_rect = pygame.Rect(self.start_x, 100, 200, 25)
        self.bg_rect = pygame.Rect(self.start_x+3, 100+3, 200-6, 25-6)
        # rótulos barra de vida
        #   nome personagem
        self.name_label_surf = self.font.render(self.screename, False, self.color_main)
        self.name_label_rect = self.name_label_surf.get_rect(bottomleft = (self.start_x, 100))
        #   hp em número

    def update_width(self, hp_atual):
        self.hp = hp_atual
        self.width = int(100 * (self.hp/self.hp_max))

class Player(pygame.sprite.Sprite):
    def __init__(self, name, hp, atk):
        super().__init__()
        # atributos do jogador
        self.screename = name
        self.name = name
        self.hp = hp
        self.atk = atk
        self.dead = False
        # coordenadas do jogador
        self.x_pos = 150
        self.y_pos = 425
        self.acceleration = 0
        self.atacando_state = False
        # imagens e rect do jogador
        self.alpha = 255
        self.alpha_timer = 0
        self.alpha_count = 0 
        self.idle_timer = 0
        self.idle = [pygame.transform.scale_by(pygame.image.load(f'dungeon_quest-main/game/assets/sprites/characters/player/player_idle_1.png').convert_alpha(), 8), pygame.transform.scale_by(pygame.image.load(f'dungeon_quest-main/game/assets/sprites/characters/player/player_idle_2.png').convert_alpha(), 8)]
        self.attack = pygame.transform.scale_by(pygame.image.load(f'dungeon_quest-main/game/assets/sprites/characters/player/player_attack.png').convert_alpha(), 8)
        self.image = self.idle[0]
        self.rect = self.image.get_rect(bottomleft = (self.x_pos, self.y_pos))
        # barra de vida
        self.health_bar = HealthBar(self.hp, 0, self.name, self.screename)
        # corte de dano
        self.slash = Slash(False)
        # sombra
        self.shadow = Shadow(False)
        # audio
        self.slash_audio = pygame.mixer.Sound('dungeon_quest-main/game/assets/audio/effects/attack.wav')

    def atacar(self, inimigo):
        inimigo.hp -= self.atk
        inimigo.health_bar.update_width(inimigo.hp)
        pygame.mixer.Sound.play(self.slash_audio)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, id, name, screename, hp, atk, type):
        super().__init__()
        # atributos do inimigo
        self.id  = id
        self.name = name
        self.screename = screename
        self.hp = hp
        self.atk = atk
        self.type = type
        self.dead = False
        # coordenadas do inimigo
        if self.name == 'skeleton':
            self.x_pos = 600
            self.y_pos = 415
        elif self.name == 'mage':
            self.x_pos = 575
            self.y_pos = 425
        elif self.name == 'dragon':
            self.x_pos = 300
            self.y_pos = 475
        elif self.name == 'bats':
            self.x_pos = 550
            self.y_pos = 415
        elif self.name == 'golem':
            self.x_pos = 500
            self.y_pos = 415
        else:
            self.x_pos = 600
            self.y_pos = 415
        self.acceleration = 0
        self.atacando_state = False
        # imagens e rect do inimigo
        self.alpha = 255
        self.alpha_timer = 0
        self.alpha_count = 0
        self.idle_timer = 0
        self.idle = [pygame.transform.scale_by(pygame.image.load(f'dungeon_quest-main/game/assets/sprites/characters/{self.name}/{self.name}_idle_1.png').convert_alpha(), 8), pygame.transform.scale_by(pygame.image.load(f'dungeon_quest-main/game/assets/sprites/characters/{self.name}/{self.name}_idle_2.png').convert_alpha(), 8)]
        self.attack = pygame.transform.scale_by(pygame.image.load(f'dungeon_quest-main/game/assets/sprites/characters/{self.name}/{self.name}_attack.png').convert_alpha(), 8)
        self.image = self.idle[0]
        self.rect = self.image.get_rect(bottomleft = (self.x_pos, self.y_pos))
        # barra de vida
        self.health_bar = HealthBar(self.hp, 1, self.name, self.screename)
        # corte de dano
        self.slash = Slash(True)
        # sombra
        self.shadow = Shadow(True)
        # audio
        self.attack_audio = pygame.mixer.Sound('dungeon_quest-main/game/assets/audio/effects/attack.wav')

    def atacar(self, jogador):
        jogador.hp -= self.atk
        jogador.health_bar.update_width(jogador.hp)
        pygame.mixer.Sound.play(self.attack_audio)


