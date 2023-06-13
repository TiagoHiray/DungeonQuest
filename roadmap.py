from campaign import *

from settings import *

class StartLevelButton:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH - (WIDTH/4)/1.05 - 25, HEIGHT - 115, (WIDTH/4)/1.05, 85)
        self.color_active = (255,255,255)
        self.color_inactive = (0,0,0)
        self.color_border = self.color_active
        self.color = self.color_inactive
        self.start_level_button_label = 'Iniciar'

class BossLevel(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # componentes de sprite
        self.origin_pos = 0
        self.image = pygame.transform.scale_by(pygame.image.load('assets/sprites/maps/level selection/boss_level.png').convert_alpha(), 6)
        self.rect = self.image.get_rect(center = (WIDTH/2, HEIGHT/2))


class Road(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # componentes de sprite
        self.origin_pos = 0
        self.image = pygame.transform.scale_by(pygame.image.load('assets/sprites/maps/level selection/road.png').convert_alpha(), 6)
        self.rect = self.image.get_rect(midbottom = (WIDTH/2, HEIGHT/2))


class Level(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # componentes de sprite
        self.origin_pos = 0
        self.image = pygame.transform.scale_by(pygame.image.load('assets/sprites/maps/level selection/level.png').convert_alpha(), 6)
        self.rect = self.image.get_rect(center = (WIDTH/2, HEIGHT/2))
    

class MiniPlayer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # imagens
        self.idle = [pygame.transform.scale_by(pygame.image.load('assets\sprites\characters\mini player\mini_player_idle_1.png').convert_alpha(), 6), pygame.transform.scale_by(pygame.image.load('assets\sprites\characters\mini player\mini_player_idle_2.png').convert_alpha(), 6)]
        # times e indices de animacao
        self.idle_index = 0
        self.idle_timer = 0
        # componentes de sprite
        self.image = self.idle[self.idle_index]
        self.rect = self.image.get_rect(center = (WIDTH/2, HEIGHT + 50))
        # sons
        self.step = pygame.mixer.Sound('assets/audio/effects/step.wav')

class Roadmap:
    def __init__(self, levels):
        self.curr_lvl = 0
        self.start_lvl = False
        self.end = False
        self.levels = levels

    def up_level(self):
        return self.curr_lvl + 1
    
    def reset_levels(self):
        return 0

class RoadmapScreen:
    def __init__(self):
        self.mini_player = pygame.sprite.GroupSingle()
        self.mini_player.add(MiniPlayer())
        self.levels = pygame.sprite.Group()
        self.roads = pygame.sprite.Group()
        self.start_level_button = StartLevelButton()
        self.added_y = 0
        self.confirm_audio = pygame.mixer.Sound('assets/audio/effects/select.wav')
        self.join_battle_audio = pygame.mixer.Sound('assets/audio/effects/join_battle.wav') 
    
    def play_dungeon_music(self):
        #   música
        pygame.mixer.music.stop()
        self.music = pygame.mixer.music.load('assets/audio/music/dungeon.wav')
        pygame.mixer.music.play(-1)
    
    def gen_levels(self):
        for lvl in range(self.roadmap.levels):
            self.roads.add(Road())
            if lvl > 0:
                self.roads.sprites()[lvl].rect.y = self.roads.sprites()[lvl - 1].rect.y - 200
            self.roads.sprites()[lvl].origin_pos = self.roads.sprites()[lvl].rect.y
        for lvl in range(self.roadmap.levels):
            if lvl == 4:
                self.levels.add(BossLevel())
            else:
                self.levels.add(Level())
            if lvl > 0:
                self.levels.sprites()[lvl].rect.y = self.levels.sprites()[lvl - 1].rect.y - 200
            self.levels.sprites()[lvl].origin_pos = self.levels.sprites()[lvl].rect.y
        self.roads.remove(self.roads.sprites()[-1])
    
    def walk_to_lvl(self):
        if self.mini_player.sprite.rect.y < HEIGHT/2:
            if self.mini_player.sprite.rect.y != self.levels.sprites()[self.roadmap.curr_lvl].rect.y:
                for road in self.roads.sprites():
                    road.rect.y += 1
                for level in self.levels.sprites():
                    level.rect.y += 1
                    self.added_y += 1
        else:
            print(self.roads.sprites()[0].rect.y)
            self.mini_player.sprite.rect.y -= 2

    def reset_walk(self):
        self.mini_player.sprite.rect.y = HEIGHT + 50
        for road in range(len(self.roads.sprites())):
            self.roads.sprites()[road].rect.y = self.roads.sprites()[road].origin_pos
        for level in range(len(self.levels.sprites())):
            self.levels.sprites()[level].rect.y = self.levels.sprites()[level].origin_pos