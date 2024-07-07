import pyodbc
from tkinter import messagebox

def get_db_connection():
    try:
        connection = pyodbc.connect(
            'DRIVER={SQL Server};'
            'SERVER=DESKTOP-LKTQGP7\\SQLEXPRESS05;'
            'DATABASE=KutuphaneOtomasyon;'
            'Trusted_Connection = True;'
        )
        return connection
    except Exception as e:
        messagebox.showerror('Bir hata oluştu:', f'{e}')