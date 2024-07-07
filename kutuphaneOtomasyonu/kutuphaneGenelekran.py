import customtkinter as ctk
from PIL import Image
import pyodbc
from db_connection import get_db_connection
from uyeEkle import AddMember
from kullaniciEkle import AddUser
from uyeIslemleri import MemberOperations
from kullanici_Islemleri import UserOperations
from kitapEkle import AddBook
from kitaplariGoruntule import ViewBooks
from oduncTakip import BorrowFollowUp
from oduncVer import LendingBooks

class generalDisplay(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)

        ctk.set_appearance_mode('Dark')
        self.configure(fg_color="#6C5B7B")
        self.title("Genel Ekran")
        self.geometry("550x450")
        self.create_widgets()

    def create_widgets(self):

        image_path_member = "C:\\Users\\EXCALIBUR\\OneDrive\\Masaüstü\\kutuphaneresimler\\member.png"
        image_member = ctk.CTkImage(dark_image=Image.open(image_path_member), size=(80, 80))

        image_path_human = "C:\\Users\\EXCALIBUR\\OneDrive\\Masaüstü\\kutuphaneresimler\\man.png"
        image_human = ctk.CTkImage(dark_image=Image.open(image_path_human), size=(80, 80))

        image_path_document = "C:\\Users\\EXCALIBUR\\OneDrive\\Masaüstü\\kutuphaneresimler\\document.png"
        image_document = ctk.CTkImage(dark_image=Image.open(image_path_document), size=(80, 80))

        image_path_timestudy = "C:\\Users\\EXCALIBUR\\OneDrive\\Masaüstü\\kutuphaneresimler\\time-to-study.png"
        image_timestudy = ctk.CTkImage(dark_image=Image.open(image_path_timestudy), size=(80, 80))

        image_path_addbook = "C:\\Users\\EXCALIBUR\\OneDrive\\Masaüstü\\kutuphaneresimler\\add.png"
        image_addbook = ctk.CTkImage(dark_image=Image.open(image_path_addbook), size=(80, 80))

        image_path_bookshelf = "C:\\Users\\EXCALIBUR\\OneDrive\\Masaüstü\\kutuphaneresimler\\bookshelf.png"
        image_bookshelf = ctk.CTkImage(dark_image=Image.open(image_path_bookshelf), size=(80, 80))

        image_path_adduser = "C:\\Users\\EXCALIBUR\\OneDrive\\Masaüstü\\kutuphaneresimler\\privacy.png"
        image_adduser = ctk.CTkImage(dark_image=Image.open(image_path_adduser), size=(80, 80))

        image_path_operations = "C:\\Users\\EXCALIBUR\\OneDrive\\Masaüstü\\kutuphaneresimler\\operations.png"
        image_operations = ctk.CTkImage(dark_image=Image.open(image_path_operations), size=(80, 80))


        # Başlık
        self.homepage_lbl = ctk.CTkLabel(self, text="ANASAYFA", text_color="#91AA9D", font= ("Comic Sans MS", 30, "bold"))
        self.homepage_lbl.pack(pady=10)

        # Üye Ekle
        self.member_add_button = ctk.CTkButton(self, text="", width=100, height=100, fg_color="#C06C84", image=image_member, command=self.show_add_member)
        self.member_add_button.place(x=20, y=100)
        self.member_add_lbl = ctk.CTkLabel(self, text="ÜYE EKLE", text_color="#FCFFF5")
        self.member_add_lbl.place(x=40, y=200)

        # Üye İşlemleri
        self.member_operations_button = ctk.CTkButton(self, text="", width=100, height=100, fg_color="#C06C84", image=image_human, command=self.show_member_operations)
        self.member_operations_button.place(x=20, y=270)
        self.member_operations_lbl = ctk.CTkLabel(self, text="ÜYE İŞLEMLERİ", text_color="#FCFFF5")
        self.member_operations_lbl.place(x=23, y=370)

        # Ödünç Verme
        self.lend_button = ctk.CTkButton(self, text="", width=100, height=100, fg_color="#C06C84", image=image_document, command=self.show_lending_books)
        self.lend_button.place(x=150, y=100)
        self.lend_lbl = ctk.CTkLabel(self, text="ÖDÜNÇ VER", text_color="#FCFFF5")
        self.lend_lbl.place(x=160, y=200)

        # Ödünç Takip
        self.tacking_loan_button = ctk.CTkButton(self, text="", width=100, height=100, fg_color="#C06C84", image=image_timestudy, command=self.show_borrow_followup)
        self.tacking_loan_button.place(x=150, y=270)
        self.tacking_loan_lbl = ctk.CTkLabel(self, text="ÖDÜNÇ TAKİP", text_color="#FCFFF5")
        self.tacking_loan_lbl.place(x=160, y=370)

        # kitap Ekle
        self.add_book_button = ctk.CTkButton(self, text="", width=100, height=100, fg_color="#C06C84", image=image_addbook, command=self.show_add_book)
        self.add_book_button.place(x=280, y=100)
        self.add_book_lbl = ctk.CTkLabel(self, text="KİTAP EKLE", text_color="#FCFFF5")
        self.add_book_lbl.place(x=290, y=200)

        # Kitapları görüntüle
        self.view_books_button = ctk.CTkButton(self, text="", width=100, height=100, fg_color="#C06C84", image=image_bookshelf, command=self.show_view_book)
        self.view_books_button.place(x=280, y=270)
        self.view_books_lbl = ctk.CTkLabel(self, text="KİTAPLARI \n GÖRÜNTÜLE", text_color="#FCFFF5")
        self.view_books_lbl.place(x=280, y=374)

        # Kullanıcı ekle
        self.add_user_button = ctk.CTkButton(self, text="", width=100, height=100, fg_color="#C06C84", image=image_adduser, command=self.show_add_user)
        self.add_user_button.place(x=410, y=100)
        self.add_user_lbl = ctk.CTkLabel(self, text="KULLANICI EKLE", text_color="#FCFFF5")
        self.add_user_lbl.place(x=410, y=200)

        # Kullanıcı işlemleri
        self.user_opertions_button = ctk.CTkButton(self, text="", width=100, height=100, fg_color="#C06C84", image=image_operations, command=self.show_user_operations)
        self.user_opertions_button.place(x=410, y=270)
        self.user_opertions_lbl = ctk.CTkLabel(self, text="KULLANICI İŞLEMLERİ", text_color="#FCFFF5")
        self.user_opertions_lbl.place(x=400, y=370)

    def show_add_member(self): # uye ekleme sayfasina git
        self.add_member = AddMember(self)
        self.add_member.grab_set()

    def show_add_user(self): # kullanici ekleme sayfasina git
        self.add_user = AddUser(self)
        self.add_user.grab_set()


    def show_member_operations(self): # üye işlemleri sayfasina git
        self.member_operation = MemberOperations(self)
        self.member_operation.grab_set()


    def show_user_operations(self): # kullanici işlemleri sayfasina git
        self.user_operation = UserOperations(self)
        self.user_operation.grab_set()


    def show_add_book(self): # kullanici işlemleri sayfasina git
        self.add_book= AddBook(self)
        self.add_book.grab_set()

    def show_view_book(self):
        self.view_book = ViewBooks(self)
        self.view_book.grab_set()

    def show_borrow_followup(self):
        self.borrow_follow = BorrowFollowUp(self)
        self.borrow_follow.grab_set()

    def show_lending_books(self):
        self.lending = LendingBooks(self)
        self.lending.grab_set()

