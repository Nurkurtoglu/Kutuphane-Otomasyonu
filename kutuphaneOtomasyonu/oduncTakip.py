import customtkinter as ctk
import tkinter as tk
from PIL import Image
import pyodbc
from db_connection import get_db_connection
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox
from datetime import datetime


class BorrowFollowUp(ctk.CTkToplevel):

    def __init__(self, parent):
        super().__init__(parent)

        ctk.set_appearance_mode('Dark')
        self.configure(fg_color="#6C5B7B")
        self.title("Ödünç Takip")
        self.geometry("1000x700")

        self.conn = get_db_connection()
        self.cursor = self.conn.cursor()

        self.create_followup_widgets()

    def create_followup_widgets(self):
        self.tittle_frame_1 = ctk.CTkFrame(self, width=400, height=40, fg_color="#EFE7CC")
        self.tittle_frame_1.place(x=10, y=30)
        self.tittle_lbl_1 = ctk.CTkLabel(self.tittle_frame_1, text="ÖDÜNÇ VERİLEN KİTAPLARI LİSTESİ", text_color="#9B7379", font=("Georgia", 15, "bold"))
        self.tittle_lbl_1.place(x=30, y=5)

        self.tittle_frame_2 = ctk.CTkFrame(self, width=400, height=40, fg_color="#EFE7CC")
        self.tittle_frame_2.place(x=535, y=30)
        self.tittle_lbl_2 = ctk.CTkLabel(self.tittle_frame_2, text="KİTAP TESLİM", text_color="#9B7379", font=("Georgia", 15, "bold"))
        self.tittle_lbl_2.place(x=130, y=5)

        # Teslim İşlemleri
        self.operating_frame = ctk.CTkFrame(self, width=430, height=250, fg_color="#DA727E")
        self.operating_frame.place(x=520, y=80)

        self.borrow_ID_lbl = ctk.CTkLabel(self.operating_frame, text="Ödünç ID: ", text_color="#355C7D", font=("Georgia", 15))
        self.borrow_ID_lbl.place(x=20, y=10)
        self.borrow_ID_entry = ctk.CTkEntry(self.operating_frame, placeholder_text="ID", text_color="white", font=("Georgia", 15))
        self.borrow_ID_entry.place(x=190, y=10)

        self.member_name_lbl = ctk.CTkLabel(self.operating_frame, text="Teslim Eden Üye Adı: ", text_color="#355C7D", font=("Georgia", 15))
        self.member_name_lbl.place(x=20, y=50)
        self.member_name_entry = ctk.CTkEntry(self.operating_frame, placeholder_text="Üye Ad", text_color="white", font=("Georgia", 15))
        self.member_name_entry.place(x=190, y=50)

        self.surname_lbl = ctk.CTkLabel(self.operating_frame, text="Soyadı: ", text_color="#355C7D", font=("Georgia", 15))
        self.surname_lbl.place(x=20, y=90)
        self.surname_entry = ctk.CTkEntry(self.operating_frame, placeholder_text="Soyadı", text_color="white", font=("Georgia", 15))
        self.surname_entry.place(x=190, y=90)

        self.book_name_lbl = ctk.CTkLabel(self.operating_frame, text="Teslim Edilen Kitap Adı: ", text_color="#355C7D", font=("Georgia", 15))
        self.book_name_lbl.place(x=20, y=130)
        self.book_name_entry = ctk.CTkEntry(self.operating_frame, placeholder_text="Kitap Ad", text_color="white", font=("Georgia", 15))
        self.book_name_entry.place(x=190, y=130)

        self.deliver_btn = ctk.CTkButton(self.operating_frame, width=70, height=70, text="TESLİM ET", text_color="#DA727E", fg_color="#6C5B7B", font=("Georgia", 15), command=self.deliver)
        self.deliver_btn.place(x=225, y=170)

        self.show_deliver_btn = ctk.CTkButton(self.operating_frame, width=70, height=70, text="Ödünç Verilen \n Kitaplar",  text_color="#DA727E", fg_color="#6C5B7B", font=("Georgia", 15), command=self.books_on_loan)
        self.show_deliver_btn.place(x=50, y=170)

        self.tittle_frame_3 = ctk.CTkFrame(self, width=400, height=40, fg_color="#EFE7CC")
        self.tittle_frame_3.place(x=10, y=340)
        self.tittle_lbl_3 = ctk.CTkLabel(self.tittle_frame_3, text="TESLİM TARİHİ GEÇMİŞ KİTAPLAR", text_color="#9B7379", font=("Georgia", 15, "bold"))
        self.tittle_lbl_3.place(x=60, y=5)

        self.tittle_frame_4 = ctk.CTkFrame(self, width=400, height=40, fg_color="#EFE7CC")
        self.tittle_frame_4.place(x=535, y=340)
        self.tittle_lbl_4 = ctk.CTkLabel(self.tittle_frame_4, text="TESLİM SÜRESİ UZATMA", text_color="#9B7379", font=("Georgia", 15, "bold"))
        self.tittle_lbl_4.place(x=90, y=5)

        # Süre Uzatma İşlemleri

        self.operating_frame_2 = ctk.CTkFrame(self, width=430, height=300, fg_color="#DA727E")
        self.operating_frame_2.place(x=520, y=390)

        self.borrow_ID_lbl_2 = ctk.CTkLabel(self.operating_frame_2, text="Ödünç ID: ", text_color="#355C7D", font=("Georgia", 15))
        self.borrow_ID_lbl_2.place(x=20, y=10)
        self.borrow_ID_entry_2 = ctk.CTkEntry(self.operating_frame_2, placeholder_text="ID", text_color="white", font=("Georgia", 15))
        self.borrow_ID_entry_2.place(x=190, y=10)

        self.member_name_lbl_2 = ctk.CTkLabel(self.operating_frame_2, text="Teslim Eden Üye Adı: ", text_color="#355C7D", font=("Georgia", 15))
        self.member_name_lbl_2.place(x=20, y=50)
        self.member_name_entry_2 = ctk.CTkEntry(self.operating_frame_2, placeholder_text="Üye Ad", text_color="white", font=("Georgia", 15))
        self.member_name_entry_2.place(x=190, y=50)

        self.surname_lbl_2 = ctk.CTkLabel(self.operating_frame_2, text="Soyadı: ", text_color="#355C7D", font=("Georgia", 15))
        self.surname_lbl_2.place(x=20, y=90)
        self.surname_entry_2 = ctk.CTkEntry(self.operating_frame_2, placeholder_text="Soyadı", text_color="white", font=("Georgia", 15))
        self.surname_entry_2.place(x=190, y=90)

        self.book_name_lbl_2 = ctk.CTkLabel(self.operating_frame_2, text="Teslim Edilen Kitap Adı: ", text_color="#355C7D", font=("Georgia", 15))
        self.book_name_lbl_2.place(x=20, y=130)
        self.book_name_entry_2 = ctk.CTkEntry(self.operating_frame_2, placeholder_text="Kitap Ad", text_color="white", font=("Georgia", 15))
        self.book_name_entry_2.place(x=190, y=130)

        # Tarih Seçicileri ve Onay Düğmeleri

        self.release_date_lbl_2 = ctk.CTkLabel(self.operating_frame_2, text="Veriliş Tarihi: ", text_color="#355C7D", font=("Georgia", 15))
        self.release_date_lbl_2.place(x=20, y=160)
        self.release_date_entry_2 = ctk.CTkEntry(self.operating_frame_2, text_color="#B7D7D8", font=("Georgia", 15))
        self.release_date_entry_2.place(x=190, y=160)

        self.delivery_date_lbl_2 = ctk.CTkLabel(self.operating_frame_2, text="Teslim Tarihi: ", text_color="#355C7D", font=("Georgia", 15))
        self.delivery_date_lbl_2.place(x=20, y=190)
        self.delivery_date_entry_2 = ctk.CTkEntry(self.operating_frame_2, text_color="#B7D7D8", font=("Georgia", 15))
        self.delivery_date_entry_2.place(x=190, y=190)

        frame_5 = ttk.Frame(self.operating_frame_2)
        frame_5.place(x=420, y=205)
        self.release_date_picker = DateEntry(frame_5, width=12, background='darkblue', foreground='white', borderwidth=2, year=2023, month=6, day=4, date_pattern='y-mm-dd')
        self.release_date_picker.pack()

        frame_6 = ttk.Frame(self.operating_frame_2)
        frame_6.place(x=420, y=240)
        self.delivery_date_picker = DateEntry(frame_6, width=12, background='darkblue', foreground='white', borderwidth=2, year=2023, month=6, day=4, date_pattern='y-mm-dd')
        self.delivery_date_picker.pack()

        def select_release_date():
            selected_date = self.release_date_picker.get_date()
            self.release_date_entry_2.delete(0, ctk.END)
            self.release_date_entry_2.insert(0, selected_date.strftime("%Y-%m-%d"))

        def select_delivery_date():
            selected_date = self.delivery_date_picker.get_date()
            self.delivery_date_entry_2.delete(0, ctk.END)
            self.delivery_date_entry_2.insert(0, selected_date.strftime("%Y-%m-%d"))

        self.select_release_date_btn_2 = ctk.CTkButton(self.operating_frame_2, text="Veriliş Tarihini Seç", text_color="#DA727E", fg_color="#355C7D", font=("Georgia", 15), command=select_release_date)
        self.select_release_date_btn_2.place(x=10, y=220)

        self.select_delivery_date_btn_2 = ctk.CTkButton(self.operating_frame_2, text="Teslim Tarihini Seç", text_color="#DA727E", fg_color="#355C7D", font=("Georgia", 15), command=select_delivery_date)
        self.select_delivery_date_btn_2.place(x=10, y=260)

        self.deliver_btn_2 = ctk.CTkButton(self.operating_frame_2, width=70, height=70, text="SÜRE UZAT", text_color="#DA727E", fg_color="#6C5B7B", font=("Georgia", 15), command=self.extend_time)
        self.deliver_btn_2.place(x=180, y=220)

        self.deliver_btn_3 = ctk.CTkButton(self.operating_frame_2, width=70, height=70, text="Gecikmiş Kitapları \n Göster", text_color="#DA727E", fg_color="#6C5B7B", font=("Georgia", 15), command=self.overdue_books)
        self.deliver_btn_3.place(x=280, y=220)

    def overdue_books(self):  #Gecikmiş kitaplar
        try:

            self.cursor.execute(
                "SELECT oduncID, uyeAdi, uyeSoyadi, kitapAdi, verilisTarihi, teslimTarihi FROM Tbl_Odunver WHERE teslimTarihi < GETDATE()")
            rows = self.cursor.fetchall()

            # Treeview widget'ı ekleme
            self.tree1 = ttk.Treeview(self)

            self.tree1["columns"] = (
                "oduncID", "uyeAdi", "uyeSoyadi", "kitapAdi", "verilisTarihi", "teslimTarihi")
            self.tree1.column("#0", width=0, stretch=tk.NO)
            self.tree1.column("oduncID", anchor=tk.W, width=60)
            self.tree1.column("uyeAdi", anchor=tk.W, width=100)
            self.tree1.column("uyeSoyadi", anchor=tk.W, width=100)
            self.tree1.column("kitapAdi", anchor=tk.W, width=100)
            self.tree1.column("verilisTarihi", anchor=tk.W, width=100)
            self.tree1.column("teslimTarihi", anchor=tk.W, width=100)

            self.tree1.heading("#0", text="", anchor=tk.W)
            self.tree1.heading("oduncID", text="oduncID", anchor=tk.W)
            self.tree1.heading("uyeAdi", text="uyeAdi", anchor=tk.W)
            self.tree1.heading("uyeSoyadi", text="uyeSoyadi", anchor=tk.W)
            self.tree1.heading("kitapAdi", text="kitapAdi", anchor=tk.W)
            self.tree1.heading("verilisTarihi", text="verilisTarihi", anchor=tk.W)
            self.tree1.heading("teslimTarihi", text="teslimTarihi", anchor=tk.W)

            # Veritabanındaki verileri Treeview'a ekleme
            for row in rows:
                self.tree1.insert("", tk.END, values=(
                    row[0], row[1], row[2], row[3], row[4], row[5]))

            self.tree1.place(x=10, y=500)

        except Exception as e:
            messagebox.showerror("Hata!", f"{e}")

    def books_on_loan(self):  #Ödünç verilen kitaplar
        try:
            self.cursor.execute("SELECT * FROM Tbl_Odunver")
            rows = self.cursor.fetchall()

            # Treeview widget'ı ekleme
            self.tree1 = ttk.Treeview(self)

            self.tree1["columns"] = (
                "oduncID", "uyeAdi", "uyeSoyadi", "kitapAdi", "verilisTarihi", "teslimTarihi")
            self.tree1.column("#0", width=0, stretch=tk.NO)
            self.tree1.column("oduncID", anchor=tk.W, width=60)
            self.tree1.column("uyeAdi", anchor=tk.W, width=100)
            self.tree1.column("uyeSoyadi", anchor=tk.W, width=100)
            self.tree1.column("kitapAdi", anchor=tk.W, width=100)
            self.tree1.column("verilisTarihi", anchor=tk.W, width=100)
            self.tree1.column("teslimTarihi", anchor=tk.W, width=100)

            self.tree1.heading("#0", text="", anchor=tk.W)
            self.tree1.heading("oduncID", text="oduncID", anchor=tk.W)
            self.tree1.heading("uyeAdi", text="uyeAdi", anchor=tk.W)
            self.tree1.heading("uyeSoyadi", text="uyeSoyadi", anchor=tk.W)
            self.tree1.heading("kitapAdi", text="kitapAdi", anchor=tk.W)
            self.tree1.heading("verilisTarihi", text="verilisTarihi", anchor=tk.W)
            self.tree1.heading("teslimTarihi", text="teslimTarihi", anchor=tk.W)

            # Veritabanındaki verileri Treeview'a ekleme
            for row in rows:
                self.tree1.insert("", tk.END, values=(
                    row[0], row[1], row[2], row[3], row[4], row[5]))

            self.tree1.place(x=10, y=150)

        except Exception as e:
            messagebox.showerror("Hata!", f"{e}")


    def deliver(self): #teslim et
        try:
            borrow_ID = self.borrow_ID_entry.get()
            member_name = self.member_name_entry.get()
            member_surname = self.surname_entry.get()
            book_name = self.book_name_entry.get()

            if not borrow_ID or not member_name or not member_surname or not book_name:
                messagebox.showerror("Hata!", "Tüm alanların doldurulması gerekmektedir.")
                return


            book_name = self.book_name_entry.get()
            query_book_quantity = "SELECT kitapAdet FROM TblKitaplar WHERE kitapAd = ?"
            self.cursor.execute(query_book_quantity, (book_name,))
            book_quantity = self.cursor.fetchone()

            odunc_ID = self.borrow_ID_entry.get()
            query = "DELETE FROM Tbl_Odunver WHERE oduncID = ?"

            self.cursor.execute(query, (odunc_ID,))
            self.conn.commit()

            # Kitap miktarını güncelle
            updated_book_quantity = book_quantity[0] + 1
            query_update_quantity = "UPDATE TblKitaplar SET kitapAdet = ? WHERE kitapAd = ?"
            self.cursor.execute(query_update_quantity, (updated_book_quantity, book_name))
            self.conn.commit()

            messagebox.showinfo("Başarılı.", "Teslim Etme İşlemi Başarılı.")

        except Exception as e:
            messagebox.showerror("Hata!", f"Bir hata oluştu! {e}")
            print(e)

    def extend_time(self): #süre uzat
        try:
            borrow_ID = self.borrow_ID_entry_2.get()
            member_name = self.member_name_entry_2.get()
            member_surname = self.surname_entry_2.get()
            book_name = self.book_name_entry_2.get()
            release_date_str = self.release_date_entry_2.get()
            delivery_date_str = self.delivery_date_entry_2.get()


            if not borrow_ID or not member_name or not member_surname or not book_name or not release_date_str or not delivery_date_str:
                messagebox.showerror("Hata!", "Tüm alanların doldurulması gerekmektedir.")
                return

            # Tarih formatlarını doğrula ve datetime objelerine dönüştür
            try:
                release_date = datetime.strptime(release_date_str, "%Y-%m-%d")
                delivery_date = datetime.strptime(delivery_date_str, "%Y-%m-%d")
            except ValueError:
                messagebox.showerror("Hata!", "Tarih formatı YYYY-AA-GG olmalıdır.")
                return

            today = datetime.now()

            # Tarihlerin doğruluğunu kontrol et
            if release_date.date() < today.date():
                messagebox.showerror("Hata!", "Veriliş tarihi bugünden küçük olamaz.")
                return
            if delivery_date.date() <= today.date():
                messagebox.showerror("Hata!", "Teslim tarihi bugünden büyük olmalıdır.")
                return

            query = "UPDATE Tbl_Odunver SET uyeAdi = ?, uyeSoyadi = ?, kitapAdi = ?, verilisTarihi = ?, teslimTarihi = ? WHERE oduncID = ?;"
            self.cursor.execute(query, (member_name, member_surname, book_name, release_date, delivery_date, borrow_ID))
            self.conn.commit()

            messagebox.showinfo("Başarılı.", "Süre Uzatma İşlemi Başarılı.")

        except Exception as e:
            messagebox.showerror("Hata!", f"Bir hata oluştu! {e}")
