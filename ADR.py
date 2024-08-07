import tkinter as tk
from tkinter import messagebox
from datetime import datetime
class ADRApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ADR Manager")
        self.create_widgets()
    def create_widgets(self):         #Title
        tk.Label(self.root, text="Title").grid(row=0, column=0, padx=10, pady=5)
        self.title_entry = tk.Entry(self.root, width=50)
        self.title_entry.grid(row=0, column=1, padx=10, pady=5)
        # Date
        tk.Label(self.root, text="Date (YYYY-MM-DD)").grid(row=1, column=0, padx=10, pady=5)
        self.date_entry = tk.Entry(self.root, width=50)
        self.date_entry.grid(row=1, column=1, padx=10, pady=5)
        self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))  # Default to current date
        # Status
        tk.Label(self.root, text="Status").grid(row=2, column=0, padx=10, pady=5)
        self.status_entry = tk.Entry(self.root, width=50)
        self.status_entry.grid(row=2, column=1, padx=10, pady=5)
        # Context
        tk.Label(self.root, text="Context").grid(row=3, column=0, padx=10, pady=5)
        self.context_entry = tk.Text(self.root, width=50, height=5)
        self.context_entry.grid(row=3, column=1, padx=10, pady=5)
        # Decision
        tk.Label(self.root, text="Decision").grid(row=4, column=0, padx=10, pady=5)
        self.decision_entry = tk.Text(self.root, width=50, height=5)
        self.decision_entry.grid(row=4, column=1, padx=10, pady=5)
        # Consequences
        tk.Label(self.root, text="Consequences").grid(row=5, column=0, padx=10, pady=5)
        self.consequences_entry = tk.Text(self.root, width=50, height=5)
        self.consequences_entry.grid(row=5, column=1, padx=10, pady=5)
        # Save button
        self.save_button = tk.Button(self.root, text="Save ADR", command=self.save_adr)
        self.save_button.grid(row=6, column=0, columnspan=2, pady=10)
    def save_adr(self):
        title = self.title_entry.get()
        date = self.date_entry.get()
        status = self.status_entry.get()
        context = self.context_entry.get("1.0", tk.END).strip()
        decision = self.decision_entry.get("1.0", tk.END).strip()
        consequences = self.consequences_entry.get("1.0", tk.END).strip()
        if not title or not date or not status or not context or not decision or not consequences:
            messagebox.showerror("Error", "All fields must be filled out")
            return
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Date must be in YYYY-MM-DD format")
            return
        adr = {
            "title": title,
            "date": date,
            "status": status,
            "context": context,
            "decision": decision,
            "consequences": consequences
        }
        with open("adrs.txt", "a") as file:
            file.write(str(adr) + "\n")
        messagebox.showinfo("Success", "ADR saved successfully!")
        self.clear_entries()
    def clear_entries(self):
        self.title_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.status_entry.delete(0, tk.END)
        self.context_entry.delete("1.0", tk.END)
        self.decision_entry.delete("1.0", tk.END)
        self.consequences_entry.delete("1.0", tk.END)
if __name__ == "__main__":
    root = tk.Tk()
    app = ADRApp(root)
    root.mainloop()
