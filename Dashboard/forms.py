from django import forms
from ckeditor.widgets import CKEditorWidget
from Ecommerce.models import Item ,Category,Questions,Howitwork,QuestionsGeneral,Slide,Blog,Info

class ItemForm(forms.ModelForm):
    title_ar = forms.CharField(label='Title [ar]', max_length=100)

    class Meta:
        model = Item
        fields = '__all__'
        help_texts = {
            'title': 'أدخل عنوان العنصر.',
            'title_ar': 'أدخل العنوان باللغة العربية للعنصر.',
            'stock_no': 'أدخل رقم المخزون للعنصر.',
            'category_id': 'حدد الفئة للعنصر.',
            'side_one': 'قم بتحميل الصورة الخاصة بالجانب الأول من العنصر.',
            'side_two': 'قم بتحميل الصورة الخاصة بالجانب الثاني من العنصر.',
            'top_slider_web': 'قم بتحميل صورة الويب لشريط التمرير الخاص بالعنصر.',
            'top_slider_mobile': 'قم بتحميل صورة الجوال لشريط التمرير الخاص بالعنصر.',
            'top_slider_video': 'أدخل رابط الفيديو لشريط التمرير الخاص بالعنصر.',
            'price': 'أدخل سعر العنصر.',
            'quantity1': 'أدخل الكمية للخيار الأول.',
            'quantity2': 'أدخل الكمية للخيار الثاني.',
            'quantity3': 'أدخل الكمية للخيار الثالث.',
            'discount_price1': 'أدخل سعر الخصم للخيار الأول.',
            'discount_price2': 'أدخل سعر الخصم للخيار الثاني.',
            'discount_price3': 'أدخل سعر الخصم للخيار الثالث.',
            'description_short': 'أدخل وصفًا موجزًا للعنصر.',
            'description_long': 'أدخل وصفًا طويلًا للعنصر.',
            'keywords': 'أدخل الكلمات الرئيسية ذات الصلة بالعنصر.',
            'is_active': 'حدّد هذا الخيار لجعل العنصر نشطًا.',
            'slug': 'أدخل معرّفًا فريدًا لعنوان URL للعنصر.',
            'Image1': 'قم بتحميل صورة إضافية 1 للعنصر.',
            'Image2': 'قم بتحميل صورة إضافية 2 للعنصر.',
            'Image3': 'قم بتحميل صورة إضافية 3 للعنصر.',
            'Image4': 'قم بتحميل صورة إضافية 4 للعنصر.',
            'Image5': 'قم بتحميل صورة إضافية 5 للعنصر.',
            'Image6': 'قم بتحميل صورة إضافية 6 للعنصر.',
            'video_link1': 'أدخل رابط الفيديو 1 للعنصر.',
            'video_link2': 'أدخل رابط الفيديو 2 للعنصر.',
            'questions': 'حدد الأسئلة المرتبطة بالعنصر.',
            'howitwork': 'حدد خطوات "كيف يعمل" المرتبطة بالعنصر.',
            'long_image': 'قم بتحميل صورة طويلة للعنصر.',
        }











class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        help_texts = {
            'title': 'أدخل عنوان الفئة.',
            'description': 'قدم وصفًا للفئة.',
            'keywords': 'أدخل الكلمات الرئيسية ذات الصلة بالفئة.',
            'Image': 'قم بتحميل صورة للفئة.',
            'top_slider_web': 'قم بتحميل صورة ويب لشريط التمرير الخاص بالفئة.',
            'top_slider_mobile': 'قم بتحميل صورة متحركة لشريط التمرير الخاص بالفئة.',
            'is_active': 'حدّد هذا الخيار لجعل الفئة نشطة.',
            'slug': 'أدخل معرّفًا فريدًا لعنوان URL للفئة.',
        }

    widgets = {
        'name': forms.TextInput(attrs={'placeholder': 'الاسم', 'class': 'inputform'}),
        'phone': forms.TextInput(attrs={'placeholder': 'رقم الهاتف', 'class': 'inputform'}),
        'companyname': forms.TextInput(attrs={'placeholder': 'اسم الشركة (اختياري)', 'class': 'inputform'}),
        'emailaddress': forms.TextInput(attrs={'placeholder': 'البريد الالكتروني', 'class': 'inputform'}),
        'country': forms.TextInput(attrs={'placeholder': 'الدولة', 'class': 'inputform'}),
        'city': forms.TextInput(attrs={'placeholder': 'البلد / المدينة', 'class': 'inputform'}),
        'shipping_address': forms.Textarea(attrs={'placeholder': 'العنوان', 'rows': 3, 'class': 'inputform'}),
        'apartment_address': forms.Textarea(attrs={'placeholder': 'عنوان آخر (اختياري)', 'rows': 2, 'class': 'inputform'}),
        'zip': forms.TextInput(attrs={'placeholder': 'الرمز البريدي / ZIP (اختياري)', 'class': 'inputform'}),
    }




class QuestionsForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = '__all__'
        widgets = {
            'question': forms.Textarea(attrs={'rows': 3}),
            'question_ar': forms.Textarea(attrs={'rows': 3}),
            'question_en': forms.Textarea(attrs={'rows': 3}),
            'answer': forms.Textarea(attrs={'rows': 4}),
            'answer_ar': forms.Textarea(attrs={'rows': 4}),
            'answer_en': forms.Textarea(attrs={'rows': 4}),
        }
        help_texts = {
            'question': 'أدخل السؤال هنا.',
            'answer': 'أدخل الإجابة هنا.',
        }

class QuestionsGeneralForm(forms.ModelForm):
    class Meta:
        model = QuestionsGeneral
        fields = '__all__'
        widgets = {
            'question': forms.Textarea(attrs={'rows': 3}),
            'question_ar': forms.Textarea(attrs={'rows': 3}),
            'question_en': forms.Textarea(attrs={'rows': 3}),
            'answer': forms.Textarea(attrs={'rows': 4}),
            'answer_ar': forms.Textarea(attrs={'rows': 4}),
            'answer_en': forms.Textarea(attrs={'rows': 4}),
                }
        help_texts = {
             'question': 'أدخل السؤال هنا.',
             'answer': 'أدخل الإجابة هنا.',
         }

class HowitworkForm(forms.ModelForm):
    class Meta:
        model = Howitwork
        fields = '__all__'

        help_texts = {
                 'title': 'أدخل عنوان العنصر.',
                 'description': 'أدخل وصفًا طويلًا للعنصر.',
             }


class SlideForm(forms.ModelForm):
    class Meta:
        model = Slide
        fields = '__all__'

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        help_texts = {
            'Image': ' صوره',
            'slideImage': 'صورة الشريحة',
            'slideVideo': 'فيديو الشريحة',
            'keywords': 'كلمات الدالة',
            'category': 'فئة',
            'Titel': 'عنوان',
            'description':' وصف',
            'body': 'محتوى',
            'active': 'حالة',
        }




class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = '__all__'
        help_texts = {
            'keywords':'أدخل الكلمات الرئيسية مفصولة بفواصل',
            'FaviconIco':'قم بتحميل أيقونة الفافيكون',
            'logo':'قم بتحميل الشعار',
            'title':'أدخل العنوان',
            'PHONE':'أدخل رقم الهاتف بدون أي حروف خاصة',
            'Whatsapp':'أدخل رقم واتساب بدون أي حروف خاصة',
            'linkedinlinke':'أدخل رابط LinkedIn',
            'snapchat':'أدخل رابط Snapchat',
            'instagramlinke':'أدخل رابط Instagram',
            'Twitterlinke':'أدخل رابط Twitter',
            'facebooklinke':'أدخل رابط Facebook',
            'Map_Address':'أدخل عنوان الخريطة',
        }
