from django.urls import path
from . import views

urlpatterns = [
    path('writeLecture/', views.write_lecture), #강의 정보 작성
    path('lectureInfo/', views.lecture_info), #강의 정보
    path('writeRview/', views.write_review), #리뷰 작성
    path('editReview/', views.edit_review), #리뷰 수정
    path('deleteReview/', views.deleteReview), #리뷰 삭제
]
