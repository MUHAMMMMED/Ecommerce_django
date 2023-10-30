
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.db.models import Sum



def send_order_email(order_id):
    order = Order.objects.get(id=order_id)
    overall_total_price = order.item.aggregate(total_price=Sum('total_price'))['total_price'] or 0
    # Construct the plain text version of the message
    message = f'Order ID: {order.id}\nOrder Date: {order.created_at}\n\nOrder Details:\n'
    message += f'Name: {order.name}\n'
    message += f'Company Name: {order.companyname}\n'
    message += f'Phone: {order.phone}\n'
    message += f'Email Address: {order.emailaddress}\n'
    message += f'Country: {order.country}\n'
    message += f'Shipping Address: {order.shipping_address}\n'
    message += f'Apartment Address: {order.apartment_address}\n'
    message += f'ZIP: {order.zip}\n'

    # Iterate over the order items and add them to the message
    for item in order.item.all():
        message += f'Item: {item.items}\nQuantity: {item.quantity}\nPrice: {item.price}\n\n'
    plain_message = strip_tags(message)
    # Construct the HTML version of the message using a template
    html_message = render_to_string('order_confirmation.html', {'order': order,'overall_total_price': overall_total_price},)
    # Send the email
    send_mail(
        subject=f"New Order - Created at {order.created_at}",
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=['amer66965@gmail.com'],
        html_message=html_message,
    )
