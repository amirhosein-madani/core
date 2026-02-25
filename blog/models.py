from django.db import models
from django.contrib.auth import get_user_model 
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

    
# getting user model object 
# User = get_user_model()

class Post(models.Model):
    """
  T     this is a class to define posts for blog app 
    """
    author = models.ForeignKey("accounts.Profile", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    published_date = models.DateTimeField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, related_name="posts")
    status = models.BooleanField()
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=60, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to="category_images", blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_articles", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Category.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Categories"