from django.urls import path,include, re_path
from Ecommerce.views.blog import*
from Ecommerce.views.Cart import*
from Ecommerce.views.categories import*
from Ecommerce.views.checkout import*
from Ecommerce.views.home import*
from Ecommerce.views.invoice import*
from Ecommerce.views.item import*
from Ecommerce.views.payment import*
from Ecommerce.views.Orderitem import*
from Ecommerce.views.TrackOrder import*



app_name='Ecommerce'

urlpatterns=[
   path('',home, name="home"),
   path('Category/',categories, name="categories"),
   re_path(r'^Category/(?P<slug>[-\w.]+)/$',CategoryDetails, name='Category'),
   re_path(r'^Item/(?P<slug>[-\w.]+)/$',item_detail, name='item_detail'),

   path('TrackOrder/',TrackOrder, name='TrackOrder'),
   path('blog',blog, name="blogAll"),
   re_path(r'^Blog/(?P<slug>[-\w.]+)/$',BlogDetails, name='blogdetails'),

   path('add-to-cart/<int:id>/', add_to_cart, name='add_to_cart'),
   path('go_to_cart/<int:id>/', go_to_cart, name='go_to_cart'),
   path('Add_to_cart/<int:id>/', Add_to_cart, name='Add_to_cart'),

   path('refresh/', refresh_cart, name='refresh_cart_item'),

   path('Orderitem/', Orderitem, name='Orderitem'),
   path('deleteitem/<int:id>/', delete_item, name='deleteitem'),
   path('update_quantity/', update_quantity, name='update_quantity'),

   path('checkout/<int:id>/', checkout, name='checkout'),
   path('payment/success/<int:order_id>/', payment_success, name='payment_success'),
   path('success/<int:order_id>/', success, name='success'),

   path('payment/confirmation/<int:order_id>/', payment_confirmation, name='payment_confirmation'),





]
