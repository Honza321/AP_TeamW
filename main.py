import tkinter as tk
from gui import PasswordApp
from logika import GeneratorLogika

if __name__ == "__main__":
    # Vytvoření hlavního okna
    root = tk.Tk()
    
    # Načtení tvé logiky
    moje_logika = GeneratorLogika()
    
    # Načtení kolegova okna a předání logiky do něj
    aplikace = PasswordApp(root, moje_logika)
    
    # Spuštění aplikace
    root.mainloop()