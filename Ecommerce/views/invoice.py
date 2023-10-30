
import random
import datetime

def generate_invoice_number():
    while True:
        random_number = random.randint(1000, 9999)
        current_date = datetime.datetime.now()
        formatted_date = current_date.strftime('%Y%m%d')
        invoice_number = f"{formatted_date}{random_number}"
        # Check if the invoice number already exists in Order objects
        if not Order.objects.filter(Tracking=invoice_number).exists():
            return invoice_number
