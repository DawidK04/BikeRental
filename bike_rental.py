import json
from datetime import datetime
import smtplib
import os



def rent_bike(customer_name, rental_duration):
    """
    Proces wynajmu roweru.
    """
    cost = calculate_cost(rental_duration)
    rental = {
        "customer_name": customer_name,
        "rental_duration": rental_duration,
        "cost": cost
    }
    save_rental(rental)
    print(f"Rower wynajęty przez {customer_name} na {rental_duration} godzin. Koszt: {cost} zł.")



def calculate_cost(rental_duration):
    """
    Obliczanie kosztu wynajmu roweru.
    """
    if rental_duration <= 0:
        raise ValueError("Czas wynajmu musi być większy od 0.")
    elif rental_duration > 1:
        return 10 + (rental_duration - 1) * 5
    else:
        return 10



def save_rental(rental):
    """
    Zapisywanie szczegółów wynajmu do rentals.json
    """
    filename = "rentals.json"
    rentals = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            rentals = json.load(file)

    rentals.append(rental)

    with open(filename, "w") as file:
        json.dump(rentals, file)



def load_rentals():
    """
    Odczytywanie wynajmu z rentals.json
    """
    filename = "rentals.json"
    if not os.path.exists(filename):
        print("Brak zapisanych wynajmów.")
        return

    with open(filename, "r") as file:
        rentals = json.load(file)

    if rentals:
        print("Zapisane wynajmy:")
        for rental in rentals:
            print(f"Klient: {rental['customer_name']}, Czas wynajmu: {rental['rental_duration']} godzin(y), Koszt: {rental['cost']} zł")
    else:
        print("Brak zapisanych wynajmów.")
