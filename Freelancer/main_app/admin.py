from django.contrib import admin
from .models import Customer_Account
from .models import Seller_Account
from .models import Profile
from .models import Deal_With
from .models import Review
from .models import Chat
from .models import Message
admin.site.register(Customer_Account)
admin.site.register(Seller_Account)
admin.site.register(Profile)
admin.site.register(Deal_With)
admin.site.register(Review)
admin.site.register(Chat)
admin.site.register(Message)

# Register your models here.
