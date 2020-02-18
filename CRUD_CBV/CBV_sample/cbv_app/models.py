from django.db import models

# Create your models here.
class  CBVModel(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()

    # def get_absolute_url(self):
    #     return reverse('detail',kwargs ={'pk':self.pk}


    def __str__(self):
        # print(self)
        return self.title
