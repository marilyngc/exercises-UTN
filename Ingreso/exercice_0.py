from customtkinter import *

app = CTk();

def button_on_click():
    print("let´s go to learn phyton!!");

button = CTkButton(master=app, text="click me!", command = button_on_click)
button.grid()

app.mainloop()