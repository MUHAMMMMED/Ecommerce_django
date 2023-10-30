from decimal import Decimal, ROUND_DOWN
from django.shortcuts import render, get_object_or_404,redirect
from Ecommerce.models import CardItem, OrderItem,Order
from Ecommerce.forms import OrderForm
 
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.db.models import Sum




def Orderitem(request):
    session_key = request.session.session_key
    orderitems = []
    items = []

    overall_total_price = Decimal(0)

    if session_key:
        orderitems = CardItem.objects.filter(session_id=session_key)

        for orderitem in orderitems:
            price = Decimal(orderitem.item.price)
            quantity = orderitem.quantity

            # Calculate the discounted price, if any.
            discounted_price = price
            discount_price1 = Decimal(orderitem.item.discount_price1) if orderitem.item.discount_price1 else Decimal(0)
            discount_price2 = Decimal(orderitem.item.discount_price2) if orderitem.item.discount_price2 else Decimal(0)
            discount_price3 = Decimal(orderitem.item.discount_price3) if orderitem.item.discount_price3 else Decimal(0)

            if quantity < orderitem.item.quantity1:
                discounted_price = price - (price * (discount_price1 / Decimal(100)))
            elif quantity < orderitem.item.quantity2:
                discounted_price = price - (price * (discount_price2 / Decimal(100)))
            elif quantity < orderitem.item.quantity3:
                discounted_price = price - (price * (discount_price3 / Decimal(100)))

            # Quantize the discounted prices to two decimal places
            discount = discounted_price.quantize(Decimal('0'), rounding=ROUND_DOWN)

            # Calculate the total price.
            Total_price = discounted_price * quantity
            total_price = Total_price.quantize(Decimal('0'), rounding=ROUND_DOWN)

            quant = orderitem.item.quantity1

            if quantity > quant:
                beforprice = price
            else:
                beforprice = 0

            # Add the order item to the list of items.
            items.append({
                'item': orderitem.item,
                'beforprice': beforprice,
                'discount_price': discount,
                'quantity': quantity,
                'total_price': total_price
            })

            # Update the overall total price.
            overall_total_price += total_price
    else:
        cart_item_count = 0

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.session_key = session_key
            new_order.save()

            for item in items:
                order_item = OrderItem.objects.create(
                    items=item['item'],
                    quantity=item['quantity'],
                    price=item['discount_price'],
                    total_price=item['total_price'],
                )

                new_order.item.add(order_item)
            new_order.save()

            send_order_email(new_order.id)

            return redirect('Ecommerce:checkout', new_order.id)

    else:
        form = OrderForm()

    context = {
        'orderitems': orderitems,
        'items': items,
        'overall_total_price': overall_total_price,
        'form': form
    }
    return render(request, 'cart.html', context)







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
