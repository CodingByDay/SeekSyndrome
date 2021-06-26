from django.db import models

# Create your models here.
class Order(models.Model):
    name=models.CharField(max_length=255,null=False)
    email=models.CharField(max_length=255,null=False)
    
    def __str__(self):
        return self.name
    
class Project(models.Model):
    name = models.CharField(max_length=255,null=False);
    project_desc= models.CharField(max_length=1000,null=False)
    def_image = models.ImageField(upload_to='images', null=True)
    github_link = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length=255,null=False)
    product = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.name
    
    
    