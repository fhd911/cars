from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="اسم التصنيف")
    slug = models.SlugField(unique=True, verbose_name="الرابط المختصر")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "تصنيف"
        verbose_name_plural = "تصنيفات"


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="التصنيف")
    name = models.CharField(max_length=200, verbose_name="اسم المنتج")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    description = models.TextField(verbose_name="الوصف")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "منتجات"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='products/', verbose_name="الصورة")

    def __str__(self):
        return f"صورة لـ {self.product.name}"

    class Meta:
        verbose_name = "صورة منتج"
        verbose_name_plural = "صور المنتجات"


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="المستخدم")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"سلة {self.user}"

    class Meta:
        verbose_name = "سلة"
        verbose_name_plural = "سلال"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="المنتج")
    quantity = models.PositiveIntegerField(default=1, verbose_name="الكمية")

    def __str__(self):
        return f"{self.product.name} (×{self.quantity})"

    class Meta:
        verbose_name = "عنصر سلة"
        verbose_name_plural = "عناصر السلة"
