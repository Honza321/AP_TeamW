import tkinter as tk
from tkinter import ttk
from logika import generuj_heslo

def spustit_aplikaci():
    # 1. Hlavní okno aplikace
    root = tk.Tk()
    root.title("Generátor silných hesel")
    root.geometry("400x350")
    root.resizable(False, False)

    # Proměnné pro nastavení z GUI
    var_delka = tk.IntVar(value=12)
    var_velka = tk.BooleanVar(value=True)
    var_cisla = tk.BooleanVar(value=True)
    var_symboly = tk.BooleanVar(value=True)

    # Funkce, která propojí tlačítko v GUI s vaší logikou
    def vygeneruj_a_zobraz():
        heslo = generuj_heslo(
            delka=var_delka.get(),
            pouzit_velka=var_velka.get(),
            pouzit_cisla=var_cisla.get(),
            pouzit_symboly=var_symboly.get()
        )
        vystup_heslo.delete(0, tk.END)
        vystup_heslo.insert(0, heslo)

    # 2. Uživatelské rozhraní (GUI Prvky)
    # Pole s výsledným heslem
    lbl_vystup = ttk.Label(root, text="Vygenerované heslo:", font=("Arial", 10, "bold"))
    lbl_vystup.pack(pady=(15, 5))
    
    vystup_heslo = ttk.Entry(root, font=("Consolas", 12), justify="center", width=30)
    vystup_heslo.pack(pady=5)

    # Nastavení délky hesla (Posuvník + text)
    frame_delka = ttk.Frame(root)
    frame_delka.pack(pady=10)
    
    ttk.Label(frame_delka, text="Délka hesla:").pack(side=tk.LEFT, padx=5)
    lbl_cislo_delka = ttk.Label(frame_delka, text="12")
    lbl_cislo_delka.pack(side=tk.RIGHT, padx=5)

    def aktualizuj_delku(val):
        lbl_cislo_delka.config(text=str(int(float(val))))

    posuvnik = ttk.Scale(root, from_=4, to=32, variable=var_delka, command=aktualizuj_delku)
    posuvnik.pack(fill=tk.X, padx=40, pady=5)

    # Zaškrtávací políčka (Checkbuttony)
    frame_volby = ttk.Frame(root)
    frame_volby.pack(pady=10)

    ttk.Checkbutton(frame_volby, text="Velká písmena (A-Z)", variable=var_velka).pack(anchor=tk.W)
    ttk.Checkbutton(frame_volby, text="Číslice (0-9)", variable=var_cisla).pack(anchor=tk.W)
    ttk.Checkbutton(frame_volby, text="Speciální znaky (!@#$)", variable=var_symboly).pack(anchor=tk.W)

    # Tlačítko pro generování
    btn_generovat = ttk.Button(root, text="Vygenerovat heslo", command=vygeneruj_a_zobraz)
    btn_generovat.pack(pady=15)

    # První vygenerování hesla po spuštění
    vygeneruj_a_zobraz()

    # Spuštění grafického okna
    root.mainloop()

if __name__ == "__main__":
    spustit_aplikaci()