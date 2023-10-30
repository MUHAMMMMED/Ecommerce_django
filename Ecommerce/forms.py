from django import forms

from ckeditor.widgets import CKEditorWidget
from Ecommerce.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'companyname', 'phone', 'emailaddress', 'country', 'city', 'shipping_address', 'apartment_address', 'zip']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'الاسم', 'class': 'inputform'}),
            'phone': forms.TextInput(attrs={'placeholder': 'رقم الهاتف', 'class': 'inputform'}),
            'companyname': forms.TextInput(attrs={'placeholder': 'اسم الشركة (اختياري)', 'class': 'inputform'}),
            'emailaddress': forms.TextInput(attrs={'placeholder': 'البريد الالكتروني', 'class': 'inputform'}),
            # 'country': forms.selct(attrs={'placeholder': 'الدولة', 'class': 'inputform'}),

            'city': forms.TextInput(attrs={'placeholder': 'البلد / المدينة', 'class': 'inputform'}),
            'shipping_address': forms.Textarea(attrs={'placeholder': 'العنوان', 'rows': 3, 'class': 'inputform'}),
            'apartment_address': forms.Textarea(attrs={'placeholder': 'عنوان آخر (اختياري)', 'rows': 2, 'class': 'inputform'}),
            'zip': forms.TextInput(attrs={'placeholder': 'الرمز البريدي / ZIP (اختياري)', 'class': 'inputform'}),
        }


# class OrderForm(forms.ModelForm):
#
#     class Meta:
#         model = Order
#         fields = ['name', 'companyname', 'phone', 'emailaddress', 'country', 'city', 'shipping_address', 'apartment_address', 'zip']
#         widgets = {
#             'name': forms.TextInput(attrs={'placeholder': 'الاسم', 'class': 'inputform'}),
#             'phone': forms.TextInput(attrs={'placeholder': 'رقم الهاتف', 'class': 'inputform'}),
#             'companyname': forms.TextInput(attrs={'placeholder': 'اسم الشركة (اختياري)', 'class': 'inputform'}),
#             'emailaddress': forms.TextInput(attrs={'placeholder': 'البريد الالكتروني', 'class': 'inputform'}),
#             'country': forms.ChoiceField('placeholder': 'الدولة', 'class': 'inputform'}),
#             'city': forms.TextInput(attrs={'placeholder': 'البلد / المدينة', 'class': 'inputform'}),
#             'shipping_address': forms.Textarea(attrs={'placeholder': 'العنوان', 'rows': 3, 'class': 'inputform'}),
#             'apartment_address': forms.Textarea(attrs={'placeholder': 'عنوان آخر (اختياري)', 'rows': 2, 'class': 'inputform'}),
#             'zip': forms.TextInput(attrs={'placeholder': 'الرمز البريدي / ZIP (اختياري)', 'class': 'inputform'}),
#         }


#
# class OrderForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = ['name', 'companyname', 'phone', 'emailaddress', 'country', 'city', 'shipping_address', 'apartment_address', 'zip']
#         widgets = {
#             'name': forms.TextInput(attrs={'placeholder': 'الاسم', 'class': 'inputform'}),
#             'phone': forms.TextInput(attrs={'placeholder': 'رقم الهاتف', 'class': 'inputform'}),
#             'companyname': forms.TextInput(attrs={'placeholder': 'اسم الشركة (اختياري)', 'class': 'inputform'}),
#             'emailaddress': forms.TextInput(attrs={'placeholder': 'البريد الالكتروني', 'class': 'inputform'}),
#             'country': forms.TextInput(attrs={'placeholder': 'الدولة', 'class': 'inputform'}),
#             'city': forms.TextInput(attrs={'placeholder': 'البلد / المدينة', 'class': 'inputform'}),
#             'shipping_address': forms.Textarea(attrs={'placeholder': 'العنوان', 'rows': 3, 'class': 'inputform'}),
#             'apartment_address': forms.Textarea(attrs={'placeholder': 'عنوان آخر (اختياري)', 'rows': 2, 'class': 'inputform'}),
#             'zip': forms.TextInput(attrs={'placeholder': 'الرمز البريدي / ZIP (اختياري)', 'class': 'inputform'}),
#         }

        # labels = {
        #     'name': '',
        #     'companyname': '',
        #     'emailaddress': '',
        #     'phone': '',
        #     'country': '',
        #     'city': '',
        #     'shipping_address': '',
        #     'apartment_address': '',
        #     'zip': '',
        # }

# form-control
