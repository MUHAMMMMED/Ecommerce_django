from django.urls import path
from .views .dashboard import*
from .views .blog import*
from .views .categories import*
from .views .howitwork import*
from .views .info import*
from .views .items import*
from .views .question import*
from .views .QuestionsGeneral import*
from .views .slide import*
from .views .PAYNEW import*
from .views .report import*

app_name='Dashboard'
urlpatterns=[
      path('',dashboard, name='dashboard'),
      path('waiting_buy/',waiting_buy, name='waiting_buy'),
      path('Processing/',OrderProcessing, name='OrderProcessing'),
      path('Shipping/',Shipping, name='Shipping'),
      path('Done/',OrderDone, name='OrderDone'),
      path('Cancel/',OrderCancel, name='OrderCancel'),
      path('paynaw/<int:id>/',paynaw, name='paynaw'),




      path('order/<int:id>/',orderdetails, name='orderdetails'),
      path('invoice/<int:id>/',invoice, name='invoice'),

      path('category/',categories, name='category'),
      path('category/create',create_category, name='create_category'),
      path('category/update/<int:id>/',update_category, name='update_category'),
      path('category/delete/<int:id>/', delete_category, name='delete_category'),

      path('items/',items, name='items'),
      path('item/create/',create_item, name='create_item'),
      path('item/update/<int:item_id>/', update_item, name='update_item'),
      path('item/delete/<int:item_id>/', delete_item, name='delete_item'),

      path('question/create/<int:id>/',create_question, name='create_question'),
      path('question/update/<int:question_id>/<int:item_id>/', update_question, name='update_question'),
      path('question/delete/<int:question_id>/<int:item_id>/', delete_question, name='delete_question'),

      path('howitwork/create/<int:item_id>/',create_howitwork, name='create_howitwork'),
      path('howitwork/update/<int:howitwork_id>/<int:item_id>/', update_howitwork, name='update_howitwork'),
      path('howitwork/delete/<int:howitwork_id>/<int:item_id>/', delete_howitwork, name='delete_howitwork'),

      path('question/', question_list, name='question_list'),
      path('Question/create/', create_or_update_question, name='create_Question'),
      path('Question/update/<int:question_id>/', create_or_update_question, name='update_Question'),
      path('Question/delete/<int:question_id>/', delete_question, name='delete_Question'),


      path('slide/', slide_list, name='slide_list'),
      path('slide/create/', create_or_update_slide, name='create_slide'),
      path('slide/update/<int:slide_id>/', create_or_update_slide, name='update_slide'),
      path('slide/delete/<int:slide_id>/', delete_slide, name='delete_slide'),

      path('blog/', blog_list, name='blog_list'),
      path('blog/create/', create_or_update_blog, name='create_blog'),
      path('blog/update/<int:blog_id>/', create_or_update_blog, name='update_blog'),
      path('blog/delete/<int:blog_id>/', delete_blog, name='delete_blog'),

      path('info/', info_list, name='info_list'),
      path('info/create/', create_or_update_info, name='create_info'),
      path('info/update/<int:info_id>/', create_or_update_info, name='update_info'),
      path('info/delete/<int:info_id>/', delete_info, name='delete_info'),

      path('Report/', order_report, name='order_report'),


]
