import customtkinter as ctk
import tkinter as tk
from PIL import Image
import pyodbc
from db_connection import get_db_connection
from tkinter import ttk
from tkinter import messagebox

class AddBook(ctk.CTkToplevel):
    def __init__(self,parent):
        super().__init__(parent)

        ctk.set_appearance_mode('Dark')
        self.configure(fg_color="#6C5B7B")
        self.title("Kitap Ekleme")
        self.geometry("400x650")

        self.conn = get_db_connection()
        self.cursor = self.conn.cursor()

        self.book_types = ["Roman", "Hikaye", "Biyografi", "Otobiyografi", "Deneme", "Tarih"]

        self.create_addbook_widgets()

    def create_addbook_widgets(self):

        # Başlık
        self.tittle_frame = ctk.CTkFrame(self, width=300, height=80, fg_color="#CCB2B3")
        self.tittle_frame.pack()
        self.tittle_lbl = ctk.CTkLabel(self.tittle_frame, text="KİTAP EKLEME", text_color="#193441", font=("Times New Roman", 30))
        self.tittle_lbl.place(x=30, y=25)


        # Kullanıcı giriş toolları
        self.frame_2 = ctk.CTkFrame(self, width=350, height=500, fg_color="#CCB2B3")
        self.frame_2.pack(pady=160)

        self.book_ISBN_lbl = ctk.CTkLabel(self.frame_2, text="Kitap ISBN NO: ", text_color="#FCFFF5", font=("Georgia", 15))
        self.book_ISBN_lbl.place(x=30, y=10)
        self.book_ISBN_entry = ctk.CTkEntry(self.frame_2, placeholder_text="Kitap ISBN NO", text_color="#FCFFF5", font=("Georgia", 15))
        self.book_ISBN_entry.place(x=150, y=10)

        self.book_name_lbl = ctk.CTkLabel(self.frame_2, text="Kitap Adı: ", text_color="#FCFFF5", font=("Georgia", 15))
        self.book_name_lbl.place(x=30, y=40)
        self.book_name_entry = ctk.CTkEntry(self.frame_2, placeholder_text="Kitap Ad", text_color="#FCFFF5", font=("Georgia", 15))
        self.book_name_entry.place(x=150, y=40)

        self.book_author_lbl = ctk.CTkLabel(self.frame_2, text="Yazar Adı: ", text_color="#FCFFF5", font=("Georgia", 15))
        self.book_author_lbl.place(x=30, y=70)
        self.book_author_entry = ctk.CTkEntry(self.frame_2, placeholder_text="Yazar Ad", text_color="#FCFFF5", font=("Georgia", 15))
        self.book_author_entry.place(x=150, y=70)

        self.book_page_lbl = ctk.CTkLabel(self.frame_2, text="Kitap Sayfa: ", text_color="#FCFFF5", font=("Georgia", 15))
        self.book_page_lbl.place(x=30, y=130)
        self.book_page_entry = ctk.CTkEntry(self.frame_2, placeholder_text="Kitap Sayfa", text_color="#FCFFF5", font=("Georgia", 15))
        self.book_page_entry.place(x=150, y=130)

        self.book_publisher_lbl = ctk.CTkLabel(self.frame_2, text="Kitap Yayınevi: ", text_color="#FCFFF5", font=("Georgia", 15))
        self.book_publisher_lbl.place(x=30, y=130)
        self.book_publisher_entry = ctk.CTkEntry(self.frame_2, placeholder_text="Kitap Yayınevi", text_color="#FCFFF5", font=("Georgia", 15))
        self.book_publisher_entry.place(x=150, y=130)

        self.book_type_lbl = ctk.CTkLabel(self.frame_2, text="Kitap Tür: ", text_color="#FCFFF5", font=("Georgia", 15))
        self.book_type_lbl.place(x=30, y=160)
        self.book_type_cmb_box = ctk.CTkComboBox(self.frame_2, values=self.book_types, text_color="#FCFFF5", font=("Georgia", 15))
        self.book_type_cmb_box.place(x=150, y=160)

        self.book_quantity_lbl = ctk.CTkLabel(self.frame_2, text="Kitap Adet: ", text_color="#FCFFF5", font=("Georgia", 15))
        self.book_quantity_lbl.place(x=30, y=190)
        self.book_quantity_entry = ctk.CTkEntry(self.frame_2, placeholder_text="Kitap Adet", text_color="#FCFFF5", font=("Georgia", 15))
        self.book_quantity_entry.place(x=150, y=190)

        self.add_book_button = ctk.CTkButton(self, text="Kitap Ekle ", text_color="#193441", fg_color="#CCB2B3", width=100, height=80, font=("Georgia", 15), command=self.add_book)
        self.add_book_button.place(x=130, y=500)

    def add_book(self):
        try:
            book_ISBNNO = self.book_ISBN_entry.get()
            book_name = self.book_name_entry.get().title()
            book_author = self.book_author_entry.get().title()
            book_page = self.book_page_entry.get()
            book_publisher = self.book_publisher_entry.get().title()
            book_type = self.book_type_cmb_box.get().capitalize()
            book_quantity = int(self.book_quantity_entry.get())


            query = ("INSERT INTO TblKitaplar (kitapISBNNO, kitapAd, kitapYazar, kitapSayfa, kitapYayinevi, kitapTur, "
                     "kitapAdet) VALUES (?, ?, ?, ?, ?, ?, ?)")

            self.cursor.execute(query, book_ISBNNO, book_name, book_author, book_page, book_publisher, book_type, book_quantity)

            self.conn.commit()

            messagebox.showinfo("İşlem Başarılı.", "Kitap Ekleme İşlemi Başarılı.")

        except Exception as e:
            messagebox.showerror("Hata", f"{e}")


