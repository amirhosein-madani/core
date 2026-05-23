from django.db import models
from django.shortcuts import reverse
# Create your models here.



class Comment(models.Model):

    post = models.ForeignKey('blog.Post',on_delete=models.CASCADE)
    user = models.ForeignKey("accounts.Profile", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def get_snippet(self):
        return self.content[0:11]
    
    def get_absolute_url(self):
        return reverse("comment-detail", kwargs={"pk": self.pk})
    

    def __str__(self):
        return f"Comment by {self.user.user.username} on {self.post.title}"

        