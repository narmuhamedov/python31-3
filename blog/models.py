from django.db import models

class BlogProgramLang(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='')
    descriptions = models.TextField(null=True)
    color = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

