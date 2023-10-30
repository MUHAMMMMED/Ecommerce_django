from django.shortcuts import get_object_or_404,redirect
from Ecommerce.models import Order,CardItem,Item
from django.http import JsonResponse

def add_to_cart(request, id):
    # Get or create session
    session_key = request.session.session_key
    if not session_key:
        request.session.save()
        session_key = request.session.session_key
    # Get item object
    item = get_object_or_404(Item, id=id)
    # Get the existing cart item or create a new one
    cart_item, created = CardItem.objects.get_or_create(session_id=session_key, item=item)
    # Update the quantity of the cart item
    cart_item.quantity += 1
    cart_item.save()
    # Get the updated cart item count
    cart_item_count = CardItem.objects.filter(session_id=session_key).count()
    # Prepare the JSON response with success message and cart item count
    data = {'cart_item_count': cart_item_count,'message': 'تم الاضافة الى السلة',}
    return JsonResponse(data)



def go_to_cart(request, id):
    # Get or create session
    session_key = request.session.session_key
    if not session_key:
        request.session.save()
        session_key = request.session.session_key
    # Get item object
    item = get_object_or_404(Item, id=id)
    # Get cart item or create a new one
    cart_item, created = CardItem.objects.get_or_create(    session_id=session_key,item=item,)
    # Prepare the JSON response with success message and cart item count
    data = {'message': 'تم الاضافة الي السلة',    }
    return JsonResponse(data)



def Add_to_cart(request, id):
    if request.method == 'POST':
        quantity = request.POST.get('quantity')  # Get the quantity from the POST data
        # print('quantity',quantity)
        session_key = request.session.session_key
        if not session_key:
            request.session.save()
            session_key = request.session.session_key
        # Get item object
        item = get_object_or_404(Item, id=id)
        # Check if the cart item already exists
        cart_item = CardItem.objects.filter(session_id=session_key, item=item).first()
        if cart_item:
            # Update the quantity of the existing cart item
            cart_item.quantity += int(quantity)
            cart_item.save()
        else:
            # Create a new cart item
            cart_item = CardItem.objects.create(session_id=session_key, item=item, quantity=quantity)
        # Get the updated cart item count
        cart_item_count = CardItem.objects.filter(session_id=session_key).count()
        # Prepare the JSON response with success message and cart item count
    data = {
        'cart_item_count': cart_item_count,
        'message': 'تم الاضافة الى السلة',
    }

    return JsonResponse(data)

def refresh_cart(request):
    session_key = request.session.session_key
    cart_item_count = CardItem.objects.filter(session_id=session_key).count()
    data = {
        'cart_item_count': cart_item_count,
     }
    return JsonResponse(data)




def delete_item(request, id):
    session_key = request.session.session_key
    item = get_object_or_404(Item, id=id)  # Update this line
    order_item = CardItem.objects.filter(item=item, session_id=session_key)
    order_item.delete()
    return redirect('Ecommerce:Orderitem')


def update_quantity(request):
    session_key = request.session.session_key
    if request.method == 'POST':
        itemId = request.POST.get('itemId')  # Access the itemId from the POST data
        quantity = request.POST.get('quantity')  # Access the quantity from the POST data
        try:
            card_item = get_object_or_404(CardItem, item=itemId, session_id=session_key)
            if quantity == 'increase':
                card_item.quantity += 1
                card_item.save()
            else:
                if card_item.quantity > 0:  # Check if quantity is greater than 0
                    card_item.quantity -= 1
                    card_item.save()
            response_data = {
                'message': 'Quantity updated successfully.',
                'newQuantity': card_item.quantity    }

            return JsonResponse(response_data)
        except CardItem.DoesNotExist:
            response_data = {
                'error': 'CardItem not found.'
            }
            return JsonResponse(response_data, status=404)
    response_data = {'error': 'Invalid request method.'}
    return JsonResponse(response_data, status=400)
