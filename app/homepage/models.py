from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField('タイトル', max_length=100)
    body = models.TextField('本文')
    image = models.ImageField('画像', upload_to='news_images', null=True, blank=True)
    item1 = models.CharField('項目1', max_length=100, null=True, blank=True)
    content1 = models.TextField('内容1', null=True, blank=True)
    item2 = models.CharField('項目2', max_length=100, null=True, blank=True)
    content2 = models.TextField('内容2', null=True, blank=True)
    item3 = models.CharField('項目3', max_length=100, null=True, blank=True)
    content3 = models.TextField('内容3', null=True, blank=True)
    is_published = models.BooleanField('公開フラグ', default=True)
    created = models.DateTimeField('作成日時', auto_now_add=True)

    def __str__(self):
        return self.title
    
class Contact(models.Model):

    name = models.CharField('名前', max_length=100)
    email = models.EmailField('返信用アドレス', max_length=255)
    body = models.TextField('内容')

    def __str__(self):
        return self.name