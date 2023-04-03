import customtkinter as ctk
import tkinter as tk
from NeuroNet import *


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("NeuroVision")

        n_f = NetworkFrame(self, [1])



class NetworkFrame:
    def __init__(self, parent, nn_shape):
        self.parent = parent

        self.main_frame = ctk.CTkFrame(parent, width=800, height=200).pack(side="left")

        ctk.CTkLabel(self.main_frame)

        for i, x in enumerate(nn_shape):
            layer_frame = ctk.CTkFrame(self.main_frame).pack(side="left")
            for j in range(x):
                node_label = ctk.CTkLabel(layer_frame).pack(side="top")







if __name__ == "__main__":
    app = App()
    app.mainloop()
