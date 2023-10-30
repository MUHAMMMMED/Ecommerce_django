from django.shortcuts import get_object_or_404,render
from Ecommerce.models import Order

def TrackOrder(request):
    order = None  # Initialize the order variable as None
    massage = None  # Initialize the massage variable as None
    if request.method == 'POST':
        ordernumber = request.POST.get('order-number')  # Get the order number from the form
        try:
            order = Order.objects.get(Tracking=ordernumber)
        except Order.DoesNotExist:
            massage = 'الطلب غير موجود'
    context = {'order': order, 'massage': massage}
    return render(request, 'TrackOrder.html', context)
