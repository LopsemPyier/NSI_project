import tkinter as Tk

ERROR_TEXT = "'{}' n'est pas un caractère correct en base {}"
RESULT_TEXT = "'{}' en base {} vaut '{}' en base {}"

DEFAULT_START_BASE = 10
DEFAULT_ARRIVED_BASE = 2
DEFAULT_START_NUMBER = 0
DEFAULT_ARRIVED_NUMBER = 0

ALPHA = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def convertBase(number, base1, base2):
    global ALPHA
    n_dec = 0
    for i in range(len(number)): #conversion en base 10
        n_dec += ALPHA.index(number[i]) * (base1 ** (len(number)-i-1))
        dig = []
    while n_dec > 0: #conversion en base b2
        r = ALPHA[n_dec % base2]
        dig.append(r)
        n_dec //= base2
    return "".join(dig)[::-1]

class Gui:
    def __init__(self, root):
        self.root = root

        self.errorBase = Tk.StringVar()
        self.startNumber = Tk.StringVar()
        self.startBase = Tk.IntVar()
        self.arrivedBase = Tk.IntVar()
        self.arrivedNumber = 0
        self.resultText = Tk.StringVar()

        self.mainFrame = Tk.Frame(self.root)
        self.explicationLabel = Tk.Label(self.mainFrame, text="Bienvenue dans notre convertiseur de base.")

        self.startNumberFrame = Tk.Frame(self.mainFrame)
        self.startNumberLabel = Tk.Label(self.startNumberFrame, text="Entrez un nombre")
        self.startNumberEntry = Tk.Entry(self.startNumberFrame, textvariable=self.startNumber)

        self.startNumberErrorLabel = Tk.Label(self.startNumberFrame, textvariable=self.errorBase, fg="red")
        
        self.startBaseFrame = Tk.Frame(self.mainFrame)
        self.startBaseLabel = Tk.Label(self.startBaseFrame, text="En base : ")
        self.startBaseSpinBox = Tk.Spinbox(self.startBaseFrame, from_=2, to=36, textvariable=self.startBase)
        self.arrivedBaseFrame = Tk.Frame(self.mainFrame)
        self.arrivedBaseLabel = Tk.Label(self.startBaseFrame, text="Vers la base : ")
        self.arrivedBaseSpinBox = Tk.Spinbox(self.mainFrame, from_=2, to=36, textvariable=self.arrivedBase)

        self.buttonFrame = Tk.Frame(self.mainFrame)
        self.calculateButton = Tk.Button(self.buttonFrame, text="Convertir", command=self.convert)
        self.resetButton = Tk.Button(self.buttonFrame, text="Reset", command=self.reset)
        self.switchButton = Tk.Button(self.buttonFrame, text="Échanger les bases", command=self.switchBase)
        self.copyButton = Tk.Button(self.buttonFrame, text="Copier le résultat", command=self.copyResult)

        self.resultLabel = Tk.Label(self.mainFrame, textvariable=self.resultText)

        self.packMainFrameItems()
        self.displayMainFrame()
    
    def packMainFrameItems(self):
        self.explicationLabel.pack()

        self.startNumberFrame.pack()
        self.startNumberLabel.pack()
        self.startNumberEntry.pack()
        
        self.startBaseFrame.pack()
        self.startBaseLabel.pack()
        self.startBaseSpinBox.pack()
        self.arrivedBaseFrame.pack()
        self.arrivedBaseLabel.pack()
        self.arrivedBaseSpinBox.pack()

        self.buttonFrame.pack()
        self.calculateButton.grid(row = 1, column = 1)
        self.resetButton.grid(row = 1, column = 2)
        self.switchButton.grid(row = 2, column = 1)
        self.copyButton.grid(row = 2, column = 2)

        self.startBase.set(DEFAULT_START_BASE)
        self.arrivedBase.set(DEFAULT_ARRIVED_BASE)

    def displayMainFrame(self):
        self.mainFrame.pack(expand=True, fill= Tk.BOTH)
    
    def convert(self):
        self.startBase.set(int(self.startBaseSpinBox.get()))
        self.arrivedBase.set(int(self.arrivedBaseSpinBox.get()))

        self.startNumber.set(self.startNumberEntry.get().upper())
        charIndex = self.checkIfNumberEntredIsCorrect()
        if charIndex != -1:
            self.errorBase.set(ERROR_TEXT.format(self.startNumber.get()[charIndex], self.startBase.get()))
            self.startNumberErrorLabel.pack()
            return
        
        self.startNumberErrorLabel.pack_forget()
        
        self.arrivedNumber = convertBase(self.startNumber.get(), self.startBase.get(), self.arrivedBase.get())

        self.resultText.set(RESULT_TEXT.format(self.startNumber.get(), self.startBase.get(), self.arrivedNumber, self.arrivedBase.get()))
        self.resultLabel.pack()

    def reset(self):
        self.startNumber.set("")
        self.arrivedNumber = DEFAULT_START_NUMBER

        self.errorBase.set("")
        self.resultText.set("")

        self.startBase.set(DEFAULT_START_BASE)
        self.arrivedBase.set(DEFAULT_ARRIVED_BASE)

        self.startNumberErrorLabel.pack_forget()
        self.resultLabel.pack_forget()

    def switchBase(self):
        b1 = self.startBase.get()
        b2 = self.arrivedBase.get()

        self.startBase.set(b2)
        self.arrivedBase.set(b1)

    def copyResult(self):
        if self.resultLabel.winfo_ismapped():
            self.root.clipboard_clear()
            self.root.clipboard_append(self.arrivedNumber)
            self.root.update()

    def checkIfNumberEntredIsCorrect(self):
        global ALPHA
        charIndex = 0
        for i in self.startNumber.get():
            if ALPHA.index(i) >= self.startBase.get():
                return charIndex
            charIndex += 1
        return -1
    
if __name__ == "__main__":
    root = Tk.Tk()
    gui = Gui(root)
    root.mainloop()