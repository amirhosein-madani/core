from django.db import models

# Create your models here.



class Comment(models.Model):

    post = models.ForeignKey('blog.Post',on_delete=models.CASCADE)
    user = models.ForeignKey("accounts.Profile", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.profile.user.username} on {self.post.title}"

        