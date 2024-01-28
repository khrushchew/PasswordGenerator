import tkinter

from classesOfExceptions import PasswordError
from Permutations import Password
from tkinter import *

window = Tk()

counter = 0
mass = []


def loop():
    global counter
    try:
        if counter == 0:
            mass.append(Password.matrix(entry_for_password.get()))
            label_for_result['text'] = 'OK!'
            label_for_result.pack()
            counter += 1
            entry_for_password.delete(first=0, last=END)
            label_for_password['text'] = 'Now write the name of your favorite actor'
        elif counter == 1:
            mass.append(Password.actor(entry_for_password.get()))
            label_for_result['text'] = 'OK!'
            label_for_result.pack()
            counter += 1
            entry_for_password.delete(first=0, last=END)
            label_for_password['text'] = 'Write any color'
        elif counter == 2:
            mass.append(Password.color(entry_for_password.get()))
            label_for_result['text'] = 'OK!'
            label_for_result.pack()
            counter += 1
            entry_for_password.delete(first=0, last=END)
            label_for_password['text'] = ''
    except PasswordError as e:
        label_for_result['text'] = f'User Error!\n{e}'
        label_for_result.pack()


window.title('Password Generator')
window.iconbitmap(default='D:\\PyProjects\\GitHub\\PasswordGenerator\\Icons\\win.ico')

window.geometry('800x600+800+400')
window.resizable(False, False)
window.configure(bg='#B0C4DE')

label_of_hello = tkinter.Label(text='Hello!', anchor='center', font=('Consolas', 24), background='#B0C4DE', pady=20)
label_of_main = tkinter.Label(text='This program is designed to generate\n a password according to a given algorithm',
                              anchor='center', font=('Consolas', 24),
                              background='#B0C4DE', pady=20)
label_of_hello.pack()
label_of_main.pack()

label_for_password = tkinter.Label(text='First, write 9 characters\n from the English alphabet', anchor='center',
                                   font=('Consolas', 24),
                                   background='#B0C4DE', pady=20)
label_for_password.pack()

entry_for_password = tkinter.Entry(font=('Consolas', 24))
entry_for_password.pack()

button_for_click = tkinter.Button(text='Click', font=('Consolas', 24), command=loop)
button_for_click.pack(anchor='center', pady=20)

label_for_result = tkinter.Label(text='', anchor='center', font=('Consolas', 24),
                                 background='#B0C4DE', pady=20)

window.mainloop()
print(mass)