from django.contrib import admin
from django.db.models import F

from bboard.models import Rubric, Bb


def title_and_rubric(rec):
    return f'{rec.title} ({rec.rubric.name})'


@admin.action(description='Уменьшить цену вдвое')
def discount(modeladmin, request, queryset):
    f = F('price')
    for rec in queryset:
        rec.price = f / 2
        rec.save()
    modeladmin.message_user(request, 'Действие выполнено')


class PriceListFilter(admin.SimpleListFilter):
    title = 'Категория цен'
    parameter_name = 'price'

    def lookups(self, request, model_admin):
        return (
            ('low', 'Низкая цена'),
            ('medium', 'Средняя цена'),
            ('high', 'Высокая цена'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'low':
            return queryset.filter(price__lt=500)
        elif self.value() == 'medium':
            return queryset.filter(price__gte=500, price__lte=5000)
        elif self.value() == 'high':
            return queryset.filter(price__gt=5000)


class BbInline(admin.StackedInline):
    model = Bb
    # extra = 1

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 3
        else:
            return 10


@admin.register(Bb)
class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric')
    # list_display = ('title_and_price', 'content', 'published', 'rubric')
    # list_display = (title_and_rubric, 'content', 'published', 'rubric')
    # list_display = ('title_and_rubric', 'content', 'price', 'published', 'rubric')
    # list_display_links = ('title', 'content')
    # list_editable = ('content', 'price', 'rubric')

    search_fields = ('title', 'content')
    # search_fields = ('^content',)
    # search_fields = ('=content',)
    search_help_text = 'Поиск по названиям товаров и содержимому'

    list_filter = (PriceListFilter,)

    # fields = ('title', 'price', 'content')
    # fields = (('title', 'price'), 'content')
    # fields = ('title', 'content', 'price', 'published')
    # readonly_fields = ('published',)

    fieldsets = (
        (None, {
            'fields': (('title', 'rubric'), 'content'),
            'classes': ('wide',),
        }),
        ('Дополнительные сведения', {
            'fields': ('price',),
            'description': 'Параметры необязательные для указания.',
        })
    )

    # exclude = ('rubric', 'kind')

    # filter_horizontal = ('spares',)
    # filter_vertical = ('machines',)

    actions = (discount,)

    def get_list_display(self, request):
        ld = ['title', 'content', 'price']
        if request.user.is_superuser:
            ld += ['published', 'rubric']
        return ld

    # def get_list_display_links(self, request, list_display):
    #     return list_display

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(is_hidden=False)

    # def get_fields(self, request, obj=None):
    #     f = ['title', 'content', 'price']
    #     if not obj:
    #         f.append('rubric')
    #     return f

    # def get_form(self, request, obj=None, **kwargs):
    #     if obj:
    #         return BbModelForm
    #     else:
    #         return BbAddModelForm

    @admin.display(description='Название и рубрика', ordering='title')
    # @admin.display(description='Название и рубрика', ordering='-title')
    # @admin.display(description='Название и рубрика', ordering='rubric__name')
    def title_and_rubric(self, rec):
        return f'{rec.title} ({rec.rubric.name})'

    # title_and_rubric.short_description = 'Название и рубрика'


@admin.register(Rubric)
class RubricAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'order')

    inlines = [BbInline]

    def get_inlines(self, request, obj=None):
        if obj:
            return ()
        else:
            return (BbInline,)


# admin.site.register(Rubric)
# admin.site.register(Bb, BbAdmin)
