import tkinter as tk
from CLase13 import *
    
ventana = tk.Tk()
ventana.title("Generador de contraseñas")

longitud = tk.Label(ventana, text="Longitud:")
longitud.pack()
largoo = tk.StringVar(value="8")
Longitud = tk.Entry(ventana, textvariable=largoo)
Longitud.pack()

may = tk.BooleanVar()
Mayusculas = tk.Checkbutton(ventana, text="Incluir mayúsculas", variable=may)
Mayusculas.pack()

esp = tk.BooleanVar()
Especial = tk.Checkbutton(ventana, text="Incluir caracteres especiales", variable=esp)
Especial.pack()



contr = tk.StringVar()
passw = tk.Entry(ventana, textvariable=contr)
passw.pack()

fort = tk.IntVar()
fortal = tk.Label(ventana, text="Fortaleza: ")
fortal.pack()
fortaleza = tk.Label(ventana, textvariable=fort)
fortaleza.pack()

gen = GenerarContraseña(Longitud, may, esp, contr, fort)
generar = tk.Button(ventana, text="Generar contraseña", command=gen.generar_contraseña)
generar.pack()
ventana.mainloop()


