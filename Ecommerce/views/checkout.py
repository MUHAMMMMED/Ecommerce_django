from django.shortcuts import get_object_or_404,render,redirect
from decimal import Decimal, ROUND_DOWN
from Ecommerce.models import Order,BaseTextTranslate
# from forex_python.converter import CurrencyRates

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


def tax_count(Subtotal,tax):
    tax_number =  Decimal(Subtotal  *  tax / 100)
    return tax_number





#
# def convert_currency(amount ):
#         amount = float(amount)
#         c = CurrencyRates()
#         conversion_rate = c.convert('SAR','USD', amount)
#         return conversion_rate
#
#
# def checkout(request, id):
#     try:
#         session_key = request.session.session_key
#         order = get_object_or_404(Order, id=id, session_key=session_key)
#         BaseTextT=BaseTextTranslate.objects.all().first()
#         shipping_price = order.country.shipping_price
#         items = []
#
#         tax_number = []
#
#         overall_total_price = Decimal(0)
#         ENoverall_total_price = []
#         Subtotal= Decimal(0)
#         for order_item in order.item.all():
#             total_price = order_item.total_price or Decimal(0)
#             items.append({
#                 'item': order_item.items,
#                 'price': order_item.price,
#                 'quantity': order_item.quantity,
#                 'total_price': total_price,
#                 'currency':BaseTextT.currency
#                   })
#
#             Subtotal += total_price
#             tax = order.country.tax
#
#             tax_number = tax_count(Subtotal,tax)
#             overall_total_price += shipping_price
#             overall_total_price += Subtotal
#             overall_total_price += tax_number
#         ENoverall_total_price= convert_currency(overall_total_price)
#
#         invoice_number = generate_invoice_number()  # Generate unique invoice number
#         order.Tracking = invoice_number
#         order.save()
#     except Order.DoesNotExist:
#         return redirect('Ecommerce:Orderitem')
#     context = {
#         'items': items,
#         'itemss':itemss,
#         'Subtotal':"{:.2f}".format(Subtotal) ,
#         'tax_number':"{:.2f}".format(tax_number),
#         'shipping_price': shipping_price,
#         'overall_total_price': overall_total_price,
#         'order': order,
#         'date': datetime.datetime.now(),
#         'invoice_number': invoice_number,
#         'ENoverall_total_price':ENoverall_total_price
#     }
#     return render(request, 'checkout.html', context)
#



def convert_currency(amount):
    conversion_rates = {
        'SAR': Decimal('0.266'),  # معدل تحويل SAR إلى USD
        'USD': Decimal('1.0'),   # معدل تحويل USD إلى نفسها
    }
    converted_amount = amount * conversion_rates['SAR']
    return converted_amount


def checkout(request, id):
    try:
        session_key = request.session.session_key
        order = get_object_or_404(Order, id=id, session_key=session_key)
        BaseTextT = BaseTextTranslate.objects.all().first()
        shipping_price = order.country.shipping_price
        items = []
        tax_number = Decimal(0)
        overall_total_price = Decimal(0)
        Subtotal = Decimal(0)
        ENoverall_total_price=[]

        for order_item in order.item.all():
            total_price = order_item.total_price or Decimal(0)
            items.append({
                'item': order_item.items,
                'price': order_item.price,
                'quantity': order_item.quantity,
                'total_price': total_price,
                'currency': BaseTextT.currency
            })
            Subtotal += total_price
        tax = order.country.tax
        tax_number = tax_count(Subtotal, tax)
        overall_total_price += shipping_price + Subtotal + tax_number
        print('overall_total_price',overall_total_price)
        if items[0]['currency'] == 'USD':
                ENoverall_total_price = overall_total_price
        else:
                ENoverall_total_price = convert_currency(overall_total_price)

        invoice_number = generate_invoice_number()  # Generate unique invoice number
        order.Tracking = invoice_number
        order.save()
    except Order.DoesNotExist:
        return redirect('Ecommerce:Orderitem')

    context = {
        'items': items,
        'currency': items[0]['currency'],
        'Subtotal': "{:.2f}".format(Subtotal),
        'tax_number': "{:.2f}".format(tax_number),
        'shipping_price': shipping_price,
        'overall_total_price': overall_total_price,
        'order': order,
        'date': datetime.datetime.now(),
        'invoice_number': invoice_number,
        'ENoverall_total_price': "{:.2f}".format(ENoverall_total_price),
    }

    return render(request, 'checkout.html', context)
