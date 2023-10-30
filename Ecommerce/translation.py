from modeltranslation.translator import translator, TranslationOptions
from .models import  Category,Item,Questions,Howitwork,Blog,QuestionsGeneral,ItemTextTranslate,TrackTextTranslate,InvoiceTextTranslate,BaseTextTranslate,MoreTextTranslate,Country


class questionsgeneralyTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')
translator.register(QuestionsGeneral,questionsgeneralyTranslationOptions)


class categoryTranslationOptions(TranslationOptions):
     fields = ('title','description','keywords')
translator.register(Category, categoryTranslationOptions)

class ItemTranslationOptions(TranslationOptions):
     fields = ('title','description_short','description_long','keywords','price')
translator.register(Item, ItemTranslationOptions)

class questionTranslationOptions(TranslationOptions):
    fields = ('question','answer')
translator.register(Questions, questionTranslationOptions)




class CountryTranslationOptions(TranslationOptions):
    fields = ('shipping_price',)
translator.register(Country, CountryTranslationOptions)




class howTranslationOptions(TranslationOptions):
      fields = ('title','description' )
translator.register(Howitwork, howTranslationOptions)

class blogTranslationOptions(TranslationOptions):
      fields = ('keywords','Titel','description','body' )
translator.register(Blog, blogTranslationOptions)



class BaseTextTranslateTranslationOptions(TranslationOptions):
    fields = (
        'currency',
        'home',
        'ourProducts',
        'blog',
        'all_Categories',
        'track_order',
        'open_site',
        'waiting_for_payment',
        'new_order',
        'order_processing',
        'shipping',
        'delivery_Confirmation',
        'cancelling_order',
        'reports',
        'questions',
        'categories',
        'items',
        'web_information',
        'tape_slider',
        'best_selle',
        'logout',
        'help_categories'
    )

translator.register(BaseTextTranslate, BaseTextTranslateTranslationOptions)






class ItemTextTranslateTranslationOptions(TranslationOptions):
    fields = (
        'howitـworks',
        'Buyـmore',
        'discount',
        'price',
        'Quantity',
        'Category',
        'Addـtoـcart',
        'questionsanswered',
        'make_purchase',
        'description',
        'Notـavailable',
    )

translator.register(ItemTextTranslate, ItemTextTranslateTranslationOptions)


class InvoiceTextTranslateTranslationOptions(TranslationOptions):
    fields = (
        'invoic_help',
        'Date',
        'shipping_information',
        'order_number',
        'Paid',
        'not_Paid',
        'contact_information',
        'product_name',
        'price',
        'Quantity',
        'total',
        'subtotal',
        'shipping',
        'tax',
        'total_all',
        'pay_help',
        'save_order_number',
        'track_order_number',
        'you_can',
        'print',
    )

translator.register(InvoiceTextTranslate, InvoiceTextTranslateTranslationOptions)



class TrackTextTranslateTranslationOptions(TranslationOptions):
    fields = (
        'track_help',
        'track_but',
        'order_number',
        'track_your_order',
        'order_status',
        'waiting',
        'processing',
        'shipped',
        'arrival_day',
        'Order_delivered',
        'cancelled',
        'Saturday',
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
    )

translator.register(TrackTextTranslate, TrackTextTranslateTranslationOptions)




class MoreTextTranslateTranslationOptions(TranslationOptions):
    fields = (
        'stockout',
        'buy_Now',
        'learn_More',
        'help_you',
        'add_new_product',
        'help_Payment',
        'go_Payment',
        'go_Shopping',
    )

translator.register(MoreTextTranslate, MoreTextTranslateTranslationOptions)
