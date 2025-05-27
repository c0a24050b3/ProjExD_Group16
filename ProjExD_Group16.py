import os
import sys
import random
import pygame as pg

WIDTH = 800
HEIGHT = 600
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
    clock = pg.time.Clock()

    # 背景画像
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)

    # こうかとん画像
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_img = pg.transform.rotozoom(kk_img, 10, 1.0)
    kk_size = kk_img.get_size()  # 敵画像にも使うため保存    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200

    # 無敵アイテム
muteki_item = Muteki("fig/muteki_cake.jpg")
    score = Score()

    
    kabes = pg.sprite.Group()
    tmr = 0
    score = 0
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

        # distance = kk_img.distance_to(kk_img) #距離に応じてスコアを追加する
        # score += distance * 0.1  # 距離に対して倍率をかける

        # 無敵処理と描画
        muteki_item.update(screen, kk_rct, kk_img, tmr)

        if tmr % 200 == 0:
            kabes.add(Kabe(kk_size))  # 主人公サイズで敵を生成
            kabes.add(Kabe(kk_size))  # 主人公サイズで敵を生成
        kabes.update()
        kabes.draw(screen)

        pg.display.update()
        tmr += 1
        clock.tick(200)

        score.update(screen) #scoreを画面に表示
        pg.display.update()

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
