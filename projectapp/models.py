from django.db import models
#title, content, image url
class WriterData(models.Model):
    Title=models.CharField(max_length=64)
    Content=models.CharField(max_length=500)
    Image=models.ImageField(upload_to='media')
class ViewerReg(models.Model):
    f_name=models.CharField(max_length=65)
    l_name=models.CharField(max_length=65)
    username=models.CharField(max_length=65)
    password=models.CharField(max_length=65)
class ViewerLog(models.Model):
    username=models.CharField(max_length=65)
    password=models.CharField(max_length=65)




