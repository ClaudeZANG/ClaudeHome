# Q1
import tkinter as tk

def show_info():
    label.config(text="Your Name\n123 Main St\nAnytown, USA")

window = tk.Tk()
window.title("Name and Address")

label = tk.Label(window, text="")
label.pack(pady=10)

show_button = tk.Button(window, text="Show Info", command=show_info)
show_button.pack(pady=10)

window.mainloop()



# Q2
import tkinter as tk

def translate(word):
    translations = {
        "sinister": "left",
        "dexter": "right",
        "medium": "center"
    }
    label.config(text=translations[word])

window = tk.Tk()
window.title("Latin Translator")

label = tk.Label(window, text="")
label.pack(pady=10)

for latin_word in ["sinister", "dexter", "medium"]:
    button = tk.Button(window, text=latin_word.capitalize(), command=lambda w=latin_word: translate(w))
    button.pack(pady=5)

window.mainloop()



# Q3
import tkinter as tk

def calculate_mpg():
    miles = float(miles_entry.get())
    gallons = float(gallons_entry.get())
    mpg = miles / gallons
    result_label.config(text=f"MPG: {mpg:.2f}")

window = tk.Tk()
window.title("MPG Calculator")

miles_label = tk.Label(window, text="Enter miles:")
miles_label.pack()
miles_entry = tk.Entry(window)
miles_entry.pack()

gallons_label = tk.Label(window, text="Enter gallons:")
gallons_label.pack()
gallons_entry = tk.Entry(window)
gallons_entry.pack()

calculate_button = tk.Button(window, text="Calculate MPG", command=calculate_mpg)
calculate_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()




# Q4
import tkinter as tk

def convert_temperature():
    celsius = float(celsius_entry.get())
    fahrenheit = 9/5 * celsius + 32
    result_label.config(text=f"Fahrenheit: {fahrenheit:.2f}")

window = tk.Tk()
window.title("Celsius to Fahrenheit")

celsius_label = tk.Label(window, text="Enter Celsius:")
celsius_label.pack()
celsius_entry = tk.Entry(window)
celsius_entry.pack()

convert_button = tk.Button(window, text="Convert", command=convert_temperature)
convert_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()



# Q5
import tkinter as tk

def calculate_tax():
    actual_value = float(value_entry.get())
    assessment_value = actual_value * 0.60
    property_tax = assessment_value / 100 * 0.75
    result_label.config(text=f"Assessment Value: ${assessment_value:.2f}\nProperty Tax: ${property_tax:.2f}")

window = tk.Tk()
window.title("Property Tax Calculator")

value_label = tk.Label(window, text="Enter property value:")
value_label.pack()
value_entry = tk.Entry(window)
value_entry.pack()

calculate_button = tk.Button(window, text="Calculate", command=calculate_tax)
calculate_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()



# Q6
import tkinter as tk

def calculate_total():
    total = 0
    if oil_change_var.get():
        total += 30
    if lube_job_var.get():
        total += 20
    if radiator_flush_var.get():
        total += 40
    if transmission_flush_var.get():
        total += 100
    if inspection_var.get():
        total += 35
    if muffler_var.get():
        total += 200
    if tire_rotation_var.get():
        total += 20
    total_label.config(text=f"Total: ${total:.2f}")

window = tk.Tk()
window.title("Joe's Automotive")

# Define variables for each service
oil_change_var = tk.BooleanVar()
lube_job_var = tk.BooleanVar()
radiator_flush_var = tk.BooleanVar()
transmission_flush_var = tk.BooleanVar()
inspection_var = tk.BooleanVar()
muffler_var = tk.BooleanVar()
tire_rotation_var = tk.BooleanVar()

# Create check buttons for each service
services = [
    ("Oil change", oil_change_var),
    ("Lube job", lube_job_var),
    ("Radiator flush", radiator_flush_var),
    ("Transmission flush", transmission_flush_var),
    ("Inspection", inspection_var),
    ("Muffler replacement", muffler_var),
    ("Tire rotation", tire_rotation_var)
]

for service, var in services:
    tk.Checkbutton(window, text=service, variable=var).pack()

# Create calculate button
calculate_button = tk.Button(window, text="Calculate Total", command=calculate_total)
calculate_button.pack()

# Create label to display total
total_label = tk.Label(window, text="")
total_label.pack()

window.mainloop()



# Q7
import tkinter as tk
from tkinter import messagebox

def calculate_charge():
    rate = rate_var.get()
    minutes = float(minutes_entry.get())
    if rate == "Daytime":
        charge = minutes * 0.07
    elif rate == "Evening":
        charge = minutes * 0.12
    else:
        charge = minutes * 0.05
    messagebox.showinfo("Charge", f"Total charge: ${charge:.2f}")

window = tk.Tk()
window.title("Long-Distance Call Calculator")

# Create radio buttons for rate categories
rate_var = tk.StringVar(value="Daytime")
rates = [("Daytime", "Daytime"), ("Evening", "Evening"), ("Off-Peak", "Off-Peak")]
for text, mode in rates:
    tk.Radiobutton(window, text=text, variable=rate_var, value=mode).pack()

# Create entry for minutes
minutes_label = tk.Label(window, text="Enter minutes:")
minutes_label.pack()
minutes_entry = tk.Entry(window)
minutes_entry.pack()

# Create button to calculate charge
calculate_button = tk.Button(window, text="Calculate Charge", command=calculate_charge)
calculate_button.pack()

window.mainloop()



# Q8
import tkinter as tk

def draw_house():
    canvas.create_rectangle(50, 150, 250, 300, fill="tan")  # House body
    canvas.create_polygon(50, 150, 150, 50, 250, 150, fill="brown")  # Roof
    canvas.create_rectangle(90, 200, 130, 300, fill="white")  # Door
    canvas.create_rectangle(170, 200, 210, 240, fill="lightblue")  # Window
    canvas.create_rectangle(170, 260, 210, 300, fill="lightblue")  # Window

window = tk.Tk()
window.title("This Old House")

canvas = tk.Canvas(window, width=300, height=400)
canvas.pack()

draw_button = tk.Button(window, text="Draw House", command=draw_house)
draw_button.pack()

window.mainloop()


# Q9
import tkinter as tk

def draw_tree_rings(canvas, center_x, center_y, number_of_rings):
    for i in range(1, number_of_rings + 1):
        radius = 10 * i
        canvas.create_oval(center_x - radius, center_y - radius,
                           center_x + radius, center_y + radius)
        canvas.create_text(center_x, center_y - radius, text=str(i))

def main():
    window = tk.Tk()
    window.title("Tree Age Rings")

    canvas = tk.Canvas(window, width=400, height=400)
    canvas.pack()

    draw_tree_rings(canvas, 200, 200, 5)  # Draw 5 rings for a 5-year-old tree

    window.mainloop()

if __name__ == "__main__":
    main()


# Q10
import tkinter as tk

def draw_star(canvas):
    # Draw the star
    canvas.create_polygon(200, 50, 150, 150, 50, 150,
                          120, 200, 80, 300, 200, 240,
                          320, 300, 280, 200, 350, 150,
                          250, 150, fill="gold", outline="black")
    # Add name
    canvas.create_text(200, 260, text="Your Name", font=("Arial", 14, "bold"))

def main():
    window = tk.Tk()
    window.title("Hollywood Star")

    canvas = tk.Canvas(window, width=400, height=400)
    canvas.pack()

    draw_star(canvas)

    window.mainloop()

if __name__ == "__main__":
    main()



# Q11
import tkinter as tk

def draw_vehicle(canvas):
    # Draw the body of the car
    canvas.create_rectangle(100, 150, 300, 200, fill="blue", outline="black")
    # Draw the roof of the car
    canvas.create_polygon(120, 150, 150, 100, 250, 100, 280, 150, fill="blue", outline="black")
    # Draw the wheels
    canvas.create_oval(130, 200, 160, 230, fill="black")
    canvas.create_oval(240, 200, 270, 230, fill="black")

def main():
    window = tk.Tk()
    window.title("Vehicle Outline")

    canvas = tk.Canvas(window, width=400, height=300)
    canvas.pack()

    draw_vehicle(canvas)

    window.mainloop()

if __name__ == "__main__":
    main()



# Q12
import tkinter as tk

def draw_solar_system(canvas):
    # Draw the sun
    canvas.create_oval(180, 180, 220, 220, fill="yellow", outline="orange")
    canvas.create_text(200, 160, text="Sun", fill="black")

    # Draw the planets
    planets = [
        ("Mercury", 240, "gray"),
        ("Venus", 280, "orange"),
        ("Earth", 320, "blue"),
        ("Mars", 360, "red"),
        ("Jupiter", 400, "brown"),
        ("Saturn", 440, "yellow"),
        ("Uranus", 480, "lightblue"),
        ("Neptune", 520, "blue"),
        ("Pluto", 560, "darkgray")
    ]

    for name, distance, color in planets:
        canvas.create_oval(200 - distance // 10, 200 - distance // 10,
                           200 + distance // 10, 200 + distance // 10,
                           outline=color)
        canvas.create_text(200 + distance // 10, 200, text=name, fill="black")

def main():
    window = tk.Tk()
    window.title("Solar System")

    canvas = tk.Canvas(window, width=800, height=600, bg="black")
    canvas.pack()

    draw_solar_system(canvas)

    window.mainloop()

if __name__ == "__main__":
    main()







