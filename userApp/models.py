from django.db import models
from django.contrib.auth.hashers import make_password

from mainPostApp.models import TotalCategories as Category, LectureInfo as Lecture
from userPostApp.models import UserCommunityPost as UserPost
# Create your models here.

class UserData(models.Model):   # 유저 정보 데이터(기본적으로 제공하는 User테이블을 사용하기에는 해당 사이트에선 닉네임을 사용하지 않기 때문)
    user_id = models.CharField(primary_key=True,max_length=40)  # 유저 아이디 / 기본키
    user_pass = models.CharField(max_length=50) #유저 비번
    user_email = models.EmailField()    # 이메일
    user_tier = models.IntegerField()   # 유저 티어
    is_manager = models.BooleanField(default=False) # 관리자 여부

    def save(self, *args, **kwargs):    #비밀번호 hashing하기 위한 용도
        self.user_pass = make_password(self.user_pass)
        super().save(*args, **kwargs)

    def __str__(self):  # 해당 모델 객체명 사용시, 사용자 아이디 반환
        return self.user_id
    
class FavoriteCategories(models.Model): # 사용자가 선호하는 카테고리
    Favorite_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(UserData,on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)

class FavoriteLectures(models.Model):   # 사용자가 즐겨찾기한 강의
    Favorite_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(UserData,on_delete=models.CASCADE)
    lecture_id = models.ForeignKey(Lecture,on_delete=models.CASCADE)

class FavoritePost(models.Model):   # 사용자가 즐겨찾기한 게시글
    Favorite_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(UserData,on_delete=models.CASCADE)
    post_id = models.ForeignKey(UserPost,on_delete=models.CASCADE)
