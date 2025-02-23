import tkinter as tk
from tkinter import ttk, messagebox
import csv

def add_entry():
    first_name = entry_first_name.get("1.0", tk.END).strip()
    last_name = entry_last_name.get("1.0", tk.END).strip()
    email = entry_email.get("1.0", tk.END).strip()
    phone = entry_phone.get("1.0", tk.END).strip()
    address = entry_address.get("1.0", tk.END).strip()
    
    if not all([first_name, last_name, email, phone, address]):
        messagebox.showwarning("Incomplete Entry", "Please fill in all fields.")
        return
    
    with open('contacts.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([first_name, last_name, email, phone, address])
    
    print("Entry added to CSV file.")
    clear_entries()

def clear_entries():
    entry_first_name.delete("1.0", tk.END)
    entry_last_name.delete("1.0", tk.END)
    entry_email.delete("1.0", tk.END)
    entry_phone.delete("1.0", tk.END)
    entry_address.delete("1.0", tk.END)

def cancel_entry():
    clear_entries()
    print("Entry canceled.")

def search_contact(event=None):
    search_name = search_entry.get("1.0", tk.END).strip()
    if not search_name:
        messagebox.showwarning("Empty Search", "Please enter a name to search.")
        return
    
    search_entry.delete("1.0", tk.END)
    
    search_parts = search_name.split()
    search_first_name = search_parts[0]
    search_last_name = search_parts[1] if len(search_parts) > 1 else ""
    
    found = False
    with open('contacts.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            stored_first_name = row[0]
            stored_last_name = row[1]
            if (search_first_name == stored_first_name and 
                search_last_name.lower() == stored_last_name.lower()):
                details_entry.delete("1.0", tk.END)
                details_entry.insert("1.0", f"Name: {stored_first_name} {stored_last_name}\nEmail: {row[2]}\nPhone: {row[3]}\nAddress: {row[4]}")
                found = True
                break
    
    if not found:
        messagebox.showinfo("Contact Not Found", f"No contact found with name '{search_name}'.")

def clear_details():
    details_entry.delete("1.0", tk.END)

root = tk.Tk()
root.title("Contact Book")
root.resizable(False, False)

labels = ['First Name', 'Last Name', 'Email Address', 'Phone Number', 'Address']
for index, label_text in enumerate(labels):
    label = ttk.Label(root, text=label_text)
    label.grid(row=index, column=0, padx=10, pady=5, sticky=tk.W)
    
entry_first_name = tk.Text(root, width=30, height=1)
entry_first_name.grid(row=0, column=1, padx=10, pady=5)
    
entry_last_name = tk.Text(root, width=30, height=1)
entry_last_name.grid(row=1, column=1, padx=10, pady=5)
    
entry_email = tk.Text(root, width=30, height=1)
entry_email.grid(row=2, column=1, padx=10, pady=5)
    
entry_phone = tk.Text(root, width=30, height=1)
entry_phone.grid(row=3, column=1, padx=10, pady=5)
    
entry_address = tk.Text(root, width=30, height=1)
entry_address.grid(row=4, column=1, padx=10, pady=5)

button_frame = ttk.Frame(root)
button_frame.grid(row=5, column=0, columnspan=2, pady=10, sticky=tk.E)

add_button = ttk.Button(button_frame, text="Add", command=add_entry, width=18)
add_button.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)

cancel_button = ttk.Button(button_frame, text="Cancel", command=cancel_entry, width=17)
cancel_button.grid(row=0, column=1, padx=10, pady=5, sticky=tk.E)

search_label = ttk.Label(root, text="Search Contact")
search_label.grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)

search_entry = tk.Text(root, width=30, height=1)
search_entry.grid(row=6, column=1, padx=10, pady=5)
search_entry.bind("<Return>", search_contact)

details_label = ttk.Label(root, text="Contact Details")
details_label.grid(row=7, column=0, padx=10, pady=5, sticky=tk.W)

details_entry = tk.Text(root, width=30, height=5)
details_entry.grid(row=7, column=1, padx=10, pady=5)

clear_button = ttk.Button(root, text="Clear", command=clear_details, width=40)
clear_button.grid(row=8, column=1, padx=10, pady=5, sticky=tk.E)

root.mainloop()
