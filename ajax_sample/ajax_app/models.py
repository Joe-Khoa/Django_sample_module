from django.db import models
    
# Create your models her.
class Post(models.Model):
    post_heading = models.CharField(max_length=200)
    post_text = models.TextField()
    def __unicode__(self):  #python_2 use string, python_3 unicode
        return unicode(self.user)

class Like(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
