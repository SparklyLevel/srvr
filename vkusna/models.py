from django.db import models
class Video(models.Model):
    length = models.IntegerField(verbose_name='Длина')
    description = models.CharField(verbose_name='Описание', max_length=255)
    Number_of_views = models.IntegerField(verbose_name='Просмотры')
    path = models.FileField(verbose_name='Путь видео', null=True, blank=True)
    
    def __str__(self):
        return self.description
    
class User(models.Model): 
    name = models.CharField(verbose_name='Имя', max_length=50)
    age = models.IntegerField(verbose_name='Возраст')
    birth_date= models.DateField(verbose_name='Дата Рождения', auto_created=True)
    IsFemboy = models.BooleanField(verbose_name='наличие пениса', default=True)
    fav_fetishes = models.ManyToManyField('Ff', related_name='users', verbose_name='ФавФетиши')
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='users', verbose_name='Видосики', null=True, blank=True)

    def __str__(self):
        return self.name
    
class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='image', verbose_name='Пользователь')
    title = models.CharField(verbose_name='Название пикчи',max_length=255)
    path = models.FileField(verbose_name='Путь пикчи')
    
    def __str__(self):
        return self.title
    
class Ff(models.Model):
    title = models.CharField(verbose_name='ФавФетиш', max_length=255)
    Number_of_views = models.IntegerField(verbose_name='Просмотры')
    Dumbness = models.BooleanField(verbose_name='Тупость', default=False)
    
    def __str__(self):
        return self.title
    



    
