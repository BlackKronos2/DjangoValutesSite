from django.db import models
from django.utils.text import slugify

class CurrencyManager(models.Manager):
    def get_currencies(self):
        return self.all()

class Currency(models.Model):
    parse_code = models.CharField('ParseCode', max_length=10)
    num_code = models.CharField('NumCode', max_length=10)

    char_code = models.CharField('Код валюты', max_length=10)
    nominal = models.IntegerField('Номинал', default=1)

    сurrency_name = models.CharField('Название', max_length=20)

    slug = models.SlugField(unique=False,db_index=True, verbose_name="URL")
    objects = CurrencyManager()

    def save(self, *args, **kwargs):
        if not self.slug: # Генерируем слаг только если он отсутствует
            self.slug = slugify(self.char_code)
        super(Currency, self).save(*args, **kwargs)

    def __str__(self):
        return self.сurrency_name
