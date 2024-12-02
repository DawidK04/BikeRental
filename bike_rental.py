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
