from django.db import models

class Exchange(models.Model):
    name = models.CharField(max_length=200)
    secret_api_key = models.CharField(max_length=200)
    public_api_key = models.CharField(max_length=200)

    def __str__(self):
    	return self.name


class Coin(models.Model):
    name = models.CharField(max_length=200)
    iso = models.CharField(max_length=200)

    def __str__(self):
    	return self.name

class Market(models.Model):
	base_coin = models.ForeignKey(Coin, related_name='base_coin', on_delete=models.CASCADE)
	quote_coin = models.ForeignKey(Coin, related_name='quote_coin', on_delete=models.CASCADE)
	exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE)
	maker = models.FloatField()
	taker = models.FloatField()

	def __str__(self):
		return self.base_coin.iso+self.quote_coin.iso+"-"+self.exchange.name

class Wallet(models.Model):
	exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE)
	coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
	address = models.CharField(max_length=200)
	balance = models.FloatField()
	available = models.FloatField()
	in_orders = models.FloatField()

	def __str__(self):
		return self.coin.iso+"_"+self.exchange.name
