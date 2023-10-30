from django.shortcuts import get_object_or_404,render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.conf import settings
from decimal import Decimal
from django.db.models import F
from django.http import JsonResponse
from decimal import Decimal, ROUND_DOWN
from Ecommerce.models import *
from .forms import OrderForm
import random
import datetime
from .models import CardItem, Item







# def home(request):
#     category = Category.objects.filter(is_active=True)
#     items = Item.objects.filter(is_active=True).order_by('-created_at')
#     context = {'category':category,'items':items, }
#     return render(request, 'index.html', context)

#
# def categories(request):
#     category = Category.objects.filter(is_active=True)
#     context = {'category':category}
#     return render(request, 'category.html', context)
#
#
# def CategoryDetails(request,slug):
#     category = get_object_or_404(Category, slug=slug)
#     context = {'category':category}
#     return render(request, 'categoryid.html', context)


#
# from decimal import Decimal, ROUND_DOWN
#
#
# def item_detail(request,slug):
#     iteM = get_object_or_404(Item, slug=slug)
#     price = iteM.price
#
#     discount_percentage1 = Decimal(iteM.discount_price1) if iteM.discount_price1 is not None else Decimal(0)
#     discount_percentage2 = Decimal(iteM.discount_price2) if iteM.discount_price2 is not None else Decimal(0)
#     discount_percentage3 = Decimal(iteM.discount_price3) if iteM.discount_price3 is not None else Decimal(0)
#
#     discounted_price1 = price - (price * (discount_percentage1 / Decimal(100)))
#     discounted_price2 = price - (price * (discount_percentage2 / Decimal(100)))
#     discounted_price3 = price - (price * (discount_percentage3 / Decimal(100)))
#
#     # Quantize the discounted prices to two decimal places
#     discounted_price1 = discounted_price1.quantize(Decimal('0.00'), rounding=ROUND_DOWN)
#     discounted_price2 = discounted_price2.quantize(Decimal('0.00'), rounding=ROUND_DOWN)
#     discounted_price3 = discounted_price3.quantize(Decimal('0.00'), rounding=ROUND_DOWN)
#
#     context = {
#         'iteM': iteM,
#         'discounted_price1': discounted_price1,
#         'discounted_price2': discounted_price2,
#         'discounted_price3': discounted_price3,
#     }
#
#     return render(request, 'single-product.html', context)
#






#
# def add_to_cart(request, id):
#
#     # Get or create session
#     session_key = request.session.session_key
#     if not session_key:
#         request.session.save()
#         session_key = request.session.session_key
#
#     # Get item object
#     item = get_object_or_404(Item, id=id)
#
#     # Get the existing cart item or create a new one
#     cart_item, created = CardItem.objects.get_or_create(session_id=session_key, item=item)
#
#     # Update the quantity of the cart item
#     cart_item.quantity += 1
#     cart_item.save()
#
#     # Get the updated cart item count
#     cart_item_count = CardItem.objects.filter(session_id=session_key).count()
#
#     # Prepare the JSON response with success message and cart item count
#     data = {
#         'cart_item_count': cart_item_count,
#         'message': 'تم الاضافة الى السلة',
#     }
#
#     return JsonResponse(data)
#
# from django.http import JsonResponse
#
#
#
#
#
#
#
#
# def go_to_cart(request, id):
#     # Get or create session
#     session_key = request.session.session_key
#     if not session_key:
#         request.session.save()
#         session_key = request.session.session_key
#     # Get item object
#     item = get_object_or_404(Item, id=id)
#     # Get cart item or create a new one
#     cart_item, created = CardItem.objects.get_or_create(    session_id=session_key,item=item,)
#     # Prepare the JSON response with success message and cart item count
#     data = {'message': 'تم الاضافة الي السلة',    }
#     return JsonResponse(data)
#
# def Add_to_cart(request, id):
#
#     if request.method == 'POST':
#         quantity = request.POST.get('quantity')  # Get the quantity from the POST data
#         # print('quantity',quantity)
#         session_key = request.session.session_key
#         if not session_key:
#             request.session.save()
#             session_key = request.session.session_key
#         # Get item object
#         item = get_object_or_404(Item, id=id)
#         # Check if the cart item already exists
#         cart_item = CardItem.objects.filter(session_id=session_key, item=item).first()
#         if cart_item:
#             # Update the quantity of the existing cart item
#             cart_item.quantity += int(quantity)
#             cart_item.save()
#         else:
#             # Create a new cart item
#             cart_item = CardItem.objects.create(session_id=session_key, item=item, quantity=quantity)
#         # Get the updated cart item count
#         cart_item_count = CardItem.objects.filter(session_id=session_key).count()
#         # Prepare the JSON response with success message and cart item count
#     data = {
#         'cart_item_count': cart_item_count,
#         'message': 'تم الاضافة الى السلة',
#     }
#
#     return JsonResponse(data)
#
# def refresh_cart(request):
#     session_key = request.session.session_key
#     cart_item_count = CardItem.objects.filter(session_id=session_key).count()
#     data = {
#         'cart_item_count': cart_item_count,
#      }
#     return JsonResponse(data)
# #
#
# from decimal import Decimal, ROUND_DOWN
# from django.shortcuts import render, get_object_or_404
# from .models import CardItem, OrderItem
#
# def Orderitem(request):
#     session_key = request.session.session_key
#     orderitems = []
#     items = []
#
#     overall_total_price = Decimal(0)
#
#     if session_key:
#         orderitems = CardItem.objects.filter(session_id=session_key)
#
#         for orderitem in orderitems:
#             price = Decimal(orderitem.item.price)
#             quantity = orderitem.quantity
#
#             # Calculate the discounted price, if any.
#             discounted_price = price
#             discount_price1 = Decimal(orderitem.item.discount_price1) if orderitem.item.discount_price1 else Decimal(0)
#             discount_price2 = Decimal(orderitem.item.discount_price2) if orderitem.item.discount_price2 else Decimal(0)
#             discount_price3 = Decimal(orderitem.item.discount_price3) if orderitem.item.discount_price3 else Decimal(0)
#
#             if quantity < orderitem.item.quantity1:
#                 discounted_price = price - (price * (discount_price1 / Decimal(100)))
#             elif quantity < orderitem.item.quantity2:
#                 discounted_price = price - (price * (discount_price2 / Decimal(100)))
#             elif quantity < orderitem.item.quantity3:
#                 discounted_price = price - (price * (discount_price3 / Decimal(100)))
#
#             # Quantize the discounted prices to two decimal places
#             discount = discounted_price.quantize(Decimal('0'), rounding=ROUND_DOWN)
#
#             # Calculate the total price.
#             Total_price = discounted_price * quantity
#             total_price = Total_price.quantize(Decimal('0'), rounding=ROUND_DOWN)
#
#             quant = orderitem.item.quantity1
#
#             if quantity > quant:
#                 beforprice = price
#             else:
#                 beforprice = 0
#
#             # Add the order item to the list of items.
#             items.append({
#                 'item': orderitem.item,
#                 'beforprice': beforprice,
#                 'discount_price': discount,
#                 'quantity': quantity,
#                 'total_price': total_price
#             })
#
#             # Update the overall total price.
#             overall_total_price += total_price
#     else:
#         cart_item_count = 0
#
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             new_order = form.save(commit=False)
#             new_order.session_key = session_key
#             new_order.save()
#
#             for item in items:
#                 order_item = OrderItem.objects.create(
#                     items=item['item'],
#                     quantity=item['quantity'],
#                     price=item['discount_price'],
#                     total_price=item['total_price'],
#                 )
#
#                 new_order.item.add(order_item)
#             new_order.save()
#
#             send_order_email(new_order.id)
#
#             return redirect('Ecommerce:checkout', new_order.id)
#
#     else:
#         form = OrderForm()
#
#     context = {
#         'orderitems': orderitems,
#         'items': items,
#         'overall_total_price': overall_total_price,
#         'form': form
#     }
#     return render(request, 'cart.html', context)

# from django.core.mail import send_mail
# from django.template.loader import render_to_string
# from django.utils.html import strip_tags
# from django.conf import settings
# from django.db.models import Sum
#

#
# def send_order_email(order_id):
#     order = Order.objects.get(id=order_id)
#     overall_total_price = order.item.aggregate(total_price=Sum('total_price'))['total_price'] or 0
#     # Construct the plain text version of the message
#     message = f'Order ID: {order.id}\nOrder Date: {order.created_at}\n\nOrder Details:\n'
#     message += f'Name: {order.name}\n'
#     message += f'Company Name: {order.companyname}\n'
#     message += f'Phone: {order.phone}\n'
#     message += f'Email Address: {order.emailaddress}\n'
#     message += f'Country: {order.country}\n'
#     message += f'Shipping Address: {order.shipping_address}\n'
#     message += f'Apartment Address: {order.apartment_address}\n'
#     message += f'ZIP: {order.zip}\n'
#
#     # Iterate over the order items and add them to the message
#     for item in order.item.all():
#         message += f'Item: {item.items}\nQuantity: {item.quantity}\nPrice: {item.price}\n\n'
#     plain_message = strip_tags(message)
#     # Construct the HTML version of the message using a template
#     html_message = render_to_string('order_confirmation.html', {'order': order,'overall_total_price': overall_total_price},)
#     # Send the email
#     send_mail(
#         subject=f"New Order - Created at {order.created_at}",
#         message=plain_message,
#         from_email=settings.EMAIL_HOST_USER,
#         recipient_list=['amer66965@gmail.com'],
#         html_message=html_message,
#     )





# def delete_item(request, id):
#     session_key = request.session.session_key
#     item = get_object_or_404(Item, id=id)  # Update this line
#     order_item = CardItem.objects.filter(item=item, session_id=session_key)
#     order_item.delete()
#     return redirect('Ecommerce:Orderitem')
#
#
# def update_quantity(request):
#     session_key = request.session.session_key
#     if request.method == 'POST':
#         itemId = request.POST.get('itemId')  # Access the itemId from the POST data
#         quantity = request.POST.get('quantity')  # Access the quantity from the POST data
#         try:
#             card_item = get_object_or_404(CardItem, item=itemId, session_id=session_key)
#             if quantity == 'increase':
#                 card_item.quantity += 1
#                 card_item.save()
#             else:
#                 if card_item.quantity > 0:  # Check if quantity is greater than 0
#                     card_item.quantity -= 1
#                     card_item.save()
#
#             response_data = {
#                 'message': 'Quantity updated successfully.',
#                 'newQuantity': card_item.quantity
#             }
#             return JsonResponse(response_data)
#         except CardItem.DoesNotExist:
#             response_data = {
#                 'error': 'CardItem not found.'
#             }
#             return JsonResponse(response_data, status=404)
#     response_data = {'error': 'Invalid request method.'}
#     return JsonResponse(response_data, status=400)

#


#
# def checkout(request, id):
#     try:
#         session_key = request.session.session_key
#         order = get_object_or_404(Order, id=id, session_key=session_key)
#         items = []
#         overall_total_price = Decimal(0)
#
#         for order_item in order.item.all():
#             total_price = order_item.total_price or Decimal(0)
#             items.append({
#                 'item': order_item.items,
#                 'price': order_item.price,
#                 'quantity': order_item.quantity,
#                 'total_price': total_price
#             })
#             overall_total_price += total_price
#
#         invoice_number = generate_invoice_number()  # Generate unique invoice number
#
#         order.Tracking = invoice_number
#         order.save()
#     except Order.DoesNotExist:
#         return redirect('Ecommerce:Orderitem')
#
#     context = {
#         'items': items,
#         'overall_total_price': overall_total_price,
#         'order': order,
#         'date': datetime.datetime.now(),
#         'invoice_number': invoice_number,
#     }
#
#     return render(request, 'checkout.html', context)
#
# import random
# import datetime
#
# def generate_invoice_number():
#     while True:
#         random_number = random.randint(1000, 9999)
#         current_date = datetime.datetime.now()
#         formatted_date = current_date.strftime('%Y%m%d')
#         invoice_number = f"{formatted_date}{random_number}"
#         # Check if the invoice number already exists in Order objects
#         if not Order.objects.filter(Tracking=invoice_number).exists():
#             return invoice_number






#
# def payment_success(request, order_id):
#     try:
#         session_key = request.session.session_key
#         order = get_object_or_404(Order, id=order_id)
#         order.default = True
#         order.save()
#
#         order_items = order.item.all()
#         for order_item in order_items:
#             Item.objects.filter(id=order_item.id).update(stock_no=F('stock_no') - order_item.quantity)
#         cart_item = CardItem.objects.filter(session_id=session_key)
#         for cart in cart_item:
#             cart.delete()
#
#         return JsonResponse(safe=True)
#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)
#
#
#
# def success(request,order_id):
#     order = Order.objects.get(id=order_id)
#     overall_total_price = order.item.aggregate(total_price=Sum('total_price'))['total_price'] or 0
#     context =  {'order': order,'overall_total_price': overall_total_price}
#     send_order_email(order.id)
#
#     return render(request, 'success.html',context)
#
#
#
# def payment_confirmation(request,order_id):
#     order = Order.objects.get(id=order_id)
#     overall_total_price = order.item.aggregate(total_price=Sum('total_price'))['total_price'] or 0
#     context =  {'order': order,'overall_total_price': overall_total_price}
#     return render(request, 'payment_confirmation.html',context)
#
# #
#
# def TrackOrder(request):
#     order = None  # Initialize the order variable as None
#     massage = None  # Initialize the massage variable as None
#     if request.method == 'POST':
#         ordernumber = request.POST.get('order-number')  # Get the order number from the form
#         try:
#             order = Order.objects.get(Tracking=ordernumber)
#         except Order.DoesNotExist:
#             massage = 'الطلب غير موجود'
#     context = {'order': order, 'massage': massage}
#     return render(request, 'TrackOrder.html', context)
