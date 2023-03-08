import tkinter as tk
import string
import random
from tkinter import messagebox
class GenerarContraseña:
    def __init__(self, Longitud, may, esp, contr, fort):
        self.Longitud = Longitud
        self.may = may
        self.esp = esp
        self.contr = contr
        self.fort = fort

    def generar_contraseña(self):
        largo = int(self.Longitud.get())
        Mayus = self.may.get()
        especial = self.esp.get()
        
        # Creamos una lista de caracteres posibles para la contraseña
        caracteres = string.ascii_lowercase
        if Mayus:
            caracteres += string.ascii_uppercase
        if especial:
            caracteres += string.punctuation
        
        # Generamos la contraseña aleatoria
        password = ''.join(random.choice(caracteres) for i in range(largo))
        self.contr.set(password)
        messagebox.showinfo("Contraseña","La contraseña generada es: " + password)
        # Verificamos la fortaleza de la contraseña
        score = 0
        if any(c.isupper() for c in password):
            score += 1
        if any(c.islower() for c in password):
            score += 1
        if any(c in string.punctuation for c in password):
            score += 2
        if largo >= 12:
            score += 1
        if score == 1:
            ff="Contraseña muy debil"
        elif score == 2:
            ff="Contraseña debil"
        elif score == 3:
            ff="Contraseña media"
        elif score == 4:
            ff="Contraseña fuerte"
        elif score == 5:
            ff="Contraseña muy fuerte"
        self.fort.set(ff)