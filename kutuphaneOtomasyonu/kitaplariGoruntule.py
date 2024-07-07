
import customtkinter as ctk
import tkinter as tk
from PIL import Image
import pyodbc
from db_connection import get_db_connection
from tkinter import ttk
from tkinter import messagebox


class ViewBooks(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)

        ctk.set_appearance_mode('Dark')
        self.configure(fg_color="#6C5B7B")
        self.title("Kitapları Görüntüleme")
        self.geometry("1050x650")

        self.conn = get_db_connection()
        self.cursor = self.conn.cursor()

        self.create_viewbooks_widgets()

    def create_viewbooks_widgets(self):

        # 1. Başlığı ayarlama
        self.frame_1 = ctk.CTkFrame(self, width=350, height=70, fg_color="#DA727E")
        self.frame_1.place(x=10, y=20)
        self.tittle_1_lbl = ctk.CTkLabel(self.frame_1, text="Kitap Ara", text_color="#FFBC67", font=("Georgia", 30))
        self.tittle_1_lbl.place(x=50, y=20)

        # isim ile arama yapmak için toollar
        self.frame_2 = ctk.CTkFrame(self, width=350, height=100, fg_color="#DA727E")
        self.frame_2.place(x=10, y=100)

        self.book_name_lbl1 = ctk.CTkLabel(self.frame_2, text="Kitap Adı: ", text_color="#FFBC67", font=("Georgia", 15))
        self.book_name_lbl1.place(x=30, y=30)
        self.book_name_entry1 = ctk.CTkEntry(self.frame_2, text_color="#FFBC67", placeholder_text="Kitap adı", fg_color="transparent", font=("Georgia", 15))
        self.book_name_entry1.place(x=110, y=30)

        self.search_btn = ctk.CTkButton(self.frame_2, width=70, height=70, text="Ara", text_color="#DA727E", fg_color="#6C5B7B", font=("Georgia", 15), command=self.book_search)
        self.search_btn.place(x=270, y=15)

        self.list_btn = ctk.CTkButton(self, width=70, height=70, text="Kitapları Listele", text_color="#FFBC67", fg_color="#DA727E", font=("Georgia", 15), command= self.list_books)
        self.list_btn.place(x=200, y=510)

        # Kitap Bilgi İşlemleri
        self.frame_2 = ctk.CTkFrame(self, width=420, height=600, fg_color="#DA727E")
        self.frame_2.place(x=600, y=20)

        self.book_processing_lbl = ctk.CTkLabel(self.frame_2, text="Kitapları Sil ve Güncelle", text_color="#355C7D", font=("Georgia", 30, "bold"))
        self.book_processing_lbl.place(x=20, y=10)

        self.book_ID_lbl = ctk.CTkLabel(self.frame_2, text="Kitap ID: ", text_color="#355C7D", font=("Georgia", 15))
        self.book_ID_lbl.place(x=20, y=60)
        self.book_ID_entry = ctk.CTkEntry(self.frame_2, placeholder_text="ID", text_color="white", font=("Georgia", 15))
        self.book_ID_entry.place(x=150, y=60)

        self.book_ISBN_lbl = ctk.CTkLabel(self.frame_2, text="Kitap ISBN NO: ", text_color="#355C7D", font=("Georgia", 15))
        self.book_ISBN_lbl.place(x=20, y=100)
        self.book_ISBN_entry = ctk.CTkEntry(self.frame_2, placeholder_text="ISBN No", text_color="white", font=("Georgia", 15))
        self.book_ISBN_entry.place(x=150, y=100)

        self.book_name_lbl2 = ctk.CTkLabel(self.frame_2, text="Kitap Adı: ", text_color="#355C7D", font=("Georgia", 15))
        self.book_name_lbl2.place(x=20, y=140)
        self.book_name_entry = ctk.CTkEntry(self.frame_2, placeholder_text="kitap adı", text_color="white", font=("Georgia", 15))
        self.book_name_entry.place(x=150, y=140)

        self.book_author_name_lbl = ctk.CTkLabel(self.frame_2, text="Kitap Yazar Adı: ", text_color="#355C7D", font=("Georgia", 15))
        self.book_author_name_lbl.place(x=20, y=180)
        self.book_author_entry = ctk.CTkEntry(self.frame_2, placeholder_text="yazar adı", text_color="white", font=("Georgia", 15))
        self.book_author_entry.place(x=150, y=180)

        self.book_page_lbl = ctk.CTkLabel(self.frame_2, text="Kitap Sayfa Sayısı: ", text_color="#355C7D", font=("Georgia", 15))
        self.book_page_lbl.place(x=20, y=220)
        self.book_page_entry = ctk.CTkEntry(self.frame_2, placeholder_text="kitap sayfa", text_color="white", font=("Georgia", 15))
        self.book_page_entry.place(x=150, y=220)

        self.book_publisher_lbl = ctk.CTkLabel(self.frame_2, text="Kitap Yayınevi: ", text_color="#355C7D", font=("Georgia", 15))
        self.book_publisher_lbl.place(x=20, y=260)
        self.book_publisher_entry = ctk.CTkEntry(self.frame_2, placeholder_text="yayınevi", text_color="white", font=("Georgia", 15))
        self.book_publisher_entry.place(x=150, y=260)

        self.book_type_lbl = ctk.CTkLabel(self.frame_2, text="Kitap Türü: ", text_color="#355C7D", font=("Georgia", 15))
        self.book_type_lbl.place(x=20, y=300)
        self.book_type_entry = ctk.CTkEntry(self.frame_2, placeholder_text="kitap tür", text_color="white", font=("Georgia", 15))
        self.book_type_entry.place(x=150, y=300)

        self.book_quantity_lbl = ctk.CTkLabel(self.frame_2, text="Kitap Adeti: ", text_color="#355C7D", font=("Georgia", 15))
        self.book_quantity_lbl.place(x=20, y=340)
        self.book_quantity_entry = ctk.CTkEntry(self.frame_2, placeholder_text="adet", text_color="white", font=("Georgia", 15))
        self.book_quantity_entry.place(x=150, y=340)

        self.delete_btn = ctk.CTkButton(self.frame_2, width=70, height=70, text="Sil", text_color="#DA727E", fg_color="#6C5B7B", font=("Georgia", 15), command=self.delete_book)
        self.delete_btn.place(x=125, y=390)

        self.update_btn = ctk.CTkButton(self.frame_2, width=70, height=70, text="Güncelle", text_color="#DA727E", fg_color="#6C5B7B", font=("Georgia", 15), command=self.book_updatee)
        self.update_btn.place(x=200, y=390)

    def list_books(self):

        self.cursor.execute("SELECT * FROM TblKitaplar")
        rows = self.cursor.fetchall()

        # Treeview widget'ı ekleme
        self.tree = ttk.Treeview(self)
        self.tree["columns"] = (
            "kitapID", "kitapISBNNO", "kitapAd", "kitapYazar", "kitapSayfa", "kitapYayinevi", "kitapTur", "kitapAdet")
        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.column("kitapID", anchor=tk.W, width=60)
        self.tree.column("kitapISBNNO", anchor=tk.W, width=100)
        self.tree.column("kitapAd", anchor=tk.W, width=100)
        self.tree.column("kitapYazar", anchor=tk.W, width=100)
        self.tree.column("kitapSayfa", anchor=tk.W, width=100)
        self.tree.column("kitapYayinevi", anchor=tk.W, width=100)
        self.tree.column("kitapTur", anchor=tk.W, width=100)
        self.tree.column("kitapAdet", anchor=tk.W, width=60)

        self.tree.heading("#0", text="", anchor=tk.W)
        self.tree.heading("kitapID", text="kitapID", anchor=tk.W)
        self.tree.heading("kitapISBNNO", text="kitapISBNNO", anchor=tk.W)
        self.tree.heading("kitapAd", text="kitapAd", anchor=tk.W)
        self.tree.heading("kitapYazar", text="kitapYazar", anchor=tk.W)
        self.tree.heading("kitapSayfa", text="kitapSayfa", anchor=tk.W)
        self.tree.heading("kitapYayinevi", text="kitapYayinevi", anchor=tk.W)
        self.tree.heading("kitapTur", text="kitapTur", anchor=tk.W)
        self.tree.heading("kitapAdet", text="kitapAdet", anchor=tk.W)

        # Veritabanındaki verileri Treeview'a ekleme
        for row in rows:
            self.tree.insert("", tk.END, values=(
                row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        self.tree.place(x=10, y=400)

        self.tree.bind("<Double-1>", self.on_double_click_2)

    def delete_book(self):
        try:
            book_ID = self.book_ID_entry.get()
            query = "DELETE FROM TblKitaplar WHERE kitapID = ?"

            self.cursor.execute(query, (book_ID,))
            self.conn.commit()
            messagebox.showinfo("Başarılı.", "Silme İşlemi Başarılı.")

        except Exception as e:
            messagebox.showerror("Hata!", f"Bir hata oluştu! {e}")

    def on_double_click_2(self, event):


        selected_item = self.tree.selection()[0]
        values = self.tree.item(selected_item, "values")


        self.book_ID_entry.delete(0, tk.END)
        self.book_ID_entry.insert(0, values[0])
        self.book_ISBN_entry.delete(0, tk.END)
        self.book_ISBN_entry.insert(0, values[1])
        self.book_name_entry.delete(0, tk.END)
        self.book_name_entry.insert(0, values[2])
        self.book_author_entry.delete(0, tk.END)
        self.book_author_entry.insert(0, values[3])
        self.book_page_entry.delete(0, tk.END)
        self.book_page_entry.insert(0, values[4])
        self.book_publisher_entry.delete(0, tk.END)
        self.book_publisher_entry.insert(0, values[5])
        self.book_type_entry.delete(0, tk.END)
        self.book_type_entry.insert(0, values[6])
        self.book_quantity_entry.delete(0, tk.END)
        self.book_quantity_entry.insert(0, values[7])


    def book_updatee(self):
        try:
            book_ID = self.book_ID_entry.get()
            book_ISBNNo = self.book_ISBN_entry.get()
            book_page = self.book_page_entry.get()
            book_publisher = self.book_publisher_entry.get().title()
            book_quantity = self.book_quantity_entry.get()


            query = "UPDATE TblKitaplar SET kitapISBNNo = ?, kitapSayfa = ?, kitapYayinevi = ?, kitapAdet = ? WHERE kitapID = ?;"
            self.cursor.execute(query, (book_ISBNNo, book_page, book_publisher, book_quantity, book_ID))
            self.conn.commit()

            messagebox.showinfo("Başarılı.", "Güncelleme İşlemi Başarılı.")

        except Exception as e:
            messagebox.showerror("Hata!", f"Bir hata oluştu! {e}")

    def book_search(self):
        try:
            book_name = self.book_name_entry1.get()

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
                self.tree.place(x=10, y=400)


            else:
                messagebox.showerror("Hata!!", f"Belirtilen isimde kitap bulunamadı.")

        except Exception as e:
            messagebox.showerror("Bir hata oluştu veya boş bırakmayınız!", f"{e}")
