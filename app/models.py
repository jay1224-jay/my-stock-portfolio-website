from django.db import models

# Create your models here.


class stock_deal(models.Model):
	company_code = models.CharField(default='null', max_length=15)
	company_name = models.CharField(default='null', max_length=6)
	share = models.IntegerField()
	bought_date = models.DateField()
	bought_price = models.FloatField()
	current_price = models.FloatField(default=0)
	profit_and_loss = models.FloatField(default=0)
