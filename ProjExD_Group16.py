import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Score:
    """
    打ち落とした爆弾，敵機の数をスコアとして表示するクラス
    爆弾：1点
    敵機：10点
    """
    def __init__(self):
        self.font = pg.font.Font(None, 50)
        self.color = (0, 0, 255)
        self.value = 0
        self.image = self.font.render(f"Score: {self.value}", 0, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = 100, 550

    def update(self, screen: pg.Surface):
        self.image = self.font.render(f"Score: {self.value}", 0, self.color)
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

    score = Score()

    

    tmr = 0
    score = 0
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

        # distance = kk_img.distance_to(kk_img) #距離に応じてスコアを追加する
        # score += distance * 0.1  # 距離に対して倍率をかける

        x = tmr%3200 #練習６ 練習９
       
        screen.blit(bg_img, [-x, 0]) #練習６
        screen.blit(bg_img2, [-x+1600 ,0])#練習７
        screen.blit(bg_img, [-x+3200, 0])#練習９

        # screen.blit(kk_img, [300, 200])#練習４

        screen.blit(kk_img, kk_rct)#練習１０.５

        pg.display.update()
        tmr += 1        
        clock.tick(200)#練習５
        score.update(screen) #scoreを画面に表示
        pg.display.update()

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()