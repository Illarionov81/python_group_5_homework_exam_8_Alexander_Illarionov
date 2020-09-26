from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

DEFAULT_CATEGORY = 'other'
CATEGORY_CHOICES = (
    (DEFAULT_CATEGORY, 'Разное'),
    ('food', 'Продукты питания'),
    ('household', 'Хоз. товары'),
    ('toys', 'Детские игрушки'),
    ('appliances', 'Бытовая техника'),
    ('carshering', 'Аренда авто'),
    ('laundry', 'Прачечная'),
)

MARK_CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)


class Product(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Название')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    category = models.CharField(max_length=200, null=False, blank=False, verbose_name='Категория',
                                choices=CATEGORY_CHOICES, default=DEFAULT_CATEGORY)
    image = models.ImageField(null=True, blank=True, upload_to='product_pics', verbose_name='Товар')

    def __str__(self):
        return f'{self.name} - {self.category}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Review(models.Model):
    author = models.ForeignKey(get_user_model(), null=False, blank=False, on_delete=models.CASCADE, verbose_name='Автор')
    product = models.ForeignKey('webapp.Product', related_name='review', on_delete=models.CASCADE,
                                verbose_name='Продукты')
    review_text = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Отзыв')
    mark = models.IntegerField(null=False, blank=False, verbose_name='Оценка',
                               choices=MARK_CHOICES)

    def __str__(self):
        return f'{self.author} - {self.mark}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
