import os
import sys
import pygame as pg
import random

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # スクリプトの場所に移動


class Muteki:
    def __init__(self, img_path):
        self.image = pg.image.load(img_path)
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (-100, -100)  # 最初は非表示
        self.active = False
        self.start_time = 0
        self.duration = 300  # 無敵時間（3秒）
        self.respawn_interval = 1000  # アイテム再出現時間（5秒）
        self.last_taken_time = -self.respawn_interval  # 最初から出現できる

    def update(self, screen, kk_rct, kk_img, tmr):
        # アイテムが非表示かつ再出現タイミングなら再配置
        if self.rect.center == (-100, -100) and tmr - self.last_taken_time >= self.respawn_interval:
            self.rect.center = (random.randint(400, 700), random.randint(100, 500))

        # こうかとんがアイテムに当たったとき
        if kk_rct.colliderect(self.rect):
            self.active = True
            self.start_time = tmr
            self.last_taken_time = tmr
            self.rect.center = (-100, -100)  # 消す

        # 無敵時間が過ぎたら無敵解除
        if self.active and tmr - self.start_time > self.duration:
            self.active = False

        # アイテム描画
        if self.rect.center != (-100, -100):
            screen.blit(self.image, self.rect)

        # こうかとん描画（無敵なら光らせる）
        if self.active:
            flash_img = pg.Surface((kk_rct.width, kk_rct.height), pg.SRCALPHA)
            flash_img.fill((255, 255, 0, 128))  # 黄色半透明
            screen.blit(kk_img, kk_rct)
            screen.blit(flash_img, kk_rct)
        else:
            screen.blit(kk_img, kk_rct)


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()

    # 背景画像
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)

    # こうかとん画像
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_img = pg.transform.rotozoom(kk_img, 10, 1.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200

    # 無敵アイテム
    muteki_item = Muteki("fig/muteki_cake.jpg")

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        # 背景スクロール
        x = tmr % 3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [-x + 1600, 0])
        screen.blit(bg_img, [-x + 3200, 0])

        # こうかとんの移動
        key_lst = pg.key.get_pressed()
        a = -1
        b = 0
        if key_lst[pg.K_UP]:
            b = -1
        elif key_lst[pg.K_DOWN]:
            b = +1
        if key_lst[pg.K_LEFT]:
            a = -2
        elif key_lst[pg.K_RIGHT]:
            a = +1
        kk_rct.move_ip(a, b)

        # 無敵処理と描画
        muteki_item.update(screen, kk_rct, kk_img, tmr)

        pg.display.update()
        tmr += 1
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
