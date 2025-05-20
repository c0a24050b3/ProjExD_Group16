import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Koukaton:
    def __init__(self, num: int, xy: tuple[int, int]):
        img0 = pg.transform.rotozoom(pg.image.load(f"fig/{num}.png"), 0, 0.9)
        img = pg.transform.flip(img0, True, False) # ノーマルこうかとん
        self.imgs = {
            (+1, 0): img,
            (+1, -1): pg.transform.rotozoom(img, 45, 0.9),
            (0, -1): pg.transform.rotozoom(img, 90, 0.9),
            (-1, -1): pg.transform.rotozoom(img0, -45, 0.9),
            (-1, 0): img0,
            (-1, +1): pg.transform.rotozoom(img0, 45, 0.9),
            (0, +1): pg.transform.rotozoom(img, -90, 0.9),
            (+1, +1): pg.transform.rotozoom(img, -45, 0.9),
        }
        self.dire = (+1, 0)
        self.image = self.imgs[self.dire]
        self.rect = self.image.get_rect(center=xy)
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



def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)#練習８

    kk_img = pg.image.load("fig/3.png") #練習１
    kk_img = pg.transform.flip(kk_img, True, False) #練習２
    kk_img = pg.transform.rotozoom(kk_img, 10,1.0)

    kk_rct = kk_img.get_rect()#練習１０.１
    kk_rct.center = 300, 200#練習１０.２
    

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed()#練習１０.４
       
        if key_lst[pg.K_UP]:#練習１０.４
            a = -1
            b = -1

        elif key_lst[pg.K_DOWN]:#練習１０.４
            a = -1
            b = +1

        elif key_lst[pg.K_LEFT]:#練習１０.４
            a = -2
            b = 0

        elif key_lst[pg.K_RIGHT]:#練習１０.４
            a = +1
            b = 0
        elif not key_lst[pg.K_RIGHT]:
            a = -1
            b = 0
            kk_rct.move_ip((a, b))#演習２

        



        
        
        x = tmr%3200 #練習６ 練習９
       
        screen.blit(bg_img, [-x, 0]) #練習６
        screen.blit(bg_img2, [-x+1600 ,0])#練習７
        screen.blit(bg_img, [-x+3200, 0])#練習９

        # screen.blit(kk_img, [300, 200])#練習４

        screen.blit(kk_img, kk_rct)#練習１０.５

        pg.display.update()
        tmr += 1        
        clock.tick(200)#練習５
    
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

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)

    kouka = Koukaton(3, (300, 200))  

    tmr = 0
    while True:
        key_lst = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_LCTRL:
                kouka.speed = 100
            if event.type == pg.KEYUP and event.key == pg.K_LCTRL:
                kouka.speed = 30

        
        kouka.update(key_lst)

        x = tmr % 200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [-x + 1600, 0])
        screen.blit(bg_img, [-x + 3200, 0])
        kouka.draw(screen)

        pg.display.update()
        tmr += 1
        clock.tick(50)



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()