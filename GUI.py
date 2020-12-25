# import PySimpleGUI as sg
#
# layout = [[sg.Text("Welcome to Coordinated-Motion-Planning Challenge \n Please choose board ")], [sg.Button("OK")]]
#
# # Create the window
# window = sg.Window("Demo", layout)
#
# # Create an event loop
# while True:
#     event, values = window.read()
#     # End program if user closes window or
#     # presses the OK button
#     if event == "OK" or event == sg.WIN_CLOSED:
#         break
#
# window.close()


import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()

ROOT.withdraw()
# the input dialog
number_board = simpledialog.askstring(title="Menu",
                                  prompt="Welcome to Coordinated-Motion-Planning Challenge \n Please choose board : ")

# check it out
print("number of board", number_board)