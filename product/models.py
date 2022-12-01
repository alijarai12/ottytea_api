from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category',blank=True, null=True, verbose_name="Category Image")

    def __str__(self):
        return self.title

class Tea(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    selling_price = models.IntegerField()
    old_price = models.IntegerField()
    weight = models.IntegerField()
    aroma = models.CharField(max_length=150)
    appearance = models.CharField(max_length=150)
    vendor = models.CharField(max_length=150)
    type = models.CharField(max_length=150)    
    product_image = models.ImageField(upload_to='product', blank=True, null=True, verbose_name="Product Image")
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title
