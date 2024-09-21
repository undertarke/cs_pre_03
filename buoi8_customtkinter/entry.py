import customtkinter

customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme('green')

root = customtkinter.CTk()
root.title('main customtkinter')
root.geometry('600x600')

entry = customtkinter.CTkEntry(master=root, placeholder_text="CTkEntry")
entry.pack()

def button_event(number):
    print(entry.get())


button = customtkinter.CTkButton(master=root, text="CTkButton",  command = lambda: button_event(2))
button.pack()



root.mainloop()
