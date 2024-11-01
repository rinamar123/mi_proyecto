#luis jose diaz urieles
#31/10/2024
#grupo 2 semestre 5

import tkinter as tk

def suma():
    try:
        resultado.set(float(entry1.get()) + float(entry2.get()))
    except ValueError:
        resultado.set("Error")

def resta():
    try:
        resultado.set(float(entry1.get()) - float(entry2.get()))
    except ValueError:
        resultado.set("Error")

def multiplicacion():
    try:
        resultado.set(float(entry1.get()) * float(entry2.get()))
    except ValueError:
        resultado.set("Error")

def division():
    try:
        if float(entry2.get()) != 0:
            resultado.set(float(entry1.get()) / float(entry2.get()))
        else:
            resultado.set("No se puede dividir por cero")
    except ValueError:
        resultado.set("Error")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Calculadora")

tk.Label(root, text="Primer número:").grid(row=0, column=0)
tk.Label(root, text="Segundo número:").grid(row=1, column=0)

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

tk.Button(root, text="+", command=suma).grid(row=2, column=0)
tk.Button(root, text="-", command=resta).grid(row=2, column=1)
tk.Button(root, text="*", command=multiplicacion).grid(row=3, column=0)
tk.Button(root, text="/", command=division).grid(row=3, column=1)

resultado = tk.StringVar()
tk.Label(root, textvariable=resultado).grid(row=4, column=0, columnspan=2)

root.mainloop()

