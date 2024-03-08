from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    class Meta:
        verbose_name_plural="categories"
    def __str__(self):
        return self.name
class Post(models.Model):
    title = models.CharField(max_length=500)
    body = models.TextField()
    created_on  = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.URLField(default='https://wmmedia.sgp1.cdn.digitaloceanspaces.com/blog.png')
    likes =  models.PositiveIntegerField(default=0)
    dislikes =  models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title