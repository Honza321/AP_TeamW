import tkinter as tk
 
class PasswordApp:
    def __init__(self, root, logika):
        self.logika = logika
        root.title("Generátor silných hesel")
        root.geometry("350x250")
 
        # Nastavení délky hesla
        tk.Label(root, text="Délka hesla:", font=("Arial", 10)).pack(pady=(15, 0))
        self.delka_var = tk.IntVar(value=12)
        tk.Spinbox(root, from_=4, to=50, textvariable=self.delka_var, width=5).pack()
 
        # Zaškrtávací políčka pro čísla a speciální znaky
        self.cisla_var = tk.BooleanVar(value=True)
        tk.Checkbutton(root, text="Obsahuje čísla (0-9)", variable=self.cisla_var).pack()
 
        self.znaky_var = tk.BooleanVar(value=True)
        tk.Checkbutton(root, text="Obsahuje speciální znaky (!@#...)", variable=self.znaky_var).pack()
 
        # Tlačítko pro generování, které pošle data do tvé logiky
        tk.Button(root, text="Vygenerovat heslo", command=self.vygeneruj, bg="lightblue").pack(pady=15)
 
        # Textové pole pro zobrazení výsledného hesla (dá se z něj kopírovat)
        self.vysledek_var = tk.StringVar()
        tk.Entry(root, textvariable=self.vysledek_var, width=35, justify='center', font=("Consolas", 12)).pack()
 
    def vygeneruj(self):
        # Načtení hodnot, co uživatel naklikal
        delka = self.delka_var.get()
        pouzit_cisla = self.cisla_var.get()
        pouzit_znaky = self.znaky_var.get()
 
        # Zavolání tvé funkce z logika.py
        nove_heslo = self.logika.vyrob_heslo(delka, pouzit_cisla, pouzit_znaky)
        # Zobrazení výsledku v okně
        self.vysledek_var.set(nove_heslo)