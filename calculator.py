from tkinter import *  # tkinter is a GUI toolkit of python


def command(num):
    global text
    text = text + str(num)
    text_variable.set(text)


def equals():
    global text
    try:
        result = str(eval(text))
        text_variable.set(result)
        text = result
    except ZeroDivisionError:
        text_variable.set('Zero Division Error')
        text = ''
    except SyntaxError as s:
        text_variable.set('Syntax Error')
        text = ''


def all_clear():
    global text
    text_variable.set('')
    text = ''


window = Tk()  # create an instance of a window GUI
window.title('Calculator')
window.geometry('500x500')
icon = PhotoImage(file='icon.png')
window.iconphoto(True, icon)
text = ''
text_variable = StringVar()

label = Label(window,
              textvariable=text_variable,
              font=('times new roman', 30),
              bg='white',
              width=15,
              height=1)
label.pack()

frame = Frame(window)  # frame to add widgets in a grid format
frame.pack()

button1 = Button(frame,
                 text=1,
                 command=lambda: command(1),
                 width=8,
                 height=4,
                 font=('times new roman', 10))
button1.grid(row=0, column=0)

button2 = Button(frame,
                 text=2,
                 command=lambda: command(2),
                 width=8,
                 height=4,
                 font=('times new roman', 10))
button2.grid(row=0, column=1)

button3 = Button(frame,
                 text=3,
                 command=lambda: command(3),
                 width=8,
                 height=4,
                 font=('times new roman', 10))
button3.grid(row=0, column=2)

button4 = Button(frame,
                 text=4,
                 command=lambda: command(4),
                 width=8,
                 height=4,
                 font=('times new roman', 10))
button4.grid(row=1, column=0)

button5 = Button(frame,
                 text=5,
                 command=lambda: command(5),
                 width=8,
                 height=4,
                 font=('times new roman', 10))
button5.grid(row=1, column=1)

button6 = Button(frame,
                 text=6,
                 command=lambda: command(6),
                 width=8,
                 height=4,
                 font=('times new roman', 10))
button6.grid(row=1, column=2)

button7 = Button(frame,
                 text=7,
                 command=lambda: command(7),
                 width=8,
                 height=4,
                 font=('times new roman', 10))
button7.grid(row=2, column=0)

button8 = Button(frame,
                 text=8,
                 command=lambda: command(8),
                 width=8,
                 height=4,
                 font=('times new roman', 10))
button8.grid(row=2, column=1)

button9 = Button(frame,
                 text=9,
                 command=lambda: command(9),
                 width=8,
                 height=4,
                 font=('times new roman', 10))
button9.grid(row=2, column=2)

button0 = Button(frame,
                 text=0,
                 command=lambda: command(0),
                 width=8,
                 height=4,
                 font=('times new roman', 10))
button0.grid(row=3, column=1)

button_decimal = Button(frame,
                        text='.',
                        command=lambda: command('.'),
                        width=8,
                        height=4,
                        font=('times new roman', 10))
button_decimal.grid(row=3, column=0)

button_equal = Button(frame,
                      text='=',
                      command=equals,
                      width=8,
                      height=4,
                      font=('times new roman', 10))
button_equal.grid(row=3, column=2)

button_divide = Button(frame,
                       text='/',
                       command=lambda: command('/'),
                       width=8,
                       height=4,
                       font=('times new roman', 10))
button_divide.grid(row=0, column=3)

button_mul = Button(frame,
                    text='*',
                    command=lambda: command('*'),
                    width=8,
                    height=4,
                    font=('times new roman', 10))
button_mul.grid(row=1, column=3)

button_plus = Button(frame,
                     text='+',
                     command=lambda: command('+'),
                     width=8,
                     height=4,
                     font=('times new roman', 10))
button_plus.grid(row=2, column=3)

button_minus = Button(frame,
                      text='-',
                      command=lambda: command('-'),
                      width=8,
                      height=4,
                      font=('times new roman', 10))
button_minus.grid(row=3, column=3)

button_clear = Button(window,
                      text='Clear',
                      command=all_clear,
                      width=36,
                      height=4,
                      font=('times new roman', 10))
button_clear.pack()

window.mainloop()   # dispay the window
