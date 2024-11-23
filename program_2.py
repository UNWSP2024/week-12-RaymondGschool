import tkinter as tk
from tkinter import messagebox

service_prices = {
    'Oil Change': 30.00,
    'Lube Job': 20.00,
    'Radiator Flush': 40.00,
    'Transmission Fluid': 100.00,
    'Inspection': 35.00,
    'Muffler Replacement': 200.00,
    'Tire Rotation': 20.00
}

def calculate_total():
    total = 0
    selected_services = []

    for service, var in check_vars.items():
        if var.get():
            selected_services.append(service)
            total += service_prices[service]
    
    total_label.config(text=f"Total: ${total:.2f}")
    selected_services_label.config(text="Selected Services: " + ", ".join(selected_services))

window = tk.Tk()
window.title("Joe's Automotive - Service Selection")
window.geometry("700x250")

check_vars = {}

for service in service_prices:
    check_vars[service] = tk.IntVar()
    checkbutton = tk.Checkbutton(window, text=service, variable=check_vars[service], command=calculate_total)
    checkbutton.pack(anchor='w')

total_label = tk.Label(window, text="Total: $0.00")
total_label.pack(pady=10)

selected_services_label = tk.Label(window, text="Selected Services: None")
selected_services_label.pack(pady=10)

window.mainloop()