from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="المستخدم")
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name="رقم الجوال")
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name="الصورة الشخصية")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "الملف الشخصي"
        verbose_name_plural = "الملفات الشخصية"


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="المستخدم")
    city = models.CharField(max_length=100, verbose_name="المدينة")
    district = models.CharField(max_length=100, verbose_name="الحي")
    street = models.CharField(max_length=200, verbose_name="الشارع")
    notes = models.TextField(null=True, blank=True, verbose_name="ملاحظات")
    is_default = models.BooleanField(default=False, verbose_name="افتراضي")

    def __str__(self):
        return f"{self.city} - {self.district}"

    class Meta:
        verbose_name = "عنوان"
        verbose_name_plural = "عناوين"
