import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        self.root = tk.Frame.__init__(self, master)
        self.count = 0
        self.leftFrame()
        self.rightFrame()

    def leftFrame(self):
        self.orderFrame = tk.Frame(master=self.root, bg="red")
        self.orderFrame.pack(side=tk.LEFT, expand=1, pady=0, padx=0)
        self.orderSkeleton()

    def rightFrame(self):
        self.helperFrame = tk.Frame(master=self.root, bg="black")
        self.helperFrame.pack(side=tk.RIGHT, expand=1, pady=0, padx=0)
        # self.createWidgets()

    def createWidgets(self):
        self.buttonsFL = tk.Frame(master=self.FL, bg="red", bd=1)
        self.buttonsFL.pack(side=tk.LEFT, expand=2, padx=240, pady=236)
        self.quit = tk.Button(self.buttonsFL, text='Quit', command=self.quit)
        self.quit.grid(row=0, column=0, sticky=tk.NW)
        self.click = tk.Button(self.buttonsFL, text=self.count,
                               command=self.addOne())
        self.click.grid(row=0, column=1, sticky=tk.E)

    def orderSkeleton(self):
        allOsmeac = []
        with open("osmeac.txt", 'r') as f:
            i = 0
            j = 0
            for line in f:
                #line = line.strip()
                allOsmeac.append(line)
                text = tk.Label(master=self.orderFrame, text=line)
                text.grid(row=i, column=j, sticky=tk.W)
                i += 1

    def addOne(self):
        self.count += 1


app = Application()
app.master.title('Order Helper')
app.mainloop()
