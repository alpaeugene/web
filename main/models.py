from django.db import models
from django.urls import reverse


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    image = models.ImageField(blank=True, upload_to='media/', help_text='150x150px', verbose_name='Ссылка картинки')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main', kwargs={"slug": self.title})

    class Meta:
        verbose_name = 'Статьи'
        verbose_name_plural = 'Cтатьи'


class Posts(models.Model):
    title = models.CharField("Название", max_length=50)
    des = models.TextField("Описание")
    cover = models.ImageField(upload_to='media/', help_text='150x150px', verbose_name='картинки')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог про кота'
        verbose_name_plural = 'Блоги про кота'


class Post(models.Model):
    author = models.CharField("Автор", max_length=50)
    created = models.DateTimeField("Создан", auto_now_add=True)
    text = models.TextField("Комментарий", max_length=4096)

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'коментарий'
        verbose_name_plural = 'коментарии'


class About(models.Model):
    titl = models.CharField("Название", max_length=50)
    desc = models.TextField("Описание")
    img = models.ImageField(upload_to='media/', help_text='150x150px', verbose_name='картинки')

    def __str__(self):
        return self.titl

    class Meta:
        verbose_name = 'Биография кота'
        verbose_name_plural = 'Биография кота'