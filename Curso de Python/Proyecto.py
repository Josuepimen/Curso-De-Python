import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
        operacion = operacion_var.get()

        if operacion == 'Suma':
            resultado = num1 + num2
        elif operacion == 'Resta':
            resultado = num1 - num2
        elif operacion == 'Multiplicación':
            resultado = num1 * num2
        elif operacion == 'División':
            if num2 != 0:
                resultado = num1 / num2
            else:
                messagebox.showerror("Error", "No se puede dividir entre cero.")
                return
        else:
            messagebox.showerror("Error", "Operación no válida.")
            return

        messagebox.showinfo("Resultado", f"El resultado es: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos.")


ventana = tk.Tk()
ventana.title("Calculadora")


operacion_var = tk.StringVar(value='Suma')


label_num1 = tk.Label(ventana, text="Ingrese el primer número:")
label_num1.pack()

entry_num1 = tk.Entry(ventana)
entry_num1.pack()

label_num2 = tk.Label(ventana, text="Ingrese el segundo número:")
label_num2.pack()

entry_num2 = tk.Entry(ventana)
entry_num2.pack()

label_operacion = tk.Label(ventana, text="Seleccione una operación:")
label_operacion.pack()


for operacion in ['Suma', 'Resta', 'Multiplicación', 'División']:
    radio_button = tk.Radiobutton(ventana, text=operacion, variable=operacion_var, value=operacion)
    radio_button.pack()


boton_calcular = tk.Button(ventana, text="Calcular", command=calcular)
boton_calcular.pack()


boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit)
boton_salir.pack()


ventana.mainloop()