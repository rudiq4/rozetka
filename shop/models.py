from django.db import models


class Category(models.Model):
    name = models.CharField('Категорія', max_length=32, db_index=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категорія')
    name = models.CharField('Назва товару', max_length=128, db_index=True)
    slug = models.SlugField(max_length=128, db_index=True)
    description = models.TextField('Опис', blank=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True)
    price = models.DecimalField('Ціна', max_digits=10, decimal_places=2)
    available = models.BooleanField('Наявність', default=True)
    created = models.DateTimeField('Створено', auto_now_add=True)
    updated = models.DateTimeField('Оновлено', auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
