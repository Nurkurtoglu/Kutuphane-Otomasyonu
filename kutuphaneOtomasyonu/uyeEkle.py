import customtkinter as ctk
import tkinter as tk
from PIL import Image
from db_connection import get_db_connection
from tkinter import ttk
from tkinter import messagebox

class AddMember(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        ctk.set_appearance_mode('Dark')
        self.configure(fg_color="#6C5B7B")
        self.title("Uye Ekleme")
        self.geometry("800x700")

        self.conn = get_db_connection()
        self.cursor = self.conn.cursor()

        self.create_member_widgets()


    def create_member_widgets(self):

        self.tittle_lbl = ctk.CTkLabel(self, text="ÜYE EKLEME", text_color="#F8B195", font=("Georgia", 50, "bold"))
        self.tittle_lbl.place(x=70, y=10)

        # Arama yapmak için isim soyisim label ve entry

        self.frame1 = ctk.CTkFrame(self, width=650, height=100, fg_color="#C06C84")
        self.frame1.place(x=50, y=90)
        self.name_lbl = ctk.CTkLabel(self.frame1, text="İsim:", bg_color="transparent")
        self.name_lbl.place(x=50, y=10)
        self.name_text = ctk.CTkEntry(self.frame1, placeholder_text="İsim", bg_color="transparent", fg_color="transparent", border_color="black")
        self.name_text.place(x=150, y=10)

        self.surname_lbl = ctk.CTkLabel(self.frame1, text="Soyisim:", bg_color="transparent")
        self.surname_lbl.place(x=50, y=50)
        self.surname_text = ctk.CTkEntry(self.frame1, placeholder_text="Soyisim", bg_color="transparent", fg_color="transparent", border_color="black")
        self.surname_text.place(x=150, y=50)

        self.search_person_btn = ctk.CTkButton(self.frame1, text="Kişiyi Ara", width=75, height=75, bg_color="transparent", fg_color="#3E606F", command=self.searh_person)
        self.search_person_btn.place(x=300, y=10)
        self.list_members_btn = ctk.CTkButton(self.frame1, text="Üyeleri Listele", width=70, height=70,  fg_color="#3E606F", command=self.list_person)
        self.list_members_btn.place(x=400, y=10)


        # Uye Ekleme için widgets

        self.frame2 = ctk.CTkFrame(self, width=650, height=260, fg_color="#C06C84")
        self.frame2.place(x=50, y=410)

        # Başlık
        self.new_tittle = ctk.CTkLabel(self.frame2, text="Yeni Üye Ekle", font=("Verdana", 40, "bold"))
        self.new_tittle.place(x=10, y=5)

        self.name2_lbl = ctk.CTkLabel(self.frame2, text="İsim:")
        self.name2_lbl.place(x=50, y=70)
        self.name_text2 = ctk.CTkEntry(self.frame2, placeholder_text="İsim", fg_color="transparent", border_color="black")
        self.name_text2.place(x=150, y=70)

        self.surname_lbl2 = ctk.CTkLabel(self.frame2, text="Soyisim")
        self.surname_lbl2.place(x=50, y=100)
        self.surname_text2 = ctk.CTkEntry(self.frame2, placeholder_text="Soyisim", fg_color="transparent", border_color="black")
        self.surname_text2.place(x=150, y=100)

        self.birthday_lbl = ctk.CTkLabel(self.frame2, text="Doğum Tarihi: ")
        self.birthday_lbl.place(x=50, y=130)
        self.birthday_entry = ctk.CTkEntry(self.frame2, placeholder_text="Doğum Tarihi", fg_color="transparent", border_color="black")
        self.birthday_entry.place(x=150, y=130)

        self.gender_lbl = ctk.CTkLabel(self.frame2, text="Cinsiyet: ")
        self.gender_lbl.place(x=50, y=160)
        self.gender_entry = ctk.CTkEntry(self.frame2, placeholder_text="Cinsiyet", fg_color="transparent", border_color="black")
        self.gender_entry.place(x=150, y=160)

        self.tel_lbl = ctk.CTkLabel(self.frame2, text="Tel No: ")
        self.tel_lbl.place(x=50, y=190)
        self.tel_entry = ctk.CTkEntry(self.frame2, placeholder_text="Tel No", fg_color="transparent",border_color="black")
        self.tel_entry.place(x=150, y=190)

        self.email_lbl = ctk.CTkLabel(self.frame2, text="E-mail: ")
        self.email_lbl.place(x=50, y=220)
        self.email_entry = ctk.CTkEntry(self.frame2, placeholder_text="E-mail", fg_color="transparent", border_color="black")
        self.email_entry.place(x=150, y=220)

        self.adress_lbl = ctk.CTkLabel(self.frame2, text="Adres: ")
        self.adress_lbl.place(x=300, y=70)
        self.adress_txtbox = ctk.CTkTextbox(self.frame2, width=150, height=150, fg_color="#FCFFF5", text_color="black",)
        self.adress_txtbox.place(x=350, y=70)

        self.add_person_btn_2 = ctk.CTkButton(self.frame2, text="Yeni Üye Ekle", width=70, height=70, fg_color="#3E606F", command=self.add_member)
        self.add_person_btn_2.place(x=520, y=100)



    def add_member(self):
        try:
            name = self.name_text2.get().capitalize()
            surname = self.surname_text2.get().capitalize()
            birthday = self.birthday_entry.get()
            gender = self.gender_entry.get().capitalize()
            telno = self.tel_entry.get()
            email = self.email_entry.get()
            adress = self.adress_txtbox.get("1.0", ctk.END).title()

            if not name or not surname or not birthday or not gender or not telno or not email or not adress:
                messagebox.showerror("Hata!", "Tüm alanların doldurulması gerekmektedir.")
                return

            if gender not in ["Kadın", "Erkek"]:
                messagebox.showerror("Geçersiz!", "Geçersiz cinsiyet bilgisi. Lütfen 'Kadın' veya 'Erkek' giriniz.")
                return

            query = ("INSERT INTO Tbl_Uyeler (uyeAd, uyeSoyad, uyeDogumTarihi, uyeCinsiyet, uyeTelefon, uyeEmail, "
                     "uyeAdres) VALUES (?, ?, ?, ?, ?, ?, ?)")

            self.cursor.execute(query, name, surname, birthday, gender, telno, email, adress)

            self.conn.commit()

            messagebox.showinfo("İşlem Başarılı.", "Üye Ekleme İşlemi Başarılı.")


        except Exception as e:
            messagebox.showerror(f"Bir hata oluştu! {e}")

    def searh_person(self):

        try:
            first_name = self.name_text.get()
            last_name = self.surname_text.get()

            query = "SELECT * FROM Tbl_Uyeler WHERE uyeAd = ? AND uyeSoyad = ?"
            self.cursor.execute(query, (first_name, last_name))
            rowss = self.cursor.fetchall()

            if rowss:
                for row in rowss:
                    # Treeview widget'ı ekleme
                    tree = ttk.Treeview(self)
                    tree["columns"] = (
                        "uyeID", "uyeAd", "uyeSoyad", "uyeDogumTarihi", "uyeCinsiyet", "uyeTelefon", "uyeEmail",
                        "uyeAdres")
                    tree.column("#0", width=0, stretch=tk.NO)
                    tree.column("uyeID", anchor=tk.W, width=120)
                    tree.column("uyeAd", anchor=tk.W, width=120)
                    tree.column("uyeSoyad", anchor=tk.W, width=120)
                    tree.column("uyeDogumTarihi", anchor=tk.W, width=120)
                    tree.column("uyeCinsiyet", anchor=tk.W, width=120)
                    tree.column("uyeTelefon", anchor=tk.W, width=120)
                    tree.column("uyeEmail", anchor=tk.W, width=120)
                    tree.column("uyeAdres", anchor=tk.W, width=120)

                    tree.heading("#0", text="", anchor=tk.W)
                    tree.heading("uyeID", text="uyeID", anchor=tk.W)
                    tree.heading("uyeAd", text="uyeAd", anchor=tk.W)
                    tree.heading("uyeSoyad", text="uyeSoyad", anchor=tk.W)
                    tree.heading("uyeDogumTarihi", text="uyeDogumTarihi", anchor=tk.W)
                    tree.heading("uyeCinsiyet", text="uyeCinsiyet", anchor=tk.W)
                    tree.heading("uyeTelefon", text="uyeTelefon", anchor=tk.W)
                    tree.heading("uyeEmail", text="uyeEmail", anchor=tk.W)
                    tree.heading("uyeAdres", text="uyeAdres", anchor=tk.W)

                    tree.insert("", tk.END, values=(
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
                tree.place(x=10, y=250)


            else:
                messagebox.showerror("Hata!!", f"Belirtilen isimde üye bulunamadı.")

        except Exception as e:
            messagebox.showerror("Bir hata oluştu veya boş bırakmayınız!", f"{e}")

    def list_person(self):
        try:
            # veri tabanı bilgileri getirme

            self.cursor.execute("SELECT * FROM Tbl_Uyeler")
            rows = self.cursor.fetchall()

            # Treeview widget'ı ekleme
            tree = ttk.Treeview(self)
            tree["columns"] = (
            "uyeID", "uyeAd", "uyeSoyad", "uyeDogumTarihi", "uyeCinsiyet", "uyeTelefon", "uyeEmail", "uyeAdres")
            tree.column("#0", width=0, stretch=tk.NO)
            tree.column("uyeID", anchor=tk.W, width=120)
            tree.column("uyeAd", anchor=tk.W, width=120)
            tree.column("uyeSoyad", anchor=tk.W, width=120)
            tree.column("uyeDogumTarihi", anchor=tk.W, width=120)
            tree.column("uyeCinsiyet", anchor=tk.W, width=120)
            tree.column("uyeTelefon", anchor=tk.W, width=120)
            tree.column("uyeEmail", anchor=tk.W, width=120)
            tree.column("uyeAdres", anchor=tk.W, width=120)

            tree.heading("#0", text="", anchor=tk.W)
            tree.heading("uyeID", text="uyeID", anchor=tk.W)
            tree.heading("uyeAd", text="uyeAd", anchor=tk.W)
            tree.heading("uyeSoyad", text="uyeSoyad", anchor=tk.W)
            tree.heading("uyeDogumTarihi", text="uyeDogumTarihi", anchor=tk.W)
            tree.heading("uyeCinsiyet", text="uyeCinsiyet", anchor=tk.W)
            tree.heading("uyeTelefon", text="uyeTelefon", anchor=tk.W)
            tree.heading("uyeEmail", text="uyeEmail", anchor=tk.W)
            tree.heading("uyeAdres", text="uyeAdres", anchor=tk.W)

            # Veritabanındaki verileri Treeview'a ekleme
            for row in rows:
                tree.insert("", tk.END, values=(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

            tree.place(x=10, y=250)

        except Exception as e:
            messagebox.showerror(f"Bir hata oluştu !", {e})








