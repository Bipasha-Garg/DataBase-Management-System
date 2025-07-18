from tkinter import *
from tkinter import ttk
import backend


def get_selected_row(event):
    """get_selected_row function to get content of the selected row.

    Arguments
    ---------
    event: a virtual interrupt.
    """
    global selected_tuple
    if lb1.curselection() != ():
        index = lb1.curselection()[0]
        selected_tuple = lb1.get(index)
        clear_entries()
        e1.insert(END, selected_tuple[1])
        e2.insert(END, selected_tuple[2])
        e3.insert(END, selected_tuple[3])
        e4.insert(END, selected_tuple[4])


def view_command():
    """view_command function to show the output database."""
    lb1.delete(0, END)
    for row in backend.view():
        lb1.insert(END, row)


def search_command():
    """search_command function to search in the database."""
    lb1.delete(0, END)
    for row in backend.search(fn.get(), ln.get(), term.get(), gpa.get()):
        lb1.insert(END, row)
    clear_entries()


def add_command():
    """add_command function to add a new student to the database."""
    backend.insert(fn.get(), ln.get(), term.get(), gpa.get())
    clear_entries()
    view_command()


def update_command():
    """update_command function to update the data of a specific student."""
    backend.update(selected_tuple[0], fn.get(), ln.get(), term.get(), gpa.get())
    clear_entries()
    view_command()


def delete_command():
    """delete_command function to delete the data of a specific student."""
    index = lb1.curselection()[0]
    selected_tuple = lb1.get(index)
    backend.delete(selected_tuple[0])
    clear_entries()
    view_command()


def delete_data_command():
    """delete_data_command function to delete the database."""
    backend.delete_data()
    view_command()


def clear_entries():
    """clear_entries function to clear content of entries."""
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)


def clear_command():
    """view_command function to clear content of Listbox."""
    lb1.delete(0, END)
    clear_entries()


# Create main window
wind = Tk()
wind.title("Student Database Management System")
wind.geometry("800x600")
wind.configure(bg="#f0f0f0")

# Configure style
style = ttk.Style()
style.theme_use("clam")

# Configure custom styles
style.configure(
    "Title.TLabel",
    font=("Arial", 20, "bold"),
    foreground="#2c3e50",
    background="#f0f0f0",
)
style.configure(
    "Heading.TLabel",
    font=("Arial", 12, "bold"),
    foreground="#34495e",
    background="#f0f0f0",
)
style.configure("Custom.TEntry", font=("Arial", 10), fieldbackground="white")
style.configure("Custom.TButton", font=("Arial", 10), padding=5)

# Create StringVar objects
fn = StringVar()
ln = StringVar()
term = StringVar()
gpa = StringVar()

# Create main frame
main_frame = Frame(wind, bg="#f0f0f0", padx=20, pady=20)
main_frame.pack(fill=BOTH, expand=True)

# Title
title_label = ttk.Label(
    main_frame, text="🎓 Student Database Management System", style="Title.TLabel"
)
title_label.grid(row=0, column=0, columnspan=4, pady=(0, 20))

# Input section frame
input_frame = LabelFrame(
    main_frame,
    text="Student Information",
    font=("Arial", 12, "bold"),
    bg="#ecf0f1",
    fg="#2c3e50",
    padx=15,
    pady=15,
)
input_frame.grid(row=1, column=0, columnspan=2, sticky="ew", padx=(0, 10), pady=(0, 10))

# Input labels and entries
ttk.Label(input_frame, text="First Name:", style="Heading.TLabel").grid(
    row=0, column=0, sticky="w", pady=5
)
e1 = ttk.Entry(input_frame, textvariable=fn, style="Custom.TEntry", width=20)
e1.grid(row=0, column=1, padx=(10, 0), pady=5, sticky="ew")

ttk.Label(input_frame, text="Last Name:", style="Heading.TLabel").grid(
    row=1, column=0, sticky="w", pady=5
)
e2 = ttk.Entry(input_frame, textvariable=ln, style="Custom.TEntry", width=20)
e2.grid(row=1, column=1, padx=(10, 0), pady=5, sticky="ew")

ttk.Label(input_frame, text="Term:", style="Heading.TLabel").grid(
    row=2, column=0, sticky="w", pady=5
)
e3 = ttk.Entry(input_frame, textvariable=term, style="Custom.TEntry", width=20)
e3.grid(row=2, column=1, padx=(10, 0), pady=5, sticky="ew")

ttk.Label(input_frame, text="GPA:", style="Heading.TLabel").grid(
    row=3, column=0, sticky="w", pady=5
)
e4 = ttk.Entry(input_frame, textvariable=gpa, style="Custom.TEntry", width=20)
e4.grid(row=3, column=1, padx=(10, 0), pady=5, sticky="ew")

# Configure input frame column weights
input_frame.columnconfigure(1, weight=1)

# Database display frame
db_frame = LabelFrame(
    main_frame,
    text="Database Records",
    font=("Arial", 12, "bold"),
    bg="#ecf0f1",
    fg="#2c3e50",
    padx=15,
    pady=15,
)
db_frame.grid(row=1, column=2, columnspan=2, sticky="nsew", padx=(10, 0), pady=(0, 10))

# Listbox with scrollbar
listbox_frame = Frame(db_frame, bg="#ecf0f1")
listbox_frame.pack(fill=BOTH, expand=True)

lb1 = Listbox(
    listbox_frame,
    height=12,
    width=50,
    font=("Courier", 10),
    bg="white",
    fg="#2c3e50",
    selectbackground="#3498db",
    selectforeground="white",
)
lb1.pack(side=LEFT, fill=BOTH, expand=True)
lb1.bind("<<ListboxSelect>>", get_selected_row)

sc = Scrollbar(listbox_frame, orient=VERTICAL, command=lb1.yview)
sc.pack(side=RIGHT, fill=Y)
lb1.configure(yscrollcommand=sc.set)

# Buttons frame
button_frame = Frame(main_frame, bg="#f0f0f0")
button_frame.grid(row=2, column=0, columnspan=4, pady=(10, 0))

# Create buttons with custom styling
buttons = [
    ("📋 View All", view_command, "#3498db"),
    ("🔍 Search", search_command, "#2ecc71"),
    ("➕ Add New", add_command, "#27ae60"),
    ("✏️ Update", update_command, "#f39c12"),
    ("🗑️ Delete", delete_command, "#e74c3c"),
    ("🧹 Clear", clear_command, "#95a5a6"),
    ("⚠️ Delete All", delete_data_command, "#c0392b"),
    ("❌ Exit", wind.destroy, "#7f8c8d"),
]

for i, (text, command, color) in enumerate(buttons):
    btn = Button(
        button_frame,
        text=text,
        command=command,
        font=("Arial", 10, "bold"),
        bg=color,
        fg="white",
        relief=FLAT,
        padx=15,
        pady=8,
        cursor="hand2",
        activebackground="#34495e",
        activeforeground="white",
    )
    btn.grid(row=i // 4, column=i % 4, padx=5, pady=5, sticky="ew")

# Configure grid weights for responsiveness
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)
main_frame.columnconfigure(2, weight=2)
main_frame.columnconfigure(3, weight=1)
main_frame.rowconfigure(1, weight=1)

for i in range(4):
    button_frame.columnconfigure(i, weight=1)

# Start the application
wind.mainloop()
