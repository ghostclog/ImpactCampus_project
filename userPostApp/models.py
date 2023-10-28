from django.db import models
from userApp.models import UserData

# Create your models here.

class UserCommunityPost(models.Model):  # 유저 작성 글
    post_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(UserData,on_delete=models.CASCADE)
    post_contents = models.TextField()
    reg_date = models.DateTimeField()
    post_title = models.CharField(max_length=40)
    # 추천 컬럼?

class RepostUserPost(models.Model): # 작성된 글 신고
    report_id = models.BigAutoField(primary_key=True)
    report_contents = models.CharField(max_length=100)  # 신고 내용. 프론트에서 정해진 내용을 쏴줄 예정임
    post_id = models.ForeignKey(UserCommunityPost,on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserData,on_delete=models.CASCADE)