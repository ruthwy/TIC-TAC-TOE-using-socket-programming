import tkinter
import socket
import _thread

clientTurn = 1
counter = 0
client = None

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
    # If Client - X is the winner
    if(btn1['text'] == 'X' and btn2['text'] == 'X' and btn3['text'] == 'X' or
       btn1['text'] == 'X' and btn4['text'] == 'X' and btn7['text'] == 'X' or
       btn1['text'] == 'X' and btn5['text'] == 'X' and btn9['text'] == 'X' or
       btn2['text'] == 'X' and btn5['text'] == 'X' and btn8['text'] == 'X' or
       btn7['text'] == 'X' and btn8['text'] == 'X' and btn9['text'] == 'X' or
       btn4['text'] == 'X' and btn5['text'] == 'X' and btn6['text'] == 'X' or
       btn3['text'] == 'X' and btn5['text'] == 'X' and btn7['text'] == 'X' or
       btn3['text'] == 'X' and btn6['text'] == 'X' and btn9['text'] == 'X'):
        sendWinner('X-Winner')
    
    # If Server - O is the Winner
    if(btn1['text'] == 'O' and btn2['text'] == 'O' and btn3['text'] == 'O' or
       btn1['text'] == 'O' and btn4['text'] == 'O' and btn7['text'] == 'O' or
       btn1['text'] == 'O' and btn5['text'] == 'O' and btn9['text'] == 'O' or
       btn2['text'] == 'O' and btn5['text'] == 'O' and btn8['text'] == 'O' or
       btn4['text'] == 'O' and btn5['text'] == 'O' and btn6['text'] == 'O' or
       btn7['text'] == 'O' and btn8['text'] == 'O' and btn9['text'] == 'O' or
       btn3['text'] == 'O' and btn5['text'] == 'O' and btn7['text'] == 'O' or
       btn3['text'] == 'O' and btn6['text'] == 'O' and btn9['text'] == 'O'):
        sendWinner('O-Winner')

    if(counter == 5):
        sendWinner('It\'s a Tie')

def socketCreation():
    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    host = '127.0.0.1'
    port = 8900
    try:
        client.connect((host, port))
    except ConnectionRefusedError:
        print("Connection refused. Make sure the server is running.")
        return

    while True:
        msg = client.recv(2048).decode('ascii')
        global clientTurn
        if (msg == 'a' and clientTurn == 0):
            btn1['text'] = 'O'
            btn1['state'] = tkinter.DISABLED
            clientTurn = 1
            check()
        elif (msg == 'b' and clientTurn == 0):
            btn2['text'] = 'O'
            btn2['state'] = tkinter.DISABLED
            clientTurn = 1
            check()
        elif (msg == 'c' and clientTurn == 0):
            btn3['text'] = 'O'
            btn3['state'] = tkinter.DISABLED
            clientTurn = 1
            check()
        elif (msg == 'd' and clientTurn == 0):
            btn4['text'] = 'O'
            btn4['state'] = tkinter.DISABLED
            clientTurn = 1
            check()
        elif (msg == 'e' and clientTurn == 0):
            btn5['text'] = 'O'
            btn5['state'] = tkinter.DISABLED
            clientTurn = 1
            check()
        elif (msg == 'f' and clientTurn == 0):
            btn6['text'] = 'O'
            btn6['state'] = tkinter.DISABLED
            clientTurn = 1
            check()
        elif (msg == 'g' and clientTurn == 0):
            btn7['text'] = 'O'
            btn7['state'] = tkinter.DISABLED
            clientTurn = 1
            check()
        elif (msg == 'h' and clientTurn == 0):
            btn8['text'] = 'O'
            btn8['state'] = tkinter.DISABLED
            clientTurn = 1
            check()
        elif (msg == 'i' and clientTurn == 0):
            btn9['text'] = 'O'
            btn9['state'] = tkinter.DISABLED
            clientTurn = 1
            check()

def closeConnection():
    global client
    if client:
        client.close()
    window.destroy()

def sendbtn1():
    global clientTurn
    if clientTurn == 1:
        clientTurn = 0
        msg = 'a'
        client.send(msg.encode('ascii'))
        btn1['text'] = 'X'
        btn1['state'] = tkinter.DISABLED
        global counter
        counter += 1
        check()

def sendbtn2():
    global clientTurn
    if clientTurn == 1:
        clientTurn = 0
        msg = 'b'
        client.send(msg.encode('ascii'))
        btn2['text'] = 'X'
        btn2['state'] = tkinter.DISABLED
        global counter
        counter += 1
        check()

def sendbtn3():
    global clientTurn
    if clientTurn == 1:
        clientTurn = 0
        msg = 'c'
        client.send(msg.encode('ascii'))
        btn3['text'] = 'X'
        btn3['state'] = tkinter.DISABLED
        global counter
        counter += 1
        check()

def sendbtn4():
    global clientTurn
    if clientTurn == 1:
        clientTurn = 0
        msg = 'd'
        client.send(msg.encode('ascii'))
        btn4['text'] = 'X'
        btn4['state'] = tkinter.DISABLED
        global counter
        counter += 1
        check()

def sendbtn5():
    global clientTurn
    if clientTurn == 1:
        clientTurn = 0
        msg = 'e'
        client.send(msg.encode('ascii'))
        btn5['text'] = 'X'
        btn5['state'] = tkinter.DISABLED
        global counter
        counter += 1
        check()

def sendbtn6():
    global clientTurn
    if clientTurn == 1:
        clientTurn = 0
        msg = 'f'
        client.send(msg.encode('ascii'))
        btn6['text'] = 'X'
        btn6['state'] = tkinter.DISABLED
        global counter
        counter += 1
        check()

def sendbtn7():
    global clientTurn
    if clientTurn == 1:
        clientTurn = 0
        msg = 'g'
        client.send(msg.encode('ascii'))
        btn7['text'] = 'X'
        btn7['state'] = tkinter.DISABLED
        global counter
        counter += 1
        check()

def sendbtn8():
    global clientTurn
    if clientTurn == 1:
        clientTurn = 0
        msg = 'h'
        client.send(msg.encode('ascii'))
        btn8['text'] = 'X'
        btn8['state'] = tkinter.DISABLED
        global counter
        counter += 1
        check()

def sendbtn9():
    global clientTurn
    if clientTurn == 1:
        clientTurn = 0
        msg = 'i'
        client.send(msg.encode('ascii'))
        btn9['text'] = 'X'
        btn9['state'] = tkinter.DISABLED
        global counter
        counter += 1
        check()

window = tkinter.Tk()
window.title('Client - X')
window.geometry('400x300')
window.protocol("WM_DELETE_WINDOW", closeConnection)

btn1 = tkinter.Button(window, text='', command=sendbtn1, height=4, width=8)
btn1.grid(column=0, row=0, padx=5, pady=5)
btn2 = tkinter.Button(window, text='', command=sendbtn2, height=4, width=8)
btn2.grid(column=1, row=0, padx=5, pady=5)
btn3 = tkinter.Button(window, text='', command=sendbtn3, height=4, width=8)
btn3.grid(column=2, row=0, padx=5, pady=5)
btn4 = tkinter.Button(window, text='', command=sendbtn4, height=4, width=8)
btn4.grid(column=0, row=1, padx=5, pady=5)
btn5 = tkinter.Button(window, text='', command=sendbtn5, height=4, width=8)
btn5.grid(column=1, row=1, padx=5, pady=5)
btn6 = tkinter.Button(window, text='', command=sendbtn6, height=4, width=8)
btn6.grid(column=2, row=1, padx=5, pady=5)
btn7 = tkinter.Button(window, text='', command=sendbtn7, height=4, width=8)
btn7.grid(column=0, row=2, padx=5, pady=5)
btn8 = tkinter.Button(window, text='', command=sendbtn8, height=4, width=8)
btn8.grid(column=1, row=2, padx=5, pady=5)
btn9 = tkinter.Button(window, text='', command=sendbtn9, height=4, width=8)
btn9.grid(column=2, row=2, padx=5, pady=5)

_thread.start_new_thread(socketCreation, ())

window.mainloop()
