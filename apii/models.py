from django.db import models

# Create your models here.
class book(models.Model):
    company_id=models.AutoField(primary_key=True)
    book_name=models.CharField(max_length=50)
    book_genration=models.CharField(max_length=50)
    is_best_seller=models.CharField(max_length=50)
    Create_date=models.DateTimeField(auto_now=True)
    update_date=models.DateTimeField(auto_now=True)
