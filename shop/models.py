from django.db import models
from django.utils.text import slugify
import transliterate

# Create your models here.
class MainIngridient(models.Model):
    name=models.CharField(max_length=500)
    description=models.TextField()

    def __str__(self):
        return self.name

class DescriptionPoint(models.Model):
    name=models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True,null=False,default='')
    image = models.ImageField(upload_to='products/', blank=True)
    short_description=models.CharField(max_length=300,blank=True)
    description_text = models.TextField(blank=True)
    description_points=models.ManyToManyField(DescriptionPoint,blank=True)
    structure = models.TextField(blank=True)
    ingredients_table=models.ManyToManyField(MainIngridient,blank=True)
    method_of_application = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    declaration=models.ImageField(upload_to='products/declarations/', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def save(self,*args,**kwargs):
        self.slug=transliterate.slugify(self.name)
        super(Product,self).save(*args,**kwargs)

    def __str__(self):
        return self.name