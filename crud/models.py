from django.db import models

class Post (models.Model): 
    title = models.CharField (max_length = 50, help_text = 'título del mensaje') 
    message = models.TextField (help_text = "Que esta en tu mente ... ") 
 
    def __str__(self): 
        return self.title
