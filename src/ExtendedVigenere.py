from pathlib import Path
from tkinter import StringVar, Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog
import tkinter as Tk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../img")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class ExtendedVigenerePage(Tk.Frame):
    def __init__(self, master, pageManager):
        super().__init__(master)
        self.master = master
        self.origin = pageManager
        self.pack()
        self.ExtendedVigenere()

    def ExtendedVigenere(self):
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

        self.key = StringVar()
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
            highlightthickness=0,
            textvariable=self.key
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
            command=lambda: self.encrypt(),
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
            command=lambda: self.reset(),
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

        self.plain = StringVar()
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
            highlightthickness=0,
            textvariable=self.plain
        )
        self.entry_2.place(
            x=88.0,
            y=360.0,
            width=503.0,
            height=103.0
        )

        self.cipher_with_space = StringVar()
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
            highlightthickness=0,
            textvariable=self.cipher_with_space
        )
        self.entry_3.place(
            x=697.0,
            y=537.0,
            width=503.0,
            height=103.0
        )

        self.cipher_no_space = StringVar()
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
            highlightthickness=0,
            textvariable=self.cipher_no_space
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
            command=lambda: self.downloadfile(),
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
            command=lambda: self.uploadfiletxt(),
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
            command=lambda: self.click_backHome(),
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
            text="Extended Vigenere Cipher",
            fill="#000000",
            font=("Inter Bold", 64 * -1)
        )

    def startPage(self):
        self.mainloop()
    
    def click_backHome(self):
        self.origin.Home()
    
    def length_key(self, plaintext,key):
        while len(key) < len(plaintext):
            key += key
        return key[:len(plaintext)]
    
    def text_with_space(self, text):
        group_text = []
        for i in range (0, len(text), 5):
            space_text = text[i:i+5]
            group_text.append(space_text)
        result = " ".join(group_text)
        return result
    
    def reset(self):
        self.plain.set("")
        self.key.set("")
        self.cipher_no_space.set("")
        self.cipher_with_space.set("")

    def uploadfiletxt(self):
        file = filedialog.askopenfile(mode='r', filetypes =[('Text files', 'txt')])
        if file != None:
            read_filetxt = file.read(10000)
            self.plain.set(read_filetxt)
    
    def downloadfile(self):
        file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if file != None:
            file.write(self.cipher_no_space.get())
            file.close()
    
    def encrypt(self):
        plaintext = self.plain.get()
        key = self.key.get()

        check_length_key = self.length_key(plaintext,key)

        ciphertext = []
        for i in range (len(plaintext)):
            plaintext_to_int = ord(plaintext[i])
            key_to_int = ord(check_length_key[i])
            encrypt_formula = (plaintext_to_int + key_to_int) % 256
            ciphertext.append(chr(encrypt_formula))
        result_no_space = "".join(ciphertext)
        self.cipher_no_space.set(result_no_space)

        result_with_space = self.text_with_space(result_no_space)
        self.cipher_with_space.set(result_with_space)