from django.db import models

class DisplayStatus(models.TextChoices):
    CAN_DISPLAY = 'CD', 'Можно отобразить'
    CANNOT_DISPLAY = 'NCD', 'Нельзя отобразить'

class CurrencyArticleManager(models.Manager):
    def get_displayable_articles(self):
        return self.filter(display_status=DisplayStatus.CAN_DISPLAY)

class CurrencyArticle(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Текст')
    date = models.DateField('Дата публикации')
    display_status = models.CharField('Статус отображения', max_length=3, choices=DisplayStatus.choices, default=DisplayStatus.CAN_DISPLAY)

    objects = models.Manager()
    displayable_objects = CurrencyArticleManager()

    def __str__(self):
        return self.title
