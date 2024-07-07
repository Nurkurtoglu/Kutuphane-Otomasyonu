import customtkinter as ctk
import tkinter as tk
from PIL import Image
from db_connection import get_db_connection
from tkinter import ttk
from tkinter import messagebox

class MemberOperations(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        ctk.set_appearance_mode('Dark')
        self.configure(fg_color="#6C5B7B")
        self.title("Uye Islemleri")
        self.geometry("900x600")

        self.conn = get_db_connection()
        self.cursor = self.conn.cursor()

        self.create_member_operations_widgets()

    def create_member_operations_widgets(self):

        self.member_frame = ctk.CTkFrame(self, width=400, height=310, fg_color="#FFBC67")
        self.member_frame.place(x=480, y=50)
        self.member_operations_tittle = ctk.CTkLabel(self, text="ÜYE İŞLEMLERİ", text_color="#FFBC67", font=("Times New Roman", 30))
        self.member_operations_tittle.place(x=500, y=5)

        # İsim , ID vb. widgets
        self.member_ID_lbl = ctk.CTkLabel(self.member_frame, text="ID: ", text_color="#6C5B7B", font=("Georgia", 15))
        self.member_ID_lbl.place(x=10, y=10)
        self.member_ID_entry = ctk.CTkEntry(self.member_frame, placeholder_text="ID", text_color="#6C5B7B", fg_color="transparent", font=("Georgia", 15))
        self.member_ID_entry.place(x=70, y=10)

        self.member_name_lbl = ctk.CTkLabel(self.member_frame, text="İsim: ", text_color="#6C5B7B", font=("Georgia", 15))
        self.member_name_lbl.place(x=10, y=50)
        self.member_name_entry = ctk.CTkEntry(self.member_frame, placeholder_text="İsim", text_color="#6C5B7B", fg_color="transparent", font=("Georgia", 15))
        self.member_name_entry.place(x=70, y=50)

        self.member_surname_lbl = ctk.CTkLabel(self.member_frame, text="Soyisim: ", text_color="#6C5B7B",  font=("Georgia", 15))
        self.member_surname_lbl.place(x=10, y=90)
        self.member_surname_entry = ctk.CTkEntry(self.member_frame, placeholder_text="Soyisim", text_color="#6C5B7B", fg_color="transparent", font=("Georgia", 15))
        self.member_surname_entry.place(x=70, y=90)

        self.member_telno_lbl = ctk.CTkLabel(self.member_frame, text="Tel No: ", text_color="#6C5B7B", font=("Georgia", 15))
        self.member_telno_lbl.place(x=10, y=130)
        self.member_telno_entry = ctk.CTkEntry(self.member_frame, placeholder_text="telno", text_color="#6C5B7B", fg_color="transparent", font=("Georgia", 15))
        self.member_telno_entry.place(x=70, y=130)

        self.member_email_lbl = ctk.CTkLabel(self.member_frame, text="E-mail: ", text_color="#6C5B7B", font=("Georgia", 15))
        self.member_email_lbl.place(x=10, y=170)
        self.member_email_entry = ctk.CTkEntry(self.member_frame, placeholder_text="email", text_color="#6C5B7B", fg_color="transparent", font=("Georgia", 15))
        self.member_email_entry.place(x=70, y=170)

        self.member_adress_lbl = ctk.CTkLabel(self.member_frame, text="Adres: ", text_color="#6C5B7B", font=("Georgia", 15))
        self.member_adress_lbl.place(x=10, y=210)
        self.member_adress_entry = ctk.CTkEntry(self.member_frame, placeholder_text="adres", text_color="#6C5B7B", fg_color="transparent", font=("Georgia", 15))
        self.member_adress_entry.place(x=70, y=210)

        self.member_delete_btn = ctk.CTkButton(self.member_frame, width=70, height=70, text="Üye Sil", text_color="#FFBC67", bg_color="transparent", fg_color="#455C7B", font=("Georgia", 15), command=self.delete_member )
        self.member_delete_btn.place(x=250, y=60)
        self.member_update_btn = ctk.CTkButton(self.member_frame, width=70, height=70, text="Üye Bilgisi \n Güncelle", text_color="#FFBC67", bg_color="transparent", fg_color="#455C7B", font=("Georgia", 15), command=self.update_member)
        self.member_update_btn.place(x=250, y=140)
        self.list_member_btn = ctk.CTkButton(self.member_frame, width=150, height=50, text="Üyeleri Listele", text_color="#FFBC67", bg_color="transparent", fg_color="#455C7B", font=("Georgia", 15), command=self.list_member)
        self.list_member_btn.place(x=80, y=250)



    def delete_member(self):
        try:
            member_ID = self.member_ID_entry.get()
            query = "DELETE FROM Tbl_Uyeler WHERE uyeID = ?"

            self.cursor.execute(query, (member_ID,))
            self.conn.commit()
            messagebox.showinfo("Başarılı.", "Silme İşlemi Başarılı.")

        except Exception as e:
            messagebox.showerror("Hata!", f"Bir hata oluştu! {e}")


    def update_member(self):
        try:
            member_ID = self.member_ID_entry.get()
            member_name = self.member_name_entry.get()
            member_surname = self.member_surname_entry.get()
            member_tel = self.member_telno_entry.get()
            member_email = self.member_email_entry.get()
            member_adre = self.member_adress_entry.get()

            query = "UPDATE Tbl_Uyeler SET uyeAd = ?, uyeSoyad = ?, uyeTelefon = ?, uyeEmail = ?, uyeAdres = ? WHERE uyeID = ?;"
            self.cursor.execute(query, (member_name, member_surname, member_tel, member_email, member_adre, member_ID))
            self.conn.commit()

            messagebox.showinfo("Başarılı.", "Güncelleme İşlemi Başarılı.")

        except Exception as e:
            messagebox.showerror("Hata!", f"Bir hata oluştu! {e}")

    def list_member(self):
        try:
            # veri tabanı bilgileri getirme

            self.cursor.execute("SELECT * FROM Tbl_Uyeler")
            rows = self.cursor.fetchall()

            # Treeview widget'ı ekleme
            self.tree = ttk.Treeview(self)
            self.tree["columns"] = (
                "uyeID", "uyeAd", "uyeSoyad", "uyeDogumTarihi", "uyeCinsiyet", "uyeTelefon", "uyeEmail", "uyeAdres")
            self.tree.column("#0", width=0, stretch=tk.NO)
            self.tree.column("uyeID", anchor=tk.W, width=120)
            self.tree.column("uyeAd", anchor=tk.W, width=120)
            self.tree.column("uyeSoyad", anchor=tk.W, width=120)
            self.tree.column("uyeDogumTarihi", anchor=tk.W, width=120)
            self.tree.column("uyeCinsiyet", anchor=tk.W, width=120)
            self.tree.column("uyeTelefon", anchor=tk.W, width=120)
            self.tree.column("uyeEmail", anchor=tk.W, width=120)
            self.tree.column("uyeAdres", anchor=tk.W, width=120)

            self.tree.heading("#0", text="", anchor=tk.W)
            self.tree.heading("uyeID", text="uyeID", anchor=tk.W)
            self.tree.heading("uyeAd", text="uyeAd", anchor=tk.W)
            self.tree.heading("uyeSoyad", text="uyeSoyad", anchor=tk.W)
            self.tree.heading("uyeDogumTarihi", text="uyeDogumTarihi", anchor=tk.W)
            self.tree.heading("uyeCinsiyet", text="uyeCinsiyet", anchor=tk.W)
            self.tree.heading("uyeTelefon", text="uyeTelefon", anchor=tk.W)
            self.tree.heading("uyeEmail", text="uyeEmail", anchor=tk.W)
            self.tree.heading("uyeAdres", text="uyeAdres", anchor=tk.W)

            # Veritabanındaki verileri Treeview'a ekleme
            for row in rows:
                self.tree.insert("", tk.END, values=(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

            self.tree.place(x=70, y=500)

            self.tree.bind("<Double-1>", self.on_double_click)

        except Exception as e:
            messagebox.showerror("Hata!", f"Bir hata oluştu! {e}")

    def on_double_click(self, event):

        selected_item = self.tree.selection()[0]
        values = self.tree.item(selected_item, "values")

        # Entry widget'larına değerleri yerleştirme

        self.member_ID_entry.delete(0, tk.END)
        self.member_ID_entry.insert(0, values[0])
        self.member_name_entry.delete(0, tk.END)
        self.member_name_entry.insert(0, values[1])
        self.member_surname_entry.delete(0, tk.END)
        self.member_surname_entry.insert(0, values[2])
        self.member_telno_entry.delete(0, tk.END)
        self.member_telno_entry.insert(0, values[5])
        self.member_email_entry.delete(0, tk.END)
        self.member_email_entry.insert(0, values[6])
        self.member_adress_entry.delete(0, tk.END)
        self.member_adress_entry.insert(0, values[7])








