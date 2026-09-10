import random
import string

class GeneratorLogika:
    def vyrob_heslo(self, delka, pouzit_cisla, pouzit_znaky):
        # Základ jsou vždy malá a velká písmena
        mozne_znaky = string.ascii_letters 
        
        # Pokud uživatel v GUI zaškrtl čísla, přidáme je do výběru
        if pouzit_cisla:
            mozne_znaky += string.digits
            
        # Pokud uživatel v GUI zaškrtl znaky, přidáme je do výběru
        if pouzit_znaky:
            mozne_znaky += string.punctuation

        # Namíchání náhodného hesla podle zvolené délky
        heslo = "".join(random.choice(mozne_znaky) for _ in range(delka))
            
        return heslo