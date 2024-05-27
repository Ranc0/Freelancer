from django.db import models

class Seller_Account(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50,null=True)
    country = models.CharField(max_length=50)
    bdate = models.DateField()
    password = models.CharField(max_length=8)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    syriatel_cash = models.BooleanField(default=False)
    usdt = models.BooleanField(default=False)
    al_haram = models.BooleanField(default=False)
    id_picture = models.CharField(max_length=255,null=True)
    def serialize(self): 
        return {
            "first_name": self.first_name,
            "second_name": self.second_name,
            "country": self.country,
            "bdate": self.bdate,
            "email": self.email,
            "phone_number": self.phone_number,
            "syriatel_cash": self.syriatel_cash,
            "usdt": self.usdt,
            "al_haram": self.al_haram,
            "id_picture": self.id_picture,
        }
    
class Profile(models.Model):
    profile_seller_id = models.IntegerField(default=1)
    language = models.CharField(max_length=50)
    work_group = models.CharField(max_length=50)
    bio = models.TextField(null=True)
    provided_services = models.IntegerField(default=0)
    member_since = models.DateTimeField(auto_now=True)
    rate = models.FloatField(default=0.0)
    seller_account = models.ForeignKey(Seller_Account, on_delete=models.CASCADE, default = 1,related_name='profile' )
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

class Customer_Account(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50,null=True)
    country = models.CharField(max_length=50)
    bdate = models.DateField()
    password = models.CharField(max_length=8)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    member_since = models.DateField(auto_now_add=True)
    def serialize(self): 
        return {
            "first_name": self.first_name,
            "second_name": self.second_name,
            "country": self.country,
            "bdate": self.bdate,
            "email": self.email,
            "phone_number": self.phone_number,
            "member_since": self.member_since,
        }
    
class Deal_With(models.Model):
    seller_account = models.ForeignKey(Seller_Account, on_delete=models.CASCADE, default = 1,related_name='deal_with_customer')
    seller_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default = 1,related_name='deal_with_customer')
    customer_account = models.ForeignKey(Customer_Account, on_delete=models.CASCADE, default = 1,related_name='deal_with_seller')
    created_at = models.DateField(auto_now_add=True)
    start_service = models.IntegerField(default=0)
    end_service = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    comment = models.TextField(null=True)
    def serialize(self): 
        return {
            "seller_account": self.seller_account,
            "seller_profile": self.seller_profile,
            "customer_account": self.customer_account,
            "start_service": self.start_service,
            "end_service": self.end_service,
            "rating": self.rating,
            "comment": self.comment,
        }
    
