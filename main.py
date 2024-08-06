from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text="type", src="English", dest="Hindi"):
    trans = Translator()
    trans1 = trans.translate(text, src=src, dest=dest)
    return trans1.text

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    msg = Sor_txt.get(1.0, END)
    textget = change(text=msg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)

root = Tk()
root.title("Translator")
root.geometry("600x750")  # width x height
root.config(bg='#2c3e50')

# Style
style = ttk.Style()
style.theme_use('clam')
style.configure('TButton', font=('Helvetica', 14), foreground='#ffffff', background='#34495e', padding=10)
style.configure('TCombobox', font=('Helvetica', 14))
style.map('TButton', background=[('active', '#1abc9c')])

# Header Frame
header_frame = Frame(root, bg='#1abc9c', bd=5)
header_frame.place(relx=0.5, rely=0.05, relwidth=0.75, relheight=0.1, anchor='n')

lab_txt = Label(header_frame, text="Translator", font=("Helvetica", 30, "bold"), bg='#1abc9c', fg='white')
lab_txt.place(relwidth=1, relheight=1)

# Source Text Label
source_label = Label(root, text="Source Text", font=("Helvetica", 18, "bold"), bg='#2c3e50', fg='#ecf0f1')
source_label.place(relx=0.5, rely=0.16, anchor='n')

# Source Text Box
source_frame = Frame(root, bg='#ecf0f1', bd=2)
source_frame.place(relx=0.5, rely=0.2, relwidth=0.85, relheight=0.2, anchor='n')

Sor_txt = Text(source_frame, font=("Helvetica", 14), wrap=WORD, bd=0, padx=5, pady=5)
Sor_txt.place(relwidth=1, relheight=1)

# Language Selection Frame
frame = Frame(root, bg='#2c3e50')
frame.place(relx=0.5, rely=0.45, anchor='n')

list_text = list(LANGUAGES.values())

# Source Language Combobox
comb_sor = ttk.Combobox(frame, value=list_text)
comb_sor.grid(row=0, column=0, padx=10, pady=10)
comb_sor.set("english")

# Translate Button
button_change = ttk.Button(frame, text="Translate", command=data)
button_change.grid(row=0, column=1, padx=10, pady=10)

# Destination Language Combobox
comb_dest = ttk.Combobox(frame, value=list_text)
comb_dest.grid(row=0, column=2, padx=10, pady=10)
comb_dest.set("english")

# Destination Text Label
dest_label = Label(root, text="Translated Text", font=("Helvetica", 18, "bold"), bg='#2c3e50', fg='#ecf0f1')
dest_label.place(relx=0.5, rely=0.55, anchor='n')

# Destination Text Box
dest_frame = Frame(root, bg='#ecf0f1', bd=2)
dest_frame.place(relx=0.5, rely=0.6, relwidth=0.85, relheight=0.2, anchor='n')

dest_txt = Text(dest_frame, font=("Helvetica", 14), wrap=WORD, bd=0, padx=5, pady=5)
dest_txt.place(relwidth=1, relheight=1)

root.mainloop()

