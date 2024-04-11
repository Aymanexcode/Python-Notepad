import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

class NotepadApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Notepad")
        self.master.geometry("600x400")

        self.setup_menu()
        self.setup_text_area()

    def setup_menu(self):
        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.file_menu.add_command(label="New", command=self.new_file) # new file
        self.file_menu.add_command(label="Open", command=self.open_file) # open file
        self.file_menu.add_command(label="Save", command=self.save_file) # save file
        self.file_menu.add_command(label="Save As", command=self.save_as_file) # save as file
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_app) # Exit app
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

    def setup_text_area(self):
        self.text_area = tk.Text(self.master, wrap="word", bg="#ffffff", fg="#000000", font=("Verdana", 14))
        self.text_area.pack(expand=True, fill="both", padx=10, pady=10)

    def new_file(self):
        self.text_area.delete("1.0", tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, content)

    def  save_file(self):
        file_path = getattr(self, "file_path", None)
        if not file_path:
            self.save_as_file()
            return
        try:
            with open(file_path, "w") as file:
                content = self.text_area.get("1.0", tk.END)
                file.write(content)
        except Exception as e:
            messagebox.showerror("Error," f"Failed to save file: {str(e)}")

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            self.file_path = file_path
            self.save_file()

    def exit_app(self):
        if messagebox.askokcancel("Exit" , "Are you sure you want to exit?" ):
            self.master.destroy()

def main():
    root = tk.Tk()
    notepad = NotepadApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

# END !