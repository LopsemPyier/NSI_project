import tkinter as Tk
import tkinter.font as Tkf

ERROR_TEXT = "'{}' est un chiffre incorrect en base {}"
RESULT_TEXT = "{}"

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

        self.customTitleFont = Tkf.Font(family="Avenir Light", size=18, weight = Tkf.NORMAL)
        self.customTextFont = Tkf.Font(family="Avenir Light", size=11, weight = Tkf.NORMAL)
        self.customEntryFont = Tkf.Font(family="Avenir Light Oblique", size=12, weight = Tkf.NORMAL)
        self.customErrorFont = Tkf.Font(family="Avenir Light", size=11, weight = Tkf.NORMAL)

        self.root = root

        self.root.title("Convertiseur de base")

        self.root.geometry("270x338")
        self.root.resizable(0,0)
        self.root.config(bg="#fff")

        self.errorBase = Tk.StringVar()
        self.startNumber = Tk.StringVar()
        self.startBase = Tk.IntVar()
        self.arrivedBase = Tk.IntVar()
        self.arrivedNumber = 0
        self.resultText = Tk.StringVar()

        self.mainFrame = Tk.Frame(self.root, bg="#fff")
        self.explicationLabel = Tk.Label(self.mainFrame, text="Convertisseur de base", font = self.customTitleFont, bg="#fff")

        self.startFrame = Tk.Frame(self.mainFrame, bg="#fff")
        self.arrivedFrame = Tk.Frame(self.mainFrame, bg="#fff")

        self.startEntryFrame = Tk.Frame(self.startFrame, width = 230, height = 36, bg="#fff", relief=Tk.SOLID, borderwidth=1)
        self.startEntryLimitFrame = Tk.Frame(self.startEntryFrame, width = 230, height = 36, bg="#fff")
        self.startNumberEntry = Tk.Entry(self.startEntryLimitFrame, relief=Tk.FLAT, textvariable = self.startNumber, bg="#fff", width = 250, font=self.customEntryFont)
        self.resetImage = Tk.PhotoImage(file="reset.png")
        self.resetLabel = Tk.Label(self.startEntryFrame, image=self.resetImage, bg="#fff")
        self.resetLabel.bind("<Button-1>",lambda e:self.reset())
        
        self.startBaseLabel = Tk.Label(self.startFrame, text="En base : ", bg="#fff", font=self.customTextFont)
        self.startBaseSpinBox = Tk.Spinbox(self.startFrame, from_=2, to=36, textvariable=self.startBase, bg="#fff", font=self.customTextFont)

        self.startNumberErrorLabel = Tk.Label(self.mainFrame, textvariable=self.errorBase, fg="#f00", bg="#fff", font=self.customErrorFont)

        self.arrowSwitchImage = Tk.PhotoImage(file="arrowSwitch.png")
        self.arrowSwitchLabel = Tk.Label(self.mainFrame, image=self.arrowSwitchImage, bg="#fff")
        self.arrowSwitchLabel.bind("<Button-1>",lambda e:self.switchBase())

        self.resultFrame = Tk.Frame(self.arrivedFrame, bg="#fff", relief=Tk.SOLID, borderwidth=1)
        self.resultLabel = Tk.Label(self.resultFrame, textvariable=self.resultText, bg="#fff", font = self.customEntryFont)
        self.copyImage = Tk.PhotoImage(file="copy.png")
        self.copyLabel = Tk.Label(self.resultFrame, image=self.copyImage, bg="#fff")
        self.copyLabel.bind("<Button-1>",lambda e:self.copyResult())

        self.arrivedBaseLabel = Tk.Label(self.arrivedFrame, text="En base : ", bg="#fff", font=self.customTextFont)
        self.arrivedBaseSpinBox = Tk.Spinbox(self.arrivedFrame, from_=2, to=36, textvariable=self.arrivedBase, bg="#fff", font=self.customTextFont)

        self.packMainFrameItems()
        self.displayMainFrame()
    
    def packMainFrameItems(self):
        self.explicationLabel.place(x=10, y=30, width=250, height = 30)

        self.startFrame.place(x=20, y=90, width=230, height = 65)
        self.startEntryFrame.pack()
        self.startEntryLimitFrame.pack()

        self.arrowSwitchLabel.place(x=130, y=175)

        self.arrivedFrame.place(x=20, y=205, width=230, height = 90)

        self.startNumberEntry.place(x=5, y=5, width=200, height = 24)
        self.resetLabel.place(x=210, y=13, width=10, height = 10)
        
        self.startBaseLabel.place(x=0, y=45, width=65, height = 20)
        self.startBaseSpinBox.place(x=70, y=45, width=160, height = 20)

        self.resultFrame.place(x=0, y=0, width=230, height = 60)
        self.arrivedBaseLabel.place(x=0, y=70, width=65, height = 20)
        self.arrivedBaseSpinBox.place(x=70, y=70, width=160, height = 20)

        self.resultLabel.place(x=5, y=5, width=200, height = 50)
        self.copyLabel.place(x=205, y=5)

        self.startNumberEntry.focus()
        self.startNumberEntry.bind('<Return>',self.convertEvent)

        self.startNumber.trace('w',self.convertTrace)

        self.startBase.set(DEFAULT_START_BASE)
        self.arrivedBase.set(DEFAULT_ARRIVED_BASE)

    def displayMainFrame(self):
        self.mainFrame.pack(expand=True, fill= Tk.BOTH)

    def convertTrace(self, a, b, c):
        self.convert()
    
    def convertEvent(self,e):
        self.convert()
    
    def convert(self):
        self.startBase.set(int(self.startBaseSpinBox.get()))
        self.arrivedBase.set(int(self.arrivedBaseSpinBox.get()))

        self.startNumber.set(self.startNumberEntry.get().upper())
        charIndex = self.checkIfNumberEntredIsCorrect()
        if charIndex != -1:
            self.errorBase.set(ERROR_TEXT.format(self.startNumber.get()[charIndex], self.startBase.get()))
            self.startNumberErrorLabel.place(x=10, y=160, width = 250, height = 25)
            self.arrowSwitchLabel.place_configure(y = 195)
            self.arrivedFrame.place_configure(y = 225)
            return
        
        self.startNumberErrorLabel.place_forget()
        self.arrowSwitchLabel.place_configure(y = 175)
        self.arrivedFrame.place_configure(y = 205)

        if self.startNumber.get() == "":
            self.resultText.set(RESULT_TEXT.format(""))
            self.arrivedNumber = -1
            return
        
        self.arrivedNumber = convertBase(self.startNumber.get(), self.startBase.get(), self.arrivedBase.get())

        self.resultText.set(RESULT_TEXT.format(self.arrivedNumber))

    def reset(self):
        self.startNumber.set("")
        self.arrivedNumber = DEFAULT_START_NUMBER

        self.errorBase.set("")
        self.resultText.set("")

        self.startBase.set(DEFAULT_START_BASE)
        self.arrivedBase.set(DEFAULT_ARRIVED_BASE)

        self.startNumberErrorLabel.pack_forget()

    def switchBase(self):
        b1 = self.startBase.get()
        b2 = self.arrivedBase.get()

        self.startBase.set(b2)
        self.arrivedBase.set(b1)

    def copyResult(self):
        if self.arrivedNumber != -1:
            self.root.clipboard_clear()
            self.root.clipboard_append(self.arrivedNumber)
            self.root.update()
        else :
            self.root.clipboard_clear()
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
