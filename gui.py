import customtkinter
import tkinter
import threading

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")


class SOft(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.chats = []

        self.title("NIMDA")
        self.geometry('1200x900')
        self.resizable(False, False)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self, width=400, corner_radius=50)
        self.frame_left.grid(row=0, column=0, sticky='nswe', padx=10, pady=10)
        self.frame_right = customtkinter.CTkFrame(master=self, width=400, corner_radius=50)
        self.frame_right.grid(row=0, column=1, sticky='nswe', padx=10, pady=10)
        self.search_bar = customtkinter.CTkEntry(master=self.frame_left, width=355, height=50, corner_radius=50,
                                                 placeholder_text='🔍 Search contacts')
        self.search_bar.place(x=20, y=20)

        self.chats_frame = customtkinter.CTkFrame(master=self.frame_left, width=380, height=720, corner_radius=0)
        self.chats_frame.place(x=10, y=90)
        self.left_canvas = customtkinter.CTkCanvas(master=self.chats_frame, width=500, height=1073, bg='#383838')
        self.left_canvas.pack(side=customtkinter.LEFT, fill=customtkinter.BOTH, expand=1)



        self.chats_scroll_bar = customtkinter.CTkScrollbar(master=self.chats_frame, command=self.left_canvas.yview,
                                                           orientation='vertical')
        self.chats_scroll_bar.pack(side=customtkinter.RIGHT, fill=customtkinter.Y)
        self.left_canvas.configure(yscrollcommand=self.chats_scroll_bar.set)
        self.left_canvas.bind('<Configure>',
                                   lambda e: self.left_canvas.configure(scrollregion=self.left_canvas.bbox("all")))

        self.left_canvas.bind("<MouseWheel>", self.mouse_right)

        self.second_frame_left = customtkinter.CTkFrame(master=self.left_canvas)
        self.left_canvas.create_window((5, 5), window=self.second_frame_left, anchor='nw')


        self.right_top = customtkinter.CTkFrame(master=self.frame_right, width=720, height=80, corner_radius=50)
        self.right_top.place(x=20, y=10)
        self.right_bottom = customtkinter.CTkFrame(master=self.frame_right, width=600, height=60, corner_radius=50)
        self.right_bottom.place(x=20, y=790)

        self.send_button = customtkinter.CTkButton(master=self.frame_right, text='Send', corner_radius=30, width=5,
                                                   height=60, text_font=('robotonic', 20))
        self.send_button.place(x=630, y=790)

        self.message_entry = customtkinter.CTkEntry(master=self.right_bottom, corner_radius=50, width=520, height=40,
                                                    placeholder_text='Type something...😁')
        self.message_entry.place(x=70, y=10)

        self.msg_frame = customtkinter.CTkFrame(master=self.frame_right, width=720, height=680, corner_radius=0)
        self.msg_frame.place(x=20, y=100)

        self.right_canvas = customtkinter.CTkCanvas(master=self.msg_frame, width=1060, height=1012, bg='#383838')
        self.right_canvas.pack(side=customtkinter.LEFT, fill=customtkinter.BOTH, expand=1)

        self.scroll_right = customtkinter.CTkScrollbar(master=self.msg_frame, command=self.right_canvas.yview,
                                                       orientation='vertical')
        self.scroll_right.pack(side=customtkinter.RIGHT, fill=customtkinter.Y)
        self.right_canvas.configure(yscrollcommand=self.scroll_right.set)
        self.right_canvas.bind('<Configure>',
                               lambda e: self.right_canvas.configure(scrollregion=self.right_canvas.bbox("all")))

        self.right_canvas.bind("<MouseWheel>", self.mouse_left)
        self.second_frame_right = customtkinter.CTkFrame(master=self.right_canvas)
        self.second_frame_right1 = customtkinter.CTkFrame(master=self.right_canvas)
        self.right_canvas.create_window((800,10), window=self.second_frame_right1, anchor='ne')
        self.right_canvas.create_window((10, 10), window=self.second_frame_right, anchor='nw')

        for i in range(1, 100):
            button = customtkinter.CTkButton(master=self.second_frame_left, text=str(i), width=320, height=80, bg_color='#383838')
            button.grid(row=i, column=0, padx=5, pady=5)
            if i % 2 == 0:
                button = customtkinter.CTkLabel(master=self.second_frame_right, text=str(i))
                button.grid(row=i, column=0,sticky='nwse', pady=10)
            else:
                button = customtkinter.CTkLabel(master=self.second_frame_right1, text=str(i))
                button.grid(row=i, column=0, sticky='senw', pady=10)


    def mouse_left(self, event):
        self.right_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def mouse_right(self, event):
        self.left_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


SOft().mainloop()