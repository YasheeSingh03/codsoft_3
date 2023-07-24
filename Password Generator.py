import random
import tkinter as tk
from tkinter import font
def generate_password():
    en=int(entry1.get())
    allowed_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"

    password = ''.join(random.choice(allowed_chars)
     for i in range(en))
    pass_ent.delete(0, tk.END)
    pass_ent.insert(tk.END, password)
    
def accept():
    window.accept_clear()
    window.accept_append(pass_ent.get())
def reset():
    user_entry.delete(0,tk.END)
    entry1.delete(0,tk.END)
    pass_ent.delete(0,tk.END)

    
window = tk.Tk()
window.title("Password Generator")
p=tk.Label(window,text="Password generator",fg="blue",font=("Arial", 12, "bold"))

custom_font = font.Font(p,p.cget("font"))
custom_font.configure(underline=True, size=10)

p.configure(font=custom_font)

p.grid(row=0,column=1)

user_name=tk.Label(window,text="Enter user name:")
user_entry=tk.Entry(window)
user_name.grid(row=4,column=0,padx=10,pady=5)
user_entry.grid(row=4,column=1)
pass_len=tk.Label(window,text="Password length:")
entry1=tk.Entry(window)

pass_len.grid(row=5,column=0,padx=10,pady=5)
entry1.grid(row=5,column=1)
pass_label = tk.Label(window, text="Generate Password:")
pass_ent = tk.Entry(window)
pass_label.grid(row=6,column=0,padx=10,pady=5)
pass_ent.grid(row=6 ,column=1)

gen_pass = tk.Button(window, text="Generate",fg="white",bg="blue", command=generate_password)
gen_pass.grid(row=7,column=1,sticky="nsew",padx=12,pady=6)

accept=tk.Button(window,text="Accept",command=accept)
accept.grid(row=8,column=1,sticky="nsew",padx=14,pady=6)
reset=tk.Button(window,text="Reset",command=reset)
reset.grid(row=9,column=1,sticky="nsew",padx=18,pady=6)
window.mainloop()