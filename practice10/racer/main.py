import pygame
import random
import time
import os

pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()
FPS = 60
sc = pygame.display.set_mode((400,600))
pygame.display.set_caption("Racer")
bgcolor = (255,255,255)
sc.fill(bgcolor)
speed = 5
score = 0
collected = 0

font = pygame.font.SysFont("Verdana", 45)
fontsmall = pygame.font.SysFont("Verdana", 15)
game = font.render("GAME", True, (0,0,0))
over = font.render("OVER", True, (0,0,0))

base_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(base_dir, "images")
sounds_dir = os.path.join(base_dir, "soundeffects")

background = pygame.image.load(os.path.join(images_dir, "AnimatedStreet.png"))
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(images_dir, "Enemy.png"))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,360), 0)

    def move(self):
        global score
        self.rect.move_ip(0,speed)
        if self.rect.bottom > 600:
            score +=1
            self.rect.top = 0
            self.rect.center = (random.randint(40,360),0)
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(images_dir, "Player.png"))
        self.rect = self.image.get_rect()
        self.rect.center = (160,520)

    def move(self):
        keys = pygame.key.get_pressed()
        if self.rect.left > 4:
            if keys[pygame.K_LEFT]:
                self.rect.move_ip(-5,0)
        if self.rect.right < 396:
            if keys[pygame.K_RIGHT]:
                self.rect.move_ip(5,0)
        
    def draw(self,surface):
        surface.blit(self.image, self.rect)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(images_dir, "Coin.png"))
        self.image = pygame.transform.smoothscale(self.image, (30,30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,360), random.randint(-300,-50))
    def move(self):
        self.rect.move_ip(0, speed)
        if self.rect.top > 600:
            self.rect.center = (random.randint(40,360), random.randint(-300,-50))

P = Player()
E = Enemy()
C = Coin()

enemies = pygame.sprite.Group()
enemies.add(E)

coins = pygame.sprite.Group()
coins.add(C)

allsprites = pygame.sprite.Group()
allsprites.add(E)
allsprites.add(P)
allsprites.add(C)
inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 1000)


running = True
while running:
    for event in pygame.event.get():
        if event.type == inc_speed:
            speed += 0.5
        if event.type == pygame.QUIT:
            running = False
    sc.blit(background, (0,0))
    scores = fontsmall.render(f"Score: {score}", True, (0, 0, 0))
    scores1 = font.render(f"Score: {score}", True, (0,0,0))
    sc.blit(scores, (10,10))
    coins1 = fontsmall.render(f"Coins: {collected}", True, (0,0,0))
    coins2 = font.render(f"Coins: {collected}", True, (0,0,0))
    sc.blit(coins1, (10, 30))

    for entity in allsprites:
        sc.blit(entity.image, entity.rect)
        entity.move()

    collectcoin = pygame.sprite.spritecollideany(P, coins)
    if collectcoin:
        collected += 1
        collectcoin.rect.center = (random.randint(40,360),random.randint(-300,-50))
        
    crash_sound = pygame.mixer.Sound(os.path.join(sounds_dir, "crash.wav"))

    if pygame.sprite.spritecollideany(P, enemies):
        crash_sound.play()
        time.sleep(1)
        sc.fill((128,0,0))
        sc.blit(game, (130,230))
        sc.blit(over, (130,280))
        sc.blit(scores1, (100, 490))
        sc.blit(coins2, (100,540))
        pygame.display.update()
        for entity in allsprites:
            entity.kill()
        time.sleep(3)
        running = False
    pygame.display.update()
    clock.tick(FPS)

