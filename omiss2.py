import tkinter as tk
from tkinter import messagebox

class User:
    def __init__(self, user_id, name, address, email):
        self.user_id = user_id
        self.name = name
        self.address = address
        self.email = email

    def __str__(self):
        return f"{self.name} ({self.user_id})"


class Parcel:
    def __init__(self, parcel_id, sender, receiver, status, tracking_number):
        self.parcel_id = parcel_id
        self.sender = sender
        self.receiver = receiver
        self.status = status
        self.tracking_number = tracking_numbergit --version


    def __str__(self):
        return f"Посылка {self.parcel_id}: {self.status}"


class ParcelService:
    def __init__(self):
        self.parcels = []

    def add_parcel(self, parcel):
        self.parcels.append(parcel)

    def track_parcel(self, tracking_number):
        for parcel in self.parcels:
            if parcel.tracking_number == tracking_number:
                return parcel
        return None


class ParcelController:
    def __init__(self, parcel_service):
        self.parcel_service = parcel_service

    def create_parcel(self, sender, receiver, status, tracking_number):
        new_parcel = Parcel(len(self.parcel_service.parcels) + 1, sender, receiver, status, tracking_number)
        self.parcel_service.add_parcel(new_parcel)
        return new_parcel

    def track_parcel(self, tracking_number):
        return self.parcel_service.track_parcel(tracking_number)


class ParcelApp:
    def __init__(self, root, parcel_controller):
        self.root = root
        self.root.title("Система отслеживания посылок")
        self.parcel_controller = parcel_controller
        self.root.geometry("500x400")  
        self.root.configure(bg="#E6E6FA")  
        self.create_ui()

    def create_ui(self):
        self.label = tk.Label(self.root, text="Введите номер отслеживания:", font=("Arial", 12), bg="#E6E6FA")
        self.label.pack(pady=10)

        self.tracking_entry = tk.Entry(self.root, font=("Arial", 12))
        self.tracking_entry.pack(pady=10)

        self.track_button = tk.Button(self.root, text="Отследить посылку", command=self.track_parcel, font=("Arial", 12), bg="#D8BFD8")
        self.track_button.pack(pady=10)

        self.create_parcel_button = tk.Button(self.root, text="Создать посылку", command=self.create_parcel, font=("Arial", 12), bg="#D8BFD8")
        self.create_parcel_button.pack(pady=10)

    def create_parcel(self):
       
        sender = User(1, "Иван Иванов", "ул. Ленина, 10", "ivan@example.com")
        receiver = User(2, "Мария Петрова", "ул. Советская, 5", "maria@example.com")
        parcel = self.parcel_controller.create_parcel(sender, receiver, "В пути", "123456789")
        messagebox.showinfo("Посылка создана", f"Посылка с ID: {parcel.parcel_id} и номером отслеживания: {parcel.tracking_number} была создана.")

    def track_parcel(self):
        tracking_number = self.tracking_entry.get()
        parcel = self.parcel_controller.track_parcel(tracking_number)

        if parcel:
            messagebox.showinfo("Статус посылки", f"Посылка {parcel.parcel_id} Статус: {parcel.status}")
        else:
            messagebox.showerror("Ошибка", "Посылка не найдена")


if __name__ == "__main__":
    
    user1 = User(1, "Иван Иванов", "ул. Ленина, 10", "ivan@example.com")
    user2 = User(2, "Мария Петрова", "ул. Советская, 5", "maria@example.com")
    parcel_service = ParcelService()
    parcel_controller = ParcelController(parcel_service)

    parcel_controller.create_parcel(user1, user2, "В пути", "123456789")

    root = tk.Tk()
    app = ParcelApp(root, parcel_controller)
    root.mainloop()
