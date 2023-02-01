from pathlib import Path
from tkinter import StringVar, Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog, messagebox
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
            381.0,
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
            x=158.0,
            y=537.0,
            width=446.0,
            height=103.0
        )

        self.plain = StringVar()
        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            381.0,
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
            x=158.0,
            y=360.0,
            width=446.0,
            height=103.0
        )

        self.cipher_with_space = StringVar()
        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            983.0,
            589.5,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            textvariable= self.cipher_with_space
        )
        self.entry_3.place(
            x=760.0,
            y=537.0,
            width=446.0,
            height=103.0
        )

        self.cipher_no_space = StringVar()
        self.entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(
            983.0,
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
            x=760.0,
            y=360.0,
            width=446.0,
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
            x=68.0,
            y=682.0,
            width=250.58251953125,
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
            x=682.0,
            y=682.0,
            width=524.0,
            height=55.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("back_button.png"))
        self.back_button = Button(
            image=self.button_image_3,
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

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("decrypt_button.png"))
        self.decrypt_button = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.decrypt(),
            relief="flat"
        )
        self.decrypt_button.place(
            x=340.41748046875,
            y=682.0,
            width=250.58250427246094,
            height=55.0
        )

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("download_no_space_button.png"))
        self.download_no_space_button = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.downloadfile_nospace(),
            relief="flat"
        )
        self.download_no_space_button.place(
            x=669.0,
            y=379.0,
            width=75.0,
            height=75.0
        )

        self.button_image_6 = PhotoImage(
            file=relative_to_assets("download_with_space_button.png"))
        self.download_with_space_button = Button(
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.downloadfile_withspace(),
            relief="flat"
        )
        self.download_with_space_button.place(
            x=669.0,
            y=556.0,
            width=75.0,
            height=75.0
        )

        self.button_image_7 = PhotoImage(
            file=relative_to_assets("uploadbiner_plaintext_button.png"))
        self.uploadbiner_plaintext_button = Button(
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.uploadfilebiner_plaintext(),
            relief="flat"
        )
        self.uploadbiner_plaintext_button.place(
            x=68.0,
            y=417.0,
            width=75.0,
            height=48.0
        )

        self.button_image_8 = PhotoImage(
            file=relative_to_assets("uploadbiner_key_button.png"))
        self.uploadbiner_key_button = Button(
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.uploadfilebiner_key(),
            relief="flat"
        )
        self.uploadbiner_key_button.place(
            x=68.0,
            y=594.0,
            width=75.0,
            height=48.0
        )

        self.button_image_9 = PhotoImage(
            file=relative_to_assets("uploadtxt_plaintext_button.png"))
        self.uploadtxt_plaintext_button = Button(
            image=self.button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.uploadfiletxt_plaintext(),
            relief="flat"
        )
        self.uploadtxt_plaintext_button.place(
            x=68.0,
            y=360.0,
            width=75.0,
            height=48.0
        )

        self.button_image_10 = PhotoImage(
            file=relative_to_assets("uploadtxt_key_button.png"))
        self.uploadtxt_key_button = Button(
            image=self.button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.uploadfiletxt_key(),
            relief="flat"
        )
        self.uploadtxt_key_button.place(
            x=68.0,
            y=537.0,
            width=75.0,
            height=48.0
        )

        self.canvas.create_text(
            773.0,
            505.0,
            anchor="nw",
            text="Ciphertext (5-word):",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            773.0,
            331.0,
            anchor="nw",
            text="Ciphertext (no space):",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            158.0,
            505.0,
            anchor="nw",
            text="Enter secret key for encryption and decryption:",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            158.0,
            331.0,
            anchor="nw",
            text="Enter text for encryption and decryption:",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            224.0,
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
    
    def checklength_key(self,plaintext, key):
        while len(key) < len(plaintext):
            key += key
            result = key[:len(plaintext)]
        finalkey = []
        for i in range(0, len(key), len(plaintext)):
            space_text = key[i:len(plaintext)]
            finalkey.append(space_text)
            result = "".join(finalkey) 
        return result 
    
    def text_with_space(self,text):
        group_text = []
        for i in range (0, len(text), 5):
            space_text = text[i:i+5]
            group_text.append(space_text)
        result = " ".join(group_text)
        return result

    def encrypt(self):
        plaintext = self.plain.get()
        key = self.key.get()
        
        if len(plaintext) == 0:
            messagebox.showerror("Error", "Please input plaintext / file")
        elif len(key) == 0:
            messagebox.showerror("Error", "Please input key / file")
        else :
            check_length_key = self.checklength_key(plaintext,key)

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
    
    def decrypt(self):
        plaintext = self.plain.get()
        key = self.key.get()

        if len(plaintext) == 0:
            messagebox.showerror("Error", "Please input plaintext / file")
        elif len(key) == 0:
            messagebox.showerror("Error", "Please input key / file")
        else :
            check_length_key = self.checklength_key(plaintext,key)

            ciphertext = []
            for i in range (len(plaintext)):
                plaintext_to_int = ord(plaintext[i]) 
                key_to_int = ord(check_length_key[i])
                encrypt_formula = (plaintext_to_int - key_to_int) % 256
                ciphertext.append(chr(encrypt_formula))
            result_no_space = "".join(ciphertext)
            self.cipher_no_space.set(result_no_space)

            result_with_space = self.text_with_space(result_no_space)
            self.cipher_with_space.set(result_with_space)
    
    def reset(self):
        self.plain.set("")
        self.key.set("")
        self.cipher_no_space.set("")
        self.cipher_with_space.set("")
    
    def uploadfiletxt_plaintext(self):
        file = filedialog.askopenfile(mode='r', filetypes =[('Text files', 'txt')])
        if file != None:
            read_filetxt = file.read(10000)
            self.plain.set(read_filetxt)
    
    def uploadfiletxt_key(self):
        file = filedialog.askopenfile(mode='r', filetypes =[('Text files', 'txt')])
        if file != None:
            read_filetxt = file.read(10000)
            self.key.set(read_filetxt)

    def uploadfilebiner_plaintext(self):
        file = filedialog.askopenfile(mode='rb', filetypes =[('All Files', '*')])
        if file != None:
            read_filetxt = file.read(10000)
            self.plain.set(read_filetxt)
    
    def uploadfilebiner_key(self):
        file = filedialog.askopenfile(mode='rb', filetypes =[('All Files', '*')])
        if file != None:
            read_filetxt = file.read(10000)
            self.key.set(read_filetxt)
    
    def downloadfile_nospace(self):
        if len(self.plain.get()) == 0:
            messagebox.showerror("Error", "Please input plaintext / file")
        else :
            file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
            if file != None:
                file.write(self.cipher_no_space.get())
                file.close()
    
    def downloadfile_withspace(self):
        if len(self.plain.get()) == 0:
            messagebox.showerror("Error", "Please input plaintext / file")
        else :
            file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
            if file != None:
                file.write(self.cipher_with_space.get())
                file.close()
