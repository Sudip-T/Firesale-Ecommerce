from django.db import models
from django.urls import reverse
from django.utils.text import slugify


CATEGORY_CHOICES = (
    ('GA','Gadgets'),
    ('HA','Home Appliances'),
    ('MF','Mens Fashions')
)


LABEL_CHOICES = (
    ('N','new'),
    ('BS','best seller'),
    ('SC','stock clerance')
)

class Product(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField(max_length=50, null=True)
    discounted_price = models.FloatField(blank=True, null=True)
    image = models.ImageField(upload_to='static/img/',null=True, blank=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=2)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()


    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    def get_absolute_url(self):
        return reverse('store:product', kwargs={
            'slug':self.slug
        })
    
    def get_add_to_cart(self):
        return reverse('store:add-to-cart', kwargs={
            'slug':self.slug
        })
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            original_slug = self.slug
            counter = 1
            while Product.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter +=1
        super().save(*args, **kwargs)
