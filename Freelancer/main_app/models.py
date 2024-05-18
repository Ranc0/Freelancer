from django.db import models

class Seller_Account(models.Model):
    syriatel_cash = models.BooleanField(default=False)
    usdt = models.BooleanField(default=False)
    al_haram = models.BooleanField(default=False)
    id_picture = models.ImageField(null=True)
    def serialize(self): 
        return {
            "payment_method": self.payment_method,
            "id_picture": self.id_picture,
            "work_group" : self.profile.work_group,
            "rate" : self.profile.rate
        }
    
class Profile(models.Model):
    language = models.CharField(max_length=50)
    work_group = models.CharField(max_length=50)
    bio = models.TextField(null=True)
    provided_services = models.IntegerField(default=0)
    member_since = models.DateTimeField(auto_now=True)
    rate = models.FloatField(default=0.0)
    seller_account = models.ForeignKey(Seller_Account, on_delete=models.CASCADE, default = 0,related_name='profile' )
    def serialize(self):
        return {
            "language": self.language,
            "work_group": self.work_group,
            "bio": self.bio,
            "provided_services": self.provided_services,
            "member_since": self.member_since
        }
    
    #collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    #promotions = models.ManyToManyField(Promotion)