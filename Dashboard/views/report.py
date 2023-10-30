
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from Ecommerce.models import Order
from django.contrib.auth.decorators import login_required


@login_required
def order_report(request):
    order_counts = Order.objects.values('Orderـstatus').annotate(count=Count('Orderـstatus'))
    waiting_buy = Order.objects.filter(default=False)
    waiting_buy_count=waiting_buy.count()
    context = {
        'order_counts': order_counts,
        'waiting_buy_count':waiting_buy_count,
    }
    return render(request, 'report.html', context)
