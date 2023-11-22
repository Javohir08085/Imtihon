from django.db import models
from account.models import CustomUser
# Create your models here.

class PoliticiansModel(models.Model):
    politician_name = models.CharField(max_length=50,verbose_name='politicians name')
    politician_country = models.CharField(max_length=50,verbose_name='politicians country')
    politician_party = models.CharField(max_length=50,verbose_name='politicians party')
    politician_position = models.CharField(max_length=50,verbose_name='politicians position')
    politician_image = models.ImageField(upload_to='politicians',null=True, blank=True)
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}. {self.politician_name}"

    class Meta:
        db_table = 'politicians'