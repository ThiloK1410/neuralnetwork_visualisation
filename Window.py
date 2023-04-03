import customtkinter as ctk
import tkinter as tk
from NeuroNet import *


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("NeuroVision")
        self.geometry("800x600")

        screen = ctk.CTkFrame(self)

        n_f = NetworkFrame(self, [1, 2, 3, 2, 1])



class NetworkFrame:
    def __init__(self, parent, nn_shape):
        self.parent = parent

        self.network = NeuralNetwork(nn_shape)

        self.main_frame = ctk.CTkFrame(self.parent, width=800, height=200)
        self.main_frame.pack(side="top", fill="x")

        self.nn_frame = ctk.CTkFrame(self.main_frame)
        self.nn_frame.pack(side="top")



        for i, x in enumerate(nn_shape[1:]):
            layer_frame = ctk.CTkFrame(self.nn_frame)
            layer_frame.pack(side="left")

            biases = self.network.network[i].biases[0]

            for j in range(x):
                node_label = ctk.CTkLabel(layer_frame)
                node_label.pack(side="top")
                text = f"+: {biases[j]}"
                node_label.configure(text=text)








if __name__ == "__main__":
    app = App()
    app.mainloop()
