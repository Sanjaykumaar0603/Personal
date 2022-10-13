import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import random
def get_input():
    secondpage.destroy()
    global name
    global startamt
    global currentamt
    global Sno
    name=value1.get()
    startamt=value2.get()
    currentamt=startamt
    Sno=1
    global pca
    pca=[name,startamt,currentamt,0]
def nofreedom():
    page5.destroy()
    forthpage()
def lastpage():
    global page5
    page5=tk.Tk()
    lb=Label(page5,text='RESULT:',bg='black',fg='white',bd=0)
    lb.place(x=10,y=40)
    page5.title('Game over')
    page5.geometry('800x500')
    page5.configure(bg='Black')
    score1=PhotoImage(file='Scoreboard.png')
    board1=Label(page5,image=score1,bd=0,bg='Black')
    board1.place(x=20,y=60)
    score2=PhotoImage(file='GAME-OVER.png')
    TEXT10=Label(page5,image=score2,bg='Black',bd=0)
    TEXT10.place(x=230,y=0)
    TEXT11=Label(page5,text='S.NO',fg='white',bg='black',bd=0,font='bold')
    TEXT11.place(x=30,y=80)
    TEXT12=Label(page5,text='PLAYER NAME',bg='black',fg='white',bd=0,font='bold')
    TEXT12.place(x=132,y=80)
    TEXT13=Label(page5,text='STARTING',bg='black',fg='white',bd=0,font='bold')
    TEXT13.place(x=295,y=75)
    TEXT14=Label(page5,text='BALANCE',bg='black',fg='white',bd=0,font='bold')
    TEXT14.place(x=295,y=100)
    TEXT15=Label(page5,text='ENDING BALANCE',bg='black',fg='white',bd=0,font='bold')
    TEXT15.place(x=480,y=80)
    TEXT16=Label(page5,text='GAMES',bg='black',fg='white',bd=0,font='bold')
    TEXT16.place(x=670,y=75)
    TEXT17=Label(page5,text='PLAYED',bg='black',fg='white',bd=0,font='bold')
    TEXT17.place(x=670,y=102)
    result1=Label(page5,text='1',fg='white',bg='black',bd=0,font='bold')
    result1.place(x=30,y=135)
    result2=Label(page5,text=pca[0],bg='black',fg='white',bd=0,font='bold')
    result2.place(x=132,y=135)
    result3=Label(page5,text=str(pca[1]),bg='black',fg='white',bd=0,font='bold')
    result3.place(x=295,y=135)
    result4=Label(page5,text=str(pca[2]),bg='black',fg='white',bd=0,font='bold')
    result4.place(x=480,y=135)
    result5=Label(page5,text=str(pca[3]),bg='black',fg='white',bd=0,font='bold')
    result5.place(x=670,y=135)  
    if pca[1]<pca[2] and pca[2]>0:
        gr0=Label(page5,text='You managed to make more money ,',fg='white',bg='black',font='Arial',bd=0)
        gr0.place(x=10,y=385)
        gr02=Label(page5,text='you take home',fg='white',bg='black',bd=0,font='Arial')
        gr02.place(x=370,y=385)
        gr01=Label(page5,text=str(pca[2]),fg='white',bg='black',bd=0,font='Arial')
        gr01.place(x=515,y=385)
        renderresult2=PhotoImage(file='YOU-WIN.png')
        gr1=Label(page5,image=renderresult2,bd=0,bg='black')
        gr1.place(x=50,y=420)

    if pca[1]>=pca[2] and pca[2]>=0:
        gr101=Label(page5,text='You didnt manage to make more money ,',fg='white',font='Arial',bg='black',bd=0)
        gr101.place(x=10,y=385)
        gr020=Label(page5,text='you take home',fg='white',bg='black',bd=0,font='Arial')
        gr020.place(x=390,y=385)
        gr010=Label(page5,text=str(pca[2]),fg='white',bg='black',bd=0,font='Arial')
        gr010.place(x=535,y=385)
        renderresult20=PhotoImage(file='YOU-LOSE.png')
        gr10=Label(page5,image=renderresult20,bd=0,bg='black')
        gr10.place(x=50,y=420)
    if pca[2]<0:
        gr101=Label(page5,text='You didnt manage to make more money ,',fg='white',font='Arial',bg='black',bd=0)
        gr101.place(x=10,y=385)
        gr020=Label(page5,text='you owe the casino',fg='white',bg='black',bd=0,font='Arial')
        gr020.place(x=390,y=385)
        global mm2
        mm2=0-pca[2]
        gr010=Label(page5,text=str(mm2),fg='white',bg='black',bd=0,font='Arial')
        gr010.place(x=570,y=385)
        renderresult20=PhotoImage(file='YOU-LOSE.png')
        gr10=Label(page5,image=renderresult20,bd=0,bg='black')
        gr10.place(x=50,y=420)
        gr021=Label(page5,text='you cannot leave until you repay',fg='white',bg='black',bd=0,font='Arial')
        gr021.place(x=510,y=420)
    quitts=PhotoImage(file='endgame.png')
    button99=Button(page5,image=quitts,relief=SUNKEN,bd=0,bg='black',activebackground='black',command=gameover)
    button99.place(x=600,y=450)
    if pca[2]<0:
        button99.destroy()
        button990=Button(page5,text='GO BACK',font='Arial',fg='white',bd=0,bg='black',activebackground='black',command=nofreedom)
        button990.place(x=600,y=450)
    page5.mainloop()
def membership():
    mem=tk.Tk()
    mem.title('Membership only')
    mem.geometry('220x220')
    mem.configure(bg='light green')
    l1abel=Label(mem,text='FOR',bg='light green',fg='red',bd=0,font='arial')
    l1abel.place(x=10,y=30)
    l2abel=Label(mem,text='PREMIUM MEMBERS',bg='light green',fg='red',bd=0,font='arial')
    l2abel.place(x=5,y=60)
    l3abel=Label(mem,text='ONLY',bg='light green',fg='red',bd=0,font='arial')
    l3abel.place(x=30,y=90)
    backbut2=Button(mem,text='GO BACK',activebackground='pink',bg='pink',fg='blue',font='arial',command=mem.destroy)
    backbut2.place(x=100,y=170)
    backbut20=Button(mem,text='BUY PREMIUM',bg='gold',activebackground='gold',fg='red',font='arial')
    backbut20.place(x=20,y=120)
    mem.mainloop()
def myaccount():
    acc=tk.Tk()
    acc.title('my account balance')
    acc.geometry('220x220')
    acc.configure(bg='White')
    balance=pca[2]
    lab1=Label(acc,text='BALANCE :',fg='black',font='arial',bg='white',bd=0)
    lab1.place(x=50,y=10)
    lab2=Label(acc,text=str(balance),font='arial',fg='black',bg='white',bd=0)
    lab2.place(x=50,y=50)
    backbut=Button(acc,text='GO BACK',activebackground='blue',bg='Blue',fg='white',font='arial',command=acc.destroy)
    backbut.place(x=100,y=170)
    acc.mainloop()
def freedom():
    fourthpage.destroy()
    lastpage()
def forthpage():
    global fourthpage
    fourthpage=tk.Tk()
    fourthpage.title('Casino royale')
    fourthpage.geometry('600x601')
    render4=PhotoImage(file='Screenshot (220).png')
    img4=Label(fourthpage,image=render4)
    img4.pack()
    imag1=PhotoImage(file='Screenshot (220)1.png')
    b01=Button(fourthpage,image=imag1,bd=0,bg='#2B86BD',activebackground='#2B86BD',command=roulette)
    b01.place(x=52,y=70)
    imag2=PhotoImage(file='Screenshot (220)2.png')
    b02=Button(fourthpage,image=imag2,bd=0,bg='#2B86BD',activebackground='#2B86BD',command=slots)
    b02.place(x=47,y=250)
    imag3=PhotoImage(file='Screenshot (220)3.png')
    b03=Button(fourthpage,image=imag3,bd=0,bg='#2B86BD',activebackground='#2B86BD',command=slots)
    b03.place(x=353,y=107)
    imag4=PhotoImage(file='Screenshot (220)5.png')
    b04=Button(fourthpage,image=imag4,bd=0,bg='#2B86BD',activebackground='#2B86BD',command=scratchcards)
    b04.place(x=417,y=45)
    imag5=PhotoImage(file='Screenshot (220)4.png')
    b05=Button(fourthpage,image=imag5,bd=0,bg='#2B86BD',activebackground='#2B86BD',command=myaccount)
    b05.place(x=237,y=40)
    imag6=PhotoImage(file='Screenshot (220)7.png')
    b06=Button(fourthpage,image=imag6,bd=0,bg='#2B86BD',activebackground='#2B86BD',command=craps)
    b06.place(x=268,y=374)
    imag7=PhotoImage(file='Screenshot (220)8.png')
    b07=Button(fourthpage,image=imag7,bd=0,bg='#2B86BD',activebackground='#2B86BD',command=membership)
    b07.place(x=449,y=245)
    imag8=PhotoImage(file='Screenshot (220)6.png')
    b08=Button(fourthpage,image=imag8,bd=0,bg='#2B86BD',activebackground='#2B86BD',command=membership)
    b08.place(x=60,y=444)
    imag9=PhotoImage(file='Screenshot (220)9.png')
    b09=Button(fourthpage,image=imag9,bd=0,bg='#2B86BD',activebackground='#2B86BD',command=membership)
    b09.place(x=238,y=483)
    imag10=PhotoImage(file='Screenshot (220)10.png')
    b010=Button(fourthpage,image=imag10,bd=0,bg='#2B86BD',activebackground='#2B86BD',command=membership)
    b010.place(x=462,y=424)
    imag11=PhotoImage(file='Screenshot (220)11.png')
    b011=Button(fourthpage,image=imag11,bd=0,bg='#2B86BD',activebackground='#2B86BD',command=freedom)
    b011.place(x=233,y=250)
    fourthpage.mainloop()
def rems2():
    if rroll0==selected:
        global info4
        info4=Label(page2,bg='#1C7022',bd=0,width=18,height=8)
        info4.place(x=420,y=20)
    else:
        global info7
        info7=Label(page2,bg='#1C7022',bd=0,width=18,height=8)
        info7.place(x=420,y=160)
    text01.destroy()
    sel1.destroy()
    if rroll0==26:
        #26
        spin1.destroy()
    if rroll0==0:
        #0
        spin2.destroy()
    if rroll0==32:
        #32
        spin3.destroy()
    if rroll0==15:
        #15
        spin4.destroy()
    if rroll0==19:
        #19
        spin5.destroy()
    if rroll0==4:
        #4
        spin6.destroy()
    if rroll0==21:
        #21
        spin7.destroy()
    if rroll0==2:
        #2
        spin8.destroy()
    if rroll0==25:
        #25
        spin9.destroy()
    if rroll0==17:
        #17
        spin10.destroy()
    if rroll0==34:
        #34
        spin11.destroy()
    if rroll0==6:
        #6
        spin12.destroy()
    if rroll0==27:
        #27
        spin13.destroy()
    if rroll0==13:
        #13
        spin14.destroy()
    if rroll0==36:
        #36
        spin15.destroy()
    if rroll0==11:
        #11
        spin16.destroy()
    if rroll0==30:
        #30
        spin17.destroy()
    if rroll0==8:
        #8
        spin18.destroy()
    if rroll0==23:
        #23
        spin19.destroy()
    if rroll0==10:
        #10
        spin20.destroy()
    if rroll0==5:
        #5
        spin21.destroy()
    if rroll0==24:
        #24
        spin22.destroy()
    if rroll0==16:
        #16
        spin23.destroy()
    if rroll0==33:
        #33
        spin24.destroy()
    if rroll0==1:
        #1
        spin25.destroy()
    if rroll0==20:
        #20
        spin26.destroy()
    if rroll0==14:
        #14
        spin27.destroy()
    if rroll0==31:
        #31
        spin28.destroy()
    if rroll0==9:
        #9
        spin29.destroy()
    if rroll0==22:
        #22
        spin30.destroy()
    if rroll0==18:
        #18
        spin31.destroy()
    if rroll0==29:
        #29
        spin32.destroy()
    if rroll0==7:
        #7
        spin33.destroy()
    if rroll0==28:
        #28
        spin34.destroy()
    if rroll0==12:
        #12
        spin35.destroy()
    if rroll0==35:
        #35
        spin36.destroy()
    if rroll0==3:
        #3
        spin37.destroy()
def jackpot():
    global text02
    text02=Label(page1,width=40,height=4,bg='#E5C826')
    text02.place(x=280,y=8)
def reset1():
    opbutton.destroy()
    global puck1
    puck1=Label(page3,text='OFF',bg='Black',fg='White',bd=0)
    puck1.place(x=130,y=120)
    try:
        opbutton22.destroy()
    except:
        pass
    optext11.destroy()
    try:
        optext12.destroy()
    except:
        pass
    try:
        optext13.destroy()
    except:
        pass
    try:
        puck2.destroy()
    except:
        pass
    try:
        puck3.destroy()
    except:
        pass
    try:
        puck4.destroy()
    except:
        pass
    try:
        puck5.destroy()
    except:
        pass
    try:
        puck6.destroy()
    except:
        pass
    try:
        puck7.destroy()
    except:
        pass
    if oproll1==1:
        opdiepic1.destroy()
    if oproll1==2:
        opdiepic10.destroy()
    if oproll1==3:
        opdiepic11.destroy()
    if oproll1==4:
        opdiepic12.destroy()
    if oproll1==5:
        opdiepic13.destroy()
    if oproll1==6:
        opdiepic14.destroy()
    if oproll2==1:
        opdiepic2.destroy()
    if oproll2==2:
        opdiepic20.destroy()
    if oproll2==3:
        opdiepic21.destroy()
    if oproll2==4:
        opdiepic22.destroy()
    if oproll2==5:
        opdiepic23.destroy()
    if oproll2==6:
        opdiepic24.destroy()
def destrcraps():
    text11.destroy()
    try:
        text12.destroy()
    except:
        pass
    try:
        text13.destroy()
    except:
        pass
    if croll1==1:
        diepic1.destroy()
    if croll1==2:
        diepic10.destroy()
    if croll1==3:
        diepic11.destroy()
    if croll1==4:
        diepic12.destroy()
    if croll1==5:
        diepic13.destroy()
    if croll1==6:
        diepic14.destroy()
    if croll2==1:
        diepic2.destroy()
    if croll2==2:
        diepic20.destroy()
    if croll2==3:
        diepic21.destroy()
    if croll2==4:
        diepic22.destroy()
    if croll2==5:
        diepic23.destroy()
    if croll2==6:
        diepic24.destroy()
def destrcraps2():
    optext11.destroy()
    optext14.destroy()
    if oproll1==1:
        opdiepic1.destroy()
    if oproll1==2:
        opdiepic10.destroy()
    if oproll1==3:
        opdiepic11.destroy()
    if oproll1==4:
        opdiepic12.destroy()
    if oproll1==5:
        opdiepic13.destroy()
    if oproll1==6:
        opdiepic14.destroy()
    if oproll2==1:
        opdiepic2.destroy()
    if oproll2==2:
        opdiepic20.destroy()
    if oproll2==3:
        opdiepic21.destroy()
    if oproll2==4:
        opdiepic22.destroy()
    if oproll2==5:
        opdiepic23.destroy()
    if oproll2==6:
        opdiepic24.destroy()
def winnerroll1():
    try:
        text11.destroy()
    except:
        pass
    if croll1==1:
        diepic1.destroy()
    if croll1==2:
        diepic10.destroy()
    if croll1==3:
        diepic11.destroy()
    if croll1==4:
        diepic12.destroy()
    if croll1==5:
        diepic13.destroy()
    if croll1==6:
        diepic14.destroy()
    if croll2==1:
        diepic2.destroy()
    if croll2==2:
        diepic20.destroy()
    if croll2==3:
        diepic21.destroy()
    if croll2==4:
        diepic22.destroy()
    if croll2==5:
        diepic23.destroy()
    if croll2==6:
        diepic24.destroy()
    global oproll1
    oproll1=random.randint(1,6)
    global oproll2
    oproll2=random.randint(1,6)
    opdies=oproll1+oproll2
    global optext11
    optext11=Label(page3,bg='Light yellow',text='You rolled '+str(opdies),font='Arial')
    optext11.place(x=50,y=400)
    if oproll1==1:
        global opdiepic1
        opdiepic1=Label(page3,text='*',bg='red',fg='white',font='arial',width=4,height=2)
        opdiepic1.place(x=360,y=370)
    if oproll1==2:
        global opdiepic10
        opdiepic10=Label(page3,text='*  *',bg='red',fg='white',font='arial',width=4,height=2)
        opdiepic10.place(x=360,y=370)
    if oproll1==3:
        global opdiepic11
        opdiepic11=Label(page3,text='*   *\n*',bg='red',fg='white',font='arial',width=4,height=2)
        opdiepic11.place(x=360,y=370)
    if oproll1==4:
        global opdiepic12
        opdiepic12=Label(page3,text='*  *\n*  *',bg='red',fg='white',font='arial',width=4,height=2)
        opdiepic12.place(x=360,y=370)
    if oproll1==5:
        global opdiepic13
        opdiepic13=Label(page3,text='* * *\n*  *',bg='red',fg='white',font='arial',width=4,height=2)
        opdiepic13.place(x=360,y=370)
    if oproll1==6:
        global opdiepic14
        opdiepic14=Label(page3,text='* * *\n* * *',bg='red',fg='white',font='arial',width=4,height=2)
        opdiepic14.place(x=360,y=370)
    if oproll2==1:
        global opdiepic2
        opdiepic2=Label(page3,text='*',bg='red',fg='white',font='arial',width=4,height=2)
        opdiepic2.place(x=420,y=370)
    if oproll2==2:
        global opdiepic20
        opdiepic20=Label(page3,text='*  *',bg='red',fg='white',font='arial',width=4,height=2)
        opdiepic20.place(x=420,y=370)
    if oproll2==3:
        global opdiepic21
        opdiepic21=Label(page3,text='*   *\n*',bg='red',fg='white',font='arial',width=4,height=2)
        opdiepic21.place(x=420,y=370)
    if oproll2==4:
        global opdiepic22
        opdiepic22=Label(page3,text='*  *\n*  *',bg='red',fg='white',font='arial',width=4,height=2)
        opdiepic22.place(x=420,y=370)
    if oproll2==5:
        global opdiepic23
        opdiepic23=Label(page3,text='* * *\n*  *',bg='red',fg='white',font='arial',width=4,height=2)
        opdiepic23.place(x=420,y=370)
    if oproll2==6:
        global opdiepic24
        opdiepic24=Label(page3,text='* * *\n* * *',bg='red',fg='white',font='arial',width=4,height=2)
        opdiepic24.place(x=420,y=370)
    if onpos==opdies:
        global optext12
        optext12=Label(page3,text='YOU WON',bg='Light yellow',fg='purple',font='ARIAL')
        optext12.place(x=650,y=10)
        global crapsl
        crapsl=[Sno,crapsl[1]+(int(entryamt3)*4)]
        gamereset1=Button(page3,text='RESET',fg='White',font='ARIAL',bg='#202C4E',command=reset1)
        gamereset1.place(x=690,y=220)
    elif opdies in (7,11):
        global optext13
        optext13=Label(page3,text='YOU LOST',bg='Light yellow',fg='purple',font='Arial')
        optext13.place(x=650,y=10)
        gamereset1=Button(page3,fg='WHITE',text='RESET',font='ARIAL',bg='#202C4E',command=reset1)
        gamereset1.place(x=690,y=220)
    else:
        global optext14
        optext14=Label(page3,text='ROLL AGAIN',bg='Light yellow',font='ARIAL')
        optext14.place(x=50,y=450)
        global opbutton22
        opbutton22=Button(page3,text='Re roll',fg='black',bg='pink',activebackground='pink',command=destrcraps2)
        opbutton22.place(x=730,y=330)
def scratchagain():
    try:
        resultcolor1.destroy()
    except:
        pass
    try:
        resultcolor2.destroy()
    except:
        pass
    try:
        resultcolor3.destroy()
    except:
        pass
    try:
        resultcolor4.destroy()
    except:
        pass
    try:
        resultcolor5.destroy()
    except:
        pass
    try:
        resultcolor6.destroy()
    except:
        pass
    try:
        resultcolor7.destroy()
    except:
        pass
    try:
        resultcolor8.destroy()
    except:
        pass
    try:
        resultcolor9.destroy()
    except:
        pass
    try:
        resultcolor10.destroy()
    except:
        pass
    try:
        resultcolor11.destroy()
    except:
        pass
    try:
        resultcolor12.destroy()
    except:
        pass
    try:
        resultcolor13.destroy()
    except:
        pass
    try:
        resultcolor14.destroy()
    except:
        pass
    try:
        resultcolor15.destroy()
    except:
        pass
    if cardlist[0]==cardlist[1] and cardlist[1]==cardlist[2]:
        global scbg4
        scbg4=Label(page4,bd=0,bg='#ABF1F3',width=22,height=9)
        scbg4.place(x=0,y=40)
    else:
        global scbg6
        scbg6=Label(page4,bd=0,bg='#ABF1F3',width=22,height=9)
        scbg6.place(x=0,y=200)
    cardlist.clear()
    try:
        scratchresult2.destroy()
    except:
        pass
def roll02():
    global entryamt1
    entryamt1=ins1.get()
    global slotsl
    slotsl=[Sno,slotsl[1]-int(entryamt1)]
    l=['red','light pink','green','blue','purple','orange']
    pic1=random.choice(l)
    pic2=random.choice(l)
    pic3=random.choice(l)
    slot1=Label(page1,bg=pic1,width=16,height=9)
    slot1.place(x=125,y=170)
    slot2=Label(page1,bg=pic2,width=16,height=9)
    slot2.place(x=344,y=170)
    slot3=Label(page1,bg=pic3,width=16,height=9)
    slot3.place(x=563,y=170)
    if pic1==pic2 and pic2==pic3:
        text02.destroy()
        button02=Button(page1,text='PLAY AGAIN',bg='red',fg='yellow',font='bold',activebackground='red',command=jackpot)
        button02.place(x=540,y=360)
        slotsl=[Sno,slotsl[1]+(int(entryamt1)*10)]          
def roll2():
    global entryamt2
    entryamt2=ins2.get()
    global roulettel
    roulettel=[Sno,roulettel[1]-int(entryamt2)] 
    global rroll0
    rroll0=random.choice([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36])
    global text01
    text01=Label(page2,fg='White',bg='#1C7022',text='BALL STOPPED AT '+str(rroll0),font='Arial')
    text01.place(x=50,y=450)
    if rroll0==26:
        #26
        global spin1
        spin1=Frame(page2,bg='blue',width=13,height=13)
        spin1.place(x=170,y=41)
    if rroll0==0:
        #0
        global spin2
        spin2=Frame(page2,bg='blue',width=13,height=13)
        spin2.place(x=194,y=40)
    if rroll0==32:
        #32
        global spin3
        spin3=Frame(page2,bg='blue',width=13,height=13)
        spin3.place(x=219,y=41)
    if rroll0==15:
        #15
        global spin4
        spin4=Frame(page2,bg='blue',width=13,height=13)
        spin4.place(x=242,y=46)
    if rroll0==19:
        #19
        global spin5
        spin5=Frame(page2,bg='blue',width=13,height=13)
        spin5.place(x=264,y=54)
    if rroll0==4:
        #4
        global spin6
        spin6=Frame(page2,bg='blue',width=13,height=13)
        spin6.place(x=285,y=64)
    if rroll0==21:
        #21
        global spin7
        spin7=Frame(page2,bg='blue',width=13,height=13)
        spin7.place(x=302,y=77)
    if rroll0==2:
        #2
        global spin8
        spin8=Frame(page2,bg='blue',width=13,height=13)
        spin8.place(x=316,y=92)
    if rroll0==25:
        #25
        global spin9
        spin9=Frame(page2,bg='blue',width=13,height=13)
        spin9.place(x=328,y=109)
    if rroll0==17:
        #17
        global spin10
        spin10=Frame(page2,bg='blue',width=13,height=13)
        spin10.place(x=334,y=127)
    if rroll0==34:
        #34
        global spin11
        spin11=Frame(page2,bg='blue',width=13,height=13)
        spin11.place(x=338,y=146)
    if rroll0==6:
        #6
        global spin12
        spin12=Frame(page2,bg='blue',width=13,height=13)
        spin12.place(x=337,y=164)
    if rroll0==27:
        #27
        global spin13
        spin13=Frame(page2,bg='blue',width=13,height=13)
        spin13.place(x=331,y=183)
    if rroll0==13:
        #13
        global spin14
        spin14=Frame(page2,bg='blue',width=13,height=13)
        spin14.place(x=322,y=200)
    if rroll0==36:
        #36
        global spin15
        spin15=Frame(page2,bg='blue',width=13,height=13)
        spin15.place(x=309,y=216)
    if rroll0==11:
        #11
        global spin16
        spin16=Frame(page2,bg='blue',width=13,height=13)
        spin16.place(x=293,y=230)
    if rroll0==30:
        #30
        global spin17
        spin17=Frame(page2,bg='blue',width=13,height=13)
        spin17.place(x=273,y=241)
    if rroll0==8:
        #8
        global spin18
        spin18=Frame(page2,bg='blue',width=13,height=13)
        spin18.place(x=252,y=250)
    if rroll0==23:
        #23
        global spin19
        spin19=Frame(page2,bg='blue',width=13,height=13)
        spin19.place(x=230,y=256)
    if rroll0==10:
        #10
        global spin20
        spin20=Frame(page2,bg='blue',width=13,height=13)
        spin20.place(x=206,y=260)
    if rroll0==5:
        #5
        global spin21
        spin21=Frame(page2,bg='blue',width=13,height=13)
        spin21.place(x=181,y=259)
    if rroll0==24:
        #24
        global spin22
        spin22=Frame(page2,bg='blue',width=13,height=13)
        spin22.place(x=158,y=256)
    if rroll0==16:
        #16
        global spin23
        spin23=Frame(page2,bg='blue',width=13,height=13)
        spin23.place(x=136,y=249)
    if rroll0==33:
        #33
        global spin24
        spin24=Frame(page2,bg='blue',width=13,height=13)
        spin24.place(x=115,y=240)
    if rroll0==1:
        #1
        global spin25
        spin25=Frame(page2,bg='blue',width=13,height=13)
        spin25.place(x=96,y=228)
    if rroll0==20:
        #20
        global spin26
        spin26=Frame(page2,bg='blue',width=13,height=13)
        spin26.place(x=80,y=214)
    if rroll0==14:
        #14
        global spin27
        spin27=Frame(page2,bg='blue',width=13,height=13)
        spin27.place(x=67,y=199)
    if rroll0==31:
        #31
        global spin28
        spin28=Frame(page2,bg='blue',width=13,height=13)
        spin28.place(x=57,y=182)
    if rroll0==9:
        #9
        global spin29
        spin29=Frame(page2,bg='blue',width=13,height=13)
        spin29.place(x=52,y=164)
    if rroll0==22:
        #22
        global spin30
        spin30=Frame(page2,bg='blue',width=13,height=13)
        spin30.place(x=51,y=145)
    if rroll0==18:
        #18
        global spin31
        spin31=Frame(page2,bg='blue',width=13,height=13)
        spin31.place(x=54,y=127)
    if rroll0==29:
        #29
        global spin32
        spin32=Frame(page2,bg='blue',width=13,height=13)
        spin32.place(x=61,y=109)
    if rroll0==7:
        #7
        global spin33
        spin33=Frame(page2,bg='blue',width=13,height=13)
        spin33.place(x=72,y=92)
    if rroll0==28:
        #28
        global spin34
        spin34=Frame(page2,bg='blue',width=13,height=13)
        spin34.place(x=86,y=77)
    if rroll0==12:
        #12
        global spin35
        spin35=Frame(page2,bg='blue',width=13,height=13)
        spin35.place(x=104,y=63)
    if rroll0==35:
        #35
        global spin36
        spin36=Frame(page2,bg='blue',width=13,height=13)
        spin36.place(x=123,y=52)
    if rroll0==3:
        #3
        global spin37
        spin37=Frame(page2,bg='blue',width=13,height=13)
        spin37.place(x=146,y=46)
    if rroll0==selected:
        info4.destroy()
        roulettel=[Sno,roulettel[1]+(int(entryamt2)*6)]
    else:
        info7.destroy()
    button12=Button(page2,text='PLAY AGAIN',fg='white',bg='blue',activebackground='blue',command=rems2)
    button12.place(x=550,y=450)
def roll3():
    global entryamt3
    entryamt3=ins3.get()
    global crapsl
    crapsl=[Sno,crapsl[1]-int(entryamt3)]
    global croll1
    croll1=random.randint(1,6)
    global croll2
    croll2=random.randint(1,6)
    global dies
    dies=croll1+croll2
    global text11
    text11=Label(page3,width=10,bg='Light yellow',text='You rolled '+str(dies),font='Arial')
    text11.place(x=50,y=400)
    if croll1==1:
        global diepic1
        diepic1=Label(page3,text='*',bg='red',fg='white',font='arial',width=4,height=2)
        diepic1.place(x=360,y=370)
    if croll1==2:
        global diepic10
        diepic10=Label(page3,text='*  *',bg='red',fg='white',font='arial',width=4,height=2)
        diepic10.place(x=360,y=370)
    if croll1==3:
        global diepic11
        diepic11=Label(page3,text='*   *\n*',bg='red',fg='white',font='arial',width=4,height=2)
        diepic11.place(x=360,y=370)
    if croll1==4:
        global diepic12
        diepic12=Label(page3,text='*  *\n*  *',bg='red',fg='white',font='arial',width=4,height=2)
        diepic12.place(x=360,y=370)
    if croll1==5:
        global diepic13
        diepic13=Label(page3,text='* * *\n*  *',bg='red',fg='white',font='arial',width=4,height=2)
        diepic13.place(x=360,y=370)
    if croll1==6:
        global diepic14
        diepic14=Label(page3,text='* * *\n* * *',bg='red',fg='white',font='arial',width=4,height=2)
        diepic14.place(x=360,y=370)
    if croll2==1:
        global diepic2
        diepic2=Label(page3,text='*',bg='red',fg='white',font='arial',width=4,height=2)
        diepic2.place(x=420,y=370)
    if croll2==2:
        global diepic20
        diepic20=Label(page3,text='*  *',bg='red',fg='white',font='arial',width=4,height=2)
        diepic20.place(x=420,y=370)
    if croll2==3:
        global diepic21
        diepic21=Label(page3,text='*   *\n*',bg='red',fg='white',font='arial',width=4,height=2)
        diepic21.place(x=420,y=370)
    if croll2==4:
        global diepic22
        diepic22=Label(page3,text='*  *\n*  *',bg='red',fg='white',font='arial',width=4,height=2)
        diepic22.place(x=420,y=370)
    if croll2==5:
        global diepic23
        diepic23=Label(page3,text='* * *\n*  *',bg='red',fg='white',font='arial',width=4,height=2)
        diepic23.place(x=420,y=370)
    if croll2==6:
        global diepic24
        diepic24=Label(page3,text='* * *\n* * *',bg='red',fg='white',font='arial',width=4,height=2)
        diepic24.place(x=420,y=370)
    if dies in (7,11):
        global text12
        text12=Label(page3,text='YOU WON',bg='Light yellow',fg='purple',font='ARIAL')
        text12.place(x=650,y=10)
        crapsl=[Sno,crapsl[1]+(int(entryamt3)*4)]
    elif dies in (2,3,12):
        global text13
        text13=Label(page3,text='YOU LOST',bg='Light yellow',fg='purple',font='Arial')
        text13.place(x=650,y=10)
    else:
        puck1.destroy()
        global onpos
        onpos=dies
        if onpos==4:
            global puck2
            puck2=Label(page3,text='ON',fg='Black',bg='White',bd=0)
            puck2.place(x=180,y=35)
        if onpos==5:
            global puck3
            puck3=Label(page3,text='ON',fg='Black',bg='White',bd=0)
            puck3.place(x=239,y=35)
        if onpos==6:
            global puck4
            puck4=Label(page3,text='ON',fg='Black',bg='White',bd=0)
            puck4.place(x=297,y=35)
        if onpos==8:
            global puck5
            puck5=Label(page3,text='ON',fg='Black',bg='White',bd=0)
            puck5.place(x=350,y=35)
        if onpos==9:
            global puck6
            puck6=Label(page3,text='ON',fg='Black',bg='White',bd=0)
            puck6.place(x=397,y=35)
        if onpos==10:
            global puck7
            puck7=Label(page3,text='ON',fg='Black',bg='White',bd=0)
            puck7.place(x=455,y=35)
        global opbutton
        opbutton=Button(page3,text='Puck Roll',bg='Orange',font='Bold',activebackground='Orange',command=winnerroll1)
        opbutton.place(x=610,y=330)
        
    button22=Button(page3,text='PLAY AGAIN',fg='Black',font='bold',bg='Light blue',activebackground='Light blue',command=destrcraps)
    button22.place(x=500,y=440)
def roll04():
    global entryamt4
    entryamt4=ins4.get()
    global scratchcardsl
    scratchcardsl=[Sno,scratchcardsl[1]-int(entryamt4)]
def slotscommand():
    global pca
    pca=[name,startamt,slotsl[1],gamesplayed]
    slotsl.clear()
    page1.destroy()
    forthpage()
def roulettecommand():
    global pca
    pca=[name,startamt,roulettel[1],gamesplayed]
    roulettel.clear()
    page2.destroy()
    forthpage()
def crapscommand():
    global pca
    pca=[name,startamt,crapsl[1],gamesplayed]
    crapsl.clear()
    page3.destroy()
    forthpage()
def scratchcardcommand():
    global pca
    pca=[name,startamt,scratchcardsl[1],gamesplayed]
    scratchcardsl.clear()
    page4.destroy()
    forthpage()
def select1():
    global selected
    selected=1
    global sel1
    sel1=Label(page2,bg='#1C7022',width=20,text='YOU SELECTED '+str(selected),font='Bold')
    sel1.place(x=50,y=400)
def select2():
    global selected
    selected=2
    global sel1
    sel1=Label(page2,bg='#1C7022',width=20,text='YOU SELECTED '+str(selected),font='bold')
    sel1.place(x=50,y=400)
def select3():
    global selected
    selected=3
    global sel1
    sel1=Label(page2,bg='#1C7022',width=20,text='YOU SELECTED '+str(selected),font='bold')
    sel1.place(x=50,y=400)
def select4():
    global selected
    selected=4
    global sel1
    sel1=Label(page2,bg='#1C7022',width=20,text='YOU SELECTED '+str(selected),font='bold')
    sel1.place(x=50,y=400) 
def select5():
    global selected
    selected=5
    global sel1
    sel1=Label(page2,bg='#1C7022',width=20,text='YOU SELECTED '+str(selected),font='bold')
    sel1.place(x=50,y=400)
def select6():
    global selected
    selected=6
    global sel1
    sel1=Label(page2,bg='#1C7022',width=20,text='YOU SELECTED '+str(selected),font='bold')
    sel1.place(x=50,y=400)
def select7():
    global selected
    selected=7
    global sel1
    sel1=Label(page2,bg='#1C7022',width=20,text='YOU SELECTED '+str(selected),font='bold')
    sel1.place(x=50,y=400)
def select8():
    global selected
    selected=8
    global sel1
    sel1=Label(page2,bg='#1C7022',width=20,text='YOU SELECTED '+str(selected),font='bold')
    sel1.place(x=50,y=400)
def select9():
    global selected
    selected=9
    global sel1
    sel1=Label(page2,bg='#1C7022',width=20,text='YOU SELECTED '+str(selected),font='bold')
    sel1.place(x=50,y=400)
def select10():
    global selected
    selected=10
    global sel1
    sel1=Label(page2,bg='#1C7022',width=20,text='YOU SELECTED '+str(selected),font='bold')
    sel1.place(x=50,y=400)
def select11():
    global selected
    selected=11
    global sel1
    sel1=Label(page2,bg='#1C7022',width=20,text='YOU SELECTED '+str(selected),font='bold')
    sel1.place(x=50,y=400)
def select12():
    global selected
    selected=12
    global sel1
    sel1=Label(page2,bg='#1C7022',width=20,text='YOU SELECTED '+str(selected),font='bold')
    sel1.place(x=50,y=400)
def select13():
    global selected
    selected=13
    global sel1
    sel1=Label(page2,bg='#1C7022',width=20,text='YOU SELECTED '+str(selected),font='bold')
    sel1.place(x=50,y=400)
def select14():
    global selected
    selected=14
    global sel1
    sel1=Label(page2,bg='#1C7022',width=20,text='YOU SELECTED '+str(selected),font='bold')
    sel1.place(x=50,y=400)
def select15():
    global selected
    selected=15
    global sel1
    sel1=Label(page2,bg='#1C7022',width=20,text='YOU SELECTED '+str(selected),font='bold')
    sel1.place(x=50,y=400)
def select16():
    global selected
    selected=16
    global sel1
    sel1=Label(page2,bg='#1C7022',width=20,text='YOU SELECTED '+str(selected),font='bold')
    sel1.place(x=50,y=400)
def select17():
    global selected
    selected=17
    global sel1
    sel1=Label(page2,bg='#1C7022',width=20,text='YOU SELECTED '+str(selected),font='bold')
    sel1.place(x=50,y=400)
def select18():
    global selected
    selected=18
    global sel1
    sel1=Label(page2,bg='#1C7022',width=20,text='YOU SELECTED '+str(selected),font='bold')
    sel1.place(x=50,y=400)
def select19():
    global selected
    selected=19
    global sel1
    sel1=Label(page2,bg='#1C7022',width=20,text='YOU SELECTED '+str(selected),font='bold')
    sel1.place(x=50,y=400)
def select20():
    global selected
    selected=20
    global sel1
    sel1=Label(page2,bg='#1C7022',width=20,text='YOU SELECTED '+str(selected),font='bold')
    sel1.place(x=50,y=400)
def select21():
    global selected
    selected=21
    global sel1
    sel1=Label(page2,bg='#1C7022',width=20,text='YOU SELECTED '+str(selected),font='bold')
    sel1.place(x=50,y=400)
def select22():
    global selected
    selected=22
    global sel1
    sel1=Label(page2,bg='#1C7022',width=20,text='YOU SELECTED '+str(selected),font='bold')
    sel1.place(x=50,y=400)
def select23():
    global selected
    selected=23
    global sel1
    sel1=Label(page2,bg='#1C7022',width=20,text='YOU SELECTED '+str(selected),font='bold')
    sel1.place(x=50,y=400)
def select24():
    global selected
    selected=24
    global sel1
    sel1=Label(page2,bg='#1C7022',width=20,text='YOU SELECTED '+str(selected),font='bold')
    sel1.place(x=50,y=400)
def select25():
    global selected
    selected=25
    global sel1
    sel1=Label(page2,bg='#1C7022',width=20,text='YOU SELECTED '+str(selected),font='bold')
    sel1.place(x=50,y=400)
def select26():
    global selected
    selected=26
    global sel1
    sel1=Label(page2,bg='#1C7022',width=20,text='YOU SELECTED '+str(selected),font='bold')
    sel1.place(x=50,y=400)
def select27():
    global selected
    selected=27
    global sel1
    sel1=Label(page2,bg='#1C7022',width=20,text='YOU SELECTED '+str(selected),font='bold')
    sel1.place(x=50,y=400)
def select28():
    global selected
    selected=28
    global sel1
    sel1=Label(page2,bg='#1C7022',width=20,text='YOU SELECTED '+str(selected),font='bold')
    sel1.place(x=50,y=400)
def select29():
    global selected
    selected=29
    global sel1
    sel1=Label(page2,bg='#1C7022',width=20,text='YOU SELECTED '+str(selected),font='bold')
    sel1.place(x=50,y=400)
def select30():
    global selected
    selected=30
    global sel1
    sel1=Label(page2,bg='#1C7022',width=20,text='YOU SELECTED '+str(selected),font='bold')
    sel1.place(x=50,y=400)
def select31():
    global selected
    selected=31
    global sel1
    sel1=Label(page2,bg='#1C7022',width=20,text='YOU SELECTED '+str(selected),font='bold')
    sel1.place(x=50,y=400)
def select32():
    global selected
    selected=32
    global sel1
    sel1=Label(page2,bg='#1C7022',width=20,text='YOU SELECTED '+str(selected),font='bold')
    sel1.place(x=50,y=400)
def select33():
    global selected
    selected=33
    global sel1
    sel1=Label(page2,bg='#1C7022',width=20,text='YOU SELECTED '+str(selected),font='bold')
    sel1.place(x=50,y=400)
def select34():
    global selected
    selected=34
    global sel1
    sel1=Label(page2,bg='#1C7022',width=20,text='YOU SELECTED '+str(selected),font='bold')
    sel1.place(x=50,y=400)
def select35():
    global selected
    selected=35
    global sel1
    sel1=Label(page2,bg='#1C7022',width=20,text='YOU SELECTED '+str(selected),font='bold')
    sel1.place(x=50,y=400)
def select36():
    global selected
    selected=36
    global sel1
    sel1=Label(page2,bg='#1C7022',width=20,text='YOU SELECTED '+str(selected),font='bold')
    sel1.place(x=50,y=400)
def card1():
    lcard=['red','light pink','green','blue','purple','orange']
    cardpic1=random.choice(lcard)
    global resultcolor1
    resultcolor1=Label(page4,bg=cardpic1,width=14,height=8,bd=0)
    resultcolor1.place(x=300,y=40)
    global cardlist
    cardlist.append(cardpic1)
    if len(cardlist)==3:
        if cardlist[0]==cardlist[1] and cardlist[1]==cardlist[2]:
            scbg4.destroy()
            global scratchcardsl
            scratchcardsl=[Sno,scratchcardsl[1]+(int(entryamt4)*4)]
        else:
            scbg6.destroy()
def card2():
    lcard=['red','light pink','green','blue','purple','orange']
    cardpic2=random.choice(lcard)
    global resultcolor2
    resultcolor2=Label(page4,bg=cardpic2,width=14,height=8,bd=0)
    resultcolor2.place(x=300,y=165)
    global cardlist
    cardlist.append(cardpic2)
    if len(cardlist)==3:
        if cardlist[0]==cardlist[1] and cardlist[1]==cardlist[2]:
            scbg4.destroy()
            global scratchcardsl
            scratchcardsl=[Sno,scratchcardsl[1]+(int(entryamt4)*4)]
        else:
            scbg6.destroy()
def card3():
    lcard=['red','light pink','green','blue','purple','orange']
    cardpic3=random.choice(lcard)
    global resultcolor3
    resultcolor3=Label(page4,bg=cardpic3,width=14,height=8,bd=0)
    resultcolor3.place(x=300,y=290)
    global cardlist
    cardlist.append(cardpic3)
    if len(cardlist)==3:
        if cardlist[0]==cardlist[1] and cardlist[1]==cardlist[2]:
            scbg4.destroy()
            global scratchcardsl
            scratchcardsl=[Sno,scratchcardsl[1]+(int(entryamt4)*4)]
        else:
            scbg6.destroy()
def card4():
    lcard=['red','light pink','green','blue','purple','orange']
    cardpic4=random.choice(lcard)
    global resultcolor4
    resultcolor4=Label(page4,bg=cardpic4,width=14,height=8,bd=0)
    resultcolor4.place(x=410,y=40)
    global cardlist
    cardlist.append(cardpic4)
    if len(cardlist)==3:
        if cardlist[0]==cardlist[1] and cardlist[1]==cardlist[2]:
            scbg4.destroy()
            global scratchcardsl
            scratchcardsl=[Sno,scratchcardsl[1]+(int(entryamt4)*4)]
        else:
            scbg6.destroy()
def card5():
    lcard=['red','light pink','green','blue','purple','orange']
    cardpic5=random.choice(lcard)
    global resultcolor5
    resultcolor5=Label(page4,bg=cardpic5,width=14,height=8,bd=0)
    resultcolor5.place(x=410,y=165)
    global cardlist
    cardlist.append(cardpic5)
    if len(cardlist)==3:
        if cardlist[0]==cardlist[1] and cardlist[1]==cardlist[2]:
           scbg4.destroy()
           global scratchcardsl
           scratchcardsl=[Sno,scratchcardsl[1]+(int(entryamt4)*4)]
        else:
            scbg6.destroy()
def card6():
    lcard=['red','light pink','green','blue','purple','orange']
    cardpic6=random.choice(lcard)
    global resultcolor6
    resultcolor6=Label(page4,bg=cardpic6,width=14,height=8,bd=0)
    resultcolor6.place(x=410,y=290)
    global cardlist
    cardlist.append(cardpic6)
    if len(cardlist)==3:
        if cardlist[0]==cardlist[1] and cardlist[1]==cardlist[2]:
            scbg4.destroy()
            global scratchcardsl
            scratchcardsl=[Sno,scratchcardsl[1]+(int(entryamt4)*4)]
        else:
            scbg6.destroy()
def card7():
    lcard=['red','light pink','green','blue','purple','orange']
    cardpic7=random.choice(lcard)
    global resultcolor7
    resultcolor7=Label(page4,bg=cardpic7,width=14,height=8,bd=0)
    resultcolor7.place(x=520,y=40)
    global cardlist
    cardlist.append(cardpic7)
    if len(cardlist)==3:
        if cardlist[0]==cardlist[1] and cardlist[1]==cardlist[2]:
            scbg4.destroy()
            global scratchcardsl
            scratchcardsl=[Sno,scratchcardsl[1]+(int(entryamt4)*4)]
        else:
            scbg6.destroy()
def card8():
    lcard=['red','light pink','green','blue','purple','orange']
    cardpic8=random.choice(lcard)
    global resultcolor8
    resultcolor8=Label(page4,bg=cardpic8,width=14,height=8,bd=0)
    resultcolor8.place(x=520,y=165)
    global cardlist
    cardlist.append(cardpic8)
    if len(cardlist)==3:
        if cardlist[0]==cardlist[1] and cardlist[1]==cardlist[2]:
            scbg4.destroy()
            global scratchcardsl
            scratchcardsl=[Sno,scratchcardsl[1]+(int(entryamt4)*4)]
        else:
            scbg6.destroy()
def card9():
    lcard=['red','light pink','green','blue','purple','orange']
    cardpic9=random.choice(lcard)
    global resultcolor9
    resultcolor9=Label(page4,bg=cardpic9,width=14,height=8,bd=0)
    resultcolor9.place(x=520,y=290)
    global cardlist
    cardlist.append(cardpic9)
    if len(cardlist)==3:
        if cardlist[0]==cardlist[1] and cardlist[1]==cardlist[2]:
            scbg4.destroy()
            global scratchcardsl
            scratchcardsl=[Sno,scratchcardsl[1]+(int(entryamt4)*4)]
        else:
            scbg6.destroy()
def card10():
    lcard=['red','light pink','green','blue','purple','orange']
    cardpic10=random.choice(lcard)
    global resultcolor10
    resultcolor10=Label(page4,bg=cardpic10,width=14,height=8,bd=0)
    resultcolor10.place(x=190,y=40)
    global cardlist
    cardlist.append(cardpic10)
    if len(cardlist)==3:
        if cardlist[0]==cardlist[1] and cardlist[1]==cardlist[2]:
            scbg4.destroy()
            global scratchcardsl
            scratchcardsl=[Sno,scratchcardsl[1]+(int(entryamt4)*4)]
        else:
            scbg6.destroy()
def card11():
    lcard=['red','light pink','green','blue','purple','orange']
    cardpic11=random.choice(lcard)
    global resultcolor11
    resultcolor11=Label(page4,bg=cardpic11,width=14,height=8,bd=0)
    resultcolor11.place(x=190,y=165)
    global cardlist
    cardlist.append(cardpic11)
    if len(cardlist)==3:
        if cardlist[0]==cardlist[1] and cardlist[1]==cardlist[2]:
            scbg4.destroy()
            global scratchcardsl
            scratchcardsl=[Sno,scratchcardsl[1]+(int(entryamt4)*4)]
        else:
            scbg6.destroy()
def card12():
    lcard=['red','light pink','green','blue','purple','orange']
    cardpic12=random.choice(lcard)
    global resultcolor12
    resultcolor12=Label(page4,bg=cardpic12,width=14,height=8,bd=0)
    resultcolor12.place(x=190,y=290)
    global cardlist
    cardlist.append(cardpic12)
    if len(cardlist)==3:
        if cardlist[0]==cardlist[1] and cardlist[1]==cardlist[2]:
           scbg4.destroy()
           global scratchcardsl
           scratchcardsl=[Sno,scratchcardsl[1]+(int(entryamt4)*4)]
        else:
            scbg6.destroy()
def card13():
    lcard=['red','light pink','green','blue','purple','orange']
    cardpic13=random.choice(lcard)
    global resultcolor13
    resultcolor13=Label(page4,bg=cardpic13,width=14,height=8,bd=0)
    resultcolor13.place(x=630,y=40)
    global cardlist
    cardlist.append(cardpic13)
    if len(cardlist)==3:
        if cardlist[0]==cardlist[1] and cardlist[1]==cardlist[2]:
           scbg4.destroy()
           global scratchcardsl
           scratchcardsl=[Sno,scratchcardsl[1]+(int(entryamt4)*4)]
        else:
            scbg6.destroy()
def card14():
    lcard=['red','light pink','green','blue','purple','orange']
    cardpic14=random.choice(lcard)
    global resultcolor14
    resultcolor14=Label(page4,bg=cardpic14,width=14,height=8,bd=0)
    resultcolor14.place(x=630,y=165)
    global cardlist
    cardlist.append(cardpic14)
    if len(cardlist)==3:
        if cardlist[0]==cardlist[1] and cardlist[1]==cardlist[2]:
            scbg4.destroy()
            global scratchcardsl
            scratchcardsl=[Sno,scratchcardsl[1]+(int(entryamt4)*4)]
        else:
            scbg6.destroy()
def card15():
    lcard=['red','light pink','green','blue','purple','orange']
    cardpic15=random.choice(lcard)
    global resultcolor15
    resultcolor15=Label(page4,bg=cardpic15,width=14,height=8,bd=0)
    resultcolor15.place(x=630,y=290)
    global cardlist
    cardlist.append(cardpic15)
    if len(cardlist)==3:
        if cardlist[0]==cardlist[1] and cardlist[1]==cardlist[2]:
            scbg4.destroy()
            global scratchcardsl
            scratchcardsl=[Sno,scratchcardsl[1]+(int(entryamt4)*4)]
        else:
            scbg6.destroy()
def slots():
    global gamesplayed
    gamesplayed=gamesplayed+1
    fourthpage.destroy()
    global curamm
    curamm=pca[2]
    global slotsl
    slotsl=[Sno,curamm]
    page01=tk.Tk()
    page01.title('Slots Rules')
    page01.geometry('800x500')
    rander1=PhotoImage(file='slotinfo.png')
    infobag1=Label(page01,image=rander1,bd=0)
    infobag1.pack()
    rander01=PhotoImage(file='plays.png')
    infobut1=Button(page01,image=rander01,bd=0,bg='black',activebackground='black',command=page01.destroy)
    infobut1.place(x=670,y=450)
    page01.mainloop()
    global page1
    page1=tk.Tk()
    page1.title('Slots')
    page1.geometry('800x500')
    page1.configure(bg='#E5C826')
    render01=PhotoImage(file='Slotsbg.png')
    pho01=Label(page1,image=render01,bd=0,bg='#E5C826')
    pho01.place(x=0,y=75)
    render04=PhotoImage(file='Slotsexit.png')
    button1=Button(page1,image=render04,bd=0,bg='#E5C826',activebackground='#E5C826',command=slotscommand)
    button1.place(x=652,y=448)
    render02=PhotoImage(file='slotsrollbutton.png')
    button01=Button(page1,image=render02,bg='#E5C826',activebackground='#E5C826',relief=FLAT,bd=0,command=roll02)
    button01.place(x=290,y=355)
    jack=PhotoImage(file='JACKPOT.png')
    texter=Label(page1,image=jack,bg='#E5C826')
    texter.place(x=280,y=8)
    global text02
    text02=Label(page1,width=40,height=4,bg='#E5C826')
    text02.place(x=280,y=8)
    global ins1
    ins1=StringVar()
    insert1=Entry(page1,text='Enter money',width=37,font='Arial',fg='Green',bd=0,bg='Black',textvariable=ins1)
    insert1.place(x=198,y=92)
    page1.mainloop()
def roulette():
    global gamesplayed
    gamesplayed=gamesplayed+1
    global curamm2
    curamm2=pca[2]
    global roulettel
    roulettel=[Sno,curamm2]
    fourthpage.destroy()
    page02=tk.Tk()
    page02.title('Roulette Rules')
    page02.geometry('800x500')
    rander2=PhotoImage(file='rouletteinfo.png')
    infobag2=Label(page02,image=rander2,bd=0)
    infobag2.pack()
    rander02=PhotoImage(file='playr.png')
    infobut2=Button(page02,image=rander02,bd=0,bg='#854A28',activebackground='#854A28',command=page02.destroy)
    infobut2.place(x=650,y=420)
    page02.mainloop()
    global page2
    page2=tk.Tk()
    page2.title('Roulette')
    page2.geometry('900x600')
    render00=PhotoImage(file='Screenshot (340).png')
    mainbrg=Label(page2,image=render00,bd=0)
    mainbrg.place(x=0,y=0)
    render11=PhotoImage(file='Screenshot (233)1.png')
    bg1=Label(page2,image=render11,bd=0,bg='#1C7022')
    bg1.place(x=0,y=0)
    render12=PhotoImage(file='roulettetable.png')
    bg2=Label(page2,image=render12,bd=0,bg='#1C7022')
    bg2.place(x=550,y=10)
    render60=PhotoImage(file='YOU.png')
    info2=Label(page2,image=render60,bd=0,bg='#1C7022')
    info2.place(x=420,y=20)
    render61=PhotoImage(file='WON.png')
    info3=Label(page2,image=render61,bd=0,bg='#1C7022')
    info3.place(x=420,y=85)
    global info4
    info4=Label(page2,bg='#1C7022',bd=0,width=18,height=8)
    info4.place(x=420,y=20)
    render62=PhotoImage(file='YOU2.png')
    info5=Label(page2,image=render62,bd=0,bg='#1C7022')
    info5.place(x=420,y=160)
    render63=PhotoImage(file='LOST2.png')
    info6=Label(page2,image=render63,bd=0,bg='#1C7022')
    info6.place(x=430,y=205)
    global info7
    info7=Label(page2,bg='#1C7022',bd=0,width=18,height=8)
    info7.place(x=420,y=160)
    render50=PhotoImage(file='reb.png')
    button2=Button(page2,bd=0,image=render50,bg='#1C7022',activebackground='#1C7022',command=roulettecommand)
    button2.place(x=650,y=450)
    render51=PhotoImage(file='rsb.png')
    rbutton11=Button(page2,image=render51,bg='#1C7022',activebackground='#1C7022',bd=0,command=roll2)
    rbutton11.place(x=440,y=440)
    info1=Label(page2,text='Enter money',bg='#1C7022',font='Bold',fg='White',bd=0)
    info1.place(x=10,y=300)
    global ins2
    ins2=StringVar()
    insert2=Entry(page2,text='Enter money',width=20,fg='Red',bg='Black',font='Arial',bd=2,textvariable=ins2)
    insert2.place(x=75,y=330)
    render13=PhotoImage(file='1.png')
    button12=Button(page2,image=render13,bd=0,command=select1)
    button12.place(x=613,y=60)
    render14=PhotoImage(file='2.png')
    button13=Button(page2,image=render14,bd=0,command=select2)
    button13.place(x=657,y=60)
    render15=PhotoImage(file='3.png')
    button14=Button(page2,image=render15,bd=0,command=select3)
    button14.place(x=701,y=60)
    render16=PhotoImage(file='4.png')
    button15=Button(page2,image=render16,bd=0,command=select4)
    button15.place(x=613,y=90)
    render17=PhotoImage(file='5.png')
    button16=Button(page2,image=render17,bd=0,command=select5)
    button16.place(x=657,y=90)
    render18=PhotoImage(file='6.png')
    button17=Button(page2,image=render18,bd=0,command=select6)
    button17.place(x=701,y=90)
    render19=PhotoImage(file='7.png')
    button18=Button(page2,image=render19,bd=0,command=select7)
    button18.place(x=613,y=120)
    render20=PhotoImage(file='8.png')
    button19=Button(page2,image=render20,bd=0,command=select8)
    button19.place(x=657,y=120)
    render21=PhotoImage(file='9.png')
    button20=Button(page2,image=render21,bd=0,command=select9)
    button20.place(x=701,y=120)
    render22=PhotoImage(file='10.png')
    button21=Button(page2,image=render22,bd=0,command=select10)
    button21.place(x=613,y=151)
    render23=PhotoImage(file='11.png')
    button22=Button(page2,image=render23,bd=0,command=select11)
    button22.place(x=657,y=150)
    render24=PhotoImage(file='12.png')
    button23=Button(page2,image=render24,bd=0,command=select12)
    button23.place(x=701,y=150)
    render25=PhotoImage(file='13.png')
    button24=Button(page2,image=render25,bd=0,command=select13)
    button24.place(x=613,y=181)
    render26=PhotoImage(file='14.png')
    button25=Button(page2,image=render26,bd=0,command=select14)
    button25.place(x=657,y=180)
    render27=PhotoImage(file='15.png')
    button26=Button(page2,image=render27,bd=0,command=select15)
    button26.place(x=701,y=180)
    render28=PhotoImage(file='16.png')
    button27=Button(page2,image=render28,bd=0,command=select16)
    button27.place(x=613,y=211)
    render29=PhotoImage(file='17.png')
    button28=Button(page2,image=render29,bd=0,command=select17)
    button28.place(x=657,y=210)
    render30=PhotoImage(file='18.png')
    button29=Button(page2,image=render30,bd=0,command=select18)
    button29.place(x=701,y=210)
    render31=PhotoImage(file='19.png')
    button30=Button(page2,image=render31,bd=0,command=select19)
    button30.place(x=613,y=241)
    render32=PhotoImage(file='20.png')
    button31=Button(page2,image=render32,bd=0,command=select20)
    button31.place(x=657,y=240)
    render33=PhotoImage(file='21.png')
    button32=Button(page2,image=render33,bd=0,command=select21)
    button32.place(x=701,y=240)
    render34=PhotoImage(file='22.png')
    button33=Button(page2,image=render34,bd=0,command=select22)
    button33.place(x=613,y=271)
    render35=PhotoImage(file='23.png')
    button34=Button(page2,image=render35,bd=0,command=select23)
    button34.place(x=657,y=270)
    render36=PhotoImage(file='24.png')
    button35=Button(page2,image=render36,bd=0,command=select24)
    button35.place(x=701,y=270)
    render37=PhotoImage(file='25.png')
    button36=Button(page2,image=render37,bd=0,command=select25)
    button36.place(x=613,y=301)
    render38=PhotoImage(file='26.png')
    button37=Button(page2,image=render38,bd=0,command=select26)
    button37.place(x=657,y=300)
    render39=PhotoImage(file='27.png')
    button38=Button(page2,image=render39,bd=0,command=select27)
    button38.place(x=701,y=300)
    render40=PhotoImage(file='28.png')
    button39=Button(page2,image=render40,bd=0,command=select28)
    button39.place(x=613,y=330)
    render41=PhotoImage(file='29.png')
    button40=Button(page2,image=render41,bd=0,command=select29)
    button40.place(x=657,y=330)
    render42=PhotoImage(file='30.png')
    button41=Button(page2,image=render42,bd=0,command=select30)
    button41.place(x=701,y=329)
    render43=PhotoImage(file='31.png')
    button42=Button(page2,image=render43,bd=0,command=select31)
    button42.place(x=613,y=360)
    render44=PhotoImage(file='32.png')
    button43=Button(page2,image=render44,bd=0,command=select32)
    button43.place(x=657,y=360)
    render45=PhotoImage(file='33.png')
    button44=Button(page2,image=render45,bd=0,command=select33)
    button44.place(x=701,y=359)
    render46=PhotoImage(file='34.png')
    button45=Button(page2,image=render46,bd=0,command=select34)
    button45.place(x=613,y=389)
    render47=PhotoImage(file='35.png')
    button46=Button(page2,image=render47,bd=0,command=select35)
    button46.place(x=657,y=389)
    render48=PhotoImage(file='36.png')
    button47=Button(page2,image=render48,bd=0,command=select36)
    button47.place(x=701,y=389)
    page2.mainloop()
def craps():
    global gamesplayed
    gamesplayed+=1
    global curamm3
    curamm3=pca[2]
    global crapsl
    crapsl=[Sno,curamm3]
    fourthpage.destroy()
    page03=tk.Tk()
    page03.title('Craps Rules')
    page03.geometry('800x500')
    rander3=PhotoImage(file='crapsinfo.png')
    infobag3=Label(page03,image=rander3,bd=0)
    infobag3.pack()
    rander03=PhotoImage(file='playc.png')
    infobut3=Button(page03,image=rander03,bd=0,bg='black',activebackground='black',command=page03.destroy)
    infobut3.place(x=650,y=420)
    page03.mainloop()
    global page3
    page3=tk.Tk()
    page3.title('Craps')
    page3.geometry('900x600')
    render000=PhotoImage(file='Screenshot 2(340).png')
    mainbcg=Label(page3,image=render000,bd=0)
    mainbcg.place(x=0,y=0)
    ren1=PhotoImage(file='Crapsbg.png')
    bgr1=Label(page3,image=ren1,bg='Brown',bd=0)
    bgr1.place(x=46,y=18)
    ren3=PhotoImage(file='ceb.png')
    button3=Button(page3,image=ren3,bd=0,bg='Light Yellow',activebackground='Light yellow',command=crapscommand)
    button3.place(x=650,y=440)
    ren2=PhotoImage(file='Diesroll1.png')
    button21=Button(page3,image=ren2,bg='Light yellow',bd=0,activebackground='Light yellow',command=roll3)
    button21.place(x=580,y=380)
    global ins3
    ins3=StringVar()
    insert3=Entry(page3,bg='Red',fg='Green',textvariable=ins3)
    insert3.place(x=210,y=325)
    global puck1
    puck1=Label(page3,text='OFF',bg='Black',fg='White',bd=0)
    puck1.place(x=130,y=120)
    page3.mainloop()
def scratchcards():
    global gamesplayed
    gamesplayed=gamesplayed+1
    global curamm4
    curamm4=pca[2]
    global scratchcardsl
    scratchcardsl=[Sno,curamm4]
    fourthpage.destroy()
    page04=tk.Tk()
    page04.title('Scartchcard Rules')
    page04.geometry('800x500')
    rander4=PhotoImage(file='scratchcardinfo.png')
    infobag4=Label(page04,image=rander4,bd=0)
    infobag4.pack()
    rander04=PhotoImage(file='playsc.png')
    infobut4=Button(page04,image=rander04,bd=0,bg='#F4DCAE',activebackground='#F4DCAE',command=page04.destroy)
    infobut4.place(x=308,y=283)
    page04.mainloop()
    global page4
    page4=tk.Tk()
    page4.title('scratchcards')
    page4.geometry('800x500')
    page4.configure(bg='#ABF1F3')
    renders4=PhotoImage(file='seb.png')
    button4=Button(page4,image=renders4,bd=0,bg='#ABF1F3',activebackground='#ABF1F3',command=scratchcardcommand)
    button4.place(x=650,y=445)
    renders1=PhotoImage(file='scratchcardsbg.png')
    scbg1=Label(page4,image=renders1,bd=0)
    scbg1.place(x=150,y=10)
    scbg2=Label(page4,text='ENTER MONEY:',font='Italic',fg='Black',bg='#ABF1F3',bd=0)
    scbg2.place(x=5,y=430)
    renders5=PhotoImage(file='YOU3.png')
    scbg3=Label(page4,image=renders5,bd=0,bg='#ABF1F3')
    scbg3.place(x=0,y=40)
    renders6=PhotoImage(file='WIN4.png')
    scbg5=Label(page4,image=renders6,bd=0,bg='#ABF1F3')
    scbg5.place(x=10,y=100)
    global scbg4
    scbg4=Label(page4,bd=0,bg='#ABF1F3',width=22,height=9)
    scbg4.place(x=0,y=40)
    renders51=PhotoImage(file='YOU4.png')
    scbg31=Label(page4,image=renders51,bd=0,bg='#ABF1F3')
    scbg31.place(x=5,y=200)
    renders61=PhotoImage(file='LOSE4.png')
    scbg51=Label(page4,image=renders61,bd=0,bg='#ABF1F3')
    scbg51.place(x=10,y=260)
    global scbg6
    scbg6=Label(page4,bd=0,bg='#ABF1F3',width=22,height=9)
    scbg6.place(x=0,y=200)
    global ins4
    ins4=StringVar()
    insert4=Entry(page4,bg='yellow',fg='purple',font='Arial',textvariable=ins4)
    insert4.place(x=5,y=460)
    renders03=PhotoImage(file='rrb.png')
    button15=Button(page4,image=renders03,bg='#ABF1F3',activebackground='#ABF1F3',bd=0,command=roll04)
    button15.place(x=250,y=450)
    global cardlist
    cardlist=[]
    renders2=PhotoImage(file='Scratchcard.png')
    button5=Button(page4,image=renders2,bd=0,bg='gold',command=card1)
    button5.place(x=300,y=40)
    button6=Button(page4,image=renders2,bd=0,bg='gold',command=card2)
    button6.place(x=300,y=165)
    button7=Button(page4,image=renders2,bd=0,bg='gold',command=card3)
    button7.place(x=300,y=290)
    button8=Button(page4,image=renders2,bd=0,bg='gold',command=card4)
    button8.place(x=410,y=40)
    button9=Button(page4,image=renders2,bd=0,bg='gold',command=card5)
    button9.place(x=410,y=165)
    button10=Button(page4,image=renders2,bd=0,bg='gold',command=card6)
    button10.place(x=410,y=290)
    button11=Button(page4,image=renders2,bd=0,bg='gold',command=card7)
    button11.place(x=520,y=40)
    button12=Button(page4,image=renders2,bd=0,bg='gold',command=card8)
    button12.place(x=520,y=165)
    button13=Button(page4,image=renders2,bd=0,bg='gold',command=card9)
    button13.place(x=520,y=290)
    render5=PhotoImage(file='sncb.png')
    button14=Button(page4,image=render5,bg='#ABF1F3',activebackground='#ABF1F3',bd=0,command=scratchagain)
    button14.place(x=450,y=450)
    button16=Button(page4,image=renders2,bd=0,bg='gold',command=card10)
    button16.place(x=190,y=40)
    button17=Button(page4,image=renders2,bd=0,bg='gold',command=card11)
    button17.place(x=190,y=165)
    button18=Button(page4,image=renders2,bd=0,bg='gold',command=card12)
    button18.place(x=190,y=290)
    button19=Button(page4,image=renders2,bd=0,bg='gold',command=card13)
    button19.place(x=630,y=40)
    button20=Button(page4,image=renders2,bd=0,bg='gold',command=card14)
    button20.place(x=630,y=169)
    button21=Button(page4,image=renders2,bd=0,bg='gold',command=card15)
    button21.place(x=630,y=290)
    page4.mainloop()
def gameover():
    page5.destroy()
    pca.clear()
global pca
global slotsl
global roulettel
global crapsl
global scratchcardsl
pca=[]
slotsl=[]
roulettel=[]
crapsl=[]
scratchcardsl=[]
mainpage=tk.Tk()
mainpage.title('Casino royale')
mainpage.geometry('800x500')
render=PhotoImage(file='Mainpage.png')
img=Label(mainpage,image=render)
img.pack()
render0100=PhotoImage(file='Mainentry1.png')
b1=Button(mainpage,image=render0100,bg='#3C0165',bd=0,activebackground='#3C0165',command=mainpage.destroy)
b1.place(x=328,y=320)
mainpage.mainloop()
global secondpage
secondpage=tk.Tk()
secondpage.title('Casino royale')
secondpage.geometry('800x500')
render2=PhotoImage(file='Secondpage.png')
img2=Label(secondpage,image=render2)
img2.pack()
value1=StringVar()
e1=Entry(secondpage,width=18,fg='red',bg='light yellow',textvariable=value1)
e1.place(x=565,y=82)
value2=IntVar()
e2=Entry(secondpage,width=20,fg='red',bg='light yellow',textvariable=value2)
e2.place(x=343,y=210)
render20=PhotoImage(file='NEXT.png')
b2=Button(secondpage,image=render20,bg='#EB3F33',bd=0,activebackground='#EB3F33',command=get_input)
b2.place(x=290,y=420)
secondpage.mainloop()
thirdpage=tk.Tk()
thirdpage.title('Casino royale')
thirdpage.geometry('800x500')
render3=PhotoImage(file='gameinfo.png')
img3=Label(thirdpage,image=render3)
img3.pack()
phot2=PhotoImage(file='Nextbutton1.png')
b4=Button(thirdpage,image=phot2,bd=0,bg='#764012',activebackground='#764012',command=thirdpage.destroy)
b4.place(x=620,y=430)
global gamesplayed
gamesplayed=0
thirdpage.mainloop()
forthpage()







