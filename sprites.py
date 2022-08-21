import pygame as pg
from pygame.locals import (K_UP,K_DOWN,K_LEFT,K_RIGHT,K_ESCAPE,KEYDOWN,QUIT,)


SKY = (135,206,250)

HEIGHT=560
WIDTH =1160

vec = pg.math.Vector2  # 2 for two dimensional
 
ACC = 0.5
FRIC = -0.12
FPS = 60

cr=[20,60,100,140,180,220,260,300,340,380,420,460,500,540,580,620,660,700,740,780,820,860,900,940,980,1020,1060,1100,1140]
 
G = 'assets/grass1.png'
D = 'assets/soil1.png'
P = 'assets/player1_011.png'
L2 = 'assets/lava_l131.png'
L1 = 'assets/lava_r161.png'




class Player(pg.sprite.Sprite):
    def __init__(self,coords):
        super().__init__()
        self.surf = pg.image.load(P).convert_alpha()
        self.rect = self.surf.get_rect(bottomleft = (coords[0]-20,coords[1]-20))

        self.pos = vec((coords[0],coords[1]-20))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
    def move(self):
        self.acc = vec(0,0.5)
    
        pressed_keys = pg.key.get_pressed()            
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC
             
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
         
        if self.pos.x > WIDTH-13:
            self.pos.x = WIDTH-13
        if self.pos.x < 13:
            self.pos.x = 13
        if self.pos.y > HEIGHT:
            self.pos.y = HEIGHT
        if self.pos.y < 18:
            self.pos.y = 18
            
        self.rect.midbottom = self.pos
    def update(self,tiles):
        hits = pg.sprite.spritecollide(self ,tiles, False, collided = self.check)
        #hits1 = pg.sprite.spritecollide(self ,tiles, False)
##        if hits1:
##            if hits1[0].rect.right >= self.rect.left:
##                self.pos.x = hits[0].rect.right + 1
##            if hits1[0].rect.left <= self.rect.right:
##                self.pos.x = hits[0].rect.left - 1
        if self.vel.y > 0:
            if hits:
                self.pos.y = hits[0].rect.top + 1
                self.vel.y = 0 
    def jump(self,tiles):
        hits = pg.sprite.spritecollide(self, tiles, False, collided = self.check)
        if hits:
            self.vel.y = -10



            
    def check(self,s,o):
        if pg.sprite.collide_rect(s,o):
            #print(_1,_1.rect.right,_1.rect.left,_2,_2.rect.right,_2.rect.left)
            if self.rect.bottom > o.rect.top:
                if self.rect.left > o.rect.left + 1 or self.rect.right < o.rect.right - 1:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

##            # check for collision in x direction
##            #if o.rect.colliderect(self.rect.x, self.rect.y, self.width, self.height):
##                #dx = 0
##            # check for collision in y direction
##            if o.rect.colliderect(self.rect.x, self.rect.y, self.width, self.height):
##                # check if below the ground i.e. jumping
##                if self.vel.y < 0:
##                    self.pos.y = o.rect.bottom - self.rect.top
##                    self.vel.y = 0
##                # check if above the ground i.e. falling
##                elif self.vel.y >= 0:
##                    self.pos.y = o.rect.top - self.rect.bottom
##                    self.vel.y = 0







class Platform(pg.sprite.Sprite):
    def __init__(self,image,coords):
        super().__init__()
        self.surf = pg.image.load(image).convert_alpha()
        self.rect = self.surf.get_rect(center = coords)














        
