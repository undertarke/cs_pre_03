import customtkinter

customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme('green')

root = customtkinter.CTk()
root.title('main customtkinter')
root.geometry('600x600')


# pack()
# frame = customtkinter.CTkFrame(master=root, fg_color="yellow", bg_color="yellow")
# frame.pack(side='bottom',expand=True,fill="both")

# frame2 = customtkinter.CTkFrame(master=root, fg_color="red", bg_color="red")
# frame2.pack(side='bottom',expand=True,fill="both")

# frame3 = customtkinter.CTkFrame(master=root, fg_color="blue", bg_color="red")
# frame3.pack(side='bottom',expand=True,fill="both")



# place() => 0 - 1: 0.1 -> 1% - 0.9->90%
# frame = customtkinter.CTkFrame(master=root, fg_color="yellow", bg_color="yellow")
# frame.place(relwidth=0.5,relheight=0.5,relx=0.25,rely=0.25)

# frame2 = customtkinter.CTkFrame(master=root, fg_color="red", bg_color="red")
# frame2.place(relwidth=0.5,relheight=0.5,relx=0.5,rely=0.25)

# grid()

root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

# Đông (East), Tây (West), Nam (South), Bắc (North)
# frame = customtkinter.CTkFrame(master=root, fg_color="yellow", bg_color="yellow")
# frame.grid(row=0,column=0,sticky="n")

# frame2 = customtkinter.CTkFrame(master=root, fg_color="red", bg_color="red")
# frame2.grid(row=0,column=0)


# BT 4 color
frameParrent = customtkinter.CTkFrame(master=root, fg_color="white", bg_color="yellow")
frameParrent.pack(side='top',expand=True,fill="both")

frame = customtkinter.CTkFrame(master=frameParrent, fg_color="yellow", bg_color="yellow")
frame.pack(side='left',expand=True,fill="both")


frame2 = customtkinter.CTkFrame(master=frameParrent, fg_color="red", bg_color="yellow")
frame2.pack(side='right',expand=True,fill="both")



frameParrent2 = customtkinter.CTkFrame(master=root, fg_color="silver", bg_color="yellow")
frameParrent2.pack(side='bottom',expand=True,fill="both")

frame3 = customtkinter.CTkFrame(master=frameParrent2, fg_color="blue", bg_color="yellow")
frame3.pack(side='left',expand=True,fill="both")


frame4 = customtkinter.CTkFrame(master=frameParrent2, fg_color="gray", bg_color="yellow")
frame4.pack(side='right',expand=True,fill="both")


root.mainloop()