from tkinter import *

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Mangement System")
        self.root.geometry("1250x9700+0+0")

        
        lbl_title = Label(self.root, text = "LIBRARY MANAGEMENT", bg="#191919", fg="#fff", bd="20", relief=RIDGE, font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbl_title.pack(side=TOP, fill=X)


if __name__ == "__main__":
    root = Tk()
    onj = LibraryManagementSystem(root)
    root.mainloop()

