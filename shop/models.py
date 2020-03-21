from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField('Категорія', max_length=32, db_index=True)
    slug = models.SlugField(unique=True)
    created = models.DateTimeField('Створено', auto_now_add=True)

    class Meta:
        ordering = ('created',)
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категорія')
    name = models.CharField('Назва товару', max_length=128, db_index=True)
    slug = models.SlugField(max_length=128, db_index=True)
    article = models.CharField('Артикул', max_length=8, db_index=True)
    description = models.TextField('Опис', blank=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True)
    price = models.DecimalField('Ціна', max_digits=10, decimal_places=2)
    available = models.BooleanField('Наявність', default=True)
    created = models.DateTimeField('Створено', auto_now_add=True)
    updated = models.DateTimeField('Оновлено', auto_now=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])


# class ProductImage(models.Model):
#     product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='products_images/')
#     is_main = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#
#     def __str__(self):
#         return "%s" % self.id
#
#     class Meta:
#         verbose_name = 'Фотография'
#         verbose_name_plural = 'Фотографии'
# class Specification(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='specifications', verbose_name='Товар')
#     value = models.CharField('Характеристика', max_length=128)
#
#     class Meta:
#         verbose_name = 'Характеристика'
#         verbose_name_plural = 'Характеристики'
#
#     def __str__(self):
#         return self.product
