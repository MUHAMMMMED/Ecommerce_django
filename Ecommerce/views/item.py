from django.shortcuts import get_object_or_404,render,redirect
from decimal import Decimal, ROUND_DOWN
from Ecommerce.models import Item



def item_detail(request,slug):
    iteM = get_object_or_404(Item, slug=slug)
    price = iteM.price

    discount_percentage1 = Decimal(iteM.discount_price1) if iteM.discount_price1 is not None else Decimal(0)
    discount_percentage2 = Decimal(iteM.discount_price2) if iteM.discount_price2 is not None else Decimal(0)
    discount_percentage3 = Decimal(iteM.discount_price3) if iteM.discount_price3 is not None else Decimal(0)

    discounted_price1 = price - (price * (discount_percentage1 / Decimal(100)))
    discounted_price2 = price - (price * (discount_percentage2 / Decimal(100)))
    discounted_price3 = price - (price * (discount_percentage3 / Decimal(100)))

    # Quantize the discounted prices to two decimal places
    discounted_price1 = discounted_price1.quantize(Decimal('0.00'), rounding=ROUND_DOWN)
    discounted_price2 = discounted_price2.quantize(Decimal('0.00'), rounding=ROUND_DOWN)
    discounted_price3 = discounted_price3.quantize(Decimal('0.00'), rounding=ROUND_DOWN)

    context = {
        'iteM': iteM,
        'discounted_price1': discounted_price1,
        'discounted_price2': discounted_price2,
        'discounted_price3': discounted_price3,
    }

    return render(request, 'single-product.html', context)
