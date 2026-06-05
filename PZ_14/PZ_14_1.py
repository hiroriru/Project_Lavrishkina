'''
В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
приближенный к оригиналу.
'''
import tkinter as tk

def register():
    print("Registration submitted!")

root = tk.Tk()
root.title("Event Registration Form")
root.geometry("600x550") 
root.resizable(False, False)

form_frame = tk.Frame(root, bg="white", bd=1, relief="solid")
form_frame.pack(padx=40, pady=20)  

header = tk.Label(form_frame, text="EVENT REGISTRATION FORM",
                  bg="black", fg="white", font=("Arial", 16, "bold"), pady=12)
header.pack(fill="x")

content = tk.Frame(form_frame, bg="white")
content.pack(padx=20, pady=10) 

ENTRY_WIDTH = 40 

row = 0

tk.Label(content, text="Name", bg="white", font=("Arial", 10)).grid(row=row, column=0, sticky="w", pady=(10, 5))

first_entry = tk.Entry(content, width=ENTRY_WIDTH//2-1, font=("Arial", 10), bg="#f0f0f0", bd=1)
first_entry.grid(row=row, column=1, padx=(0, 5), pady=5)
tk.Label(content, text="First Name", bg="white", font=("Arial", 8), fg="#777").grid(row=row+1, column=1, sticky="w")

last_entry = tk.Entry(content, width=ENTRY_WIDTH//2 - 1, font=("Arial", 10), bg="#f0f0f0", bd=1)
last_entry.grid(row=row, column=2, pady=5)
tk.Label(content, text="Last Name", bg="white", font=("Arial", 8), fg="#777").grid(row=row+1, column=2, sticky="w")

row += 2
tk.Label(content, text="Company", bg="white", font=("Arial", 10)).grid(row=row, column=0, sticky="w", pady=(10, 5))
company_entry = tk.Entry(content, width=ENTRY_WIDTH+2, font=("Arial", 10), bg="#f0f0f0", bd=1)
company_entry.grid(row=row, column=1, columnspan=2, pady=5)

row += 1
tk.Label(content, text="Email", bg="white", font=("Arial", 10)).grid(row=row, column=0, sticky="w", pady=(10, 5))
email_entry = tk.Entry(content, width=ENTRY_WIDTH+2, font=("Arial", 10), bg="#f0f0f0", bd=1)
email_entry.grid(row=row, column=1, columnspan=2, pady=5)

row += 1
tk.Label(content, text="Phone", bg="white", font=("Arial", 10)).grid(row=row, column=0, sticky="w", pady=(10, 5))

area_entry = tk.Entry(content, width=ENTRY_WIDTH//2-1, font=("Arial", 10), bg="#f0f0f0", bd=1)
area_entry.grid(row=row, column=1, padx=(0, 5), pady=5)
tk.Label(content, text="Area Code", bg="white", font=("Arial", 8), fg="#777").grid(row=row+1, column=1, sticky="w")

phone_entry = tk.Entry(content, width=ENTRY_WIDTH//2-1, font=("Arial", 10), bg="#f0f0f0", bd=1)
phone_entry.grid(row=row, column=2, pady=5)
tk.Label(content, text="Phone Number", bg="white", font=("Arial", 8), fg="#777").grid(row=row+1, column=2, sticky="w")

row += 2
tk.Label(content, text="Subject", bg="white", font=("Arial", 10)).grid(row=row, column=0, sticky="w", pady=(10, 5))
subject_var = tk.StringVar(value="Choose option")
subject_menu = tk.OptionMenu(content, subject_var,
                              "Choose option",
                              "General Inquiry",
                              "Technical Support",
                              "Sales",
                              "Other")
subject_menu.config(width=ENTRY_WIDTH, font=("Arial", 10), bg="#f0f0f0", bd=1, anchor="w")
subject_menu["menu"].config(font=("Arial", 10), bg="white", bd=1)
subject_menu.grid(row=row, column=1, columnspan=2, pady=5)

row += 1
tk.Label(content, text="Are you an existing customer?", bg="white", font=("Arial", 10)).grid(
    row=row, column=0, columnspan=3, sticky="w", pady=(20, 10))

existing_var = tk.StringVar(value="Yes")
yes_rb = tk.Radiobutton(content, text="Yes", variable=existing_var, value="Yes",
                        bg="white", font=("Arial", 10), indicatoron=1)
no_rb = tk.Radiobutton(content, text="No", variable=existing_var, value="No",
                       bg="white", font=("Arial", 10), indicatoron=1)
yes_rb.grid(row=row+1, column=1, sticky="w")
no_rb.grid(row=row+1, column=2, sticky="w")

row += 2
register_btn = tk.Button(content, text="REGISTER", command=register,
                         bg="#e74c3c", fg="white", font=("Arial", 11, "bold"),
                         width=16, height=2, bd=1, relief="raised")
register_btn.grid(row=row, column=0, sticky="w", pady=(25, 10))  # ← только слева, без columnspan

content.grid_columnconfigure(1, minsize=0)
content.grid_columnconfigure(2, minsize=0)

def on_closing():
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()