import customtkinter as ctk
import tkinter as tk
from PIL import Image
from db_connection import get_db_connection
from tkinter import ttk
from tkinter import messagebox


class AddUser(ctk.CTkToplevel):
    def __init__(self,parent):
        super().__init__(parent)

        ctk.set_appearance_mode('Dark')
        self.configure(fg_color="#6C5B7B")
        self.title("Kullanici Ekleme")
        self.geometry("400x600")

        self.conn = get_db_connection()
        self.cursor = self.conn.cursor()

        self.create_user_widgets()
    def create_user_widgets(self):

        # Başlık
        self.tittle_frame = ctk.CTkFrame(self, width=300, height=80, fg_color="#F67280")
        self.tittle_frame.pack()
        self.tittle_lbl = ctk.CTkLabel(self.tittle_frame, text="KULLANICI EKLEME", text_color="#193441", font=("Times New Roman", 30))
        self.tittle_lbl.place(x=5, y=25)


        # Kullanıcı giriş toolları
        self.frame_2 = ctk.CTkFrame(self, width=350, height=100, fg_color="#F67280")
        self.frame_2.pack(pady=20)

        self.user_name_lbl = ctk.CTkLabel(self.frame_2, text="Kullanıcı ad: ", text_color="#FCFFF5", font=("Georgia", 15))
        self.user_name_lbl.place(x=30, y=10)

        self.user_name_entry = ctk.CTkEntry(self.frame_2, placeholder_text="İsim", text_color="#FCFFF5", font=("Georgia", 15))
        self.user_name_entry.place(x=150, y=10)

        self.user_password_lbl = ctk.CTkLabel(self.frame_2, text="Şifre ", text_color="#FCFFF5", font=("Georgia", 15))
        self.user_password_lbl.place(x=30, y=40)

        self.user_password_entry = ctk.CTkEntry(self.frame_2, placeholder_text="Şifre", text_color="#FCFFF5", font=("Georgia", 15))
        self.user_password_entry.place(x=150, y=40)

        self.user_add_button = ctk.CTkButton(self, text="Kullanıcı Ekle ", text_color="#193441", fg_color="#C06C84", width=60, height=60, font=("Georgia", 10), command=self.add_user)
        self.user_add_button.place(x=100, y=200)

        self.user_list_button = ctk.CTkButton(self, text="Kullanıcı Listele ", text_color="#193441", fg_color="#C06C84", width=60, height=60, font=("Georgia", 10), command=self.user_list)
        self.user_list_button.place(x=200, y=200)


    def user_list(self):

        self.cursor.execute("SELECT * FROM Tbl_Kullanicilar")
        rows = self.cursor.fetchall()

        # Treeview widget'ı ekleme
        tree = ttk.Treeview(self)
        tree["columns"] = (
        "kullaniciID", "kullaniciAd", "kullaniciSifre")
        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("kullaniciID", anchor=tk.W, width=120)
        tree.column("kullaniciAd", anchor=tk.W, width=120)
        tree.column("kullaniciSifre", anchor=tk.W, width=120)

        tree.heading("#0", text="", anchor=tk.W)
        tree.heading("kullaniciID", text="kullaniciID", anchor=tk.W)
        tree.heading("kullaniciAd", text="kullaniciAd", anchor=tk.W)
        tree.heading("kullaniciSifre", text="kullaniciSifre", anchor=tk.W)

        # Veritabanındaki verileri Treeview'a ekleme
        for row in rows:
            tree.insert("", tk.END, values=(
                row[0], row[1], row[2]))
        tree.place(x=50, y=350)

    def add_user(self):
        try:
            user_name = self.user_name_entry.get()
            user_password = self.user_password_entry.get()

            if not user_name or not user_password :
                messagebox.showerror("Hata!", "Tüm alanların doldurulması gerekmektedir.")
                return

            query = "INSERT INTO Tbl_Kullanicilar (kullaniciAd, kullaniciSifre) VALUES (?, ?)"

            self.cursor.execute(query, user_name, user_password)

            self.conn.commit()

            messagebox.showinfo("İşlem Başarılı.", "Kullanıcı Ekleme İşlemi Başarılı.")



        except Exception as e:
            messagebox.showerror("Bir hata oluştu! ", f"{e}")

