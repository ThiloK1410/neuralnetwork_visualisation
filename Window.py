import customtkinter as ctk
import tkinter as tk
from NeuroNet import *
from functools import partial


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

        self.node_buttons = []
        self.node_button_focus = None



        for i, x in enumerate(nn_shape[1:]):
            layer_frame = ctk.CTkFrame(self.nn_frame)
            layer_frame.pack(side="left")

            biases = self.network.network[i].biases[0]

            for j in range(x):

                node_button = ctk.CTkButton(layer_frame)
                self.node_buttons.append(node_button)
                index = len(self.node_buttons) - 1
                node_button.pack(side="top")
                temp = "{:.5f}".format(biases[j])
                text = f"+: {temp}"
                node_button.configure(text=text, command=lambda index=index: self.set_focus(self.node_buttons[index]))

    def set_focus(self, button):
        for b in self.node_buttons:
            b.configure(fg_color="blue")
        button.configure(fg_color="green")
        self.node_button_focus = button



if __name__ == "__main__":
    app = App()
    app.mainloop()
