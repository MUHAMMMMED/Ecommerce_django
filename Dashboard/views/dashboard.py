from django.shortcuts import render, redirect, get_object_or_404
from Ecommerce.models import  Order,BaseTextTranslate
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from decimal import Decimal, ROUND_DOWN



def tax_count(Subtotal,tax):
    tax_number =  Decimal(Subtotal  *  tax / 100)
    return tax_number

def convert_currency(amount):
    conversion_rates = {
        'SAR': Decimal('0.266'),  # معدل تحويل SAR إلى USD
        'USD': Decimal('1.0'),   # معدل تحويل USD إلى نفسها
    }
    converted_amount = amount * conversion_rates['SAR']
    return converted_amount


@login_required
def dashboard(request):
    if not request.user.is_manager():
     return render(request, 'error.html', {'message': 'You are not authorized to access this page.'})
    order = Order.objects.filter(default=True,Orderـstatus='waiting')
    order_count=order.count()
    Title=' طلب جديد'
    context =  {'order': order,'order_count':order_count,'Title':Title}
    return render(request, 'Dashboard.html',context)

@login_required
def waiting_buy(request):

    if not request.user.is_manager():
        return render(request, 'error.html', {'message': 'You are not authorized to access this page.'})

    order = Order.objects.filter(default=False)
    order_count=order.count()
    Title='انتظار للدفع'
    context =  {'order': order,'order_count':order_count,'Title':Title}
    return render(request, 'waiting_buy.html',context)

@login_required
def OrderProcessing(request):

    if not request.user.is_manager():
            return render(request, 'error.html', {'message': 'You are not authorized to access this page.'})
    order = Order.objects.filter(default=True,Orderـstatus='Orderprocessing')
    order_count=order.count()
    Title=' تجهيز الطلب'
    context =  {'order': order,'order_count':order_count,'Title':Title}
    return render(request, 'Processing.html',context)

@login_required
def Shipping(request):

    if not request.user.is_manager():
        return render(request, 'error.html', {'message': 'You are not authorized to access this page.'})

    order = Order.objects.filter(default=True,Orderـstatus='Shipping')
    order_count=order.count()
    Title=' تم الشحن'
    context =  {'order': order,'order_count':order_count,'Title':Title}
    return render(request, 'Processing.html',context)

@login_required
def OrderDone(request):
    if not request.user.is_manager():
        return render(request, 'error.html', {'message': 'You are not authorized to access this page.'})

    order = Order.objects.filter(default=True,Orderـstatus='Orderdone')
    order_count=order.count()
    Title='تم التسليم'
    context =  {'order': order,'order_count':order_count,'Title':Title}
    return render(request, 'Processing.html',context)

@login_required
def OrderCancel(request):

    if not request.user.is_manager():
        return render(request, 'error.html', {'message': 'You are not authorized to access this page.'})

    order = Order.objects.filter(Orderـstatus='cancel')
    order_count=order.count()
    Title=' الغاء الطلب'
    context =  {'order': order,'order_count':order_count,'Title':Title}
    return render(request, 'Processing.html',context)

@login_required

def orderdetails(request, id):
    if not request.user.is_manager:
        return render(request, 'error.html', {'message': 'You are not authorized to access this page.'})

    order = get_object_or_404(Order, id=id)
    BaseTextT=BaseTextTranslate.objects.all().first()
    overall_total_price = Decimal(0)
    shipping_price = order.country.shipping_price
    Subtotal = order.item.aggregate(total_price=Sum('total_price'))['total_price'] or 0
    tax = order.country.tax
    tax_number = tax_count(Subtotal,tax)

    overall_total_price += Subtotal
    overall_total_price += tax_number
    overall_total_price += shipping_price

    ENoverall_total_price = convert_currency(overall_total_price)


    if request.method == 'POST':
        if 'status' in request.POST:
            status = request.POST.get('stat')  # Get the selected status from the form
            print('status', status)
            order.Orderـstatus = status  # Update the order status field
            order.save()  # Save the changes to the database
            print('status', order.Orderـstatus)

            return redirect('Dashboard:dashboard')

        elif 'day' in request.POST:
            day = request.POST.get('Day')  # Get the selected day from the form
            print('day', day)
            order.anticipation = day  # Update the order anticipation field
            print('order', order.anticipation)

            order.save()  # Save the changes to the database
            return redirect('Dashboard:dashboard')
    context = {
    'order': order,
    # 'currency': items[0]['currency'],
    'Subtotal':"{:.2f}".format(Subtotal) ,
    'tax_number':"{:.2f}".format(tax_number),
    'shipping_price': shipping_price,
    'overall_total_price': overall_total_price ,
    'ENoverall_total_price':"{:.2f}".format(ENoverall_total_price) ,

 }

    return render(request, 'orderdetails.html', context)










def invoice(request,id):
    order = Order.objects.get(id=id)
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

    return render(request, 'invoice.html',context)
