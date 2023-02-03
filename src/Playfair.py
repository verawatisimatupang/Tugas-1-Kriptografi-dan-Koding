from pathlib import Path
import string
from tkinter import StringVar, Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog, messagebox
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
            file=relative_to_assets("downloadbiner_no_space_button.png"))
        self.downloadbiner_no_space_button = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.downloadfilebiner_nospace(),
            relief="flat"
        )
        self.downloadbiner_no_space_button.place(
            x=669.0,
            y=417.0,
            width=75.0,
            height=48.0
        )

        self.button_image_6 = PhotoImage(
            file=relative_to_assets("downloadbiner_with_space_button.png"))
        self.downloadbiner_with_space_button = Button(
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.downloadfilebiner_withspace(),
            relief="flat"
        )
        self.downloadbiner_with_space_button.place(
            x=670.0,
            y=594.0,
            width=75.0,
            height=48.0
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

        self.button_image_11 = PhotoImage(
            file=relative_to_assets("downloadtxt_no_space_button.png"))
        self.downloadtxt_no_space_button = Button(
            image=self.button_image_11,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.downloadfiletxt_nospace(),
            relief="flat"
        )
        self.downloadtxt_no_space_button.place(
            x=669.0,
            y=360.0,
            width=75.0,
            height=48.0
        )

        self.button_image_12 = PhotoImage(
            file=relative_to_assets("downloadtxt_with_space_button.png"))
        self.downloadtxt_with_space_button = Button(
            image=self.button_image_12,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.downloadfiletxt_withspace(),
            relief="flat"
        )
        self.downloadtxt_with_space_button.place(
            x=670.0,
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
            text="Playfair Cipher",
            fill="#000000",
            font=("Inter Bold", 64 * -1)
        )

    def startPage(self):
        self.mainloop()

    # Back to home
    def click_backHome(self):
        self.origin.Home()
    
    # Reset
    def reset(self):
        self.plain.set("")
        self.key.set("")
        self.cipher_no_space.set("")
        self.cipher_with_space.set("")
    
    # Remove not aplhabet
    def remove_not_alphabet(self, text):
        remove = "".join(i for i in text if i.isalpha())
        return remove
    
    # Text with space
    def text_with_space(self, text):
        group_text = []
        for i in range (0, len(text), 5):
            space_text = text[i:i+5]
            group_text.append(space_text)
        result = " ".join(group_text)
        return result

    # Bigram no same letters
    def bigram_no_same_letters(self,plaintext):
        i = 0
        final_plaintext = self.remove_not_alphabet(plaintext).upper()
        while (i<len(final_plaintext)):
            l1 = final_plaintext[i]
            if i == len(final_plaintext)-1:
                final_plaintext = final_plaintext + 'X'
                i += 2
                continue
            l2 = final_plaintext[i+1]
            if l1==l2:
                final_plaintext = final_plaintext[:i+1] + "X" + final_plaintext[i+1:]
            i +=2

        bigram_text = []
        for i in range(0, len(final_plaintext), 2):
            space_text = final_plaintext[i:i+2]
            bigram_text.append(space_text)
        if (len(plaintext) % 2 != 0):
            bigram_text[-1] += 'X'
        return bigram_text

    # Remove duplicate and J
    def remove_duplicatesnJ(self, input_list):
        output_list = []
        for element in input_list:
            if element not in output_list and element != "J":
                output_list.append(element)
        return output_list
    
    # Generate key table
    def generate_key_table(self, plaintext):
            output_plaintext = self.remove_not_alphabet(plaintext)

            L = list(string.ascii_uppercase)
            result = output_plaintext.upper() + "".join(L)
            text = self.remove_duplicatesnJ(result)
            final_text = [text[i:i + 5] for i in range(0, len(text), 5)]
            return final_text

    # Search
    def search(self, karakter, key):
        for i in range (len(key)):
                for j in range (len(key[i])):
                        if (karakter == key[i][j]) :
                                return i,j

    # Encrypt
    def encrypt(self):
        plaintext = self.plain.get()
        key = self.key.get()
        bigram_text = self.bigram_no_same_letters(plaintext)
        keyMatrix = self.generate_key_table(key)
        self.key.set(keyMatrix)

        if len(plaintext) == 0:
            messagebox.showerror("Error", "Please input plaintext / file")
        else:
            ciphertext = []
            for i in range(len(bigram_text)):
                if bigram_text[i] == "J":
                    bigram = bigram_text[i].replace('J', 'I')
                else :
                    bigram = bigram_text

                    row_a, col_a = self.search(bigram[i][0], keyMatrix)
                    row_b, col_b = self.search(bigram[i][1], keyMatrix)

                    ciphertext_a = keyMatrix[row_a][col_b]
                    ciphertext_b = keyMatrix[row_b][col_a]

                    if row_a == row_b:
                        ciphertext_a = keyMatrix[row_a][(col_a + 1) % 5] 
                        ciphertext_b = keyMatrix[row_b][(col_b + 1) % 5]
                    elif col_a == col_b:
                        ciphertext_a = keyMatrix[(row_a + 1) % 5][col_a] 
                        ciphertext_b = keyMatrix[(row_b +1) % 5][col_b]

                    ciphertext.append(ciphertext_a + ciphertext_b)

            result_no_space = "".join(ciphertext)
            self.cipher_no_space.set(result_no_space)

            result_with_space = self.text_with_space(result_no_space)
            self.cipher_with_space.set(result_with_space)

    # Decrypt
    def decrypt(self):
        plaintext = self.plain.get()
        key = self.key.get()
        keyMatrix = self.generate_key_table(key)
        bigram_text = self.bigram_no_same_letters(plaintext)
        self.key.set(keyMatrix)

        if len(plaintext) == 0:
            messagebox.showerror("Error", "Please input plaintext / file")
        else:
            ciphertext = []
            for i in range(len(bigram_text)):
                if bigram_text[i] == "J":
                    bigram = bigram_text[i].replace('J', 'I')
                else :
                    bigram = bigram_text
                    
                    row_a, col_a = self.search(bigram[i][0], keyMatrix)
                    row_b, col_b = self.search(bigram[i][1], keyMatrix)
                    
                    ciphertext_a = keyMatrix[row_a][col_b]
                    ciphertext_b = keyMatrix[row_b][col_a]

                    if row_a == row_b:
                        ciphertext_a = keyMatrix[row_a][(col_a - 1) % 5] 
                        ciphertext_b = keyMatrix[row_b][(col_b - 1) % 5]
                    elif col_a == col_b:
                        ciphertext_a = keyMatrix[(row_a - 1)%5][col_a] 
                        ciphertext_b = keyMatrix[(row_b - 1)%5][col_b]

                    ciphertext += ciphertext_a + ciphertext_b

            result = "".join(ciphertext)
            result_replace = result.replace("X","")

            result_no_space = "".join(result_replace)
            self.cipher_no_space.set(result_no_space)

            result_with_space = self.text_with_space(result_no_space)
            self.cipher_with_space.set(result_with_space)

    # Upload file txt of plaintext
    def uploadfiletxt_plaintext(self):
        file = filedialog.askopenfile(mode='r', filetypes =[('Text files', 'txt')])
        if file != None:
            read_filetxt = file.read()
            self.plain.set(read_filetxt)
    
    # Upload file txt of key
    def uploadfiletxt_key(self):
        file = filedialog.askopenfile(mode='r', filetypes =[('Text files', 'txt')])
        if file != None:
            read_filetxt = file.read()
            self.key.set(read_filetxt)

    # Upload file biner of plaintext
    def uploadfilebiner_plaintext(self):
        file = filedialog.askopenfile(mode='rb', filetypes =[('All Files', '*')])
        if file != None:
            read_filebiner = file.read()
            text = read_filebiner.decode("latin-1")
            self.plain.set(text)
    
    # Upload file biner of key
    def uploadfilebiner_key(self):
        file = filedialog.askopenfile(mode='rb', filetypes =[('All Files', '*')])
        if file != None:
            read_filebiner = file.read()
            text = read_filebiner.decode("latin-1")
            self.key.set(text)

    # Download file txt no space
    def downloadfiletxt_nospace(self):
        if len(self.plain.get()) == 0:
            messagebox.showerror("Error", "Please input plaintext / file")
        else :
            file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
            if file != None:
                file.write(self.cipher_no_space.get())
                file.close()
    
    # Download file txt with space
    def downloadfiletxt_withspace(self):
        if len(self.plain.get()) == 0:
            messagebox.showerror("Error", "Please input plaintext / file")
        else :
            file = filedialog.asksaveasfile(mode='wb', defaultextension=".bin")
            if file != None:
                file.write(self.cipher_with_space.get())
                file.close()
    
    # Download file biner no space
    def downloadfilebiner_nospace(self):
        if len(self.plain.get()) == 0:
            messagebox.showerror("Error", "Please input plaintext / file")
        else :
            file = filedialog.asksaveasfile(mode='wb', filetypes =[('All Files', '*')])
            if file != None:
                get_filebiner = self.cipher_no_space.get()
                write_filebiner = get_filebiner.encode("latin-1")
                file.write(write_filebiner)
                file.close()
    
    # Download file biner with space
    def downloadfilebiner_withspace(self):
        if len(self.plain.get()) == 0:
            messagebox.showerror("Error", "Please input plaintext / file")
        else :
            file = filedialog.asksaveasfile(mode='wb', filetypes =[('All Files', '*')])
            if file != None:
                get_filebiner = self.cipher_with_space.get()
                write_filebiner = get_filebiner.encode("latin-1")
                file.write(write_filebiner)
                file.close()
