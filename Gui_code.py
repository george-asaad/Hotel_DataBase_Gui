import tkinter as tk
from tkinter import ttk, messagebox
import pyodbc

# Database connection
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=DESKTOP-R7DOAT3\SERVER2;'
    'DATABASE=HotelDB;'
    'Trusted_Connection=yes;'
)
cursor = conn.cursor()

# Function to execute query
def execute_query(query, params=()):
    try:
        cursor.execute(query, params)
        conn.commit()
        messagebox.showinfo("Success", "Operation completed successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to fetch data
def fetch_data(query):
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return []

# GUI Setup
root = tk.Tk()
root.title("Hotel Management System")
root.geometry("1200x700")
root.configure(bg="#DDD6CE")

# Sidebar
sidebar = tk.Frame(root, bg="#A9B5C2", width=300)
tk.Label(sidebar, text="HOTEL_DB", bg="#A9B5C2", font=("Arial", 14)).pack(pady=10)
sidebar.pack(side=tk.LEFT, fill=tk.Y)

# Main Content Area
main_content = tk.Frame(root, bg="#EEEAE3")
tk.Label(main_content, text="WELCOME TO OUR HOTEL", bg="#DDD6CE", font=("Arial", 30)).pack(pady=10)
tk.Label(main_content, 
         text="\n\n\n Our system ensures smooth bookings, quick\n\nand personalized service to make\n\n your stay comfortable and memorable.\n\n\" Thank you for choosing us ! \" ", 
         bg="#EEEAE3", 
         font=("Arial", 20), 
         anchor="center", 
         justify="center").pack(pady=10)

main_content.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

# Functions for forms and data display
def load_guest_form():
    for widget in main_content.winfo_children():
        widget.destroy()

    tk.Label(main_content, text="Guest Information", bg="#EEEAE3", font=("Arial", 14)).pack(pady=10)
    name_label = tk.Label(main_content, text="Name", bg="#EEEAE3")
    name_label.pack()
    name_entry = tk.Entry(main_content)
    name_entry.pack()

    phone_label = tk.Label(main_content, text="Phone", bg="#EEEAE3")
    phone_label.pack()
    phone_entry = tk.Entry(main_content)
    phone_entry.pack()

    email_label = tk.Label(main_content, text="Email", bg="#EEEAE3")
    email_label.pack()
    email_entry = tk.Entry(main_content)
    email_entry.pack()

    address_label = tk.Label(main_content, text="Address", bg="#EEEAE3")
    address_label.pack()
    address_entry = tk.Entry(main_content)
    address_entry.pack()

    def save_guest():
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()
        query = "INSERT INTO Guest (Name, Phone, Email, Address) VALUES (?, ?, ?, ?)"
        execute_query(query, (name, phone, email, address))

    save_button = tk.Button(main_content, text="Save", command=save_guest)
    save_button.pack(pady=10)

    view_button = tk.Button(main_content, text="View Data", command=view_guest_data)
    view_button.pack(pady=10)

def view_guest_data():
    for widget in main_content.winfo_children():
        widget.destroy()

    data = fetch_data("SELECT * FROM Guest")
    cols = ("GuestID", "Name", "Phone", "Email", "Address")

    tree = ttk.Treeview(main_content, columns=cols, show="headings")
    for col in cols:
        tree.heading(col, text=col)
    for row in data:
        tree.insert("", tk.END, values=row)
    tree.pack(fill=tk.BOTH, expand=True)

def load_room_form():
    for widget in main_content.winfo_children():
        widget.destroy()

    tk.Label(main_content, text="Room Information", bg="#EEEAE3", font=("Arial", 14)).pack(pady=10)
    type_label = tk.Label(main_content, text="Room Type", bg="#EEEAE3")
    type_label.pack()
    type_entry = ttk.Combobox(main_content, values=["Single", "Double", "Triple"])
    type_entry.pack()

    price_label = tk.Label(main_content, text="Price Per Night", bg="#EEEAE3")
    price_label.pack()
    price_entry = tk.Entry(main_content)
    price_entry.pack()

    status_label = tk.Label(main_content, text="Status", bg="#EEEAE3")
    status_label.pack()
    status_entry = ttk.Combobox(main_content, values=["Available", "Occupied"])
    status_entry.pack()

    def save_room():
        room_type = type_entry.get()
        price = price_entry.get()
        status = status_entry.get()
        query = "INSERT INTO Room (RoomType, PricePerNight, Status) VALUES (?, ?, ?)"
        execute_query(query, (room_type, price, status))

    save_button = tk.Button(main_content, text="Save", command=save_room)
    save_button.pack(pady=10)

    view_button = tk.Button(main_content, text="View Data", command=view_room_data)
    view_button.pack(pady=10)

def view_room_data():
    for widget in main_content.winfo_children():
        widget.destroy()

    data = fetch_data("SELECT * FROM Room")
    cols = ("RoomID", "RoomType", "PricePerNight", "Status")

    tree = ttk.Treeview(main_content, columns=cols, show="headings")
    for col in cols:
        tree.heading(col, text=col)
    for row in data:
        tree.insert("", tk.END, values=row)
    tree.pack(fill=tk.BOTH, expand=True)

def load_reservation_form():
    for widget in main_content.winfo_children():
        widget.destroy()

    tk.Label(main_content, text="Reservation Information", bg="#EEEAE3", font=("Arial", 14)).pack(pady=10)
    guest_id_label = tk.Label(main_content, text="Guest ID", bg="#EEEAE3")
    guest_id_label.pack()
    guest_id_entry = tk.Entry(main_content)
    guest_id_entry.pack()

    room_id_label = tk.Label(main_content, text="Room ID", bg="#EEEAE3")
    room_id_label.pack()
    room_id_entry = tk.Entry(main_content)
    room_id_entry.pack()

    checkin_label = tk.Label(main_content, text="Check-in Date (Y-M-D)", bg="#EEEAE3")
    checkin_label.pack()
    checkin_entry = tk.Entry(main_content)
    checkin_entry.pack()

    checkout_label = tk.Label(main_content, text="Check-out Date (Y-M-D)", bg="#EEEAE3")
    checkout_label.pack()
    checkout_entry = tk.Entry(main_content)
    checkout_entry.pack()

    total_amount_label = tk.Label(main_content, text="Total Amount", bg="#EEEAE3")
    total_amount_label.pack()
    total_amount_entry = tk.Entry(main_content)
    total_amount_entry.pack()

    def save_reservation():
        guest_id = guest_id_entry.get()
        room_id = room_id_entry.get()
        checkin = checkin_entry.get()
        checkout = checkout_entry.get()
        total_amount = total_amount_entry.get()
        query = "INSERT INTO Reservation (GuestID, RoomID, CheckInDate, CheckOutDate, TotalAmount) VALUES (?, ?, ?, ?, ?)"
        execute_query(query, (guest_id, room_id, checkin, checkout, total_amount))

    save_button = tk.Button(main_content, text="Save", command=save_reservation)
    save_button.pack(pady=10)

    view_button = tk.Button(main_content, text="View Data", command=view_reservation_data)
    view_button.pack(pady=10)

def view_reservation_data():
    for widget in main_content.winfo_children():
        widget.destroy()

    data = fetch_data("SELECT * FROM Reservation")
    cols = ("ReservationID", "GuestID", "RoomID", "CheckInDate", "CheckOutDate", "TotalAmount")

    tree = ttk.Treeview(main_content, columns=cols, show="headings")
    for col in cols:
        tree.heading(col, text=col)
    for row in data:
        tree.insert("", tk.END, values=row)
    tree.pack(fill=tk.BOTH, expand=True)

def load_service_form():
    for widget in main_content.winfo_children():
        widget.destroy()

    tk.Label(main_content, text="Service Information", bg="#EEEAE3", font=("Arial", 14)).pack(pady=10)
    service_name_label = tk.Label(main_content, text="Service Name", bg="#EEEAE3")
    service_name_label.pack()
    service_name_entry = tk.Entry(main_content)
    service_name_entry.pack()

    description_label = tk.Label(main_content, text="Description", bg="#EEEAE3")
    description_label.pack()
    description_entry = ttk.Combobox(main_content, values=["Breakfast", "Lunch", "Dinner", "Trip", "Drinks"])
    description_entry.pack()

    price_label = tk.Label(main_content, text="Price", bg="#EEEAE3")
    price_label.pack()
    price_entry = tk.Entry(main_content)
    price_entry.pack()

    def save_service():
        service_name = service_name_entry.get()
        description = description_entry.get()
        price = price_entry.get()
        query = "INSERT INTO Service (ServiceName, Description, Price) VALUES (?, ?, ?)"
        execute_query(query, (service_name, description, price))

    save_button = tk.Button(main_content, text="Save", command=save_service)
    save_button.pack(pady=10)

    view_button = tk.Button(main_content, text="View Data", command=view_service_data)
    view_button.pack(pady=10)

def view_service_data():
    for widget in main_content.winfo_children():
        widget.destroy()

    data = fetch_data("SELECT * FROM Service")
    cols = ("ServiceID", "ServiceName", "Description", "Price")

    tree = ttk.Treeview(main_content, columns=cols, show="headings")
    for col in cols:
        tree.heading(col, text=col)
    for row in data:
        tree.insert("", tk.END, values=row)
    tree.pack(fill=tk.BOTH, expand=True)

def load_reservation_service_form():
    for widget in main_content.winfo_children():
        widget.destroy()

    tk.Label(main_content, text="Reservation Service Information", bg="#EEEAE3", font=("Arial", 14)).pack(pady=10)
    reservation_id_label = tk.Label(main_content, text="Reservation ID", bg="#EEEAE3")
    reservation_id_label.pack()
    reservation_id_entry = tk.Entry(main_content)
    reservation_id_entry.pack()

    service_id_label = tk.Label(main_content, text="Service ID", bg="#EEEAE3")
    service_id_label.pack()
    service_id_entry = tk.Entry(main_content)
    service_id_entry.pack()

    quantity_label = tk.Label(main_content, text="Quantity", bg="#EEEAE3")
    quantity_label.pack()
    quantity_entry = tk.Entry(main_content)
    quantity_entry.pack()

    def save_reservation_service():
        reservation_id = reservation_id_entry.get()
        service_id = service_id_entry.get()
        quantity = quantity_entry.get()
        query = "INSERT INTO ReservationService (ReservationID, ServiceID, Quantity) VALUES (?, ?, ?)"
        execute_query(query, (reservation_id, service_id, quantity))

    save_button = tk.Button(main_content, text="Save", command=save_reservation_service)
    save_button.pack(pady=10)

    view_button = tk.Button(main_content, text="View Data", command=view_reservation_service_data)
    view_button.pack(pady=10)

def view_reservation_service_data():
    for widget in main_content.winfo_children(): 
        widget.destroy()

    data = fetch_data("SELECT * FROM ReservationService")
    cols = ("ReservationServiceID", "ReservationID", "ServiceID", "Quantity")

    tree = ttk.Treeview(main_content, columns=cols, show="headings")
    for col in cols:
        tree.heading(col, text=col)
    for row in data:
        tree.insert("", tk.END, values=row)
    tree.pack(fill=tk.BOTH, expand=True)

# Sidebar buttons
tk.Button(sidebar, text="Guests", command=load_guest_form, bg="#4695ED").pack(fill=tk.X, pady=5)
tk.Button(sidebar, text="Rooms", command=load_room_form, bg="#4695ED").pack(fill=tk.X, pady=5)
tk.Button(sidebar, text="Reservations", command=load_reservation_form, bg="#4695ED").pack(fill=tk.X, pady=5)
tk.Button(sidebar, text="Services", command=load_service_form, bg="#4695ED").pack(fill=tk.X, pady=5)
tk.Button(sidebar, text="Reservation Services", command=load_reservation_service_form, bg="#4695ED").pack(fill=tk.X, pady=5)

# Run the application
root.mainloop()

# Close database connection on exit
conn.close()
