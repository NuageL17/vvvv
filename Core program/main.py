import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox

# Nom du fichier pour stocker les données utilisateur
USER_FILE = "users.txt"

# Variables globales pour stocker les informations de l'utilisateur connectéaaaaaa
current_user_first_name = ""
current_user_last_name = ""
current_user_age = ""
current_user_type = ""

def register_user(first_name, last_name, age, user_type):
    """Enregistre un nouvel utilisateur (patient ou admin) dans le fichier"""
    with open(USER_FILE, "a") as file:
        file.write(f"{first_name},{last_name},{age},{user_type}\n")

def verify_login(first_name, last_name, user_type):
    """Vérifie les informations de connexion"""
    try:
        with open(USER_FILE, "r") as file:
            for line in file:
                user_first_name, user_last_name, user_age, user_role = line.strip().split(',')
                if user_first_name == first_name and user_last_name == last_name and user_role == user_type:
                    return user_age
    except FileNotFoundError:
        return None
    return None

def submit_registration(user_type):
    """Soumet le formulaire d'inscription pour le type d'utilisateur spécifié"""
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    age = entry_age.get()

    if first_name and last_name and age:
        try:
            register_user(first_name, last_name, age, user_type)
            messagebox.showinfo("Registration", f"{user_type} registration successful!")
            global current_user_first_name, current_user_last_name, current_user_age, current_user_type
            current_user_first_name = first_name
            current_user_last_name = last_name
            current_user_age = age
            current_user_type = user_type
            if user_type == "Patient":
                show_patient_content()
            else:
                show_admin_content()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("Registration", "Please fill in all fields")

def submit_login():
    """Soumet le formulaire de connexion"""
    first_name = entry_login_first_name.get()
    last_name = entry_login_last_name.get()
    user_type = user_type_var.get()

    age = verify_login(first_name, last_name, user_type)
    if age:
        global current_user_first_name, current_user_last_name, current_user_age, current_user_type
        current_user_first_name = first_name
        current_user_last_name = last_name
        current_user_age = age
        current_user_type = user_type
        
        if user_type == "Patient":
            messagebox.showinfo("Login", "Login successful!")
            show_patient_content()
        elif user_type == "Admin":
            messagebox.showinfo("Login", "Admin login successful!")
            show_admin_content()
    else:
        messagebox.showerror("Login Error", "Incorrect name, surname, or user type")

def show_patient_content():
    """Affiche le contenu pour les patients après la connexion"""
    for widget in frame.winfo_children():
        widget.destroy()

    window.geometry("1280x720")
    main_frame = ctk.CTkFrame(frame)
    main_frame.pack(pady=20, padx=20, fill="both", expand=True)

    user_info_label = ctk.CTkLabel(main_frame, text=f"{current_user_first_name} {current_user_last_name} | Age: {current_user_age}", font=("Helvetica", 12, "bold"))
    user_info_label.pack(pady=10, anchor="nw")

    def game1():
        messagebox.showinfo("Game 1", "This is Game 1!")

    def game2():
        messagebox.showinfo("Game 2", "This is Game 2!")

    button_game1 = ctk.CTkButton(main_frame, text="Game 1", command=game1)
    button_game1.pack(pady=10)

    button_game2 = ctk.CTkButton(main_frame, text="Game 2", command=game2)
    button_game2.pack(pady=10)

    button_logout = ctk.CTkButton(main_frame, text="Logout", command=logout)
    button_logout.pack(pady=10)

def show_admin_content():
    """Affiche le contenu pour les administrateurs après la connexion"""
    for widget in frame.winfo_children():
        widget.destroy()

    window.geometry("1280x720")
    main_frame = ctk.CTkFrame(frame)
    main_frame.pack(pady=20, padx=20, fill="both", expand=True)

    user_info_label = ctk.CTkLabel(main_frame, text=f"Admin: {current_user_first_name} {current_user_last_name}", font=("Helvetica", 12, "bold"))
    user_info_label.pack(pady=10, anchor="nw")

    def view_data():
        messagebox.showinfo("Data", "Here you can view patients' data.")

    def manage_users():
        messagebox.showinfo("Manage Users", "Here you can manage users.")

    button_view_data = ctk.CTkButton(main_frame, text="View Data", command=view_data)
    button_view_data.pack(pady=10)

    button_manage_users = ctk.CTkButton(main_frame, text="Manage Users", command=manage_users)
    button_manage_users.pack(pady=10)

    button_logout = ctk.CTk.Button(main_frame, text="Logout", command=logout)
    button_logout.pack(pady=10)

def show_registration_frame(user_type):
    """Affiche le formulaire d'inscription dans le cadre pour le type d'utilisateur spécifié"""
    for widget in frame.winfo_children():
        widget.destroy()

    label_first_name = ctk.CTkLabel(frame, text="First Name")
    label_first_name.pack(pady=5)

    global entry_first_name
    entry_first_name = ctk.CTkEntry(frame)
    entry_first_name.pack(pady=5)

    label_last_name = ctk.CTkLabel(frame, text="Last Name")
    label_last_name.pack(pady=5)

    global entry_last_name
    entry_last_name = ctk.CTkEntry(frame)
    entry_last_name.pack(pady=5)

    label_age = ctk.CTkLabel(frame, text="Age")
    label_age.pack(pady=5)

    global entry_age
    entry_age = ctk.CTkEntry(frame)
    entry_age.pack(pady=5)

    button_submit = ctk.CTkButton(frame, text="Submit", command=lambda: submit_registration(user_type))
    button_submit.pack(pady=20)

    button_back = ctk.CTkButton(frame, text="Back", command=show_choice_frame)
    button_back.pack(pady=10)

def show_login_frame():
    """Affiche le formulaire de connexion dans le cadre"""
    for widget in frame.winfo_children():
        widget.destroy()

    label_login_first_name = ctk.CTkLabel(frame, text="First Name")
    label_login_first_name.pack(pady=5)

    global entry_login_first_name
    entry_login_first_name = ctk.CTkEntry(frame)
    entry_login_first_name.pack(pady=5)

    label_login_last_name = ctk.CTkLabel(frame, text="Last Name")
    label_login_last_name.pack(pady=5)

    global entry_login_last_name
    entry_login_last_name = ctk.CTkEntry(frame)
    entry_login_last_name.pack(pady=5)

    # Nouveau champ pour le type d'utilisateur
    global user_type_var
    user_type_var = tk.StringVar(value="Patient")
    radio_patient = ctk.CTkRadioButton(frame, text="Patient", variable=user_type_var, value="Patient")
    radio_patient.pack(pady=5)
    radio_admin = ctk.CTkRadioButton(frame, text="Admin", variable=user_type_var, value="Admin")
    radio_admin.pack(pady=5)

    button_submit = ctk.CTkButton(frame, text="Login", command=submit_login)
    button_submit.pack(pady=20)

    button_back = ctk.CTkButton(frame, text="Back", command=show_choice_frame)
    button_back.pack(pady=10)

def show_choice_frame():
    """Affiche le choix d'inscription ou de connexion dans le cadre principal"""
    for widget in frame.winfo_children():
        widget.destroy()

    # Espace pour le logo
    logo_label = ctk.CTkLabel(frame, text="LOGO PLACEHOLDER", font=("Helvetica", 24))
    logo_label.pack(pady=40)

    # Conteneur pour les boutons Register et Login
    button_frame = ctk.CTkFrame(frame)
    button_frame.pack(pady=10)

    button_register_patient = ctk.CTkButton(button_frame, text="Register Patient", command=lambda: show_registration_frame("Patient"))
    button_register_patient.grid(row=0, column=0, padx=20)

    button_register_admin = ctk.CTkButton(button_frame, text="Register Admin", command=lambda: show_registration_frame("Admin"))
    button_register_admin.grid(row=0, column=1, padx=20)

    button_login = ctk.CTkButton(button_frame, text="Login", command=show_login_frame)
    button_login.grid(row=0, column=2, padx=20)

def logout():
    """Déconnecte l'utilisateur et retourne à la fenêtre de connexion"""
    global current_user_first_name, current_user_last_name, current_user_age, current_user_type
    current_user_first_name = ""
    current_user_last_name = ""
    current_user_age = ""
    current_user_type = ""
    show_choice_frame()

# Lancer la fenêtre principale
window = ctk.CTk()
window.title("User Management")
window.geometry("1280x720")

frame = ctk.CTkFrame(window)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Afficher le choix initial
show_choice_frame()

# Lancer la boucle principale Tkinter
window.mainloop()
