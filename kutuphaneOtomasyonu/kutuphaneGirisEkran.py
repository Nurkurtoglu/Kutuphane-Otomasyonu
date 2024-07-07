import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
from kutuphaneGenelekran import generalDisplay
import pyodbc
from db_connection import get_db_connection


class LoginApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode('Dark')
        self.configure(fg_color="#6C5B7B")
        self.title("Kullanici Giris Paneli")
        self.geometry("600x500")
        self.create_widgets()
        self.conn = get_db_connection()
        self.cursor = self.conn.cursor()

    def create_widgets(self):

        image_path_lock = "C:\\Users\\EXCALIBUR\\OneDrive\\Masaüstü\\kutuphaneresimler\\locked.png"
        lock_image = ctk.CTkImage(dark_image=Image.open(image_path_lock))
        self.lock_lbl = ctk.CTkLabel(self, text=" ", image=lock_image)
        self.lock_lbl.place(x=225, y=270)

        image_path_developer = "C:\\Users\\EXCALIBUR\\OneDrive\\Masaüstü\\kutuphaneresimler\\developers.png"
        developer_image = ctk.CTkImage(dark_image=Image.open(image_path_developer), size=(200, 200))
        self.developer_lbl = ctk.CTkLabel(self, text=" ", image=developer_image)
        self.developer_lbl.pack()

        image_path_user = "C:\\Users\\EXCALIBUR\\OneDrive\\Masaüstü\\kutuphaneresimler\\user.png"
        user_image = ctk.CTkImage(dark_image=Image.open(image_path_user))
        self.user_lbl = ctk.CTkLabel(self, text=" ", image=user_image)
        self.user_lbl.place(x=190, y=220)


        # Kullanici adı etiketi ve girisi

        self.username_label = ctk.CTkLabel(self, text="Kullanıcı Adı :", text_color="#F8B195")
        self.username_label.place(x=214, y=220)

        self.username_entry = ctk.CTkEntry(self, placeholder_text="Kullanıcı Adı", text_color="#F8B195", fg_color="transparent")
        self.username_entry.place(x=300, y=220)


        # Şifre etiketi ve girişi
        self.password_label = ctk.CTkLabel(self, text="Şifre :", text_color="#F8B195")
        self.password_label.place(x=250, y=270)


        self.password_entry = ctk.CTkEntry(self, placeholder_text="Şifre", show="*", text_color="#F8B195", fg_color="transparent")
        self.password_entry.place(x=300, y=270)

        # Giriş butonu
        self.login_button = ctk.CTkButton(self, text="Giriş Yap", fg_color="#C06C84", command=self.login)
        self.login_button.place(x=300, y=320)

    def login(self):
        try:

            username = self.username_entry.get()
            password = self.password_entry.get()

            query = "SELECT kullaniciAd, kullaniciSifre FROM Tbl_Kullanicilar WHERE kullaniciAd = ? AND kullaniciSifre = ?"
            self.cursor.execute(query, (username, password))
            result = self.cursor.fetchone()

            if result is not None and username == result[0] and password == result[1]:
                messagebox.showinfo("Başarılı", "Giriş başarılı!")
                self.show_general_screen()
            else:
                messagebox.showerror("Hata", "Geçersiz kullanıcı adı veya şifre!")
        except Exception as e:
            messagebox.showerror("Hata!", f"{e}")


    def show_general_screen(self):
        self.kutuphane_pencere = generalDisplay(self)
        self.kutuphane_pencere.grab_set()
        self.withdraw()


if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()