import tkinter as tk
from tkinter import messagebox

class ManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Grocery & Café Management Systems")
        self.root.geometry("450x450")
        self.root.configure(padx=20, pady=20)

        # Carts (Baskets)
        self.basket_grocery = []
        self.basket_cafe = []

        # Available Items
        self.grocery_items = [
            "Vegetables", "Fruits", "Dairy", "Bakery", "Meat",
            "Frozen Foods", "Canned Goods", "Household Items",
            "Personal Care", "Beverages", "Snacks", "Condiments & Sauces"
        ]

        self.cafe_items = [
            "Coffee", "Tea", "Pastries", "Sandwiches",
            "Salads", "Smoothies", "Juices"
        ]

        self.create_widgets()

    def create_widgets(self):
        # Main Title
        title_label = tk.Label(self.root, text="Grocery & Café Management", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=(0, 20))

        # --- Grocery Section ---
        grocery_frame = tk.LabelFrame(self.root, text=" Grocery System ", font=("Helvetica", 10, "bold"), padx=10, pady=10)
        grocery_frame.pack(fill="x", pady=5)

        tk.Label(grocery_frame, text="Select Item:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.grocery_var = tk.StringVar()
        self.grocery_var.set(self.grocery_items[0])
        grocery_dropdown = tk.OptionMenu(grocery_frame, self.grocery_var, *self.grocery_items)
        grocery_dropdown.config(width=20)
        grocery_dropdown.grid(row=0, column=1, padx=5, pady=5)

        tk.Button(grocery_frame, text="Add to Cart", command=self.add_grocery, width=15).grid(row=1, column=0, pady=5)
        tk.Button(grocery_frame, text="View Order Status", command=self.view_grocery, width=15).grid(row=1, column=1, pady=5)


        # --- Café Section ---
        cafe_frame = tk.LabelFrame(self.root, text=" Café System ", font=("Helvetica", 10, "bold"), padx=10, pady=10)
        cafe_frame.pack(fill="x", pady=15)

        tk.Label(cafe_frame, text="Select Item:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.cafe_var = tk.StringVar()
        self.cafe_var.set(self.cafe_items[0])
        cafe_dropdown = tk.OptionMenu(cafe_frame, self.cafe_var, *self.cafe_items)
        cafe_dropdown.config(width=20)
        cafe_dropdown.grid(row=0, column=1, padx=5, pady=5)

        tk.Button(cafe_frame, text="Add to Cart", command=self.add_cafe, width=15).grid(row=1, column=0, pady=5)
        tk.Button(cafe_frame, text="View Order Status", command=self.view_cafe, width=15).grid(row=1, column=1, pady=5)


        # --- Exit Button ---
        tk.Button(self.root, text="Exit", command=self.root.quit, bg="#ff4c4c", fg="white", font=("Helvetica", 11, "bold"), width=15).pack(pady=10)

    # --- Grocery Methods ---
    def add_grocery(self):
        item = self.grocery_var.get()
        self.basket_grocery.append(item)
        messagebox.showinfo("Success", f"'{item}' has been added to your Grocery Cart!")

    def view_grocery(self):
        if self.basket_grocery:
            items = "\n".join([f"- {item}" for item in self.basket_grocery])
            messagebox.showinfo("Grocery Order Status", f"Your current grocery order includes:\n\n{items}")
        else:
            messagebox.showwarning("Grocery Order Status", "Your grocery basket is empty.")

    # --- Café Methods ---
    def add_cafe(self):
        item = self.cafe_var.get()
        self.basket_cafe.append(item)
        messagebox.showinfo("Success", f"'{item}' has been added to your Café Cart!")

    def view_cafe(self):
        if self.basket_cafe:
            items = "\n".join([f"- {item}" for item in self.basket_cafe])
            messagebox.showinfo("Café Order Status", f"Your current café order includes:\n\n{items}")
        else:
            messagebox.showwarning("Café Order Status", "Your café basket is empty.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ManagementSystem(root)
    root.mainloop()
