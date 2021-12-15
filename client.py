import tkinter
import socket
import _thread
clientTurn = 1
counter = 0
def sendWinner(msg):
    client.send(msg.encode('ascii'))
    btn1['state']= tkinter.NORMAL
    btn2['state']= tkinter.NORMAL
    btn3['state']= tkinter.NORMAL
    btn4['state']= tkinter.NORMAL
    btn5['state']= tkinter.NORMAL
    btn6['state']= tkinter.NORMAL
    btn7['state']= tkinter.NORMAL
    btn8['state']= tkinter.NORMAL
    btn9['state']= tkinter.NORMAL
    btn1['text']= ''
    btn2['text']= ''
    btn3['text']= ''
    btn4['text']= ''
    btn5['text']= ''
    btn6['text']= ''
    btn7['text']= ''
    btn8['text']= ''
    btn9['text']= ''
    global clientTurn
    clientTurn = 1
    global counter
    counter = 0
def check():
#If Client - X is the winner
    
    if(btn1['text'] == 'X'):
        if(btn2['text']=='X'):
            if(btn3['text']=='X'):
                sendWinner('X-Winner')
        if(btn4['text']=='X'):
            if(btn7['text']=='X'):
                sendWinner('X-Winner')
        if(btn5['text']=='X'):
            if(btn9['text']=='X'):
                sendWinner('X-Winner')
    if(btn2['text'] == 'X'):
        if(btn5['text']=='X'):
            if(btn8['text']=='X'):
                sendWinner('X-Winner')
    if(btn7['text'] == 'X'):
        if(btn8['text']=='X'):
            if(btn9['text']=='X'):
                sendWinner('X-Winner')
    if(btn4['text'] == 'X'):
        if(btn5['text']=='X'):
            if(btn6['text']=='X'):
                sendWinner('X-Winner')
    if(btn3['text'] == 'X'):
        if(btn5['text']=='X'):
            if(btn7['text']=='X'):
                sendWinner('X-Winner')
        if(btn6['text']=='X'):
            if(btn9['text']=='X'):
                sendWinner('X-Winner')
#If Server - O is the Winner
    if(btn1['text'] == 'O'):
        if(btn2['text']=='O'):
            if(btn3['text']=='O'):
                sendWinner('O-Winner')
        if(btn4['text']=='O'):
            if(btn7['text']=='O'):
                sendWinner('O-Winner')
        if(btn5['text']=='O'):
            if(btn9['text']=='O'):
                sendWinner('O-Winner')
    if(btn2['text'] == 'O'):
        if(btn5['text']=='O'):
            if(btn8['text']=='O'):
                sendWinner('O-Winner')
    if(btn4['text'] == 'O'):
        if(btn5['text']=='O'):
            if(btn6['text']=='O'):
                sendWinner('O-Winner')
    if(btn7['text'] == 'O'):
        if(btn8['text']=='O'):
            if(btn9['text']=='O'):
                sendWinner('O-Winner')
    if(btn3['text'] == 'O'):
        if(btn5['text']=='O'):
            if(btn7['text']=='O'):
                sendWinner('O-Winner')
        if(btn6['text']=='O'):
            if(btn9['text']=='O'):
                sendWinner('O-Winner')
    if(counter == 5):
        sendWinner('It\'s a Tie')
    

def socketCreation ():    
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    host = '127.0.0.1'
    port = 8900
    c.connect((host,port))
    global client
    client = c
    while True:
        msg= c.recv(2048).decode('ascii')
        global clientTurn
        if ( msg == 'a' and clientTurn == 0):
            btn1['text']='O'
            btn1['state']= tkinter.DISABLED
            clientTurn = 1
            check()
        elif ( msg == 'b' and clientTurn == 0):
            btn2['text']='O'
            btn2['state']= tkinter.DISABLED
            clientTurn = 1
            check()
        elif ( msg == 'c' and clientTurn == 0):
            btn3['text']='O'
            btn3['state']= tkinter.DISABLED
            clientTurn = 1
            check()
        elif ( msg == 'd' and clientTurn == 0):
            btn4['text']='O'
            btn4['state']= tkinter.DISABLED
            clientTurn = 1
            check()
        elif ( msg == 'e' and clientTurn == 0):
            btn5['text']='O'
            btn5['state']= tkinter.DISABLED
            clientTurn = 1
            check()
        elif ( msg == 'f' and clientTurn == 0):
            btn6['text']='O'
            btn6['state']= tkinter.DISABLED
            clientTurn = 1
            check()
        elif ( msg == 'g' and clientTurn == 0):
            btn7['text']='O'
            btn7['state']= tkinter.DISABLED
            clientTurn = 1
            check()
        elif ( msg == 'h' and clientTurn == 0):
            btn8['text']='O'
            btn8['state']= tkinter.DISABLED
            clientTurn = 1
            check()
        elif ( msg == 'i' and clientTurn == 0):
            btn9['text']='O'
            btn9['state']= tkinter.DISABLED
            clientTurn = 1
            check()
       
                
def sendbtn1 ():
    global clientTurn
    if clientTurn == 1:
         clientTurn = 0
         msg = 'a'
         client.send(msg.encode('ascii'))
         btn1['text']='X'
         btn1['state']= tkinter.DISABLED
         global counter
         counter += 1
         check()
def sendbtn2 ():
     global clientTurn
     if clientTurn == 1:
         clientTurn = 0
         msg = 'b'
         client.send(msg.encode('ascii'))
         btn2['text']='X'
         btn2['state']= tkinter.DISABLED
         global counter
         counter += 1
         check()
def sendbtn3 ():
    global clientTurn
    if clientTurn == 1:
         clientTurn = 0
         msg = 'c'
         client.send(msg.encode('ascii'))
         btn3['text']='X'
         btn3['state']= tkinter.DISABLED
         global counter
         counter += 1
         check()
def sendbtn4 ():
    global clientTurn
    if clientTurn == 1:
         clientTurn = 0
         msg = 'd'
         client.send(msg.encode('ascii'))
         btn4['text']='X'
         btn4['state']= tkinter.DISABLED
         global counter
         counter += 1
         check()
def sendbtn5 ():
    global clientTurn
    if clientTurn == 1:
         clientTurn = 0
         msg = 'e'
         client.send(msg.encode('ascii'))
         btn5['text']='X'
         btn5['state']= tkinter.DISABLED
         global counter
         counter += 1
         check()
def sendbtn6 ():
    global clientTurn
    if clientTurn == 1:
         clientTurn = 0
         msg = 'f'
         client.send(msg.encode('ascii'))
         btn6['text']='X'
         btn6['state']= tkinter.DISABLED
         global counter
         counter += 1
         check()
def sendbtn7 ():
    global clientTurn
    if clientTurn == 1:
         clientTurn = 0
         msg = 'g'
         client.send(msg.encode('ascii'))
         btn7['text']='X'
         btn7['state']= tkinter.DISABLED
         global counter
         counter += 1
         check()
def sendbtn8 ():
    global clientTurn
    if clientTurn == 1:
         clientTurn = 0
         msg = 'h'
         client.send(msg.encode('ascii'))
         btn8['text']='X'
         btn8['state']= tkinter.DISABLED
         global counter
         counter += 1
         check()
def sendbtn9 ():
    global clientTurn
    if clientTurn == 1:
         clientTurn = 0
         msg = 'i'
         client.send(msg.encode('ascii'))
         btn9['text']='X'
         btn9['state']= tkinter.DISABLED
         global counter
         counter += 1
         check()
#Creating a window
window = tkinter.Tk()
window.title('CLIENT')
window['bg']='wheat4'
window['padx']=10
window['pady']=10
#Adding Elements
#Label
lbl = tkinter.Label(window,text='TIC-TAC-TOE')
lbl['font']=35
lbl['bg']='wheat4'
lbl.grid(column=2,row=0,padx=5,pady=5)
#Label
lbl2= tkinter.Label(window,text='Client-X')
lbl2['font']=35
lbl2['bg']='wheat4'
lbl2.grid(column=1,row=1,padx=5,pady=5)
#Label
lbl3 = tkinter.Label(window,text='Server-O')
lbl3['font']=35
lbl3['bg']='wheat4'
lbl3.grid(column=3,row=1,padx=5,pady=5)
#Button
btn1 = tkinter.Button(window)
btn1['relief']=tkinter.GROOVE
btn1['bg']='cornsilk2'
btn1['fg']='green'
btn1['activebackground']='ivory3'
btn1['padx']=3
btn1['font']=35
btn1['width']= 10
btn1['height']= 5
btn1.grid(column=1,row=2,padx=5,pady=5)
#Button
btn2 = tkinter.Button(window)
btn2['relief']=tkinter.GROOVE
btn2['bg']='cornsilk2'
btn2['fg']='green'
btn2['activebackground']='ivory3'
btn2['padx']=3
btn2['font']=35
btn2['width']= 10
btn2['height']= 5
btn2.grid(column=2,row=2,padx=5,pady=5)
#Button
btn3 = tkinter.Button(window)
btn3['relief']=tkinter.GROOVE
btn3['bg']='cornsilk2'
btn3['fg']='green'
btn3['activebackground']='ivory3'
btn3['padx']=3
btn3['font']=35
btn3['width']= 10
btn3['height']= 5
btn3.grid(column=3,row=2,padx=5,pady=5)
#Button
btn4 = tkinter.Button(window)
btn4['relief']=tkinter.GROOVE
btn4['bg']='cornsilk2'
btn4['fg']='green'
btn4['activebackground']='ivory3'
btn4['padx']=3
btn4['font']=35
btn4['width']= 10
btn4['height']= 5
btn4.grid(column=1,row=3,padx=5,pady=5)
#Button
btn5 = tkinter.Button(window)
btn5['relief']=tkinter.GROOVE
btn5['bg']='cornsilk2'
btn5['fg']='green'
btn5['activebackground']='ivory3'
btn5['padx']=3
btn5['font']=35
btn5['width']= 10
btn5['height']= 5
btn5.grid(column=2,row=3,padx=5,pady=5)
#Button
btn6 = tkinter.Button(window)
btn6['relief']=tkinter.GROOVE
btn6['bg']='cornsilk2'
btn6['fg']='green'
btn6['activebackground']='ivory3'
btn6['padx']=3
btn6['font']=35
btn6['width']= 10
btn6['height']= 5
btn6.grid(column=3,row=3,padx=5,pady=5)
#Button
btn7 = tkinter.Button(window)
btn7['relief']=tkinter.GROOVE
btn7['bg']='cornsilk2'
btn7['fg']='green'
btn7['activebackground']='ivory3'
btn7['padx']=3
btn7['font']=35
btn7['width']= 10
btn7['height']= 5
btn7.grid(column=1,row=4,padx=5,pady=5)
#Button
btn8 = tkinter.Button(window)
btn8['relief']=tkinter.GROOVE
btn8['bg']='cornsilk2'
btn8['fg']='green'
btn8['activebackground']='ivory3'
btn8['padx']=3
btn8['font']=35
btn8['width']= 10
btn8['height']= 5
btn8.grid(column=2,row=4,padx=5,pady=5)
#Button
btn9 = tkinter.Button(window)
btn9['relief']=tkinter.GROOVE
btn9['bg']='cornsilk2'
btn9['fg']='green'
btn9['activebackground']='ivory3'
btn9['padx']=3
btn9['font']=35
btn9['width']= 10
btn9['height']= 5
btn9.grid(column=3,row=4,padx=5,pady=5)
btn1['command']=sendbtn1
btn2['command']=sendbtn2
btn3['command']=sendbtn3
btn4['command']=sendbtn4
btn5['command']=sendbtn5
btn6['command']=sendbtn6
btn7['command']=sendbtn7
btn8['command']=sendbtn8
btn9['command']=sendbtn9
   
_thread.start_new_thread(socketCreation, () )
window.mainloop()