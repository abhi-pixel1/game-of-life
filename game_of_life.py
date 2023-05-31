import numpy as np
import tkinter as tk
import time
import patterns

s=30
flg=1

# n=np.zeros([s,s],dtype=int)
n=patterns.swastik
# print(n)


def color_changer(m,x,y):
    # l[m].config(bg = "blue")
    if l[m].config()["background"][4]=='blue':
        l[m].config(bg = "white")
        n[x][y]=0
    else:
        l[m].config(bg = "blue")
        n[x][y]=1
    # print(n)

def begin():
    global n
    global flg
    flg=1
    while flg:
        root.update()
        n1=np.zeros([s,s],dtype=int)
        for i in range(0,s):
            for j in range(0,s):
                # i=9
                # j=7
                if decider(i,j):
                    # print(i,j,decider(i,j))
                    l[(s*i)+j].config(bg = "blue")
                    n1[i][j]=1
                else:
                    # print(i,j,decider(i,j))
                    l[(s*i)+j].config(bg = "white")
                    # n1[i][j]=0
            
        n=n1
        time.sleep(0.5)
        # root.update()
    # print(n)


def decider(x,y):
    p=n[x][y]
    c=0
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if i==x and j==y:
                continue
            elif i>-1 and j>-1 and i<s and j<s:
                if n[i][j]==1:
                    c=c+1

    if p==0 and c==3:
        return 1
    elif p==1 and (c==3 or c==2):
        return 1
    else:
        return 0

def show():
    for i in range(s):
        for j in range(s):
            if n[i][j]==1:
                l[(s*i)+j].config(bg = "blue")

def stop():
    global flg
    flg=0

def save():
    for i in range(s):
        for j in range(s):
            if n[i][j]==1:
                print((i,j))


root = tk.Tk()

l=[]
k=0
for i in range(0,s):
    for j in range(0,s):
        l.append(tk.Button(text = ' ', command = lambda m=k,x=i,y=j: color_changer(m,x,y),bg='white',width=3))#.grid(row=i,column=j))
        l[k].grid(row=i,column=j)
        k=k+1

start_btn=tk.Button(text="play", command = begin,bg='white').grid(row=0,column=s,columnspan=3)
show_btn=tk.Button(text="show", command = show,bg='white').grid(row=1,column=s,columnspan=3)
stop_btn=tk.Button(text="stop", command = stop,bg='white').grid(row=2,column=s,columnspan=3)
save_btn=tk.Button(text="save", command = save,bg='white').grid(row=3,column=s,columnspan=3)

root.mainloop()