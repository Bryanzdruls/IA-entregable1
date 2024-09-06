import clips
import tkinter as tk
from tkinter import messagebox

# Crear el entorno de CLIPS
sistemaExperto = clips.Environment()
sistemaExperto.clear()

# Definir reglas para diagnóstico médico
reglaFiebre = """
(defrule reglaFiebre
    (fiebre)
    =>
    (assert (accion tomarParacetamol))
    (printout t "Se recomienda tomar Paracetamol para reducir la fiebre." crlf)
)
"""

reglaTos = """
(defrule reglaTos
    (tos)
    =>
    (assert (accion tomarJarabe))
    (printout t "Se recomienda tomar jarabe para aliviar la tos." crlf)
)
"""

reglaDolorGarganta = """
(defrule reglaDolorGarganta
    (dolorGarganta)
    =>
    (assert (accion hacerGargaras))
    (printout t "Se recomienda hacer gárgaras con agua salada para aliviar el dolor de garganta." crlf)
)
"""

# Cargar reglas en el entorno de CLIPS
sistemaExperto.build(reglaFiebre)
sistemaExperto.build(reglaTos)
sistemaExperto.build(reglaDolorGarganta)

# Función para ejecutar el sistema experto basado en el síntoma ingresado
def diagnosticar():
    sintoma = sintoma_var.get().strip().lower()
    if sintoma in ["fiebre", "tos", "dolorgarganta"]:
        sistemaExperto.assert_string(f"({sintoma})")
        sistemaExperto.run()
        
        acciones = []
        for fact in sistemaExperto.facts():
            factString = str(fact)
            if "tomarParacetamol" in factString:
                acciones.append("Tomar Paracetamol para reducir la fiebre.")
            if "tomarJarabe" in factString:
                acciones.append("Tomar jarabe para la tos.")
            if "hacerGargaras" in factString:
                acciones.append("Hacer gárgaras con agua salada para aliviar el dolor de garganta.")
        
        if acciones:
            messagebox.showinfo("Recomendaciones", "\n".join(acciones))
        else:
            messagebox.showinfo("Recomendaciones", "No se encontraron acciones recomendadas para el síntoma.")
    else:
        messagebox.showwarning("Error", "Síntoma no reconocido. Por favor, ingrese 'fiebre', 'tos' o 'dolorGarganta'.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Sistema Experto de Diagnóstico Médico")

# Variables y widgets
sintoma_var = tk.StringVar()

tk.Label(ventana, text="Ingrese un síntoma (fiebre, tos, dolorGarganta):").pack(pady=10)
tk.Entry(ventana, textvariable=sintoma_var).pack(pady=5)
tk.Button(ventana, text="Diagnosticar", command=diagnosticar).pack(pady=10)

# Iniciar la interfaz gráfica
ventana.mainloop()
