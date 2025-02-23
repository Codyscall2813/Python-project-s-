import tkinter as tk
from tkinter import messagebox
import random
import os

class BillApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = "#abbd9a"
        
        # Title
        title = tk.Label(self.root, text="Billing Software", font=('Roboto', 30, 'bold'), pady=2, bd=12, bg=bg_color, fg="Black", relief=tk.GROOVE)
        title.pack(fill=tk.X)
        
        # Variables
        self.initialize_variables()
        
        # Customer Details
        self.create_customer_details_frame(bg_color)
        
        # Product Frames
        self.create_product_frame("Medical Purpose", bg_color, 5, 180, self.medical_items)
        self.create_product_frame("Grocery Items", bg_color, 340, 180, self.grocery_items)
        self.create_product_frame("Cold Drinks", bg_color, 670, 180, self.cold_drinks_items)
        
        # Bill Area
        self.create_bill_area_frame()
        
        # Button Frame
        self.create_button_frame(bg_color)
        
        self.welcome_bill()

    def initialize_variables(self):
        # Product variables
        self.medical_items = {
            "Sanitizer": tk.IntVar(),
            "Mask": tk.IntVar(),
            "Hand Gloves": tk.IntVar(),
            "Dettol": tk.IntVar(),
            "Newsprin": tk.IntVar(),
            "Thermal Gun": tk.IntVar(),
        }
        
        self.grocery_items = {
            "Rice": tk.IntVar(),
            "Food Oil": tk.IntVar(),
            "Wheat": tk.IntVar(),
            "Daal": tk.IntVar(),
            "Flour": tk.IntVar(),
            "Maggi": tk.IntVar(),
        }
        
        self.cold_drinks_items = {
            "Sprite": tk.IntVar(),
            "Limka": tk.IntVar(),
            "Mazza": tk.IntVar(),
            "Coke": tk.IntVar(),
            "Fanta": tk.IntVar(),
            "Mountain Duo": tk.IntVar(),
        }
        
        # Total product price and taxes
        self.medical_price = tk.StringVar()
        self.grocery_price = tk.StringVar()
        self.cold_drinks_price = tk.StringVar()
        self.medical_tax = tk.StringVar()
        self.grocery_tax = tk.StringVar()
        self.cold_drinks_tax = tk.StringVar()
        
        # Customer details
        self.c_name = tk.StringVar()
        self.c_phone = tk.StringVar()
        self.bill_no = tk.StringVar()
        self.bill_no.set(str(random.randint(1000, 9999)))
        self.search_bill = tk.StringVar()

    def create_customer_details_frame(self, bg_color):
        F1 = tk.LabelFrame(self.root, text="Customer Details", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)
        
        customer_details = [
            ("Customer Name:", self.c_name),
            ("Customer Phone:", self.c_phone),
            ("Bill Number:", self.search_bill)
        ]
        
        for i, (label, variable) in enumerate(customer_details):
            tk.Label(F1, text=label, bg=bg_color, font=('times new roman', 15, 'bold')).grid(row=0, column=i*2, padx=20, pady=5)
            tk.Entry(F1, width=15, textvariable=variable, font='arial 15', bd=7, relief=tk.GROOVE).grid(row=0, column=i*2+1, pady=5, padx=10)
        
        tk.Button(F1, text="Search", command=self.find_bill, width=10, bd=7, font=('arial', 12, 'bold'), relief=tk.GROOVE).grid(row=0, column=6, pady=5, padx=10)

    def create_product_frame(self, title, bg_color, x, y, items):
        F = tk.LabelFrame(self.root, text=title, font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg=bg_color)
        F.place(x=x, y=y, width=325, height=380)
        
        for i, (item, variable) in enumerate(items.items()):
            tk.Label(F, text=item, font=('times new roman', 16, 'bold'), bg=bg_color, fg="black").grid(row=i, column=0, padx=10, pady=10, sticky='W')
            tk.Entry(F, width=10, textvariable=variable, font=('times new roman', 16, 'bold'), bd=5, relief=tk.GROOVE).grid(row=i, column=1, padx=10, pady=10)

    def create_bill_area_frame(self):
        F5 = tk.Frame(self.root, bd=10, relief=tk.GROOVE)
        F5.place(x=1010, y=180, width=350, height=380)
        
        tk.Label(F5, text="Bill Area", font='arial 15 bold', bd=7, relief=tk.GROOVE).pack(fill=tk.X)
        scroll_y = tk.Scrollbar(F5, orient=tk.VERTICAL)
        self.txtarea = tk.Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=tk.BOTH, expand=1)

    def create_button_frame(self, bg_color):
        F6 = tk.LabelFrame(self.root, text="Bill Area", font=('times new roman', 14, 'bold'), bd=10, fg="Black", bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)
        
        labels = [
            ("Total Medical Price", self.medical_price),
            ("Total Grocery Price", self.grocery_price),
            ("Total Cold Drinks Price", self.cold_drinks_price),
            ("Medical Tax", self.medical_tax),
            ("Grocery Tax", self.grocery_tax),
            ("Cold Drinks Tax", self.cold_drinks_tax),
        ]
        
        for i, (label, variable) in enumerate(labels):
            tk.Label(F6, text=label, font=('times new roman', 14, 'bold'), bg=bg_color, fg="black").grid(row=i % 3, column=(i // 3) * 2, padx=20, pady=1, sticky='W')
            tk.Entry(F6, width=18, textvariable=variable, font='arial 10 bold', bd=7, relief=tk.GROOVE).grid(row=i % 3, column=(i // 3) * 2 + 1, padx=18, pady=1)
        
        btn_f = tk.Frame(F6, bd=7, relief=tk.GROOVE)
        btn_f.place(x=760, width=580, height=105)
        
        buttons = [
            ("Total", self.total),
            ("Generate Bill", self.bill_area),
            ("Clear", self.clear_data),
            ("Exit", self.exit_app)
        ]
        
        for i, (label, command) in enumerate(buttons):
            tk.Button(btn_f, text=label, command=command, bg="#535C68", bd=2, fg="white", pady=15, width=12, font='arial 13 bold').grid(row=0, column=i, padx=5, pady=5)

    def total(self):
        self.calculate_total(self.medical_items, self.medical_price, self.medical_tax, 0.05)
        self.calculate_total(self.grocery_items, self.grocery_price, self.grocery_tax, 0.05)
        self.calculate_total(self.cold_drinks_items, self.cold_drinks_price, self.cold_drinks_tax, 0.1)
        self.total_bill = float(self.medical_price.get().split()[-1]) + float(self.grocery_price.get().split()[-1]) + float(self.cold_drinks_price.get().split()[-1]) + \
                          float(self.medical_tax.get().split()[-1]) + float(self.grocery_tax.get().split()[-1]) + float(self.cold_drinks_tax.get().split()[-1])

    def calculate_total(self, items, price_var, tax_var, tax_rate):
        total_price = sum(var.get() * price for var, price in zip(items.values(), [2, 5, 12, 30, 5, 15]))
        price_var.set(f"Rs. {total_price:.2f}")
        tax_var.set(f"Rs. {total_price * tax_rate:.2f}")

    def welcome_bill(self):
        self.txtarea.delete('1.0', tk.END)
        self.txtarea.insert(tk.END, "\tWelcome to Baban Kirana Store\n")
        self.txtarea.insert(tk.END, f"Bill Number: {self.bill_no.get()}\n")
        self.txtarea.insert(tk.END, f"Customer Name: {self.c_name.get()}\n")
        self.txtarea.insert(tk.END, f"Phone Number: {self.c_phone.get()}\n")
        self.txtarea.insert(tk.END, "=====================================\n")
        self.txtarea.insert(tk.END, "Products\t\tQTY\t\tPrice\n")
        self.txtarea.insert(tk.END, "=====================================\n")

    def bill_area(self):
        if self.c_name.get() == "" or self.c_phone.get() == "":
            messagebox.showerror("Error", "Customer details are required")
        elif self.medical_price.get() == "Rs. 0.00" and self.grocery_price.get() == "Rs. 0.00" and self.cold_drinks_price.get() == "Rs. 0.00":
            messagebox.showerror("Error", "No product purchased")
        else:
            self.welcome_bill()
            for category, items in zip(["Medical", "Grocery", "Cold Drinks"], [self.medical_items, self.grocery_items, self.cold_drinks_items]):
                self.add_items_to_bill(items, category)
            self.add_bill_footer()

    def add_items_to_bill(self, items, category):
        self.txtarea.insert(tk.END, f"--------- {category} ---------\n")
        for item, var in items.items():
            if var.get() != 0:
                price = var.get() * (var.get() * 5)  # Replace 5 with the correct price per item if available
                self.txtarea.insert(tk.END, f"{item}\t\t{var.get()}\t\t{price}\n")

    def add_bill_footer(self):
        self.txtarea.insert(tk.END, "-------------------------------------\n")
        self.txtarea.insert(tk.END, f"Total Medical Tax:\t\tRs. {self.medical_tax.get()}\n")
        self.txtarea.insert(tk.END, f"Total Grocery Tax:\t\tRs. {self.grocery_tax.get()}\n")
        self.txtarea.insert(tk.END, f"Total Cold Drinks Tax:\t\tRs. {self.cold_drinks_tax.get()}\n")
        self.txtarea.insert(tk.END, f"Total Bill Amount:\t\tRs. {self.total_bill}\n")
        self.txtarea.insert(tk.END, "-------------------------------------\n")
        self.save_bill()

    def save_bill(self):
    # Ensure the 'bills' directory exists
        if not os.path.exists("bills"):
         os.makedirs("bills")
        bill_data = self.txtarea.get('1.0', tk.END)
        with open(f"bills/{self.bill_no.get()}.txt", "w") as f:
            f.write(bill_data)
        messagebox.showinfo("Saved", f"Bill {self.bill_no.get()} saved successfully!")

    def find_bill(self):
        bill_file = f"bills/{self.search_bill.get()}.txt"
        try:
            with open(bill_file, "r") as f:
                self.txtarea.delete('1.0', tk.END)
                for line in f:
                    self.txtarea.insert(tk.END, line)
        except FileNotFoundError:
            messagebox.showerror("Error", "Invalid Bill Number")

    def clear_data(self):
        self.initialize_variables()
        self.welcome_bill()
        self.txtarea.delete('1.0', tk.END)

    def exit_app(self):
        self.root.destroy()

root = tk.Tk()
app = BillApp(root)
root.mainloop()
