import tkinter

import logic
from tkinter import *

window = Tk()

window.title('Password Generator')
window.iconbitmap(default='D:\PyProjects\GitHub\PasswordGenerator\Icons\win.ico')

window.geometry('800x600+800+400')
window.resizable(False, False)
window.configure(bg='#B0C4DE')

label_of_hello = tkinter.Label(text='Hello!', anchor='center', font=('Consolas', 24), background='#B0C4DE', pady=20)
label_of_main = tkinter.Label(text='This program is designed to generate\n a password according to a given algorithm', anchor='center', font=('Consolas', 24),
                              background='#B0C4DE', pady=20)
label_of_hello.pack()
label_of_main.pack()

label_for_password = tkinter.Label(text='First, write 9 characters\n from the English alphabet', anchor='center', font=('Consolas', 24),
                                   background='#B0C4DE', pady=20)
label_for_password.pack()

entry_for_password = tkinter.Entry(font=('Consolas', 24))
entry_for_password.pack()

button_for_click = tkinter.Button(text="Click", font=('Consolas', 24), command=get_text)
c = entry_for_password.get()

# def get_text():
#     global counter
#     mass.append(entry_for_password.get())
#     if counter == 0:
#         label_for_password['text'] = 'fwefwefwefwef'
#         label_for_result['text'] = Permutations.Password.matrix(mass[self.__counter])
#         counter += 1
#     elif counter == 1:
#         label_for_password['text'] = 'fwefw'
#         counter += 1
#

button_for_click.pack(anchor='center', pady=20)

label_for_result = tkinter.Label(text='fewf', anchor='center', font=('Consolas', 24),
                                   background='#B0C4DE', pady=20)
label_for_result.pack()

window.mainloop()

