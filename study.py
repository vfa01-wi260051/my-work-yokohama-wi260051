
import time                      
import random                              

def mogura(r):                                                
    m = ""
    n = ""
    for i in range(8):
        ana = "."
        if i==r:
            ana = "O"
        m = m + " _" + ana + "_ "
        n = n + " [" + str(i) + "] "
    print(m)
    print(n)

print("=============ゲームスタート！==============")
hit=0
ts=time.time()
for i in range(10):
    r = random.randint(0,7)
    mogura(r)
    p = input("モグラはどこ？")
    if p == str(r):
        print("HIT!")                      
        hit = hit + 1
    else:
        print("MISS")
t = int(time.time()-ts)
bonus=0
if t<60:
    bonus = 60-t
print("==========ゲームエンド=============")
print("TIME",t,"sec")                      
print("HIT",hit,"✕ BONUS", bonus)
print("SCORE",hit*bonus)














import time
t = time.localtime()
print(t)
d = time.strftime("%Y/%m/%d %A", t)               
h = time.strftime("%H:%M:%S",t)
print(d)
print(h)









import datetime
n = datetime.datetime.now()          
print(n)
print("時を取り出す", n.hour)         
print("分を取り出す", n.minute)        
print("秒を取り出す", n.second)      









import calendar
print(calendar.month(2021,3))       









import tkinter
root = tkinter.Tk()
root.title("ウィンドウのタイトル") 
root.mainloop()











import tkinter
root = tkinter.Tk()                           
root.title("キャンバスに文字列を提示")
cvs = tkinter.Canvas(width=600, height=400, bg="white")
cvs.create_text(300,200,text="Python", font=("Times New Roman", 40))
cvs.pack()
root.mainloop() 













import tkinter
root = tkinter.Tk()
root.title("色を指定する英単語")
cvs = tkinter.Canvas(width=360, height=480, bg="black")

COL = [
    "maroon", "brown" , "red", "orange" ,"gold","yellow","lime","limegreen",
    "green", "skyblue","cyan","blue","navy", "indigo","purple",
    "magenta", "white", "lightgray", "silver", "gray", "olive","pink"
]

FNT=("Times, New Roman",24);
x=120                       
y=40
for c in COL:
    cvs.create_text(x,y, text=c, fill=c, font=FNT)                    
    y += 40   
    if y>=480:
        y=40                                                              
        x += 120                                                        
 
cvs.pack()
root.mainloop()











import tkinter
root = tkinter.Tk()
root.title("キャンバスに図形を描く")
cvs = tkinter.Canvas(width=1000, height=1000, bg="white")
cvs.create_line(20,40,120,360, fill="red", width=8)
cvs.create_rectangle(160,60,260,340,fill="orange", width=10)
cvs.create_oval(300,100,500,300,outline="yellow", width=12)
cvs.create_polygon(600,100,500,300,700,300,fill="green", outline="lime", width=16)
cvs.create_arc(500,400,700,600,fill="blue", outline="yellow", width=10, start=40, extent=150 ,style=tkinter.CHORD)
cvs.pack()
root.mainloop()