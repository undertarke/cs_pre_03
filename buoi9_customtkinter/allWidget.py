import customtkinter

customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme('green')

root = customtkinter.CTk()
root.title('main customtkinter')
root.geometry('600x600')


def checkbox_event():
    print("checkbox toggled, current value:", check_var.get())


check_var = customtkinter.StringVar(value="on")
checkbox = customtkinter.CTkCheckBox(
    master=root, text="CTkCheckBox", command=checkbox_event,   variable=check_var, onvalue="on", offvalue="off")
checkbox.pack()

label = customtkinter.CTkLabel(root, text="Nhập email: ", fg_color="transparent")
label.pack()


def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)

optionmenu = customtkinter.CTkOptionMenu(root, values=["option 1", "option 2"],
                                         command=optionmenu_callback)
optionmenu.set("option 2")
optionmenu.pack()

progressbar = customtkinter.CTkProgressBar(root, orientation="horizontal")
progressbar.pack()

def radiobutton_event():
    print("radiobutton toggled, current value:", radio_var.get())

radio_var = customtkinter.IntVar(value=0)
radiobutton_1 = customtkinter.CTkRadioButton(root, text="CTkRadioButton 1",
                                             command=radiobutton_event, variable= radio_var, value=1)
radiobutton_2 = customtkinter.CTkRadioButton(root, text="CTkRadioButton 2",
                                             command=radiobutton_event, variable= radio_var, value=2)
radiobutton_1.pack()
radiobutton_2.pack()

def switch_event():
    print("switch toggled, current value:", switch_var.get())

switch_var = customtkinter.StringVar(value="on")
switch = customtkinter.CTkSwitch(root, text="CTkSwitch", command=switch_event,
                                 variable=switch_var, onvalue="on", offvalue="off")
switch.pack()

root.mainloop()



