from django.db import models

# Create your models here.
class Seller_Account(models.Model):
    SYRIATEL_CASH = "Syriatel_cash"
    AL_HARAM = "Al_haram"
    USTD = "USTD"

    PAYMENT_CHOICES = [
        (SYRIATEL_CASH, "Syriatel_cash"),
        (AL_HARAM, "Al_haram"),
        (USTD , "USTD"),
    ]
    payment_method = models.CharField(max_length=50, choices=PAYMENT_CHOICES, default=SYRIATEL_CASH)
    id_pecture = models.ImageField()
    def serialize(self): 
        return {
            "payment_method": self.payment_method,
            "id_pecture": self.id_pecture
        }
class Profile(models.Model):
    language = models.CharField(max_length=50)
    work_group = models.CharField(max_length=50)
    bio = models.TextField()
    provided_services = models.IntegerField()
    member_since = models.DateTimeField(auto_now=True)
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
