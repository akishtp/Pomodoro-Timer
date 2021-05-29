from tkinter import *
import tkinter.font as font
import time

win=Tk()
win.title('Pomodoro Timer')
win.configure(bg='#1c1c1c')
window_height = 550
window_width = 1000
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

photo = PhotoImage(file = "Images/Icon.png")
win.iconphoto(False, photo)

def TimeUpdate():
    global temp
    global restTime
    global nextTime
    global x
    if x =="FOCUS":
        topText.set("REST")
    else:
        topText.set("FOCUS")
    try:
        temp = int(int(minutText.get())*60 + int(secundText.get()))
        if x=="FOCUS":
            if temp<1800:
                restTime=5
            elif temp>1800 and temp<=2700:
                restTime=10
            elif temp>2700 and temp<=3600:
                restTime=15
            elif temp>3600 and temp<=4500:
                restTime=20
            elif temp>4500 and temp<=5400:
                restTime=25
            elif temp>5400:
                restTime=30
        elif x=="REST":
            if temp==300:
                nextTime=25
            elif temp==600:
                nextTime=40
            elif temp==900:
                nextTime=45
            elif temp==1200:
                nextTime=60
            elif temp==1500:
                nextTime=75
            elif temp==1800:
                nextTime=90
    except:
        print("Please input the right value")
    while temp >= 1:
        mins,secs = divmod(temp,60)
        minutText.set("{0:2d}".format(mins))
        secundText.set("{0:2d}".format(secs))
        try:
            win.update()
        except:
            break
        time.sleep(1)
        temp-=1
    if temp == 0:
        if x=="REST":
            secundText.set("00")
            minutText.set(nextTime)
            topText.set("FOCUS")
            x=="FOCUS"
        elif x=="FOCUS":
            secundText.set("00")
            minutText.set(restTime)
            topText.set("REST")
            x="REST"
        
def TimeStop():
    global temp
    topText.set("POMODORO TIMER")
    minutText.set("00")
    secundText.set("00")
    temp = -1

def TimePause():
    global temp
    temp = -1
    x=topText.get()
    if x=="FOCUS":
        x="REST"
    elif x=="REST":
        x="FOCUS"
    topText.set("PAUSED")

def TimeDec():
    Dec = int(minutText.get())
    if Dec >= 5:
        DecVal = Dec - 5
        minutText.set(DecVal)
    else:
        minutText.set("00")

def TimeInc():
    Inc = int(minutText.get())
    if Inc < 95:
        IncVal = Inc + 5
        minutText.set(IncVal)
    else:
        minutText.set("99")

clkFont = font.Font(size=130)
txtFont = font.Font(size=50)
topFont = font.Font(size=30)

temp = 0
nextTime = 0
restTime = 0
x = "REST"

minutText = StringVar()
minutText.set("00")

secundText = StringVar()
secundText.set("00")

topText = StringVar()
topText.set('POMODORO TIMER')

Top = Label(win, textvariable=topText, font=topFont, bg = '#1c1c1c')
Top.grid(row=0, column=1, columnspan=3, pady=35)

MinusBtn = Button(win, text = '-', height = 2, width = 2, font=txtFont, bg = '#1c1c1c', activebackground='#1c1c1c', highlightbackground="#1c1c1c", highlightcolor="#1c1c1c", command= lambda:TimeDec())
MinusBtn.grid(row=1,column=0, padx=36)

minut = Entry(win, textvariable=minutText, width=2, justify=RIGHT, font=clkFont, bg="#1c1c1c", highlightbackground="#1c1c1c", highlightcolor="#1c1c1c")
minut.grid(row=1,column=1)

colon=Label(win, text=":", font=clkFont, bg="#1c1c1c")
colon.grid(row=1,column=2, pady=33)

secund = Entry(win, textvariable=secundText, width=2, justify=RIGHT, font=clkFont, bg="#1c1c1c", highlightbackground="#1c1c1c", highlightcolor="#1c1c1c")
secund.grid(row=1,column=3)

PlusBtn = Button(win, text = '+', height = 2, width = 2, font=txtFont, bg = '#1c1c1c', activebackground='#1c1c1c', highlightbackground="#1c1c1c", highlightcolor="#1c1c1c", command= lambda:TimeInc())
PlusBtn.grid(row=1,column=4, padx=36)

StartBtn = Button(win, text = 'START', height = 2, width = 20, bg = '#48A14D', activebackground='#09b34a', command= lambda:TimeUpdate())
StartBtn.grid(row=2,column=1)

PauseBtn = Button(win, text = 'PAUSE', height = 2, width = 20, bg = '#ED944D', activebackground='#f57814', command= lambda:TimePause())
PauseBtn.grid(row=2,column=2, pady=50)

StopBtn = Button(win, text = 'STOP', height = 2, width = 20, bg = '#B33F40', activebackground='#db0909', command= lambda:TimeStop())
StopBtn.grid(row=2,column=3)

win.mainloop()
