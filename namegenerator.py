import tkinter as tk
from tkinter import ttk, messagebox
import requests

def get_random_name(gender: str) -> str:
    try:
        response = requests.get(f"https://randomuser.me/api/?gender={gender}")
        response.raise_for_status()
        data = response.json()
        first_name = data['results'][0]['name']['first']
        last_name = data['results'][0]['name']['last']
        return f"{first_name} {last_name}"
    except requests.RequestException as e:
        return f"Error: {e}"

def generate_name():
    gender = gender_var.get()
    if gender not in ['male', 'female']:
        messagebox.showerror("Input Error", "Please select a valid gender.")
        return
    name = get_random_name(gender)
    name_label.config(text=name)

# GUI setup
root = tk.Tk()
root.title("Random Name Generator")
root.geometry("350x200")
root.resizable(False, False)

# Gender selection
gender_var = tk.StringVar()

frame = ttk.Frame(root, padding=20)
frame.pack(expand=True)

ttk.Label(frame, text="Select Gender:").pack(pady=5)
gender_combo = ttk.Combobox(frame, textvariable=gender_var, values=["male", "female"], state="readonly")
gender_combo.pack()

# Generate button
ttk.Button(frame, text="Generate Name", command=generate_name).pack(pady=10)

# Output label
name_label = ttk.Label(frame, text="", font=("Helvetica", 14))
name_label.pack(pady=10)

# Start GUI loop
root.mainloop()
