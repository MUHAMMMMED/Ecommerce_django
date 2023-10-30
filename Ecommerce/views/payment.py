from django.shortcuts import get_object_or_404,render,redirect
from Ecommerce.models import Order,Item,CardItem,InvoiceTextTranslate,TrackTextTranslate,BaseTextTranslate

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.db.models import Sum
from django.http import JsonResponse
from django.db.models import F
from decimal import Decimal





def payment_success(request, order_id):

    try:
        session_key = request.session.session_key
        order = get_object_or_404(Order, id=order_id)
        order.default = True
        order.save()
        print('ok1')
        order_items = order.item.all()
        for order_item in order_items:
            Item.objects.filter(id=order_item.id).update(stock_no=F('stock_no') - order_item.quantity)
            print('ok')
        cart_item = CardItem.objects.filter(session_id=session_key)
        for cart in cart_item:
            cart.delete()
            print('delete')
        # return redirect('Ecommerce:success', order.id)

        return JsonResponse(safe=True)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)



def tax_count(Subtotal,tax):
    tax_number = Subtotal  *  tax / 100
    return tax_number

def success(request,order_id):

    order = Order.objects.get(id=order_id)
    BaseTextT=BaseTextTranslate.objects.all().first()
    overall_total_price = Decimal(0)
    shipping_price = order.country.shipping_price
    Subtotal = order.item.aggregate(total_price=Sum('total_price'))['total_price'] or 0
    tax = order.country.tax
    tax_number = tax_count(Subtotal,tax)

    overall_total_price += Subtotal
    overall_total_price += tax_number
    overall_total_price += shipping_price

    context = {
    'order': order,
    # 'currency': items[0]['currency'],
    'Subtotal':"{:.2f}".format(Subtotal) ,
    'tax_number':"{:.2f}".format(tax_number),
    'shipping_price': shipping_price,
    'overall_total_price': overall_total_price ,

 }

    send_order_email(order.id)
    return render(request, 'success.html',context)



def payment_confirmation(request,order_id):
    order = Order.objects.get(id=order_id)
    BaseTextT=BaseTextTranslate.objects.all().first()
    overall_total_price = Decimal(0)
    shipping_price = order.country.shipping_price
    Subtotal = order.item.aggregate(total_price=Sum('total_price'))['total_price'] or 0
    tax = order.country.tax
    tax_number = tax_count(Subtotal,tax)

    overall_total_price += Subtotal
    overall_total_price += tax_number
    overall_total_price += shipping_price

    context = {
    'order': order,
    # 'currency': items[0]['currency'],
    'Subtotal':"{:.2f}".format(Subtotal) ,
    'tax_number':"{:.2f}".format(tax_number),
    'shipping_price': shipping_price,
    'overall_total_price': overall_total_price ,
  }

    return render(request, 'payment_confirmation.html',context)





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

    context = {
    'order': order,
    # 'currency': items[0]['currency'],
    'Subtotal':"{:.2f}".format(Subtotal) ,
    'tax_number':"{:.2f}".format(tax_number),
    'shipping_price': shipping_price,
    'overall_total_price': overall_total_price,

     'InvoiceTextT':InvoiceTextT,
     'TrackTextT':TrackTextT,





      }

    html_message = render_to_string('order_confirmation.html',context,)
    # Send the email
    send_mail(
        subject=f"New Order - Created at {order.created_at}",
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=['amer66965@gmail.com'],
        html_message=html_message,
    )
