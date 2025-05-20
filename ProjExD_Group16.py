import tkinter
import pygame
import random

#変数定義
スタートフラグ=0
key = ""
px=2 #パックマンのx座標
py=1 #パックマンのy座標
e1x=10 #敵1のx座標
e1y=10 #敵1のy座標
e2x=10 #敵1のx座標
e2y=10 #敵1のy座標
i=0
count = 0 #残りのクッキーの数

#関数定義
def key_down(e):
    global key
    key= e.keysym

def key_down(e):
    global key
    key= e.keysym

def エンディング():
    canvas.delete("all")
    canvas.create_image(400,315,image=ゲームエンディング)
    効果音_オープニング.stop()
    パクパク音.stop()
    クリア.play()

#メイン処理
def main_proc():
    global key,スタートフラグ,px,py,パックマン,i
    i=i+1
    if スタートフラグ==0:
        px=1
        py=1
    if key == "space":
        スタートフラグ=1
        canvas.delete("スタートメッセージ")
    if key == "Right" and スタートフラグ==1:
        if maze[py][px+1]==0 or maze[py][px+1]==2: 
            px = px + 1
            パクパク音.play()
            maze[py][px]=2
            canvas.delete("パックマン")
            canvas.create_image(px*30+80,py*30+50,image=パックマン右[i%3],tag="パックマン")

    if key == "Left" and スタートフラグ==1:
        if maze[py][px-1]==0 or maze[py][px-1]==2:
            px = px - 1
            パクパク音.play()
            maze[py][px]=2
            canvas.delete("パックマン")
            canvas.create_image(px*30+80,py*30+50,image=パックマン左[i%3],tag="パックマン")

    if key == "Down" and スタートフラグ==1:
        if maze[py+1][px]==0 or maze[py+1][px]==2: 
            py = py + 1
            パクパク音.play()
            maze[py][px]=2
            canvas.delete("パックマン")
            canvas.create_image(px*30+80,py*30+50,image=パックマン下[i%3],tag="パックマン")

    if key == "Up" and スタートフラグ==1:
        if maze[py-1][px]==0 or maze[py-1][px]==2: 
            py = py - 1
            パクパク音.play()
            maze[py][px]=2
            canvas.delete("パックマン")
            canvas.create_image(px*30+80,py*30+50,image=パックマン上[i%3],tag="パックマン")
        
    canvas.delete("黄色")
    for y in range(19):
        for x in range(23):
            if maze[y][x]==0:
                canvas.create_oval(x*30+80,y*30+50,x*30+90,y*30+60,fill="yellow",tag="黄色")

    #クッキーの数を調べる
    count = 0
    for row in maze:
        count =count + row.count(0)

    #衝突判定
    パックマンの座標取得=canvas.coords("パックマン")
    パックマンの座標リスト=[パックマンの座標取得[0],パックマンの座標取得[1]]
    敵1の座標取得=canvas.coords("敵1")
    敵1の座標リスト=[敵1の座標取得[0],敵1の座標取得[1]]
    敵2の座標取得=canvas.coords("敵2")
    敵2の座標リスト=[敵2の座標取得[0],敵2の座標取得[1]]
    if abs(パックマンの座標リスト[0] - 敵1の座標リスト[0])<15 and abs(敵1の座標リスト[1]-パックマンの座標リスト[1])<15:
        canvas.delete("パックマン")
        消滅.play()
        効果音_オープニング.stop()
        canvas.create_image(px*30+80,py*30+50,image=衝突,tag="衝突1")
        return
    
    if abs(パックマンの座標リスト[0] - 敵2の座標リスト[0])<15 and abs(敵2の座標リスト[1]-パックマンの座標リスト[1])<15:
        canvas.delete("パックマン")
        消滅.play()
        効果音_オープニング.stop()
        canvas.create_image(px*30+80,py*30+50,image=衝突,tag="衝突1")
        return    

    #エンディング
    if count == 0:
        エンディング()
        return
    
    root.after(100,main_proc)
    
        
#敵の動作
def 敵の動作():
    global e1y,e1x,e2x,e2y
    canvas.delete("敵1")
    canvas.delete("敵2")
    a=[1,0,-1]
    if maze[e1y][e1x] != 3:
        e1x = e1x + random.choice(a)
        e1y = e1y + random.choice(a)
    else:
        e1x=10
        e1y=10
    if maze[e2y][e2x] != 3:
        e2x = e2x + random.choice(a)
        e2y = e2y + random.choice(a)
    else:
        e2x=10
        e2y=10
    canvas.create_image(e1x*30+50,e1y*30+50,image=敵1,tag="敵1")
    canvas.create_image(e2x*30+50,e2y*30+50,image=敵2,tag="敵2")

    root.after(800,敵の動作)

#画面作成
root=tkinter.Tk()
root.title("パックマン")
root.resizable(False,False)
root.bind("",key_down)
canvas = tkinter.Canvas(width=800,height=630,bg="black")
canvas.pack()

#効果音
pygame.init()
効果音_オープニング=pygame.mixer.Sound("sound\オープニングソング.wav")
パクパク音=pygame.mixer.Sound("sound\パクパク音.wav")
クリア=pygame.mixer.Sound("sound\エンディング.wav")
消滅=pygame.mixer.Sound("sound\消滅.wav")

#BGM
効果音_オープニング.play(-1)

#画像のアップロード
背景チップ = tkinter.PhotoImage(file="image\背景チップ.png")
敵1=tkinter.PhotoImage(file="image\敵1.png")
敵2=tkinter.PhotoImage(file="image\敵2.png")
ゲームエンディング=tkinter.PhotoImage(file="image\エンディング.png")
衝突=tkinter.PhotoImage(file="image\衝突.png")

#リスト管理する画像
パックマン右=[
    tkinter.PhotoImage(file="image\パックマン1.png"),
    tkinter.PhotoImage(file="image\パックマン2.png"),
    tkinter.PhotoImage(file="image\パックマン3.png"),
    ]

パックマン左=[
    tkinter.PhotoImage(file="image\パックマン1.png"),
    tkinter.PhotoImage(file="image\パックマン4.png"),
    tkinter.PhotoImage(file="image\パックマン5.png"),
    ]

パックマン上=[
    tkinter.PhotoImage(file="image\パックマン1.png"),
    tkinter.PhotoImage(file="image\パックマン6.png"),
    tkinter.PhotoImage(file="image\パックマン7.png"),
    ]

パックマン下=[
    tkinter.PhotoImage(file="image\パックマン1.png"),
    tkinter.PhotoImage(file="image\パックマン8.png"),
    tkinter.PhotoImage(file="image\パックマン9.png"),
    ]

#二次元リストで迷路の定義（0:床、1:壁、2:敵、3:焦げ跡、4:壁2）
maze = [
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],#1
    [3,2,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,3],#2
    [3,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,3],#3
    [3,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,3],#4
    [3,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,3],#5
    [3,0,1,0,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,3],#6
    [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,3],#7
    [3,1,1,1,1,0,1,0,1,1,1,0,1,1,1,0,0,1,1,1,1,1,1,3],#8
    [3,1,1,1,1,0,1,0,1,0,0,0,0,0,1,0,0,1,1,1,1,1,1,3],#9
    [3,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,3],#10
    [3,1,1,1,1,0,1,0,1,0,0,0,0,0,1,0,0,1,1,1,1,1,1,3],#11
    [3,1,1,1,1,0,1,0,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,3],#12
    [3,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,3],#13
    [3,1,1,0,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,1,3],#14
    [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,3],#15
    [3,1,1,0,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,3],#16
    [3,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0,1,3],#17
    [3,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,1,0,0,0,0,1,3],#18
    [3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3],#19
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]#20(ストッパー)
    ]
         
#パックマンの描画(初回)
canvas.create_image(px*30+50,py*30+50,image=パックマン右[0],tag="パックマン")

#敵の描画(初回)
canvas.create_image(e1x*30+50,e1y*30+50,image=敵1,tag="敵1")
canvas.create_image(e2x*30+50,e2y*30+50,image=敵2,tag="敵2")

#迷路の描画(初回)
for y in range(19):
    for x in range(23):
        if maze[y][x]==0:
           canvas.create_oval(x*30+80,y*30+50,x*30+90,y*30+60,fill="yellow",tag="黄色")
        if maze[y][x]==1 or maze[y][x]==3:
            canvas.create_image(x*30+80,y*30+50,image=背景チップ,tag="背景チップ")

#スタートの合図
canvas.create_text(400,300,text="スペースキーでスタート",font=("system",54)
                   ,fill="orange",tag="スタートメッセージ")

#メインプロセスの呼び出し
main_proc()
敵の動作()

#ループ処理
root.mainloop()