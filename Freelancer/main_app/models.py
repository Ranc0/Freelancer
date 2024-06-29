from django.db import models
from django.contrib.auth.models import User, auth
from .default_for_img import *

class Seller_Account(models.Model):
    username = models.ForeignKey(User , null = True , on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50,null=True)
    country = models.CharField(max_length=50)
    bdate = models.DateField()
    #password = models.CharField(max_length=8)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    syriatel_cash = models.BooleanField(default=False)
    usdt = models.BooleanField(default=False)
    al_haram = models.BooleanField(default=False)
    id_picture = models.TextField(max_length=900000, blank=True, default = default_img)
    img = models.TextField(max_length=900000, blank=True, default = default_img )
    def serialize(self): 
        return {
            #"id" : self.id,
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
            "img" : self.img
        }
    
class Profile(models.Model):
    profile_seller_id = models.IntegerField(default=1)
    language = models.CharField(max_length=50)
    work_group = models.CharField(max_length=50)
    bio = models.TextField(null=True)
    provided_services = models.IntegerField(default=0)
    member_since = models.DateTimeField(auto_now=True)
    rate_sum = models.FloatField(default=0.0)
    rate_cnt = models.FloatField(default=0.0)
    rate = models.FloatField(default=0.0)
    is_active = models.BooleanField(default=True)
    seller_account = models.ForeignKey(Seller_Account, on_delete=models.CASCADE, default = 1,related_name='profile' )
    def serialize(self):
        return {
            "language": self.language,
            "work_group": self.work_group,
            "bio": self.bio,
            "provided_services": self.provided_services,
            "member_since": self.member_since,
            "is_active" : self.is_active 
            

        }
    
    #collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    #promotions = models.ManyToManyField(Promotion)

class Customer_Account(models.Model):
    username = models.ForeignKey(User , null = True , on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50,null=True)
    country = models.CharField(max_length=50)
    bdate = models.DateField()
    #password = models.CharField(max_length=8)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    member_since = models.DateField(auto_now_add=True)
    img = models.TextField(max_length=900000, blank=True, default = default_img )
    def serialize(self): 
        return {
            #"id" : self.id,
            "first_name": self.first_name,
            "second_name": self.second_name,
            "country": self.country,
            "bdate": self.bdate,
            "email": self.email,
            "phone_number": self.phone_number,
            "member_since": self.member_since,
            "img" : self.img
        }
    
class Deal_With(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , null=True)
    profile = models.IntegerField(null=True)
    person2_id = models.CharField(max_length=50 , null=True)
    send_date = models.DateField(auto_now_add=True)
    send_time = models.TimeField(auto_now_add = True)
    is_accepted = models.IntegerField(default=0)
    is_active = models.IntegerField(default=1)
    accept_time = models.DateField(null=True)
    end_time = models.DateTimeField(null=True)
    def serialize(self):
        return {
            "seller_user" : self.user.username,
            "profile_id" : self.profile,
            "customer_user id" : self.person2_id,
            "is_accepted": self.is_accepted,
            "is_active" : self.is_active,
            "accept_time" : self.accept_time,
            "end_time" : self.end_time,
        }
    
class Review(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , null=True)
    profile = models.IntegerField(null=True)
    person2_id = models.CharField(max_length=50 , null=True)
    rate = models.IntegerField(default=0)
    comment = models.TextField(null=True)
    def serialize(self):
        return {
            "review_id" : self.id,
            "profile_id" : self.profile,
            "customer_id" : self.person2_id,
            "rate" : self.rate,
            "comment" : self.comment
        }


class Chat(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , null=True)   
    person2_username = models.CharField(max_length=50 , null=True)
    unread_cnt = models.IntegerField(default=0)
    time = models.DateTimeField(null=True)
    def serialize(self):
        return {
            "person2 username" : self.person2_username,
            "unread_cnt" : self.unread_cnt,
        }
    
class Message (models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE , null = True)
    message = models.TextField()
    image_message = models.TextField(max_length=900000, blank=True, null = True )
    sender = models.CharField(max_length=50 , null=True)
    reciever = models.CharField(max_length=50 , null = True) 
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    def serialize(self): 
        return {
            "message": self.message,
            "image_message" : self.image_message,
            "date" : self.date,
            "time": self.time,
            "sender" : self.sender,
            "reciever" : self.reciever,
        }


    
