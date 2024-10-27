from django.db import models

class User(models.Model): 
    name = models.CharField(verbose_name='Имя', max_length=50)
    age = models.IntegerField(verbose_name='хыхыдед')
    birth_date= models.DateField(verbose_name='Вотстольколетназадслучилсяапокалипсисаименнотвоёрождение', auto_created=True)
    IsFemboy = models.BooleanField(verbose_name='увыиах', default=True)
    
