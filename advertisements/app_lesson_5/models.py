from django.db import models


# Create your models here.
class Advertisement(models.Model):
    title = models.CharField("название", max_length=120)
    descriptions = models.TextField("описание")
    price = models.DecimalField("цена", max_digits=9, decimal_places=2)
    trades = models.BooleanField("торг", help_text="Если хотим торговаться")
    date_now = models.DateTimeField("Дата создания", auto_now_add=True)
    date_update = models.DateField("Дата обновления", auto_now=True)

    class Meta:
        db_table = "advertisements"

    def __str__(self):
        return self.title

