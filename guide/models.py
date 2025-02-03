from django.db import models


# Create your models here.
class GuidePost(models.Model):
    CATEGORY = (("strategy", "攻略"), ("anecdote", "小ネタ"), ("pr", "PR"))

    title = models.CharField(verbose_name="タイトル", max_length=50)

    content = models.TextField(verbose_name="本文")

    category = models.CharField(
        verbose_name="カテゴリー", max_length=50, choices=CATEGORY
    )
    posted_at = models.DateTimeField(verbose_name="投稿日時", auto_now_add=True)
    image = models.ImageField(upload_to="images/", height_field=None, width_field=None, max_length=None)

    thumbnail=models.ImageField(upload_to="images/")
    

    def __str__(self):
        return self.title


class Comment(models.Model):
    guidepost = models.ForeignKey(GuidePost, on_delete=models.CASCADE, related_name='comments')

    name = models.CharField(verbose_name="名前",max_length=15)

    compost_at = models.DateTimeField(verbose_name="コメント日時", auto_now_add=True)

    compost=models.TextField(verbose_name='コメント')
    
    def __str__(self):
        return self.name