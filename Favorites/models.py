from django.db import models
from mainPostApp.models import TotalCategories as Category, LectureInfo as Lecture

class FavoriteCategories(models.Model): # 사용자가 선호하는 카테고리
    Favorite_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey('userApp.UserData',on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)

class FavoriteLectures(models.Model):   # 사용자가 즐겨찾기한 강의
    Favorite_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey('userApp.UserData',on_delete=models.CASCADE)
    lecture_id = models.ForeignKey(Lecture,on_delete=models.CASCADE)

class FavoritePost(models.Model):   # 사용자가 즐겨찾기한 게시글
    Favorite_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey('userApp.UserData', on_delete=models.CASCADE)          #순환 참고가 발생하여 코드 수정
    post_id = models.ForeignKey('userPostApp.UserCommunityPost', on_delete=models.CASCADE)