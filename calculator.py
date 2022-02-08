from sympy import *
from tkinter import *
import re
from PIL import Image, ImageTk, ImageOps
from io import BytesIO

defaults = object()
semboller=["π","sqrt(","∫","∑","Δ","^","β","ℏ","Eq(","λ","∞","→","(",")","[","]","{","}"]
global canvas,myimg
global x,y,z,w 
global f,g,h
x,y,z,w= symbols('x y z w')
f,g,h=symbols('f g h', cls=Function)

def result_show(result):
    # change answer label with result
    obj = BytesIO()
    preview(result, viewer='BytesIO', outputbuffer=obj)
    obj.seek(0)
    img=Image.open(obj)
    invImg=ImageOps.invert(img)
    answer.img = ImageTk.PhotoImage(invImg)
    answer.config(image=answer.img)

def u_integrate(queue):
    a = defaults
    b = defaults
    queueList = queue.split(",")
    if len(queueList) == 3:
        a = queueList[1]
        b = queueList[2]
        queue = queueList[0]

    if a == defaults or b == defaults:
        queue = str(queue[1:])
        expression = sympify(queue)
        if "x" in queue:
            result = integrate(expression,x)
        if "y" in queue:
            result = integrate(expression,y)
        if "z" in queue:
            result = integrate(expression,z)
        if "w" in queue:
            result = integrate(expression,w)
        result_show(result,queue)

    else:
        queue = str(queue[1:])
        expression = sympify(queue)
        if "x" in queue:
            result = integrate(expression,(x,a,b))
        if "y" in queue:
            result = integrate(expression,(y,a,b))
        if "z" in queue:
            result = integrate(expression,(z,a,b))
        if "w" in queue:
            result = integrate(expression,(w,a,b))
        result_show(result)

def u_solve_poly_system(queue):
    system = []
    request = ""
    queue = str(queue[1:])
    queue = re.split(r'[,=\s]\s*',queue)
    queue.pop(-1)
    for i in range(len(queue)):
        if (i - 1) % 2:
            queue[i] = sympify(queue[i])
            system.append("Eq(" + str(queue[i]) + "," + str(queue[i + 1]) + ")")
    for i in range(len(system)):
        if i != len(system):

            request += str(system[i]) + ","
        else:
            request += str(system[i])
    result = solve(sympify(request))
    result_show(result)

def u_diff(queue):
    queue = str(queue[1:])
    expression = sympify(queue)
    result = diff(expression)
    result_show(result)

def u_plot(queue):
    queue = str(queue[1:])
    expression = sympify(queue)
    plot(*expression)

def api():
    request=queue.get("1.0",END)

    if request[0] == "∫":
        u_integrate(request)
    if request[0] == "s":
        u_solve_poly_system(request)
    if request[0] == "Δ":
        u_diff(request)
    if request[0] == "p":
        u_plot(request)


def press(a):
    queue.insert(queue.index(INSERT),semboller[a])
    return

def main():
    global queue
    global answer
    root=Tk()
    root.title("Calculator")
    root.resizable(0,0)
    buttonOK = Button(root,text=">>",command=api,height=8)
    buttonOK.grid(row=0,column=5)

    queue=Text(root,height=5,width=25,font=("Arial","18"),bg="#222232",fg="white")
    # var=queue.get("1.0",END)
    queue.grid(row=0,column=0,columnspan=5)

    button0 = Button(root,text=semboller[0],command=lambda:press(0),font=('Arial', '25'),width=2)
    button1 = Button(root,text=semboller[1],command=lambda:press(1),font=('Arial', '25'),width=2)
    button2 = Button(root,text=semboller[2],command=lambda:press(2),font=('Arial', '25'),width=2)
    button3 = Button(root,text=semboller[3],command=lambda:press(3),font=('Arial', '25'),width=2)
    button4 = Button(root,text=semboller[4],command=lambda:press(4),font=('Arial', '25'),width=2)
    button5 = Button(root,text=semboller[5],command=lambda:press(5),font=('Arial', '25'),width=2)
    button6 = Button(root,text=semboller[6],command=lambda:press(6),font=('Arial', '25'),width=2)
    button7 = Button(root,text=semboller[7],command=lambda:press(7),font=('Arial', '25'),width=2)
    button8 = Button(root,text=semboller[8],command=lambda:press(8),font=('Arial', '25'),width=2)
    button9 = Button(root,text=semboller[9],command=lambda:press(9),font=('Arial', '25'),width=2)
    button10 = Button(root,text=semboller[10],command=lambda:press(10),font=('Arial', '25'),width=2)
    button11 = Button(root,text=semboller[11],command=lambda:press(11),font=('Arial', '25'),width=2)
    button12 = Button(root,text=semboller[12],command=lambda:press(12),font=('Arial', '25'),width=2)
    button13 = Button(root,text=semboller[13],command=lambda:press(13),font=('Arial', '25'),width=2)
    button14 = Button(root,text=semboller[14],command=lambda:press(14),font=('Arial', '25'),width=2)
    button15 = Button(root,text=semboller[15],command=lambda:press(15),font=('Arial', '25'),width=2)
    button16 = Button(root,text=semboller[16],command=lambda:press(16),font=('Arial', '25'),width=2)
    button17 = Button(root,text=semboller[17],command=lambda:press(17),font=('Arial', '25'),width=2)

    answer=Label(root,text="Answer Here",font=('Arial', '25'))
    answer.grid(row=4,columnspan=6)

    button0.grid(row=1,column=0)
    button1.grid(row=1,column=1)
    button2.grid(row=1,column=2)
    button3.grid(row=1,column=3)
    button4.grid(row=1,column=4)
    button5.grid(row=1,column=5)
    button6.grid(row=2,column=0)
    button7.grid(row=2,column=1)
    button8.grid(row=2,column=2)
    button9.grid(row=2,column=3)
    button10.grid(row=2,column=4)
    button11.grid(row=2,column=5)
    button12.grid(row=3,column=0)
    button13.grid(row=3,column=1)
    button14.grid(row=3,column=2)
    button15.grid(row=3,column=3)
    button16.grid(row=3,column=4)
    button17.grid(row=3,column=5)
    queue.focus_set()
    root.mainloop()


if __name__ == '__main__':
    main()
