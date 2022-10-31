from django.contrib.auth.models import User
from django.db import models




class Suv(models.Model):
    brend=models.CharField(max_length=30)
    narx=models.PositiveSmallIntegerField()
    litr=models.PositiveSmallIntegerField()
    batafsil=models.CharField(max_length=100)

    def __str__(self):
        return self.brend
class Mijoz(models.Model):
    ism=models.CharField(max_length=50)
    tel=models.CharField(max_length=15)
    manzil=models.CharField(max_length=30)
    qarz=models.PositiveSmallIntegerField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.ism
class Admin(models.Model):
    ism = models.CharField(max_length=50)
    yosh=models.PositiveSmallIntegerField()
    ish_vaqti=models.CharField(max_length=20, choices=[("8:00; 18:00", "8:00; 18:00"), ("18:00; 00:00", "18:00; 00:00")])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.ism
class Haydovchi(models.Model):
    ism = models.CharField(max_length=50)
    tel = models.CharField(max_length=15)
    kiritilgan_sana=models.DateField()

    def __str__(self):
        return self.ism
class Buyurtma(models.Model):
    suv=models.ManyToManyField(Suv)
    mijoz=models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    admin=models.ForeignKey(Admin, on_delete=models.CASCADE)
    haydovchi=models.ForeignKey(Haydovchi, on_delete=models.CASCADE)
    sana=models.DateTimeField()
    miqdor=models.CharField(max_length=30)
    umumiy_summa=models.PositiveIntegerField()
    def __str__(self):
        return f"{self.umumiy_summa}"



    


