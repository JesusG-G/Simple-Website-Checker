import tkinter as tk
from tkinter import filedialog


class FileManager():
    @staticmethod
    def get_path_file():
        root = tk.Tk()
        root.withdraw()

        return( filedialog.askopenfilename() )
    @staticmethod
    def get_path_to_save_file():
        root = tk.Tk()
        root.withdraw()

        return( filedialog.asksaveasfilename())

