from django.shortcuts import render
# Create your views here.
from .models import *

def Basegeneric(request):
    info= Info.objects.all().first()
    slide=Slide.objects.all().first()
    CategoryNav= Category.objects.filter(is_active=True)
    questionsgeneral=QuestionsGeneral.objects.all()
    BaseTextT=BaseTextTranslate.objects.all().first()
    InvoiceTextT=InvoiceTextTranslate.objects.all().first()
    TrackTextT=TrackTextTranslate.objects.all().first()
    MoreText=MoreTextTranslate.objects.all().first()
    ItemText=ItemTextTranslate.objects.all().first()
    session_key = request.session.session_key
    item = Item.objects.filter(is_active=True).order_by('?')
    cart_item_count = CardItem.objects.filter(session_id=session_key).count()
    paynaw = Order.objects.filter(default=False, session_key=session_key)
    context = {
    'BaseTextT':BaseTextT,
    'InvoiceTextT':InvoiceTextT,
    'TrackTextT':TrackTextT,
    'MoreText':MoreText,
    'info':info,
    'slide':slide,
    'questionsgeneral':questionsgeneral,
    'CategoryNav':CategoryNav,
    'item':item,
    'ItemText':ItemText,
     'cart_item_count': cart_item_count,
     'paynaw':paynaw,
   }
    return context
