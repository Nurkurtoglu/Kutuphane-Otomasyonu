import customtkinter as ctk
import tkinter as tk
from PIL import Image
import pyodbc
from db_connection import get_db_connection
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox
from datetime import datetime

class LendingBooks(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)

        ctk.set_appearance_mode('Dark')
        self.configure(fg_color="#6C5B7B")
        self.title("Ödünç Verme")
        self.geometry("1050x650")

        self.conn = get_db_connection()
        self.cursor = self.conn.cursor()


        self.create_lending_widgets()

    def create_lending_widgets(self):

        self.tittle_lbl = ctk.CTkLabel(self, text="KİTAP ÖDÜNÇ VERME", text_color="#B7D7D8", font=("Georgia", 30))
        self.tittle_lbl.pack()

        self.frame_1 = ctk.CTkFrame(self, width=500, height=100, fg_color="#C9DFF1")
        self.frame_1.place(x=10, y=40)
        self.book_name_lbl = ctk.CTkLabel(self.frame_1, text="Kitap Adı: ", text_color="#204E5F")
        self.book_name_lbl.place(x=10, y=30)
        self.book_name_entry = ctk.CTkEntry(self.frame_1, placeholder_text="kitap ad", text_color="#B7D7D8", font=("Georgia", 15))
        self.book_name_entry.place(x=70, y=30)
        self.search_btn_1 = ctk.CTkButton(self.frame_1,  width=70, height=40, text="Ara", text_color="#79A7A8", fg_color="#355C7D", font=("Georgia", 15), command=self.search_the_books)
        self.search_btn_1.place(x=250, y=30)
        self.list_book_btn = ctk.CTkButton(self.frame_1, width=70, height=40, text="Listele", text_color="#79A7A8", fg_color="#355C7D", font=("Georgia", 15), command=self.list_the_books)
        self.list_book_btn.place(x=350, y=30)


        self.frame_2 = ctk.CTkFrame(self, width=500, height=100, fg_color="#C9DFF1")
        self.frame_2.place(x=10, y=350)
        self.member_name_lbl = ctk.CTkLabel(self.frame_2, text="Üye Adı: ", text_color="#204E5F")
        self.member_name_lbl.place(x=10, y=30)
        self.member_name_entry = ctk.CTkEntry(self.frame_2, placeholder_text="üye ad", text_color="#B7D7D8", font=("Georgia", 15))
        self.member_name_entry.place(x=80, y=30)
        self.member_surname_lbl = ctk.CTkLabel(self.frame_2, text="Üye Soyadı: ", text_color="#204E5F")
        self.member_surname_lbl.place(x=10, y=60)
        self.member_surname_entry = ctk.CTkEntry(self.frame_2, placeholder_text="soyad", text_color="#B7D7D8", font=("Georgia", 15))
        self.member_surname_entry.place(x=80, y=60)
        self.search_btn_2 = ctk.CTkButton(self.frame_2, width=70, height=40, text="Ara", text_color="#79A7A8", fg_color="#355C7D", font=("Georgia", 15), command=self.search_the_member)
        self.search_btn_2.place(x=250, y=30)
        self.list_mem_btn = ctk.CTkButton(self.frame_2, width=70, height=40, text="Listele", text_color="#79A7A8", fg_color="#355C7D", font=("Georgia", 15), command=self.list_the_members)
        self.list_mem_btn.place(x=350, y=30)



        self.frame_3 = ctk.CTkFrame(self, width=350, height=300, fg_color="#C9DFF1")
        self.frame_3.place(x=600, y=60)
        self.member_ID_lbl = ctk.CTkLabel(self.frame_3, text="Üye ID: ", text_color="#204E5F")
        self.member_ID_lbl.place(x=10, y=30)
        self.member_ID_entry = ctk.CTkEntry(self.frame_3, placeholder_text=" üye ID", text_color="#B7D7D8", font=("Georgia", 15))
        self.member_ID_entry.place(x=100, y=30)

        self.book_ID_lbl = ctk.CTkLabel(self.frame_3, text="Kitap ID: ", text_color="#204E5F")
        self.book_ID_lbl.place(x=10, y=60)
        self.book_ID_entry = ctk.CTkEntry(self.frame_3, placeholder_text="kitap ID", text_color="#B7D7D8", font=("Georgia", 15))
        self.book_ID_entry.place(x=100, y=60)

        self.release_date_lbl = ctk.CTkLabel(self.frame_3, text="Veriliş Tarihi: ", text_color="#204E5F")
        self.release_date_lbl.place(x=10, y=90)
        self.release_date_entry = ctk.CTkEntry(self.frame_3, text_color="#B7D7D8", font=("Georgia", 15))
        self.release_date_entry.place(x=100, y=90)


        self.delivery_date_lbl = ctk.CTkLabel(self.frame_3, text="Teslim Tarihi: ", text_color="#204E5F")
        self.delivery_date_lbl.place(x=10, y=120)
        self.delivery_date_entry = ctk.CTkEntry(self.frame_3, text_color="#B7D7D8", font=("Georgia", 15))
        self.delivery_date_entry.place(x=100, y=120)

        # Tarih Seçicileri ve Onay Düğmeleri
        frame_4 = ttk.Frame(self.frame_3)
        frame_4.place(x=305, y=120)
        self.release_date_picker = DateEntry(frame_4, width=12, background='darkblue', foreground='white', borderwidth=2, year=2023, month=6, day=4, date_pattern='y-mm-dd')
        self.release_date_picker.pack()

        frame_5 = ttk.Frame(self.frame_3)
        frame_5.place(x=305, y=155)
        self.delivery_date_picker = DateEntry(frame_5, width=12, background='darkblue', foreground='white', borderwidth=2, year=2023, month=6, day=4, date_pattern='y-mm-dd')
        self.delivery_date_picker.pack()

        def select_release_date():
            selected_date = self.release_date_picker.get_date()
            self.release_date_entry.delete(0, ctk.END)
            self.release_date_entry.insert(0, selected_date.strftime("%Y-%m-%d"))

        def select_delivery_date():
            selected_date = self.delivery_date_picker.get_date()
            self.delivery_date_entry.delete(0, ctk.END)
            self.delivery_date_entry.insert(0, selected_date.strftime("%Y-%m-%d"))

        self.select_release_date_btn = ctk.CTkButton(self.frame_3, text="Veriliş Tarihini Seç", text_color="#393E46", fg_color="#355C7D", command=select_release_date)
        self.select_release_date_btn.place(x=10, y=150)

        self.select_delivery_date_btn = ctk.CTkButton(self.frame_3, text="Teslim Tarihini Seç", text_color="#393E46", fg_color="#355C7D", command=select_delivery_date)
        self.select_delivery_date_btn.place(x=150, y=150)

        self.lend_btn = ctk.CTkButton(self.frame_3, width=70, height=40, text="ÖDÜNÇ VER", text_color="#393E46", fg_color="#355C7D", font=("Georgia", 15), command=self.lend)
        self.lend_btn.place(x=100, y=200)



    def list_the_books(self):

        self.cursor.execute("SELECT * FROM TblKitaplar")
        rows_2 = self.cursor.fetchall()

        # Treeview widget'ı ekleme
        self.tree2 = ttk.Treeview(self)

        self.tree2["columns"] = (
            "kitapID", "kitapISBNNO", "kitapAd", "kitapYazar", "kitapSayfa", "kitapYayinevi", "kitapTur",b"kitapAdet")
        self.tree2.column("#0", width=0, stretch=tk.NO)
        self.tree2.column("kitapID", anchor=tk.W, width=60)
        self.tree2.column("kitapISBNNO", anchor=tk.W, width=100)
        self.tree2.column("kitapAd", anchor=tk.W, width=100)
        self.tree2.column("kitapYazar", anchor=tk.W, width=100)
        self.tree2.column("kitapSayfa", anchor=tk.W, width=100)
        self.tree2.column("kitapYayinevi", anchor=tk.W, width=100)
        self.tree2.column("kitapTur", anchor=tk.W, width=100)
        self.tree2.column("kitapAdet", anchor=tk.W, width=60)

        self.tree2.heading("#0", text="", anchor=tk.W)
        self.tree2.heading("kitapID", text="kitapID", anchor=tk.W)
        self.tree2.heading("kitapISBNNO", text="kitapISBNNO", anchor=tk.W)
        self.tree2.heading("kitapAd", text="kitapAd", anchor=tk.W)
        self.tree2.heading("kitapYazar", text="kitapYazar", anchor=tk.W)
        self.tree2.heading("kitapSayfa", text="kitapSayfa", anchor=tk.W)
        self.tree2.heading("kitapYayinevi", text="kitapYayinevi", anchor=tk.W)
        self.tree2.heading("kitapTur", text="kitapTur", anchor=tk.W)
        self.tree2.heading("kitapAdet", text="kitapAdet", anchor=tk.W)

        # Veritabanındaki verileri Treeview'a ekleme
        for row in rows_2:
            self.tree2.insert("", tk.END, values=(
                row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        self.tree2.place(x=10, y=200)

        self.tree2.bind("<Double-1>", self.on_double_click_2)


    def list_the_members(self):
        try:
            self.cursor.execute("SELECT * FROM Tbl_Uyeler")
            rows = self.cursor.fetchall()

            # Treeview widget'ı ekleme
            self.tree1 = ttk.Treeview(self)

            self.tree1["columns"] = (
                "uyeID", "uyeAd", "uyeSoyad", "uyeDogumTarihi", "uyeCinsiyet", "uyeTelefon", "uyeEmail", "uyeAdres")
            self.tree1.column("#0", width=0, stretch=tk.NO)
            self.tree1.column("uyeID", anchor=tk.W, width=60)
            self.tree1.column("uyeAd", anchor=tk.W, width=100)
            self.tree1.column("uyeSoyad", anchor=tk.W, width=100)
            self.tree1.column("uyeDogumTarihi", anchor=tk.W, width=100)
            self.tree1.column("uyeCinsiyet", anchor=tk.W, width=100)
            self.tree1.column("uyeTelefon", anchor=tk.W, width=100)
            self.tree1.column("uyeEmail", anchor=tk.W, width=100)
            self.tree1.column("uyeAdres", anchor=tk.W, width=150)

            self.tree1.heading("#0", text="", anchor=tk.W)
            self.tree1.heading("uyeID", text="uyeID", anchor=tk.W)
            self.tree1.heading("uyeAd", text="uyeAd", anchor=tk.W)
            self.tree1.heading("uyeSoyad", text="uyeSoyad", anchor=tk.W)
            self.tree1.heading("uyeDogumTarihi", text="uyeDogumTarihi", anchor=tk.W)
            self.tree1.heading("uyeCinsiyet", text="uyeCinsiyet", anchor=tk.W)
            self.tree1.heading("uyeTelefon", text="uyeTelefon", anchor=tk.W)
            self.tree1.heading("uyeEmail", text="uyeEmail", anchor=tk.W)
            self.tree1.heading("uyeAdres", text="uyeAdres", anchor=tk.W)

            # Veritabanındaki verileri Treeview'a ekleme
            for row in rows:
                self.tree1.insert("", tk.END, values=(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

            self.tree1.place(x=10, y=580)

            self.tree1.bind("<Double-1>", self.on_double_click_1)


        except Exception as e:
            messagebox.showerror("Hata", f"{e}")

    def on_double_click_1(self, event):
        try:

            selected_item = self.tree1.selection()[0]
            values = self.tree1.item(selected_item, "values")

            # Entry widget'larına değerleri yerleştirme

            self.member_ID_entry.delete(0, tk.END)
            self.member_ID_entry.insert(0, values[0])

        except Exception as e:
            messagebox.showerror("Hata", f"{e}")

    def on_double_click_2(self, event):

        selected_item = self.tree2.selection()[0]
        values = self.tree2.item(selected_item, "values")

        # Entry widget'larına değerleri yerleştirme
        self.book_ID_entry.delete(0, tk.END)
        self.book_ID_entry.insert(0, values[0])

    def search_the_member(self):
        try:
            name = self.member_name_entry.get()
            surname = self.member_surname_entry.get()

            query = "SELECT * FROM Tbl_Uyeler WHERE uyeAd = ? AND uyeSoyad = ?"
            self.cursor.execute(query, (name, surname))
            rowss = self.cursor.fetchall()

            if rowss:
                for row in rowss:
                    # Treeview widget'ı ekleme
                    self.tree3 = ttk.Treeview(self)
                    self.tree3["columns"] = (
                        "uyeID", "uyeAd", "uyeSoyad", "uyeDogumTarihi", "uyeCinsiyet", "uyeTelefon", "uyeEmail",
                        "uyeAdres")
                    self.tree3.column("#0", width=0, stretch=tk.NO)
                    self.tree3.column("uyeID", anchor=tk.W, width=60)
                    self.tree3.column("uyeAd", anchor=tk.W, width=100)
                    self.tree3.column("uyeSoyad", anchor=tk.W, width=100)
                    self.tree3.column("uyeDogumTarihi", anchor=tk.W, width=100)
                    self.tree3.column("uyeCinsiyet", anchor=tk.W, width=100)
                    self.tree3.column("uyeTelefon", anchor=tk.W, width=100)
                    self.tree3.column("uyeEmail", anchor=tk.W, width=100)
                    self.tree3.column("uyeAdres", anchor=tk.W, width=150)

                    self.tree3.heading("#0", text="", anchor=tk.W)
                    self.tree3.heading("uyeID", text="uyeID", anchor=tk.W)
                    self.tree3.heading("uyeAd", text="uyeAd", anchor=tk.W)
                    self.tree3.heading("uyeSoyad", text="uyeSoyad", anchor=tk.W)
                    self.tree3.heading("uyeDogumTarihi", text="uyeDogumTarihi", anchor=tk.W)
                    self.tree3.heading("uyeCinsiyet", text="uyeCinsiyet", anchor=tk.W)
                    self.tree3.heading("uyeTelefon", text="uyeTelefon", anchor=tk.W)
                    self.tree3.heading("uyeEmail", text="uyeEmail", anchor=tk.W)
                    self.tree3.heading("uyeAdres", text="uyeAdres", anchor=tk.W)

                    self.tree3.insert("", tk.END, values=(
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
                self.tree3.place(x=10, y=580)




            else:
                messagebox.showerror("Hata!!", f"Belirtilen isimde üye bulunamadı.")

        except Exception as e:
            messagebox.showerror("Bir hata oluştu veya boş bırakmayınız!", f"{e}")

    def search_the_books(self):
        try:
            book_name = self.book_name_entry.get()

            query = "SELECT * FROM TblKitaplar WHERE kitapAd = ?"
            self.cursor.execute(query, (book_name))
            rowss = self.cursor.fetchall()

            if rowss:
                for row in rowss:
                    self.tree = ttk.Treeview(self)
                    self.tree["columns"] = (
                        "kitapID", "kitapISBNNo", "kitapAd", "kitapYazar", "kitapSayfa", "kitapYayinevi", "kitapTur",
                        "kitapAdet")
                    self.tree.column("#0", width=0, stretch=tk.NO)
                    self.tree.column("kitapID", anchor=tk.W, width=60)
                    self.tree.column("kitapISBNNo", anchor=tk.W, width=100)
                    self.tree.column("kitapAd", anchor=tk.W, width=100)
                    self.tree.column("kitapYazar", anchor=tk.W, width=100)
                    self.tree.column("kitapSayfa", anchor=tk.W, width=100)
                    self.tree.column("kitapYayinevi", anchor=tk.W, width=100)
                    self.tree.column("kitapTur", anchor=tk.W, width=100)
                    self.tree.column("kitapAdet", anchor=tk.W, width=60)

                    self.tree.heading("#0", text="", anchor=tk.W)
                    self.tree.heading("kitapID", text="kitapID", anchor=tk.W)
                    self.tree.heading("kitapISBNNo", text="kitapISBNNo", anchor=tk.W)
                    self.tree.heading("kitapAd", text="kitapAd", anchor=tk.W)
                    self.tree.heading("kitapYazar", text="kitapYazar", anchor=tk.W)
                    self.tree.heading("kitapSayfa", text="kitapSayfa", anchor=tk.W)
                    self.tree.heading("kitapYayinevi", text="kitapYayinevi", anchor=tk.W)
                    self.tree.heading("kitapTur", text="kitapTur", anchor=tk.W)
                    self.tree.heading("kitapAdet", text="kitapAdet", anchor=tk.W)

                    self.tree.insert("", tk.END, values=(
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
                self.tree.place(x=10, y=200)




            else:
                messagebox.showerror("Hata!!", f"Belirtilen isimde kitap bulunamadı.")

        except Exception as e:
            messagebox.showerror("Bir hata oluştu veya boş bırakmayınız!", f"{e}")

    def lend(self):

        try:
            member_id = self.member_ID_entry.get()
            book_id = self.book_ID_entry.get()
            release_date_str = self.release_date_entry.get()  # veriliş tarihi
            delivery_date_str = self.delivery_date_entry.get()  # teslim tarihi

            # Eksik alanları kontrol et
            if not member_id or not book_id or not release_date_str or not delivery_date_str:
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

            # Üye adı ve soyadını sorgula
            query_member = "SELECT uyeAd, uyeSoyad FROM Tbl_Uyeler WHERE uyeID = ?"
            self.cursor.execute(query_member, (member_id,))
            member_name_surname = self.cursor.fetchone()

            if not member_name_surname:
                messagebox.showerror("Hata!", "Geçersiz üye ID.")
                return

            # Kitap adını sorgula
            query_book = "SELECT kitapAd FROM TblKitaplar WHERE kitapID = ?"
            self.cursor.execute(query_book, (book_id,))
            book_name = self.cursor.fetchone()

            if not book_name:
                messagebox.showerror("Hata!", "Geçersiz kitap ID.")
                return

            # Kitap miktarını sorgula
            query_book_quantity = "SELECT kitapAdet FROM TblKitaplar WHERE kitapID = ?"
            self.cursor.execute(query_book_quantity, (book_id,))
            book_quantity = self.cursor.fetchone()

            if not book_quantity or book_quantity[0] <= 0:
                messagebox.showerror("Hata!", "Kitap mevcut değil.")
                return

            # Ödünç verme tablosuna veri ekle
            query_insert = "INSERT INTO Tbl_Odunver (uyeAdi, uyeSoyadi, kitapAdi, verilisTarihi, teslimTarihi) VALUES (?, ?, ?, ?, ?)"
            self.cursor.execute(query_insert, (
                member_name_surname[0], member_name_surname[1], book_name[0], release_date_str, delivery_date_str))
            self.conn.commit()

            # Kitap miktarını güncelle
            updated_book_quantity = book_quantity[0] - 1
            query_update_quantity = "UPDATE TblKitaplar SET kitapAdet = ? WHERE kitapID = ?"
            self.cursor.execute(query_update_quantity, (updated_book_quantity, book_id))
            self.conn.commit()

            messagebox.showinfo("İşlem Başarılı.", "Ödünç Verme İşlemi Başarılı.")

        except Exception as e:
            messagebox.showerror("Bir hata oluştu!", f"{e}")
            print(e)



