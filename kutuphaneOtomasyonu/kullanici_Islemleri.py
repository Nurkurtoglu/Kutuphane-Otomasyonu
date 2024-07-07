import customtkinter as ctk
import tkinter as tk
from PIL import Image

from db_connection import get_db_connection
from tkinter import ttk
from tkinter import messagebox

class UserOperations(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        ctk.set_appearance_mode('Dark')
        self.configure(fg_color="#6C5B7B")
        self.title("Kullanıcı İşlemleri")
        self.geometry("600x550")

        self.conn = get_db_connection()
        self.cursor = self.conn.cursor()

        self.create_user_operations_widgets()

    def create_user_operations_widgets(self):
        self.user_frame = ctk.CTkFrame(self, width=400, height=200, fg_color="#BF4565")
        self.user_frame.place(x=180, y=50)
        self.user_operations_tittle = ctk.CTkLabel(self, text="KULLANICI İŞLEMLERİ", text_color="#FFBC67", font=("Times New Roman", 30))
        self.user_operations_tittle.place(x=200, y=5)

        # İsim , ID vb. widgets
        self.user_ID_lbl = ctk.CTkLabel(self.user_frame, text="ID: ", text_color="#FFBC67", font=("Georgia", 15))
        self.user_ID_lbl.place(x=10, y=10)
        self.user_ID_entry = ctk.CTkEntry(self.user_frame, placeholder_text="ID", text_color="#FFBC67", fg_color="transparent", font=("Georgia", 15))
        self.user_ID_entry.place(x=70, y=10)

        self.user_name_lbl = ctk.CTkLabel(self.user_frame, text="İsim: ", text_color="#FFBC67", font=("Georgia", 15))
        self.user_name_lbl.place(x=10, y=50)
        self.user_name_entry = ctk.CTkEntry(self.user_frame, placeholder_text="İsim", text_color="#FFBC67", fg_color="transparent", font=("Georgia", 15))
        self.user_name_entry.place(x=70, y=50)

        self.user_password_lbl = ctk.CTkLabel(self.user_frame, text="Şifre: ", text_color="#FFBC67",font=("Georgia", 15))
        self.user_password_lbl.place(x=10, y=90)
        self.user_password_entry = ctk.CTkEntry(self.user_frame, placeholder_text="Şifre", text_color="#FFBC67", fg_color="transparent", font=("Georgia", 15))
        self.user_password_entry.place(x=70, y=90)

        self.user_delete_btn = ctk.CTkButton(self.user_frame, width=70, height=70, text="Kullanıcı Sil", text_color="#FFBC67", bg_color="transparent", fg_color="#455C7B", font=("Georgia", 15), command=self.delete_user)
        self.user_delete_btn.place(x=250, y=10)
        self.user_update_btn = ctk.CTkButton(self.user_frame, width=70, height=70, text="Kullanıcı Bilgisi \n Güncelle", text_color="#FFBC67", bg_color="transparent", fg_color="#455C7B", font=("Georgia", 15), command=self.update_user)
        self.user_update_btn.place(x=250, y=90)
        self.list_user_btn = ctk.CTkButton(self.user_frame, width=150, height=50, text="Kullanıcıları Listele", text_color="#FFBC67", bg_color="transparent", fg_color="#455C7B", font=("Georgia", 15), command=self.list_user)
        self.list_user_btn.place(x=80, y=140)

    def delete_user(self):
        try:
            user_ID = self.user_ID_entry.get()
            user_name = self.user_name_entry.get()
            user_password = self.user_password_entry.get()

            query = "DELETE FROM Tbl_Kullanicilar WHERE kullaniciID = ?"

            if not user_name or not user_password:
                messagebox.showerror("Hata!", "Tüm alanların doldurulması gerekmektedir.")
                return

            self.cursor.execute(query, (user_ID,))
            self.conn.commit()
            messagebox.showinfo("Başarılı.", "Silme İşlemi Başarılı.")

        except Exception as e:
            messagebox.showerror("Hata!", f"Bir hata oluştu! {e}")


    def update_user(self):
        try:
            user_ID = self.user_ID_entry.get()
            user_name = self.user_name_entry.get()
            user_password = self.user_password_entry.get()

            if not user_name or not user_password :
                messagebox.showerror("Hata!", "Tüm alanların doldurulması gerekmektedir.")
                return

            query = "UPDATE Tbl_Kullanicilar SET kullaniciAd = ?, kullaniciSifre = ? WHERE kullaniciID = ?;"
            self.cursor.execute(query, (user_name, user_password, user_ID))
            self.conn.commit()

            messagebox.showinfo("Başarılı.", "Güncelleme İşlemi Başarılı.")

        except Exception as e:
            messagebox.showerror("Hata!", f"Bir hata oluştu! {e}")


    def list_user(self):

        self.cursor.execute("SELECT * FROM Tbl_Kullanicilar")
        rows = self.cursor.fetchall()

        # Treeview widget'ı ekleme
        self.tree = ttk.Treeview(self)
        self.tree["columns"] = (
            "kullaniciID", "kullaniciAd", "kullaniciSifre")
        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.column("kullaniciID", anchor=tk.W, width=120)
        self.tree.column("kullaniciAd", anchor=tk.W, width=120)
        self.tree.column("kullaniciSifre", anchor=tk.W, width=120)

        self.tree.heading("#0", text="", anchor=tk.W)
        self.tree.heading("kullaniciID", text="kullaniciID", anchor=tk.W)
        self.tree.heading("kullaniciAd", text="kullaniciAd", anchor=tk.W)
        self.tree.heading("kullaniciSifre", text="kullaniciSifre", anchor=tk.W)

        # Veritabanındaki verileri Treeview'a ekleme
        for row in rows:
            self.tree.insert("", tk.END, values=(
                row[0], row[1], row[2]))

        self.tree.place(x=100, y=350)

        self.tree.bind("<Double-1>", self.on_double_click)

    def on_double_click(self, event):

        selected_item = self.tree.selection()[0]
        values = self.tree.item(selected_item, "values")

        # Entry widget'larına değerleri yerleştirme
        self.user_ID_entry.delete(0, tk.END)
        self.user_ID_entry.insert(0, values[0])
        self.user_name_entry.delete(0, tk.END)
        self.user_name_entry.insert(0, values[1])
        self.user_password_entry.delete(0, tk.END)
        self.user_password_entry.insert(0, values[2])