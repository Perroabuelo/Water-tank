import ttkbootstrap as tkb

class WaterTankGUI:

    def __init__(self):

        self.window = tkb.Window(themename="darkly", resizable=(300,300), title="Caluladora Tranque")
        self.test_text = tkb.Label(text="Hola")
        self.test_text.pack()

        self.window.mainloop()



WaterTankGUI()