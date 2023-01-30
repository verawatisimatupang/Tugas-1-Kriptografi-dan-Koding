from tkinter import Tk
import Home, Vigenere, ExtendedVigenere, Playfair, OneTimePad

class pageManager():
    def __init__(self):
        self.user = None
        self.window = Tk()
        self.window.geometry("1280x832")
        self.window.configure(bg = "#F4F3F9")
        self.window.title('Kriptografi dan Koding')
        self.window.resizable(False, False)

        self.page = Home.HomePage(master = self.window, pageManager = self)

    def run(self):
        self.page.startPage()
    
    def Home(self):
        self.page = Home.HomePage(master = self.window, pageManager = self)
        self.page.startPage()

    def Vigenere(self):
        self.page = Vigenere.VigenerePage(master = self.window, pageManager = self)
        self.page.startPage()
        
    def ExtendedVigenere(self):
        self.page = ExtendedVigenere.ExtendedVigenerePage(master = self.window, pageManager = self)
        self.page.startPage()
        
    def Playfair(self):
        self.page = Playfair.PlayfairPage(master = self.window, pageManager = self)
        self.page.startPage()
        
    def OneTimePad(self):
        self.page = OneTimePad.OneTimePadPage(master = self.window, pageManager = self)
        self.page.startPage()
