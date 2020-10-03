from django.contrib import admin
from .models import Exchange
from .models import Coin
from .models import Market
from .models import Wallet

admin.site.register(Exchange)
admin.site.register(Coin)
admin.site.register(Market)
admin.site.register(Wallet)