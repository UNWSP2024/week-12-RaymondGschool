import tkinter as tk

window = tk.Tk()
window.title("Miles per gallon calc")
window.geometry("200x150")

def keyhandler(key):
    if not key.char in "0123456789.," and key.char != "\x08": # backspace
        return "break" # return "break" to indicate that the character should not be in the text box (delete it)

miles_label: tk.Label = tk.Label(window, text = "Miles")
miles_label.place(x = 20, y= 20)

gallons_label: tk.Label = tk.Label(window, text = "Gallons")
gallons_label.place(x = 20, y= 40)

miles_text: tk.Text = tk.Text(window, height=1, width=10)
miles_text.place(x = 70, y= 20)
miles_text.bind("<Key>", keyhandler)

gallons_text: tk.Text = tk.Text(window, height=1, width=10)
gallons_text.place(x = 70, y= 40)
gallons_text.bind("<Key>", keyhandler)

output_label: tk.Label = tk.Label(window, height=1, width=20)
output_label.place(x=20, y=85)

def commit_calculation() -> None:
    global output_label

    MPG: float = float(miles_text.get('1.0', tk.END)) / float(gallons_text.get('1.0', tk.END))
    output_label.configure(text=f"{MPG:.2f}")

calculate_button: tk.Button = tk.Button(window, text="Calculate", height=1, width=20, command=commit_calculation)
calculate_button.place(x= 20, y= 65)


window.mainloop()