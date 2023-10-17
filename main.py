import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import threading
import subprocess
from ttkthemes import ThemedTk

def calculate_bmi(height, weight):
    height_in_meters = height / 100
    bmi = weight / (height_in_meters * height_in_meters)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Untergewicht"
    elif 18.5 <= bmi < 24.9:
        return "Normalgewicht"
    elif 25 <= bmi < 29.9:
        return "Übergewicht"
    else:
        return "Adipositas"

def calculate_button_clicked():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())
    except ValueError:
        messagebox.showerror("Fehler", "Bitte geben Sie gültige Werte ein.")
        return
    result_label.config(text="Berechnung läuft...")
    calculate_bmi_thread = threading.Thread(target=calculate_bmi_background, args=(height, weight))
    calculate_bmi_thread.start()

def calculate_bmi_background(height, weight):
    try:
        subprocess.call(['pip', 'install', 'tk']) 
        bmi_result = calculate_bmi(height, weight)
        interpretation = interpret_bmi(bmi_result)
        result_label.config(text=f"Ihr BMI beträgt: {bmi_result:.2f}\nInterpretation: {interpretation}")
    except Exception as e:
        result_label.config(text="Fehler bei der Berechnung.")

root = ThemedTk(theme="radiance")
root.title("BMI-Rechner")

frame = ttk.Frame(root)
frame.pack(padx=20, pady=20)

height_label = ttk.Label(frame, text="Größe (in cm):")
height_label.grid(row=0, column=0, padx=10, pady=10)
height_entry = ttk.Entry(frame)
height_entry.grid(row=0, column=1, padx=10, pady=10)

weight_label = ttk.Label(frame, text="Gewicht (in kg):")
weight_label.grid(row=1, column=0, padx=10, pady=10)
weight_entry = ttk.Entry(frame)
weight_entry.grid(row=1, column=1, padx=10, pady=10)

calculate_button = ttk.Button(frame, text="BMI berechnen", command=calculate_button_clicked)
calculate_button.grid(row=2, column=0, columnspan=2, pady=20)

result_label = ttk.Label(frame, text="", wraplength=300, anchor="center")
result_label.grid(row=3, column=0, columnspan=2)

root.mainloop()
