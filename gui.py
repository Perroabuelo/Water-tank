import ttkbootstrap as tkb


import functions as fn


class WaterTankGUI:

    def __init__(self):

        self.window = tkb.Window(themename="darkly",maxsize=(300, 300), minsize=(300, 300)  ,resizable=(0, 0), title="Caluladora Tranque")

        self.text = tkb.StringVar()
        self.text.trace("w", self.get_value)
        self.width_entry = tkb.Entry(textvariable=self.text)
        self.width_entry.grid(column=0, row=0)


        self.window.mainloop()

    def get_value(self, *args):

        value = self.width_entry.get()
        print(value)



