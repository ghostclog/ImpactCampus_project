from django.db import models
from userApp.models import UserData

class TotalCategories(models.Model):    #카테고리 모음집. 강의나 유저의 카테고리랑은 다름
    category_id = models.IntegerField(primary_key=True)
    top_category_code = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True) # 상위 카테고리 존재시.
    category_name = models.CharField(max_length=20)
    degree = models.IntegerField()  # 해당 컬럼은 1, 2, 3. 이것만 들어갈 예정(최상위 카테고리, 상위 카테고리, 카테고리)

    def __str__(self):      # 해당 모델 객체명 사용시, 카테고리 이름과 ID값을 반환
        return str({
            "category_id" : self.category_id,
            "category" : self.category_name,
        })
    
class LectureInfo(models.Model):    # 강의 정보
    lecture_id = models.BigAutoField(primary_key=True)
    lecture_name = models.CharField(max_length=40)
    appropriate_grade = models.CharField(max_length=5)  # 초급 중급 심화. 총 3개로 나눠질 예정
    platform = models.CharField(max_length=20)
    lecture_infomation = models.TextField()

class LectureCategories(models.Model):  # 강의의 카테고리 정보
    lecture_category_id = models.BigAutoField(primary_key=True)
    lecture_id = models.ForeignKey(LectureInfo,on_delete=models.CASCADE)
    category_id = models.ForeignKey(TotalCategories,on_delete=models.CASCADE)

class LectureReview(models.Model):  # 강의 리뷰.
    review_id = models.BigAutoField(primary_key=True)
    review_contents = models.CharField(max_length=200, blank=True, null=True)
    review_star = models.IntegerField()
    review_date = models.DateTimeField()
    lecture_id = models.ForeignKey(LectureInfo,on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserData,on_delete=models.CASCADE)