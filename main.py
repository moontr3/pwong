from pygame import *

mode = input("Welcome to PWong made by moontr3!\n\nSelect mode:\n[1] Easy\n[2] Normal\n[3] Hard\n[4] Custom\n\n>> ")

try:
    mode = int(mode)
    if mode <= 4 and mode >= 1:
        pass
    else:
        exit()
    
except:
    input("Mode should be integer from 1 to 4!")
    exit()

if mode != 4:
    if mode == 1:
        diff = "Easy"
        speed_x = 1
        speed_y = 1
        spl = 5
        spr = 5
        p1d = 7
        p2d = 7

    elif mode == 2:
        diff = "Normal"
        speed_x = 2
        speed_y = 2
        spl = 4
        spr = 4
        p1d = 5
        p2d = 5
    elif mode == 3:
        diff = "Hard"
        speed_x = 3
        speed_y = 3
        spl = 3
        spr = 3
        p1d = 3
        p2d = 3
        
else:
    diff = "Custom"
    speed_x = input("Type horizontal speed of the ball: ")
    speed_y = input("Type vertical speed of the ball: ")
    spl = input("Type speed of BLUE player: ")
    spr = input("Type speed of RED player: ")
    p1d = input("Number points for BLUE lose: ")
    p2d = input("Number points for RED lose: ")

    try:
        speed_x = int(speed_x)
        speed_y = int(speed_y)
        spl = int(spl)
        spr = int(spr)
        p1d = int(p1d)
        p2d = int(p2d)
    except:
        input("Results should be integer!")
        exit()

print(f'Current settings:\n\nDifficulty: {diff}\nBall speed: X:{speed_x} Y:{speed_y}\nPlayers speed: Blue:{spl} Red:{spr}\nNumber points to lose: Blue:{p2d} Red:{p1d}')
    
sc1 = 0
sc2 = 0
stateb = 0

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self,spd):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y-=spd
        elif keys[K_DOWN] and self.rect.y < window_height-155:
            self.rect.y+=spd

    def update_l(self,spd):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y-=spd
        elif keys[K_s] and self.rect.y < window_height-155:
            self.rect.y+=spd



back = (200,255,255)
window_width = 600
window_height = 500
window = display.set_mode((window_width, window_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

racket1 = Player("img/left.png", 30, 200, 4, 50, 150)
racket2 = Player("img/right.png", 520, 200, 4, 50, 150)
ball = GameSprite("img/ballred.png", 200,200, 4, 50, 50)

font.init()
fontsc = font.Font("font.ttf", 50)

# lose2 = font.Font(None, 35).render("PLAYER 1 LOSE!", True, (180,0,0))


while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
        
    if finish != True:
        if stateb == 1:
            ball = GameSprite("img/ballred.png", ball.rect.x, ball.rect.y, 4, 50, 50)
        else:
            ball = GameSprite("img/ballblue.png", ball.rect.x, ball.rect.y, 4, 50, 50)

        window.fill(back)
        racket1.update_l(spl)
        racket2.update_r(spr)
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        p1 = fontsc.render(f"{sc1}", True, (0,0,100))
        p2 = fontsc.render(f"{sc2}", True, (100,0,0))

        window.blit(p1, (240, 225))
        window.blit(p2, (340, 225))

        if sprite.collide_rect(racket1, ball):
            speed_x *= -1
            speed_y *= 1
            stateb = 0
        elif sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1
            stateb = 1

        if ball.rect.y > window_height-50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
           ball.rect.x = 300
           ball.rect.y = 250
           sc2 +=1

        if ball.rect.x > window_width:
            ball.rect.x = 300
            ball.rect.y = 250
            sc1+=1

        if sc2 == p1d:
            game = False
            window.blit(font.Font("font.ttf", 30).render(f"RED wins.", True, (0,0,0)), (245, 100))

        if sc1 == p2d:
            game = False
            window.blit(font.Font("font.ttf", 30).render(f"BLUE wins.", True, (0,0,0)), (230, 100))
            game_over = False

        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)

input("Thanks for playing!")