from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as Tk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../img")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class HomePage(Tk.Frame):
    def __init__(self, master, pageManager):
        super().__init__(master)
        self.master = master
        self.origin = pageManager
        self.pack()
        self.Home()
    
    def Home(self):
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
        self.button_onetimepad = PhotoImage(
            file=relative_to_assets("onetimepad_button.png"))
        self.onetimepad_button = Button(
            image=self.button_onetimepad,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.click_onetimepad(),
            relief="flat"
        )
        self.onetimepad_button.place(
            x=462.0,
            y=586.0,
            width=356.0,
            height=76.0
        )

        self.button_playfair = PhotoImage(
            file=relative_to_assets("playfair_button.png"))
        self.playfair_button = Button(
            image=self.button_playfair,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.click_playfair(),
            relief="flat"
        )
        self.playfair_button.place(
            x=462.0,
            y=468.0,
            width=356.0,
            height=76.0
        )

        self.button_extendedvigenere = PhotoImage(
            file=relative_to_assets("extendedvigenere_button.png"))
        self.extendedvigenere_button = Button(
            image=self.button_extendedvigenere,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.click_extendedvigenere(),
            relief="flat"
        )
        self.extendedvigenere_button.place(
            x=462.0,
            y=350.0,
            width=356.0,
            height=76.0
        )

        self.button_vigenere = PhotoImage(
            file=relative_to_assets("vigenere_button.png"))
        self.vigenere_button = Button(
            image=self.button_vigenere,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:self.click_vigenere(),
            relief="flat"
        )
        self.vigenere_button.place(
            x=462.0,
            y=232.0,
            width=356.0,
            height=76.0
        )

        self.canvas.create_text(
            410.0,
            158.0,
            anchor="nw",
            text="by : Verawati Esteria S. Simatupang & Agnes Tamara",
            fill="#000000",
            font=("OpenSansItalic Regular", 20 * -1)
        )

        self.canvas.create_text(
            535.0,
            55.0,
            anchor="nw",
            text="Cipher",
            fill="#000000",
            font=("OpenSansRoman Bold", 64 * -1)
        )

    def startPage(self):
        self.mainloop()
    
    def click_vigenere(self):
        self.origin.Vigenere()

    def click_extendedvigenere(self):
        self.origin.ExtendedVigenere()

    def click_playfair(self):
        self.origin.Playfair()

    def click_onetimepad(self):
        self.origin.OneTimePad()