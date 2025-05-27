import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
class Koukaton:#こうかとん 
    def __init__(self, num: int, xy: tuple[int, int]):
        super().__init__()
        img0 = pg.transform.rotozoom(pg.image.load(f"fig/{num}.png"), 0, 0.9)
        img = pg.transform.flip(img0, True, False) # デフォルトのこうかとん
        self.imgs = {
            (+1, 0): img, # 右
            (+1, -1): pg.transform.rotozoom(img, 45, 0.9), # 右上
            (0, -1): pg.transform.rotozoom(img, 90, 0.9), # 上
            (-1, -1): pg.transform.rotozoom(img0, -45, 0.9), # 左上
            (-1, 0): img0, # 左
            (-1, +1): pg.transform.rotozoom(img0, 45, 0.9), # 左下
            (0, +1): pg.transform.rotozoom(img, -90, 0.9), # 下
            (+1, +1): pg.transform.rotozoom(img, -45, 0.9), # 右下
        }
        self.dire = (+1, 0)
        self.image = self.imgs[self.dire]
        self.rect = self.image.get_rect()
        self.rect.center = xy
        self.speed = 30
    def update(self, key_lst):
        a = b = 0
        if key_lst[pg.K_UP]:
            b = -1
        if key_lst[pg.K_DOWN]:
            b = +1
        if key_lst[pg.K_LEFT]:
            a = -1
        if key_lst[pg.K_RIGHT]:
            a = +1
        self.dire = (a, b)
        if (a, b) != (0, 0):
            self.image = self.imgs.get((a, b), self.image)
            self.rect.move_ip(a * self.speed / 30, b * self.speed / 30)
    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Enemy:#敵
    def __init__(self, xy):
        self.image = pg.image.load("fig/enemy.png")  
        self.rect = self.image.get_rect(center=xy)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    


    


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)#練習８88888888888
    

    
    kouka = Koukaton(3, (300, 200))
    enemy = Enemy((1000, 300))
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False) 
    tmr = 0


    while True:
        key_lst = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_LCTRL:#左コントロールを押すと加速
                kouka.speed = 100
            if event.type == pg.KEYUP and event.key == pg.K_LCTRL:#元の速さ（押していないとき）
                kouka.speed = 30

        kouka.update(key_lst)
        

                   
        

        if kouka.rect.colliderect(enemy.rect):#敵に触れた際ゲームオーバー
            print("Game Over!")
            return 

      

        key_lst = pg.key.get_pressed()#練習１０.４
       
        
            

        



        
        
        x = tmr%3200 #練習６ 練習９
       
        screen.blit(bg_img, [-x, 0]) #練習６
        screen.blit(bg_img2, [-x+1600 ,0])#練習７
        screen.blit(bg_img, [-x+3200, 0])#練習９

        # screen.blit(kk_img, [300, 200])#練習４

        kouka.draw(screen)
        enemy.draw(screen)

       
        
        pg.display.update()
        tmr += 1        
        clock.tick(200)#練習５
        



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
    