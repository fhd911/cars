from django.db import models
from django.contrib.auth.models import User
from store.models import Product


class Order(models.Model):
    ORDER_STATUS = (
        ('pending', 'قيد المعالجة'),
        ('paid', 'مدفوع'),
        ('shipped', 'تم الشحن'),
        ('completed', 'تم التسليم'),
        ('canceled', 'ملغي'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="المستخدم")
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="الإجمالي")
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default='pending', verbose_name="الحالة")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"طلب رقم {self.id}"

    class Meta:
        verbose_name = "طلب"
        verbose_name_plural = "طلبات"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items", verbose_name="الطلب")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="المنتج")
    quantity = models.PositiveIntegerField(default=1, verbose_name="الكمية")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")

    def __str__(self):
        return f"{self.product.name} - {self.order.id}"

    class Meta:
        verbose_name = "عنصر طلب"
        verbose_name_plural = "عناصر الطلب"
