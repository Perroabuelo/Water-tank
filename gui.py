from tkinter.constants import DISABLED, NORMAL

import ttkbootstrap as tkb


import functions as fn


class WaterTankGUI:

    def __init__(self):

        self.window = tkb.Window(themename="cosmo",maxsize=(400, 500), minsize=(400, 500)  ,resizable=(0, 0), title="Caluladora Tranque")

        # ETo entrada de texto y encabezado
        self.eto_label = tkb.Label(self.window, text="ETo (mm/día)")
        self.eto_label.grid(column=0, row=0)
        self.eto_entry = tkb.Entry(self.window)
        self.eto_entry.grid(column=0, row=1)
        self.eto_entry.bind("<KeyRelease>", self.get_eto)

        # Kc entrada de texto y encabezado
        self.kc_label = tkb.Label(self.window, text="kc")
        self.kc_label.grid(column=1, row=0)
        self.kc_entry = tkb.Entry(self.window)
        self.kc_entry.grid(column=1, row=1)
        self.kc_entry.bind("<KeyRelease>", self.get_eto)

        #ETc valor y encabezado
        self.etc_label = tkb.Label(self.window, text="ETc (mm/día)")
        self.etc_label.grid(column=1, row = 2)
        self.etc_text = tkb.IntVar()
        self.etc_entry = tkb.Entry(self.window, textvariable=self.etc_text, state=DISABLED, background="grey")
        self.etc_entry.grid(column=1, row=3)

        self.window.mainloop()

    def get_eto(self, event, *args):

        try:
            kc_str = self.eto_entry.get()
            eto_str = self.kc_entry.get()
            kc = float(kc_str) if kc_str else 0
            eto = float(eto_str) if eto_str else 0
            etc = kc * eto
            self.etc_text.set(f"{etc:.2f}")

        except ValueError:
            self.etc_text.set("Usar . en lugar de ,")







