from django.db import models
from datetime import date
class Blog(models.Model):
    blog_type=models.CharField(max_length=100)
    blog_date=models.DateField(default=date.today())
    cover_photo=models.ImageField(upload_to='photos/%Y/%m/%d/')
    blog_author=models.CharField(max_length=200)
    blog_title=models.CharField(max_length=200)
    blog_jist=models.TextField()
    blog_description=models.TextField()
    def __str__(self):
        return self.blog_title

class Comment(models.Model):
    comment_on=models.ForeignKey(Blog,on_delete=models.DO_NOTHING)
    comment_author=models.CharField(max_length=100)
    comment_date=models.DateField(default=date.today())
    comment_content=models.TextField()
    comment_author_email=models.CharField(max_length=300)
    def __str__(self):
        return self.comment_author

class Reply(models.Model):
    reply_on=models.ForeignKey(Blog,on_delete=models.DO_NOTHING)
    reply_to=models.ForeignKey(Comment,on_delete=models.DO_NOTHING)
    reply_by=models.CharField(max_length=100)
    reply_content=models.TextField()
    reply_date=models.DateField(default=date.today())
    
    def __str__(self):
        return self.reply_by