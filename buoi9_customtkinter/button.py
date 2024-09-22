import customtkinter

customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme('green')

root = customtkinter.CTk()
root.title('main customtkinter')
root.geometry('600x600')


def button_event(number):
    print(number)


button = customtkinter.CTkButton(master=root, text="CTkButton",  command = lambda: button_event(2), bg_color="red", fg_color="blue", hover_color="red")
button.pack()

root.mainloop()