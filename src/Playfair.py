from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as Tk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../img")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class PlayfairPage(Tk.Frame):
    def __init__(self, master, pageManager):
        super().__init__(master)
        self.master = master
        self.origin = pageManager
        self.pack()
        self.Playfair()

    def Playfair(self):
        self.canvas = Canvas(
            self.master,
            bg = "#F4F3F9",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            339.5,
            589.5,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=88.0,
            y=537.0,
            width=503.0,
            height=103.0
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("encrypt_button.png"))
        self.encrypt_button = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("encrypt_button clicked"),
            relief="flat"
        )
        self.encrypt_button.place(
            x=88.0,
            y=682.0,
            width=241.0,
            height=55.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("reset_button.png"))
        self.reset_button = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("reset_button clicked"),
            relief="flat"
        )
        self.reset_button.place(
            x=697.0,
            y=682.0,
            width=503.0,
            height=55.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("decrypt_button.png"))
        self.decrypt_button = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("decrypt_button clicked"),
            relief="flat"
        )
        self.decrypt_button.place(
            x=350.0,
            y=682.0,
            width=241.0,
            height=55.0
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            339.5,
            412.5,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=88.0,
            y=360.0,
            width=503.0,
            height=103.0
        )

        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            948.5,
            589.5,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_3.place(
            x=697.0,
            y=537.0,
            width=503.0,
            height=103.0
        )

        self.entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(
            948.5,
            412.5,
            image=self.entry_image_4
        )
        self.entry_4 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_4.place(
            x=697.0,
            y=360.0,
            width=503.0,
            height=103.0
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("download_button.png"))
        self.download_button = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("download_button clicked"),
            relief="flat"
        )
        self.download_button.place(
            x=697.0,
            y=226.0,
            width=262.0,
            height=75.0
        )

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("upload_button.png"))
        self.upload_button = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("upload_button clicked"),
            relief="flat"
        )
        self.upload_button.place(
            x=88.0,
            y=226.0,
            width=262.0,
            height=75.0
        )

        self.button_image_6 = PhotoImage(
            file=relative_to_assets("back_button.png"))
        self.back_button = Button(
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("back_button clicked"),
            relief="flat"
        )
        self.back_button.place(
            x=88.0,
            y=104.0,
            width=97.0,
            height=55.0
        )

        self.canvas.create_text(
            697.0,
            505.0,
            anchor="nw",
            text="Ciphertext (5-word):",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            697.0,
            331.0,
            anchor="nw",
            text="Ciphertext (no space):",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            88.0,
            505.0,
            anchor="nw",
            text="Enter secret key for encryption and decryption:",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            88.0,
            331.0,
            anchor="nw",
            text="Enter text for encryption and decryption:",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            310.0,
            97.0,
            anchor="nw",
            text="Playfair Cipher",
            fill="#000000",
            font=("Inter Bold", 64 * -1)
        )

    def startPage(self):
        self.mainloop()