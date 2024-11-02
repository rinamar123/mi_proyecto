import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Rina Mar")
root.geometry("300x400")
root.configure(bg="#202124")

# Variable para almacenar la expresión
expression = ""

# Función para actualizar la expresión en la entrada
def update_expression(value):
    global expression
    expression += value
    entry_var.set(expression)

# Función para evaluar la expresión
def evaluate_expression():
    global expression
    try:
        result = str(eval(expression))
        entry_var.set(result)
        expression = result
    except Exception as e:
        entry_var.set("Error")
        expression = ""

# Función para limpiar la entrada
def clear_expression():
    global expression
    expression = ""
    entry_var.set("")

# Variable para la entrada
entry_var = tk.StringVar()

# Caja de entrada
entry = ttk.Entry(root, textvariable=entry_var, font=('Arial', 18), justify='right')
entry.pack(fill='x', padx=10, pady=10)

# Botones
button_frame = tk.Frame(root, bg="#202124")
button_frame.pack()

# Configuración de los botones con colores
button_config = {
    'width': 5, 'height': 2, 'font': ('Arial', 16), 'relief': 'flat'
}
button_colors = {
    "bg": "#5f6368", "fg": "#FFFFFF", "activebackground": "#202124"
}

# Botones de la calculadora
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

# Crear y organizar los botones
for (text, row, col) in buttons:
    action = evaluate_expression if text == "=" else lambda t=text: update_expression(t)
    tk.Button(button_frame, text=text, command=action, **button_config, **button_colors)\
        .grid(row=row, column=col, padx=5, pady=5)

# Botón de limpiar
tk.Button(root, text="C", command=clear_expression, **button_config,
          bg="#f28b82", fg="#FFFFFF", activebackground="#d93025")\
    .pack(fill='x', padx=10, pady=10)

# Ejecutar la aplicación
root.mainloop()
