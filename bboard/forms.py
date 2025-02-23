from django.forms import ModelForm, modelform_factory, DecimalField
from django.forms.widgets import Select
from bboard.models import Bb, Rubric, IceCream
from django import forms
from django.contrib.auth.models import User
from django.core import validators
from django.core.exceptions import ValidationError
import re
# class BbForm(ModelForm):
#     class Meta:
#         model = Bb
#         fields = ('title', 'content', 'price', 'rubric')
#         labels={'title': 'Наименование товара'}
#         help_texts={'rubric': 'Не забудьте выбрать рубрику!'}
#         field_classes={'price': DecimalField}
#         widgets={'rubric': Select(attrs={'size': 8})}

# BbForm = modelform_factory(
#     Bb, 
#     fields=('title', 'content', 'price', 'rubric'),
#     labels={'title': 'Наименование товара'},
#     help_texts={'rubric': 'Не забудьте выбрать рубрику!'},
#     field_classes={'price': DecimalField},
#     widgets={'rubric': Select(attrs={'size': 8})}
# )

class BbForm(ModelForm):
    title = forms.CharField(label='Наименование товара', validators=[validators.RegexValidator(regex='^.{4,}$')], error_messages={'invalid' : 'Слишком короткое название товара'})
    content = forms.CharField(label='Описание', widget=forms.widgets.Textarea())
    price = forms.DecimalField(label='Цена', decimal_places=2)
    rubric = forms.ModelChoiceField(queryset=Rubric.objects.all(), label='Рубрика', help_text='Не забудьте выбрать рубрику!', widget=forms.widgets.Select(attrs={'size': 3}))
    
    def clean_title(self):
        val = self.cleaned_data['title']
        if val == 'Прошлогодний снег':
            raise ValidationError('К продаже не допускается')
        return val
    
    def clean(self):
        super().clean()
        errors = {}
        
        if not self.cleaned_data['content']:
            errors['content'] = ValidationError('Укажите описание продаваемого товара')

        if not self.cleaned_data['price'] < 0:
            errors['price'] = ValidationError('Укажите неотрицательное значение цены')
            
        if errors:
            raise ValidationError(errors)
        
    class Meta:
        model = Bb
        fields = ('title', 'content', 'price', 'rubric')
        


class RegisterUserForm(forms.ModelForm):
    password1 = forms.CharField(label='Пароль')
    password2 = forms.CharField(label='Пароль (повторно)')
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')

class IceCreamForm(forms.ModelForm):
    class Meta:
        model = IceCream
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError("Название не может быть пустым.")
        if not re.match(r'^[a-zA-Zа-яА-Я\s]+$', name):
            raise forms.ValidationError("Название должно содержать только буквы.")
        if len(name) > 100:
            raise forms.ValidationError("Название слишком длинное (максимум 100 символов).")
        return name

    def clean_flavor(self):
        flavor = self.cleaned_data.get('flavor')
        allowed_flavors = ["ваниль", "шоколад", "клубника", "фисташка"]
        if flavor.lower() not in allowed_flavors:
            raise forms.ValidationError(f"Вкус должен быть из списка: {', '.join(allowed_flavors)}.")
        return flavor

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("Цена должна быть больше 0.")
        return price