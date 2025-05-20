import os
import sys
import pygame as pg
import random

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 無敵処理
def muteki(screen, kk_img, kk_rct, muteki_img, muteki_rct, tmr, muteki_flag, muteki_time):
    # アイテムに触れたら無敵ON
    if kk_rct.colliderect(muteki_rct):
        muteki_flag = True
        muteki_time = tmr
        muteki_rct.center = (-100, -100)  # 画面外へ移動（消す）

    # 無敵時間経過で解除（約3秒＝300フレーム）
    if muteki_flag and tmr - muteki_time > 300:
        muteki_flag = False

    # アイテム表示
    if muteki_rct.center != (-100, -100):
        screen.blit(muteki_img, muteki_rct)

    # 無敵中はこうかとんが光る
    if muteki_flag:
        flash_img = pg.Surface((kk_rct.width, kk_rct.height), pg.SRCALPHA)
        flash_img.fill((255, 255, 0, 128))  # 黄色半透明
        screen.blit(kk_img, kk_rct)
        screen.blit(flash_img, kk_rct)
    else:
        screen.blit(kk_img, kk_rct)

    return muteki_flag, muteki_time

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()

    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)

    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_img = pg.transform.rotozoom(kk_img, 10, 1.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200

    # 無敵アイテム
    muteki_img = pg.image.load("fig/muteki_cake.jpg")
    muteki_img = pg.transform.scale(muteki_img, (50, 50))
    muteki_rct = muteki_img.get_rect()
    muteki_rct.center = (random.randint(400, 700), random.randint(100, 500))

    muteki_flag = False
    muteki_time = 0

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

        # 移動処理
        key_lst = pg.key.get_pressed()
        a = -1  # デフォルト速度
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

        # 無敵処理（こうかとんとmutekiアイテムの当たり判定含む）
        muteki_flag, muteki_time = muteki(
            screen, kk_img, kk_rct,
            muteki_img, muteki_rct,
            tmr, muteki_flag, muteki_time
        )

        pg.display.update()
        tmr += 1
        clock.tick(200)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
