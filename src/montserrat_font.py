import tkinter as tk
from tkinter import font as tkfont
import os


def font_mon(root, font_name="Montserrat", font_size=12, font_path=None):
    if font_path and os.path.exists(font_path):
        try:
            root.tk.call("font", "create", font_name, "-family", font_name, "-size", font_size, "-file", font_path)
        except Exception as e:
            print(f" Error: {e}")
    else:
        print(f"something wrong with path: {font_path}")

    root.option_add("*Font", f"{font_name} {font_size}")

    return tkfont.Font(family=font_name, size=font_size)
