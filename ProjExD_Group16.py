import os
import random
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Enemy(pg.sprite.Sprite):
    """
    敵に関するクラス
    """
    
    def __init__(self):
        super().__init__()
        img = pg.image.load("fig/enemy.png")
        self.image = pg.transform.rotozoom(img, 0, 0.2)
        self.rect = self.image.get_rect()
        self.rect.center = 800, random.randint(0,600)
        self.vx, self.vy = -2 , 0
        self.up_down_moving = False  # 上下移動開始フラグ
        self.direction = 1  # 上下移動の方向（1:下, -1:上）
        self.base_y = self.rect.centery


        
    def update(self, tmr):
        """
        敵を右から左に移動させる
        時間経過で挙動変更
        """
        self.rect.move_ip(self.vx,self.vy)
        if tmr >= 3000:
            self.vx = -4  # 移動速度を倍にする
        if tmr >= 2000:
            self.up_down_moving = True

        if self.up_down_moving:
            self.vy = 1 * self.direction
            self.rect.move_ip(self.vx, self.vy)

            # 基準座標から±20～40ピクセル以上動いたら方向転換
            if self.rect.centery > self.base_y + random.randint(200,300):
                self.direction = -1
            elif self.rect.centery < self.base_y - random.randint(200,300):
                self.direction = 1

            # 画面上端または下端で方向反転
            if self.rect.top <= 0:
                self.direction = 1
            elif self.rect.bottom >= 600:
                self.direction = -1

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

    emys = pg.sprite.Group()

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

        if tmr%400 == 0:    # 敵を2秒間隔で追加
            emys.add(Enemy())
       
        screen.blit(bg_img, [-x, 0]) #練習６
        screen.blit(bg_img2, [-x+1600 ,0])#練習７
        screen.blit(bg_img, [-x+3200, 0])#練習９

        # screen.blit(kk_img, [300, 200])#練習４

        for enemy in emys:
            enemy.update(tmr)
        emys.draw(screen)

        screen.blit(kk_img, kk_rct)#練習１０.５

        pg.display.update()
        tmr += 1        
        clock.tick(200)#練習５

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()