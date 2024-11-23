import tkinter as tk
from tkinter import messagebox

rates = {
    'Daytime': 0.02,    # 6 AM -> 5:59 PM
    'Evening': 0.12,    # 6 PM -> 11:59 PM
    'Off-Peak': 0.05    # midnight -> 5:59 AM
}

def calculate_charge():
    selected_rate_category = rate_var.get()
    
    try:
        minutes = float(minutes_entry.get())
        if minutes < 0:
            raise ValueError("Minutes cannot be negative.")
    except ValueError as e:
        messagebox.showerror("Input Error", "Please enter a valid number of minutes.")
        return
    
    rate_per_minute = rates[selected_rate_category]
    total_charge = minutes * rate_per_minute
    
    messagebox.showinfo("Charge Info", f"The charge for {minutes} minute(s) during {selected_rate_category} is ${total_charge:.2f}")

window = tk.Tk()
window.title("Telephone Call Charge Calculator")

rate_var = tk.StringVar(value='Daytime')

daytime_radio = tk.Radiobutton(window, text="Daytime (6:00 AM - 5:59 PM):  $0.02/min", variable=rate_var, value='Daytime')
evening_radio = tk.Radiobutton(window, text="Evening (6:00 PM - 11:59 PM):  $0.12/min", variable=rate_var, value='Evening')
offpeak_radio = tk.Radiobutton(window, text="Off-Peak (Midnight - 5:59 AM):  $0.05/min", variable=rate_var, value='Off-Peak')

daytime_radio.pack(anchor='w')
evening_radio.pack(anchor='w')
offpeak_radio.pack(anchor='w')

minutes_label = tk.Label(window, text="Enter the number of minutes:")
minutes_label.pack(pady=5)

minutes_entry = tk.Entry(window)
minutes_entry.pack(pady=5)

calculate_button = tk.Button(window, text="Calculate Charge", command=calculate_charge)
calculate_button.pack(pady=20)

window.mainloop()
