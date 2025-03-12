import pygame
import random
import math
from pygame.locals import *
import button

# initialize the screen
SIZE = 50
sc_len = 15*SIZE 
sc_wid = 9*SIZE
speed = 6
ratio = 15 / 9
font1_size_adj =  (sc_len / sc_wid) / ratio

class Bullet:

    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        bullet_path = "D:\code\practise\space_game\Bullet.png"
        bullet_img =pygame.image.load(bullet_path)
        self.bullet_img = pygame.transform.scale(bullet_img, (int(SIZE/3),int(SIZE/3)))
        self.bullet_count = 0
        self.bullet_left = 15
        self.bullet_x = 0
        self.bullet_y = int(sc_wid*(4/5))
        self.bullet_x_cng = 0
        self.bullet_y_cng = speed + 5

        self.bullet_state = "aim" #another state is fire

        #bullet gain icon
        self.bullet_icon = pygame.image.load("D:\code\practise\Battle_game\img\Icons\potion.png").convert_alpha()
        self.bullet_icon = pygame.transform.scale(self.bullet_icon , (25,25) )
        self.bullet_icon_x  = random.randint(0, sc_len - 20)
        self.bullet_icon_y = 0
        self.bullet_icon_y_cng = 3000

    def move_bullet_icon(self):

            if self.bullet_icon_y > sc_wid:
                
                    self.bullet_icon_x  = random.randint(0, sc_len - 20)
                    self.bullet_icon_y = -self.bullet_icon_y_cng
       
            self.parent_screen.blit(self.bullet_icon , (self.bullet_icon_x , self.bullet_icon_y))
            self.bullet_icon_y += 5

    def draw(self):
       
        self.bullet_state = "fire"
        self.parent_screen.blit(self.bullet_img , (self.bullet_x + 10 ,self.bullet_y - 10))
        self.bullet_y -= self.bullet_y_cng

        if self.bullet_y<=0:
            self.bullet_y = int(sc_wid*(4/5))
            self.bullet_state = "aim"

class Stone():

    def __init__(self, parent_screen, length):
        self.parent_screen  = parent_screen

        self.stone_num = length
        stone_path = "D:\code\practise\space_game\Stone1.png"

        self.stone_img = pygame.image.load(stone_path)
        self.stone_img = pygame.transform.scale(self.stone_img, (30, 30))
        self.stone_x =  []*self.stone_num
        self.stone_y = [0]*self.stone_num
        # self.stone_x_cng = []*self.stone_num
        self.stone_y_cng = []*self.stone_num
        

        for i in range(self.stone_num):
            
            self.stone_x.append(random.randint(0, sc_len - SIZE))
            # self.stone_y.append(0)

            # self.stone_x_cng.append((speed))
            self.stone_y_cng.append(int(speed * 0.7))

    def draw_stone(self):

        for i in range(self.stone_num):

            self.parent_screen.blit(self.stone_img , (self.stone_x[i], self.stone_y[i]))
            self.stone_y[i] += self.stone_y_cng[i]
            if self.stone_y[i] > sc_wid + 50:
                self.stone_x[i] = (random.randint(0, sc_len - SIZE))
                self.stone_y[i] = random.randint(10, int(sc_wid*(1/8)))
                # self.stone_y[i] = 0

    def increase_num(self):
        self.stone_num += 1
        # self.stone_x.append(-1)
        self.stone_x.append(random.randint(0, sc_len - SIZE))

        self.stone_y.append(0)
        # self.stone_y_cng.append(-1)
        self.stone_y_cng.append(int(speed * 0.7))


class Enemy():

    def __init__(self, parent_screen, length):

        self.parent_screen = parent_screen

        self.enemy_num = length

        enemy_path = "D:\code\practise\space_game\Enemy.png"

        self.enemy_img = pygame.image.load(enemy_path)
        self.enemy_img = pygame.transform.scale(self.enemy_img, (SIZE,SIZE))

        self.enemy_x =  []*self.enemy_num
        self.enemy_y = []*self.enemy_num
        self.enemy_x_cng = []*self.enemy_num
        self.enemy_y_cng = []*self.enemy_num

        for i in range(self.enemy_num):
            
            self.enemy_x.append(random.randint(0, sc_len - SIZE))
            self.enemy_y.append(random.randint(50, int(sc_wid*(1/5))))

            self.enemy_x_cng.append((speed))
            self.enemy_y_cng.append( (30))

    def draw_enemy(self, i):

        self.parent_screen.blit(self.enemy_img , (self.enemy_x[i], self.enemy_y[i]))
        
    def move_enemy(self):
        for i in range(self.enemy_num):
                self.enemy_x[i] += self.enemy_x_cng[i]
                if (self.enemy_x[i] <= 0 ):
                    self.enemy_x_cng[i] = speed
                    self.enemy_y[i] += self.enemy_y_cng[i]
                elif (self.enemy_x[i] > sc_len-SIZE):
                    self.enemy_x_cng[i] = -speed
                    self.enemy_y[i] += self.enemy_y_cng[i]
                
                self.draw_enemy(i)

    def increase_num(self):
        self.enemy_num += 1
        self.enemy_x.append(-1)
        self.enemy_y.append(-1)
        self.enemy_x_cng.append(-1)
        self.enemy_y_cng.append(-1)


    def reset_enemy(self, i):
        i = i
        self.enemy_x[i] = random.randint(0, sc_len - SIZE)
        self.enemy_y[i] =  random.randint(10, int(sc_wid*(1/5)))
                

class player():

    def __init__(self, parent_screen):

        self.parent_screen = parent_screen
        player_path = "D:\code\practise\space_game\spaceship.png"
        self.player_img =pygame.image.load(player_path)
        self.player_img = pygame.transform.scale(self.player_img, (SIZE,SIZE))
        self.player_x = int(sc_len/2)
        self.player_y = int(sc_wid*(4/5))
        self.player_x_cng = 0
        self.player_y_cng = 0
    
    def draw_player(self):
        
        self.player_x += self.player_x_cng
        if self.player_x <=0:
            self.player_x = 0
        if self.player_x >= sc_len - SIZE:
            self.player_x = sc_len - SIZE

        self.parent_screen.blit(self.player_img , (self.player_x,self.player_y))
        
class Game:

    def __init__(self):

        # pygame initialization
        pygame.init()
        pygame.mixer.init()
        self.play_bgm()
        # creating Window and icon
        self.surface = pygame.display.set_mode((sc_len,sc_wid))
        self.surface.fill((25,12,45))
        pygame.display.set_caption("Alien Hunter")
        icon = pygame.image.load("D:\code\practise\space_game/alien-hunter-logo.jpg")
        icon = pygame.transform.scale(icon , (SIZE,SIZE))
        pygame.display.set_icon(icon)

        # Creating objects
        self.player = player(self.surface)
        self.enemy = Enemy(self.surface, 4)
        self.bullet = Bullet(self.surface)
        self.stone  =Stone(self.surface, 4)

        #game variables
        self.running = True
        self.pause = True
        self.game_over = False
        self.sound = True
        self.score = 0
        self.sudo_score = 0
    def play_bgm(self):

        pygame.mixer.music.load("D:\code\practise\space_game\Audio\Bgm.mp3")
        pygame.mixer.music.play(-1)

    def play_sound(self,sound):

        sound = pygame.mixer.Sound(f"D:\code\practise\space_game\Audio\{sound}.mp3")
        pygame.mixer.Sound.play(sound)
    
    def render_bg(self):

        bg = pygame.image.load("D:\code\practise\space_game\B2.jpg")
        bg = pygame.transform.scale(bg, (sc_len, sc_wid))
        self.surface.blit(bg , (0,0))

    def play(self):

        self.render_bg()
        self.player.draw_player()  
        self.display_score() 
        self.enemy.move_enemy()
        self.stone.draw_stone()
        self.bullet.move_bullet_icon()
            
        if self.bullet.bullet_state == "fire":
            self.bullet.draw()
        pygame.display.flip()

        for i in range(self.enemy.enemy_num):
            collision = self.is_collision(self.enemy.enemy_x[i], self.enemy.enemy_y[i], self.bullet.bullet_x , self.bullet.bullet_y)
            
            if collision:
                self.bullet.bullet_y = int(sc_wid*(4/5))  #reseting the bullet
                self.bullet.bullet_state = "aim"
                self.score += 1
                self.sudo_score = self.score - 1
                #reseting  enemy
                self.enemy.reset_enemy(i)
            collision2  = self.is_collision(self.player.player_x, self.player.player_y, self.stone.stone_x[i] , self.stone.stone_y[i] )
            
            if self.enemy.enemy_y[i] >= int(sc_wid*(7/10)) or collision2:
                self.pause = True
                self.game_over = True
            
            if self.is_collision(self.player.player_x, self.player.player_y, self.bullet.bullet_icon_x , self.bullet.bullet_icon_y ):
                self.bullet.bullet_left += 5
                self.bullet.bullet_icon_y = - self.bullet.bullet_icon_y_cng
                self.bullet.move_bullet_icon()
            
        if (self.sudo_score % 4 == 0 and self.sudo_score != 0):
                self.stone.increase_num()
                self.enemy.increase_num()
                self.sudo_score += 1
                
    def show_game_over(self):

        pygame.mixer.music.pause()
        # self.render_bg()
        # bg_img = "D:\code\practise\space_game\premium_vector-1721907573406-f6b0569a5c2f.jpg"
        bg_img = "D:\code\practise\space_game\spaceships_blur.jpg"
        bg_img = pygame.image.load(bg_img)
        bg_img = pygame.transform.scale(bg_img, (sc_len, sc_wid))
        self.surface.blit(bg_img, (0,0))


        if self.game_over:
            if self.sound:
                self.play_sound("game_over")
                self.sound = False
            
            
            # font1 = pygame.font.SysFont('Times New Roman bold', int(100*font1_size_adj))
            font2 = pygame.font.SysFont('Forte regular', int(120*font1_size_adj))
            # line1 = font1.render("Game over !!", True , (0,255,0))

            game_over = "D:\code\practise\space_game\Game-Over-8-29-2024.png"
            game_over = pygame.image.load(game_over)
            game_over = pygame.transform.scale(game_over, (580,109))


            game_over_x = int(sc_len*(1/6))
            game_over_y = int(sc_wid*(1/12))
            line2 = font2.render(f" {self.score}", True , (235, 225, 25))

            score_txt = "D:\code\practise\space_game\Your-Score-8-29-2024.png"
            score_txt = pygame.image.load(score_txt)
            score_txt = pygame.transform.scale(score_txt, (350, 86))


            score_x = int(sc_len*(1/6)) + int(sc_wid*(1/10))
            score_y = int(sc_wid*(1/6)) + int(sc_wid*(1/6))
            self.surface.blit(game_over, (game_over_x, game_over_y))
            self.surface.blit(score_txt, (score_x, score_y))
            self.surface.blit(line2, ((sc_len / 2) - 30, score_y + 80))
            # self.surface.blit(line2, (score_x + 310, score_y + 10))
            # pygame.display.flip()

        else:
            # font = pygame.font.SysFont('Times New Roman bold', int(70*font1_size_adj))
            # line1 = font.render(f"Welcome To The Game ", True , (245, 188, 66))

            welcome_txt  = "D:\code\practise\space_game\WELCOME-TO-THE-GAME-8-29-2024.png"
            welcome_txt = pygame.image.load(welcome_txt)
            welcome_txt = pygame.transform.scale(welcome_txt, (580,109))

            welcome_x = int(sc_len*(1/10))
            welcome_y = int(sc_wid*(1/8))
            # font2 = pygame.font.SysFont('arial bold', int(60*font1_size_adj))
            # line2 = font2.render(f"ALIEN HUNTER ", True , (245,55,45))
            alienhunter_x = int(sc_len*(1/6)) + int(sc_len*(1/10))
            alienhunter_y = int(sc_wid*(1/4)) + int(sc_wid*(1/6))
            alien_hunter_img = "D:\code\practise\space_game\download.png"
            alien_hunter_img = pygame.image.load(alien_hunter_img)
            alien_hunter_img = pygame.transform.scale(alien_hunter_img, (350, 86))

            self.surface.blit(welcome_txt, (welcome_x, welcome_y))
            self.surface.blit(alien_hunter_img, (alienhunter_x, alienhunter_y))

        self.show_button()
        pygame.display.flip()
        
    def show_button(self):

        #loading button images
        self.start_img = pygame.image.load("D:\code\practise\space_game\start-button.png").convert_alpha()
        self.exit_img = pygame.image.load("D:\code\practise\space_game\exit.png").convert_alpha()
        #creating object button
        self.start_button = button.Button(self.surface, 200, 300, self.start_img, 100, 100)
        self.exit_button = button.Button(self.surface, 400, 300, self.exit_img, 100, 100)
            
        if self.start_button.draw():
            pygame.mixer.music.unpause()
            self.pause = False 
            self.reset()
            self.score = 0
        
        if self.exit_button.draw():
            self.running = False
        
    def reset(self):
        
        self.player = player(self.surface)   
        self.enemy = Enemy(self.surface, 4)
        self.bullet = Bullet(self.surface)
        self.stone = Stone(self.surface, 4)

    def is_collision(self, x1, y1, x2, y2):

        distance = math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2),2))
        if distance < 27:
            self.play_sound("crush")
            return True
        else:
            return False
        
    def display_score(self):
        
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"score: {self.score}", True, (255,255,255))
        self.surface.blit(score, (sc_len-120, 10))
        bullet_left = font.render(f"Bullet : {self.bullet.bullet_left}", True , (255, 255, 255))
        self.surface.blit(bullet_left , (sc_len - 120, 40))

    def run(self):
        
        #game variable
        # handaling event
        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False
                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        self.pause = False 
                    if event.key == pygame.K_RIGHT:
                       self.player.player_x_cng = speed*2

                    if event.key == pygame.K_LEFT:
                       self.player.player_x_cng = -speed*2

                    if event.key == pygame.K_SPACE:
                        if self.bullet.bullet_state == "aim":
                            if self.bullet.bullet_left != 0:    
                                self.bullet.bullet_count += 1
                                self.bullet.bullet_left -= 1
                                self.play_sound("ding")
                                self.bullet.bullet_x = self.player.player_x
                                self.bullet.draw()
                            
                            if self.bullet.bullet_left == 0:
                                pass
                            
                
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.player.player_x_cng = 0
                    
            if not  self.pause:
                
                self.play()
            else:
                self.show_game_over()
        #exiting Game
        pygame.quit()
        quit()

if __name__ == "__main__":
    game = Game()
    game.run()


