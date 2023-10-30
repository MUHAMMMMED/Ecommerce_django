from django.db import models
# from Users.models import *
from django.contrib.sessions.models import Session
from ckeditor.fields import RichTextField
from django.utils.text import slugify
import os

class Slide(models.Model):

    top_slider_web= models.FileField(upload_to="files/images/Item/%Y/%m/%d/", blank=True, null=True)
    top_slider_mobile= models.FileField(upload_to="files/images/Item/%Y/%m/%d/", blank=True, null=True)
    is_active = models.BooleanField(default=True)




class Info(models.Model):
      keywords= models.CharField(max_length = 300,blank=True, null=True)
      FaviconIco= models.FileField(upload_to = "files/images/FaviconIco/%Y/%m/%d/",blank=True, null=True)
      logo = models.FileField(upload_to = "files/images/logo/%Y/%m/%d/",blank=True, null=True)
      title = models.CharField(max_length=100,blank=True, null=True)
      PHONE = models.CharField(max_length = 15 ,blank=True, null=True)
      Whatsapp= models.CharField(max_length=15,blank=True, null=True)
      linkedinlinke= models.CharField(max_length=500,blank=True, null=True)
      snapchat= models.CharField(max_length=300,blank=True, null=True)
      instagramlinke= models.CharField(max_length=300,blank=True, null=True)
      Twitterlinke= models.CharField(max_length=300,blank=True, null=True)
      facebooklinke= models.CharField(max_length=300,blank=True, null=True)
      Map_Address= models.CharField(max_length=300,blank=True, null=True)

      def __str__(self):
         return self.title

class QuestionsGeneral(models.Model):
      question= models.CharField(max_length = 300 ,blank=True, null=True)
      answer = models.CharField(max_length=300,blank=True, null=True)
      def __str__(self):
         return self.question

class Category(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    keywords = models.CharField(max_length=300, blank=True, null=True)
    top_slider_web= models.FileField(upload_to="files/images/Item/%Y/%m/%d/", blank=True, null=True)
    top_slider_mobile= models.FileField(upload_to="files/images/Item/%Y/%m/%d/", blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    Image = models.FileField(upload_to="files/images/Category/%Y/%m/%d/", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    slug = models.CharField(max_length=100, blank=True, null=True)


    def delete(self, *args, **kwargs):
        self.Image.delete()
        self.top_slider_web.delete()
        self.top_slider_mobile.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title








class Questions(models.Model):
      question= models.CharField(max_length = 300 ,blank=True, null=True)
      answer = models.CharField(max_length=300,blank=True, null=True)
      def __str__(self):
         return self.question


class Howitwork(models.Model):
      Image = models.FileField(upload_to="files/images/Item/%Y/%m/%d/", blank=True, null=True)
      title = models.CharField(max_length=100)
      description= models.CharField(max_length=300)
      def __str__(self):
         return self.title


class Item(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    stock_no = models.IntegerField(default=0)
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE, related_name='item', blank=True, null=True)


    side_one = models.FileField(upload_to="files/images/side_one/%Y/%m/%d/", blank=True, null=True)
    side_two = models.FileField(upload_to="files/images/side_one/%Y/%m/%d/", blank=True, null=True)

    top_slider_web= models.FileField(upload_to="files/images/Item/%Y/%m/%d/", blank=True, null=True)
    top_slider_mobile= models.FileField(upload_to="files/images/Item/%Y/%m/%d/", blank=True, null=True)
    top_slider_video= models.CharField(max_length=300, blank=True, null=True)


    price = models.DecimalField(max_digits=10, decimal_places=2,default=0)

    quantity1= models.IntegerField(default=0)
    quantity2= models.IntegerField(default=0)
    quantity3= models.IntegerField(default=0)

    discount_price1 = models.FloatField(default=0,blank=True, null=True)
    discount_price2 = models.FloatField(default=0,blank=True, null=True)
    discount_price3 = models.FloatField(default=0,blank=True, null=True)

    description_short = models.CharField(max_length=50,blank=True, null=True)
    description_long = models.TextField(blank=True, null=True)

    keywords = models.CharField(max_length=300, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    slug = models.CharField(max_length=100, blank=True, null=True)

    Image1 = models.FileField(upload_to="files/images/Item/%Y/%m/%d/", blank=True, null=True)
    Image2 = models.FileField(upload_to="files/images/Item/%Y/%m/%d/", blank=True, null=True)
    Image3 = models.FileField(upload_to="files/images/Item/%Y/%m/%d/", blank=True, null=True)
    Image4 = models.FileField(upload_to="files/images/Item/%Y/%m/%d/", blank=True, null=True)
    Image5 = models.FileField(upload_to="files/images/Item/%Y/%m/%d/", blank=True, null=True)
    Image6 = models.FileField(upload_to="files/images/Item/%Y/%m/%d/", blank=True, null=True)

    video_link1= models.CharField(max_length=300, blank=True, null=True)
    video_link2= models.CharField(max_length=300, blank=True, null=True)

    questions=models.ManyToManyField(Questions, blank=True )
    howitwork=models.ManyToManyField(Howitwork,blank=True )
    long_image = models.FileField(upload_to = "files/images/long/%Y/%m/%d/",blank=True, null=True)



    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.side_one.delete()
        self.side_two.delete()
        self.top_slider_web.delete()
        self.top_slider_mobile.delete()
        self.Image1.delete()
        self.Image2.delete()
        self.Image3.delete()
        self.Image4.delete()
        self.Image5.delete()
        self.Image6.delete()

        super().delete(*args, **kwargs)





class CardItem(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return str(self.item)



class OrderItem(models.Model):
    items = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='orderItem')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    # def __str__(self):
    #     return f"{self.item} ({self.quantity})"



class Country(models.Model):
    name = models.CharField(max_length=100)
    shipping_price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    tax  = models.IntegerField(default=0)
    def __str__(self):
        return str(self.name)

class Order(models.Model):

    STATUS_CHOICES = [
     ('waiting','انتظار'),
     ('Orderprocessing', 'تجهيز الطلب'),
     ('Shipping', 'تم الشحن'),
     ('Orderdone','تم'),
     ('cancel','الغاء'),


      ]

    DAY = [
        ('mon', 'الاثنين'),
        ('tue', 'الثلاثاء'),
        ('wed', 'الأربعاء'),
        ('thu', 'الخميس'),
        ('fri', 'الجمعة'),
        ('sat', 'السبت'),
        ('sun', 'الأحد'),
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    companyname = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    emailaddress = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country_order')
    city = models.CharField(max_length=100)
    shipping_address= models.CharField(max_length=500)
    apartment_address = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    item=models.ManyToManyField(OrderItem,blank=True)
    session_key= models.CharField(max_length=100)
    default = models.BooleanField(default=False)
    Orderـstatus = models.CharField(max_length=20, choices=STATUS_CHOICES, default='waiting')
    anticipation = models.CharField(max_length=20, choices=DAY, blank=True, null=True)
    Tracking = models.CharField(max_length=20, blank=True, null=True)
    def __str__(self):
        return self.name










class Blog(models.Model):
   created_at = models.DateTimeField(auto_now_add=True)
   active = models.BooleanField(default = False)
   slug = models.CharField(max_length=100, blank=True, null=True)
   keywords = models.CharField(max_length=300, blank=True, null=True)
   category=models.ForeignKey(Category,on_delete=models.CASCADE, related_name='Blog', blank=True, null=True)
   Image = models.FileField(upload_to = "files/images/Blog/Image/%Y/%m/%d/",blank=True, null=True)
   Titel= models.CharField(max_length = 100 , null = True)
   description = models.TextField()
   slideImage =models.FileField(upload_to = "files/images/Blog/slideImage/%Y/%m/%d/",blank=True, null=True)
   slideVideo= models.CharField(max_length=300,blank=True, null=True)
   body= RichTextField()

   def __str__(self):
        return self.Titel


class BaseTextTranslate(models.Model):
   currency= models.CharField(max_length = 50 ,blank=True, null=True)
   home= models.CharField(max_length = 50 ,blank=True, null=True)
   ourProducts= models.CharField(max_length = 50 ,blank=True, null=True)
   blog= models.CharField(max_length = 50 ,blank=True, null=True)
   all_Categories= models.CharField(max_length = 50 ,blank=True, null=True)
   track_order= models.CharField(max_length = 50 ,blank=True, null=True)
   open_site= models.CharField(max_length = 50 ,blank=True, null=True)
   waiting_for_payment= models.CharField(max_length = 50 ,blank=True, null=True)
   new_order= models.CharField(max_length = 50 ,blank=True, null=True)
   order_processing= models.CharField(max_length = 50 ,blank=True, null=True)
   shipping= models.CharField(max_length = 50 ,blank=True, null=True)
   delivery_Confirmation= models.CharField(max_length = 50 ,blank=True, null=True)
   cancelling_order= models.CharField(max_length = 50 ,blank=True, null=True)
   reports= models.CharField(max_length = 50 ,blank=True, null=True)
   questions= models.CharField(max_length = 50 ,blank=True, null=True)
   categories= models.CharField(max_length = 50 ,blank=True, null=True)
   items= models.CharField(max_length = 50 ,blank=True, null=True)
   web_information= models.CharField(max_length = 50 ,blank=True, null=True)
   tape_slider= models.CharField(max_length = 50 ,blank=True, null=True)
   best_selle= models.CharField(max_length = 50 ,blank=True, null=True)
   logout= models.CharField(max_length = 50 ,blank=True, null=True)
   help_categories= models.CharField(max_length = 50 ,blank=True, null=True)



class MoreTextTranslate(models.Model):
   stockout= models.CharField(max_length = 50 ,blank=True, null=True)
   buy_Now= models.CharField(max_length = 50,blank=True, null=True)
   learn_More= models.CharField(max_length = 50 ,blank=True, null=True)
   help_you= models.CharField(max_length = 50 ,blank=True, null=True)
   add_new_product= models.CharField(max_length = 50 ,blank=True, null=True)
   help_Payment= models.CharField(max_length = 150 ,blank=True, null=True)
   go_Payment= models.CharField(max_length = 50 ,blank=True, null=True)
   go_Shopping= models.CharField(max_length = 50 ,blank=True, null=True)
 # add_New_Category= models.CharField(max_length = 50 ,blank=True, null=True)
 # update= models.CharField(max_length = 50 ,blank=True, null=True)
 # save= models.CharField(max_length = 50 ,blank=True, null=True)
 # delete= models.CharField(max_length = 50 ,blank=True, null=True)
 # cancel= models.CharField(max_length = 50 ,blank=True, null=True)
 # number_of_Orders= models.CharField(max_length = 50  ,blank=True, null=True)
 # view_Order= models.CharField(max_length = 50 ,blank=True, null=True)
 # delete_this= models.CharField(max_length = 50 ,blank=True, null=True)
 # available_Quantity= models.CharField(max_length = 50 ,blank=True, null=True)
 # no_available= models.CharField(max_length = 50 ,blank=True, null=True)

   # cover_Image= models.CharField(max_length = 50 ,blank=True, null=True)
   # mobile_Cover_Image= models.CharField(max_length = 50 ,blank=True, null=True)
   # faviconIco = models.CharField(max_length = 50 ,blank=True, null=True)
   # logo= models.CharField(max_length = 50 ,blank=True, null=True)
   # title= models.CharField(max_length = 50 ,blank=True, null=True)
   # phone= models.CharField(max_length = 50 ,blank=True, null=True)
   # whatsapp= models.CharField(max_length = 50 ,blank=True, null=True)
   # linkedinlinke= models.CharField(max_length = 50 ,blank=True, null=True)
   # snapchat= models.CharField(max_length = 50 ,blank=True, null=True)
   # instagramlinke = models.CharField(max_length = 50 ,blank=True, null=True)
   # twitterlinke = models.CharField(max_length = 50 ,blank=True, null=True)
   # facebooklinke = models.CharField(max_length = 50 ,blank=True, null=True)
   # map_Address= models.CharField(max_length = 50 ,blank=True, null=True)
    # Currency= models.CharField(max_length = 50 )
   # Currency= models.CharField(max_length = 50 )
   # Currency= models.CharField(max_length = 50 )
   # Currency= models.CharField(max_length = 50 )
   # Currency= models.CharField(max_length = 50 )
   # Currency= models.CharField(max_length = 50 )
   # Currency= models.CharField(max_length = 50 )
   #

   #
   # def __str__(self):
   #         return self.currency

class InvoiceTextTranslate(models.Model):
  invoic_help= models.CharField(max_length = 50 ,blank=True, null=True)
  Date= models.CharField(max_length = 50 ,blank=True, null=True)
  shipping_information= models.CharField(max_length = 50 ,blank=True, null=True)
  order_number = models.CharField(max_length = 50 ,blank=True, null=True)
  Paid= models.CharField(max_length = 50 ,blank=True, null=True)
  not_Paid= models.CharField(max_length = 50 ,blank=True, null=True)
  contact_information = models.CharField(max_length = 50 ,blank=True, null=True)
  product_name= models.CharField(max_length = 50 ,blank=True, null=True)
  price = models.CharField(max_length = 50 ,blank=True, null=True)
  Quantity = models.CharField(max_length = 50 ,blank=True, null=True)
  total= models.CharField(max_length = 50 ,blank=True, null=True)
  subtotal= models.CharField(max_length = 50 ,blank=True, null=True)
  shipping= models.CharField(max_length = 50 ,blank=True, null=True)
  tax= models.CharField(max_length = 50 ,blank=True, null=True)
  total_all= models.CharField(max_length = 50 ,blank=True, null=True)
  pay_help= models.CharField(max_length = 50 ,blank=True, null=True)
  save_order_number= models.CharField(max_length = 100 ,blank=True, null=True)
  track_order_number= models.CharField(max_length = 100 ,blank=True, null=True)
  you_can=models.CharField(max_length = 100 ,blank=True, null=True)
  print= models.CharField(max_length = 50 ,blank=True, null=True)





class TrackTextTranslate(models.Model):

   track_help= models.CharField(max_length = 50 ,blank=True, null=True)
   track_but = models.CharField(max_length = 50 ,blank=True, null=True)
   order_number = models.CharField(max_length = 50 ,blank=True, null=True)
   track_your_order = models.CharField(max_length = 50 ,blank=True, null=True)
   order_status = models.CharField(max_length = 50 ,blank=True, null=True)
   waiting = models.CharField(max_length = 50 ,blank=True, null=True)
   processing = models.CharField(max_length = 50 ,blank=True, null=True)
   shipped  = models.CharField(max_length = 50 ,blank=True, null=True)
   arrival_day = models.CharField(max_length = 50 ,blank=True, null=True)
   Order_delivered = models.CharField(max_length = 50 ,blank=True, null=True)
   cancelled= models.CharField(max_length = 50 ,blank=True, null=True)
   Saturday= models.CharField(max_length = 50 ,blank=True, null=True)
   Sunday= models.CharField(max_length = 50 ,blank=True, null=True)
   Monday= models.CharField(max_length = 50 ,blank=True, null=True)
   Tuesday= models.CharField(max_length = 50 ,blank=True, null=True)
   Wednesday= models.CharField(max_length = 50 ,blank=True, null=True)
   Thursday= models.CharField(max_length = 50 ,blank=True, null=True)
   Friday= models.CharField(max_length = 50 ,blank=True, null=True)




class ItemTextTranslate(models.Model):
   howitـworks= models.CharField(max_length = 50 ,blank=True, null=True)
   Buyـmore= models.CharField(max_length = 100 ,blank=True, null=True)
   discount= models.CharField(max_length = 50 ,blank=True, null=True)
   price= models.CharField(max_length = 50 ,blank=True, null=True)
   Quantity= models.CharField(max_length = 50 ,blank=True, null=True)
   Category= models.CharField(max_length = 50 ,blank=True, null=True)
   Addـtoـcart= models.CharField(max_length = 50 ,blank=True, null=True)
   questionsanswered= models.CharField(max_length = 50 ,blank=True, null=True)
   make_purchase= models.CharField(max_length = 50 ,blank=True, null=True)
   description= models.CharField(max_length = 50 ,blank=True, null=True)
   Notـavailable= models.CharField(max_length = 50 ,blank=True, null=True)
