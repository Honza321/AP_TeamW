import random
import string

def generuj_heslo(delka=12, pouzit_velka=True, pouzit_cisla=True, pouzit_symboly=True):
    """
    Vygeneruje náhodné bezpečné heslo na základě parametrů z uživatelského rozhraní.
    
    :param delka: Požadovaná délka hesla (int)
    :param pouzit_velka: Zda zahrnout velká písmena (bool)
    :param pouzit_cisla: Zda zahrnout číslice (bool)
    :param pouzit_symboly: Zda zahrnout speciální znaky (bool)
    :return: Vygenerovaný řetězec hesla nebo chybová zpráva
    """
    # Základní sada vždy obsahuje malá písmena
    znakova_sada = string.ascii_lowercase
    
    # Rozšiřování sady podle zaškrtnutých voleb
    if pouzit_velka:
        znakova_sada += string.ascii_uppercase
    if pouzit_cisla:
        znakova_sada += string.digits
    if pouzit_symboly:
        znakova_sada += string.punctuation
        
    # Ošetření stavu, kdy uživatel odškrtne všechny možnosti
    if not znakova_sada:
        return "Vyberte alespoň 1 sadu znaků!"

    # Generování náhodných znaků ze zvolené sady
    heslo = "".join(random.choice(znakova_sada) for _ in range(int(delka)))
    return heslo