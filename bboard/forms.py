from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm, modelform_factory, DecimalField, BaseModelFormSet
from django.forms.widgets import Select
from django.core import validators

from bboard.models import Bb, Rubric, Img


# BbForm = modelform_factory(
#     Bb,
#     fields=('title', 'content', 'price', 'rubric'),
#     labels={'title': 'Название товара'},
#     help_texts={'rubric': 'Не забудьте выбрать рубрику!'},
#     field_classes={'price': DecimalField},
#     widgets={'rubric': Select(attrs={'size': 8})}
# )


# class BbForm(ModelForm):
#     class Meta:
#         model = Bb
#         fields = ('title', 'content', 'price', 'rubric')
#         labels = {'title': 'Название товара'}
#         help_texts = {'rubric': 'Не забудьте выбрать рубрику!'}
#         field_classes = {'price': DecimalField}
#         widgets = {'rubric': Select(attrs={'size': 8})}


class BbForm(ModelForm):
    title = forms.CharField(
        label='Название товара',
        validators=[validators.RegexValidator(regex='^.{4,}$')],
        error_messages={'invalid': 'Слишком короткое название товара'}
    )
    content = forms.CharField(label='Описание',
                              widget=forms.widgets.Textarea())
    price = forms.DecimalField(label='Цена', decimal_places=2)
    rubric = forms.ModelChoiceField(queryset=Rubric.objects.all(),
                                    label='Рубрика',
                                    help_text='Не забудьте выбрать рубрику!',
                                    widget=forms.widgets.Select(attrs={'size': 8}))
    captcha = CaptchaField(
        label='Введите текст с картинки',
        error_messages={'invalid': 'Неправильный текст'},
        # generator='captcha.helpers.random_char_challenge',
        # generator='captcha.helpers.math_challenge',
        # generator='captcha.helpers.word_challenge',
    )

    def clean_title(self):
        val = self.cleaned_data['title']
        if val == 'Прошлогодний снег':
            raise ValidationError('К продаже не допускается')
        return val

    def clean(self):
        super().clean()
        errors = {}

        if not self.cleaned_data['content']:
            errors['content'] = ValidationError(
                'Укажите описание продаваемого товара'
            )

        if self.cleaned_data['price'] < 0:
            errors['price'] = ValidationError(
                'Укажите неотрицательное значение цены'
            )

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
        fields = ('username', 'email', 'password1', 'password2',
                  'first_name', 'last_name')


class RubricBaseFormSet(BaseModelFormSet):
    def clean(self):
        super().clean()
        names = [form.cleaned_data['name'] for form in self.forms
                 if 'name' in form.cleaned_data]
        if ('Недвижимость' not in names) or ('Транспорт' not in names) \
            or ('Мебель' not in names):
            raise ValidationError(
                'Добавьте рубрики недвижимости, транспорта и мебели'
            )


class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=20, label='Искомое слово')
    rubric = forms.ModelChoiceField(queryset=Rubric.objects.all(),
                                    label='Рубрика')


class ImgForm(forms.ModelForm):
    image = forms.ImageField(
        label='Изображение',
        validators=[validators.FileExtensionValidator(
            allowed_extensions=['gif', 'jpg', 'png'])],
        error_messages={
            'invalid_extension': 'Этот формат не поддерживается'},
        # widget=forms.widgets.ClearableFileInput(attrs={'multiple': True})
    )

    desc = forms.CharField(label='Описание',
                           widget=forms.widgets.Textarea())

    class Meta:
        model = Img
        fields = '__all__'



