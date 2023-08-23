from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()

# Create your models here.
class Post(models.Model):
    category_choices=(('족발,보쌈','족발,보쌈'),('찜,탕,찌개','찜,탕,찌개'),('돈까스,회,일식','돈까스,회,일식'),('피자','피자'),('고기구이','고기구이'),('양식','양식'),('치킨','치킨'),
                      ('중식','중식'),('아시안','아시안'),('백반,죽,국수','백반,죽,국수'),('도시락','도시락'),('분식','분식'),('카페,디저트','카페,디저트'),('페스트푸드','페스트푸드'),)
    title = models.CharField(max_length=30)
    category = models.CharField(max_length=30, choices=category_choices, default='치킨',verbose_name='카테고리종류')
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    # 완료여부
    is_compelete = models.BooleanField(default=True)
    # 목표인원
    target_number = models.IntegerField("목표인원", default = 0, validators=[MinValueValidator(0), MaxValueValidator(10)], help_text="최대 10명만 가능합니다.")
    # 참여인원
    join_number = models.PositiveIntegerField(default=0)
    recruited_users = models.ManyToManyField(User, related_name='recruited_posts', blank=True)



class Comment(models.Model):
    post = models.ForeignKey('Post',on_delete=models.CASCADE)
    content = models.TextField()
    writer = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.content
    

class HashTag(models.Model):
    post = models.ForeignKey('Post',on_delete=models.CASCADE)    
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name