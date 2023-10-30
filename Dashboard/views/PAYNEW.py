from django.shortcuts import render, redirect, get_object_or_404
from Ecommerce.models import  Order,InvoiceTextTranslate,TrackTextTranslate,MoreTextTranslate
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.db.models import Sum
from decimal import Decimal, ROUND_DOWN



def tax_count(Subtotal,tax):
    tax_number = Subtotal  *  tax / 100
    return tax_number

def paynaw(request, id):
    send_order_email(id)
    return redirect('Dashboard:waiting_buy')



def send_order_email(order_id):
    order = Order.objects.get(id=order_id)
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

    overall_total_price = Decimal(0)
    shipping_price = order.country.shipping_price
    Subtotal = order.item.aggregate(total_price=Sum('total_price'))['total_price'] or 0
    tax = order.country.tax
    tax_number = tax_count(Subtotal,tax)

    overall_total_price += Subtotal
    overall_total_price += tax_number
    overall_total_price += shipping_price

    InvoiceTextT=InvoiceTextTranslate.objects.all().first()
    TrackTextT=TrackTextTranslate.objects.all().first()
    MoreText=MoreTextTranslate.objects.all().first()




    context = {
    'order': order,
    'Subtotal':"{:.2f}".format(Subtotal) ,
    'tax_number':"{:.2f}".format(tax_number),
    'shipping_price': shipping_price,
    'overall_total_price': overall_total_price,
     'InvoiceTextT':InvoiceTextT,
     'TrackTextT':TrackTextT,
     'MoreText':MoreText


      }

    html_message = render_to_string('paynew.html',context,)
    # Send the email
    send_mail(
        subject=f"New Order - Created at {order.created_at}",
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=['amer66965@gmail.com','order.emailaddress'],
        html_message=html_message,
    )
