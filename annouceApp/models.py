from django.db import models

# Create your models here.

class Inquiry(models.Model):
    inquiry_id = models.BigAutoField(primary_key=True)
    inquiry_title = models.CharField(max_length=40)
    inquiry_content = models.CharField(max_length=800)
    user_id = models.ForeignKey('userApp.UserData', on_delete=models.CASCADE)       #순환 참고가 발생하여 코드 수정
    is_open = models.BooleanField()

class ForEmailChk(models.Model):
    chk_id = models.BigAutoField(primary_key=True)
    user_email = models.EmailField(unique=True)
    chk_num = models.CharField(max_length=40)

class Announcement(models.Model):
    announcement_id = models.BigAutoField(primary_key=True)
    announcement_title = models.CharField(max_length=40)
    announcement_contents = models.TextField()