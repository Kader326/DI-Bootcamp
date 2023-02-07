from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.URLField( null=True, blank=True)
    
    def __str__(self):
        return self.name
    
        
    
class Todo(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField()
    has_been_done = models.BooleanField(default=False)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_completion  = models.DateTimeField()
    deadline_date = models.DateTimeField()
    category = models.ForeignKey(Category, blank=True, on_delete=models.CASCADE)
    
# Create your models here.
