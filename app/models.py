from django.db import models

class Author(models.Model):
    CHOICE_COUNTRY = [
        ('Uzbekiston', 'Uzbekiston'),
        ('Angliya', 'Angliya'),
        ('Amerika', 'Amerika')
    ]
    full_name = models.CharField(max_length=350)
    image = models.ImageField(upload_to=True)
    country = models.CharField(max_length=150, choices=CHOICE_COUNTRY)
    def __str__(self):
        return self.full_name
class Book(models.Model):
    title = models.CharField(max_length=450)
    price = models.IntegerField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    image = models.ImageField(upload_to=True)

    def __str__(self):
        return self.title

