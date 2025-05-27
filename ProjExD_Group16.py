import os
import sys
import random
import pygame as pg

WIDTH = 800
HEIGHT = 600

os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Kabe(pg.sprite.Sprite):
    """敵機に関するクラス"""
    imgs = [pg.image.load("fig/shougaibutu1.png") for _ in range(3)]  # 画像を1回だけ読み込む

    def __init__(self, size):
        super().__init__()
        img = random.choice(__class__.imgs)
        self.image = pg.transform.scale(img, size)
        self.rect = self.image.get_rect()
        
        # 敵を右端の外から出現させる
        self.rect.left = WIDTH - 100  # 画面の右端より外側から出現
        self.rect.centery = random.randint(50, HEIGHT - 50)  # 垂直位置はランダム
        
        self.vx, self.vy = -4, 0  # 左方向に移動
        self.state = "fly"
        self.interval = random.randint(50, 300)

    def update(self):
        self.rect.move_ip(self.vx, self.vy)
        # 画面外に出たら削除
        if self.rect.right < 0:
            self.kill()


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)#練習８

    kk_img = pg.image.load("fig/3.png") #練習１
    kk_img = pg.transform.flip(kk_img, True, False) #練習２
    kk_img = pg.transform.rotozoom(kk_img, 10,1.0)
    kk_size = kk_img.get_size()  # 敵画像にも使うため保存
    kk_rct = kk_img.get_rect()#練習１０.１
    kk_rct.center = 300, 200#練習１０.２
    
    kabes = pg.sprite.Group()
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

        if tmr % 200 == 0:
            kabes.add(Kabe(kk_size))  # 主人公サイズで敵を生成
            kabes.add(Kabe(kk_size))  # 主人公サイズで敵を生成
        kabes.update()
        kabes.draw(screen)

        pg.display.update()
        tmr += 1        
        clock.tick(200)#練習５

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()