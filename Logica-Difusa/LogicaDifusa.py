import numpy as np
import skfuzzy as fuzz
from skfuzzy.control import Antecedent, Consequent, Rule, ControlSystem, ControlSystemSimulation
import tkinter as tk
from tkinter import ttk

# Definir las variables difusas
color = Antecedent(np.arange(0, 11, 1), 'color')
simetria = Antecedent(np.arange(0, 11, 1), 'simetria')
belleza = Consequent(np.arange(0, 101, 1), 'belleza')

# Definir los conjuntos difusos
color['palido'] = fuzz.trapmf(color.universe, [0, 0, 3, 5])
color['moderado'] = fuzz.trimf(color.universe, [3, 5, 7])
color['vibrante'] = fuzz.trapmf(color.universe, [5, 7, 10, 10])

simetria['baja'] = fuzz.trapmf(simetria.universe, [0, 0, 3, 5])
simetria['media'] = fuzz.trimf(simetria.universe, [3, 5, 7])
simetria['alta'] = fuzz.trapmf(simetria.universe, [5, 7, 10, 10])

belleza['poca'] = fuzz.trapmf(belleza.universe, [0, 0, 20, 40])
belleza['moderada'] = fuzz.trimf(belleza.universe, [30, 50, 70])
belleza['mucha'] = fuzz.trapmf(belleza.universe, [60, 80, 100, 100])

# Definir las reglas difusas
regla1 = Rule(color['vibrante'] & simetria['alta'], belleza['mucha'])
regla2 = Rule(color['vibrante'] & simetria['media'], belleza['moderada'])
regla3 = Rule(color['moderado'] & simetria['alta'], belleza['moderada'])
regla4 = Rule(color['palido'] | simetria['baja'], belleza['poca'])

# Crear el sistema de control difuso
control_belleza = ControlSystem([regla1, regla2, regla3, regla4])
simulacion_belleza = ControlSystemSimulation(control_belleza)

# Función para calcular la belleza
def calcular_belleza():
    try:
        # Obtener los valores de las entradas de texto
        valor_color = float(color_entry.get())
        valor_simetria = float(simetria_entry.get())

        # Verificar que los valores estén dentro del rango permitido
        if not (0 <= valor_color <= 10 and 0 <= valor_simetria <= 10):
            resultado_label.config(text="Error: Los valores deben estar entre 0 y 10.")
            return

        # Asignar valores de entrada a la simulación
        simulacion_belleza.input['color'] = valor_color
        simulacion_belleza.input['simetria'] = valor_simetria
        simulacion_belleza.compute()

        # Mostrar el resultado
        resultado = simulacion_belleza.output['belleza']
        resultado_label.config(text=f"Grado de belleza: {resultado:.2f}%")

    except ValueError:
        resultado_label.config(text="Error: Por favor, ingrese valores numéricos válidos.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Evaluador de Belleza Difusa")

# Crear entradas de texto y etiquetas para ingresar los valores
color_label = ttk.Label(ventana, text="Color (0: Pálido, 10: Vibrante):")
color_label.pack()
color_entry = ttk.Entry(ventana)
color_entry.pack()

simetria_label = ttk.Label(ventana, text="Simetría (0: Baja, 10: Alta):")
simetria_label.pack()
simetria_entry = ttk.Entry(ventana)
simetria_entry.pack()

# Botón para calcular la belleza
calcular_button = ttk.Button(ventana, text="Calcular Belleza", command=calcular_belleza)
calcular_button.pack()

# Etiqueta para mostrar el resultado
resultado_label = ttk.Label(ventana, text="Grado de belleza: ")
resultado_label.pack()

# Ejecutar la ventana principal
ventana.mainloop()
