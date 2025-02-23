import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calculate_bmi(weight, height):
    """Calculates the Body Mass Index (BMI) based on weight and height."""
    return weight / (height ** 2)

def get_bmi_category(bmi):
    """Determines the BMI category based on the BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal Weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def calculate():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight_unit_var.get() == "lbs":
            weight *= 0.453592
        if height_unit_var.get() == "feet":
            height *= 0.3048

        bmi = calculate_bmi(weight, height)
        bmi_category = get_bmi_category(bmi)

        bmi_label.config(text=f"BMI: {bmi:.2f}")
        category_label.config(text=f"Category: {bmi_category}")

        weight_range = get_weight_range(height)
        height_range = get_height_range(weight)

        weight_range_label.config(text=f"Suggested Weight Range: {weight_range[0]:.2f} - {weight_range[1]:.2f} kg")
        height_range_label.config(text=f"Suggested Height Range: {height_range[0]:.2f} - {height_range[1]:.2f} feet")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numerical values for weight and height.")

def get_weight_range(height):
    """Provides a suggested weight range based on the height."""
    lower_limit = 18.5 * (height ** 2)
    upper_limit = 24.9 * (height ** 2)
    return lower_limit, upper_limit

def get_height_range(weight):
    """Provides a suggested height range based on the weight."""
    lower_limit = (weight / 24.9) ** 0.5
    upper_limit = (weight / 18.5) ** 0.5
    lower_limit_in_feet = lower_limit / 0.3048
    upper_limit_in_feet = upper_limit / 0.3048
    return lower_limit_in_feet, upper_limit_in_feet

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("500x200")
root.configure(bg="#f0f0f0")

style = ttk.Style()
style.configure('TButton', background='#4CAF50')
style.map('TButton', background=[('active', '#43A047')])

main_frame = ttk.Frame(root, padding="20")
main_frame.pack(expand=True, fill="both")

weight_label = ttk.Label(main_frame, text="Weight:", font=("Helvetica", 12))
weight_label.grid(row=0, column=0, sticky="w")

weight_entry = ttk.Entry(main_frame)
weight_entry.grid(row=0, column=1)

weight_unit_var = tk.StringVar(value="kgs")
weight_unit_combo = ttk.Combobox(main_frame, textvariable=weight_unit_var, values=("kgs", "lbs"), state="readonly", width=5)
weight_unit_combo.grid(row=0, column=2, padx=5)

height_label = ttk.Label(main_frame, text="Height:", font=("Helvetica", 12))
height_label.grid(row=1, column=0, sticky="w")

height_entry = ttk.Entry(main_frame)
height_entry.grid(row=1, column=1)

height_unit_var = tk.StringVar(value="feet")
height_unit_combo = ttk.Combobox(main_frame, textvariable=height_unit_var, values=("meters", "feet"), state="readonly", width=5)
height_unit_combo.grid(row=1, column=2, padx=5)

calculate_button = ttk.Button(main_frame, text="Calculate", command=calculate, style='TButton')
calculate_button.grid(row=2, column=0, columnspan=3, pady=10)

bmi_label = ttk.Label(main_frame, text="BMI: ", font=("Helvetica", 12))
bmi_label.grid(row=3, column=0, sticky="w")

category_label = ttk.Label(main_frame, text="Category: ", font=("Helvetica", 12))
category_label.grid(row=4, column=0, sticky="w")

weight_range_label = ttk.Label(main_frame, text="Suggested Weight Range: ", font=("Helvetica", 12))
weight_range_label.grid(row=5, column=0, sticky="w")

height_range_label = ttk.Label(main_frame, text="Suggested Height Range: ", font=("Helvetica", 12))
height_range_label.grid(row=6, column=0, sticky="w")

root.mainloop()
