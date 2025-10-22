import tkinter as tk
from tkinter import messagebox

def dolarKeRupiah():
    try:
        angka = textbox.get()
        dollar = float(angka) * 16624
        text.set(f"RP. {dollar:,.2f}")
        label2.config(fg="#1e90ff")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")

# Window utama
window = tk.Tk()
window.title("💰 Konversi USD ke IDR 💰")
window.geometry("500x300")
window.configure(bg="#f0f4f8")

# Judul
judul = tk.Label(
    window, 
    text="Konverter Mata Uang", 
    font=("SuperCartoon", 22, "bold"), 
    bg="#f0f4f8", 
    fg="#333"
)
judul.pack(pady=10)

# Frame utama untuk isi
frame = tk.Frame(window, bg="#ffffff", bd=2, relief="groove")
frame.pack(padx=20, pady=10, fill="both", expand=True)

label1 = tk.Label(
    frame, 
    text="Masukkan jumlah USD:", 
    font=('SuperCartoon', 12, "bold"), 
    bg="#ffffff"
)
label1.pack(pady=5)

textbox = tk.Entry(
    frame, 
    font=('SuperCartoon', 15, "bold"), 
    width=12, 
    justify=tk.CENTER, 
    bg="#f9f9f9", 
    relief="solid", 
    bd=1
)
textbox.pack(pady=5)

btn = tk.Button(
    frame, 
    text="Konversi", 
    command=dolarKeRupiah, 
    font=('SuperCartoon', 12, "bold"), 
    bg="#1e90ff", 
    fg="white", 
    activebackground="#4682b4", 
    activeforeground="white", 
    relief="raised", 
    cursor="hand2"
)
btn.pack(pady=10)

text = tk.StringVar()
text.set("IDR")

label2 = tk.Label(
    frame, 
    font=('SuperCartoon', 14, "bold"), 
    textvariable=text, 
    bg="#ffffff", 
    fg="#555"
)
label2.pack(pady=5)

window.mainloop()
