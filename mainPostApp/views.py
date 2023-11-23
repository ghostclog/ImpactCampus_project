from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.db.models import Avg

from .models import TotalCategories, LectureInfo, LectureCategories, LectureReview




#강의 목록
def lecture_list(request):
    if request.method == 'POST':
        pass
    #(티어, 카테고리, 작성, 찜한 글, 찜한 강의) 반환

#강의 검색 결과
def search_lecture(request):
    if request.method == 'POST':
        pass
    #(티어, 카테고리, 작성, 찜한 글, 찜한 강의) 반환

#정렬?
def sort_lecture(request):
    if request.method == 'POST':
        pass
    #(티어, 카테고리, 작성, 찜한 글, 찜한 강의) 반환

#강의 정보 작성 및 정보 저장
def write_lecture(request):
    if request.method == 'POST':
        pass
    #(티어, 카테고리, 작성, 찜한 글, 찜한 강의) 반환

#강의 정보 보기
from django.core import serializers

def lecture_info(request):
    if request.method == 'POST':
        lecture_id = request.POST['lecture_id']
        try:
            # 강의 정보
            lecture_info = LectureInfo.objects.get(lecture_id= lecture_id)
            
            # 강의 카테고리 정보
            categories_info = LectureCategories.objects.filter(lecture_id = lecture_id).values_list('category_id', flat=True)
            lecture_category = []
            for i in categories_info:
                lecture_category.append(TotalCategories.objects.filter(category_id = i).values('category_name'))
            
            # 강의 리뷰 및 댓글
            lecture_review = LectureReview.objects.filter(lecture_id= lecture_id)
            lecture_review = serializers.serialize('json', lecture_review)
            
            # 강의 별점
            lecture_star = LectureReview.objects.filter(lecture_id= lecture_id).aggregate(Avg('review_star'))['review_star__avg']

            # 반환 데이터
            lecture_info_data = {
                'lecture_id' : lecture_info.lecture_id,
                'lecture_name' : lecture_info.lecture_name,
                'appropriate_grade' : lecture_info.appropriate_grade,
                'platform' : lecture_info.platform,
                'lecture_infomation' : lecture_info.lecture_infomation,
                'lecture_category':lecture_category,
                'lecture_star' : lecture_star
            }
            return JsonResponse({'lecture_info_data':lecture_info_data,'lecture_review':lecture_review})
        except:
            return JsonResponse({'message':"잘못된 강의입니다."})



#강의에 리뷰 작성하기
def write_review(request):
    if request.method == 'POST':
        pass
    #(티어, 카테고리, 작성, 찜한 글, 찜한 강의) 반환

#리뷰 수정
def edit_review(request):
    if request.method == 'POST':
        pass
    #(티어, 카테고리, 작성, 찜한 글, 찜한 강의) 반환

#리뷰 삭제
def delete_review(request):
    if request.method == 'POST':
        pass
    #(티어, 카테고리, 작성, 찜한 글, 찜한 강의) 반환

#리뷰 정렬
def sort_reivew(request):
    if request.method == 'POST':
        pass
    #(티어, 카테고리, 작성, 찜한 글, 찜한 강의) 반환