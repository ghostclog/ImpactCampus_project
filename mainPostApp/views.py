from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.db.models import Avg, Max
from datetime import datetime
from django.core import serializers

from .models import TotalCategories, LectureInfo, LectureCategories, LectureReview




#강의 검색 결과(비로그인/로그인 두 가지로 나눠짐.)
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
        lecture_id = LectureInfo.objects.aggregate(Max('lecture_id'))['lecture_id__max']

        LectureInfo.objects.create(
            lecture_id = lecture_id,
            lecture_name = request.POST['lecture_name'],
            appropriate_grade = request.POST['appropriate_grade'],
            platform = request.POST['platform'],
            lecture_infomation = request.POST['lecture_infomation'],
        )

        categories = request.POST['lecture_name']
        category_list = [LectureCategories(lecture_id = lecture_id,category_id = category_id) for category_id in categories]
        LectureCategories.objects.bulk_create(
            category_list
        )



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
            lecture_review_data = LectureReview.objects.filter(lecture_id= lecture_id)
            lecture_review = serializers.serialize('json', lecture_review_data)
            
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
        #강의 정보
        lecture_id = request.POST['lecture_id']
        #강의 평점
        review_star = request.POST['review_star']
        #작성자
        user_id = request.POST['user_id']

        #만약 리뷰 내용이 있는 경우.
        if 'review_contents' in request.POST:
            review_contents = request.POST['review_contents']
            LectureReview.objects.create(
                lecture_id = lecture_id,
                review_star = review_star,
                user_id = user_id,
                review_contents = review_contents,
                review_date = datetime.now(),
                )
        #리뷰 내용이 없는 경우.
        else:
            LectureReview.objects.create(
                lecture_id = lecture_id,
                review_star = review_star,
                user_id = user_id,
                review_date = datetime.now(),
                )
        return JsonResponse({'message':"작성 완료."})

#리뷰 수정
def edit_review(request):
    # 수정 버튼 누를때, 리뷰 데이터 보내주기.
    if request.method == 'GET':
        # 리뷰 아이디 값 받아주기
        review_id = request.POST['review_id']
        # 해당 아이디에 맞는 데이터 추출
        review_date = LectureCategories.objects.get(review_id = review_id)
        # 데이터 변환
        review = serializers.serialize('json',review_date)
        return JsonResponse({'review':review})
    if request.method == 'POST':
        # 리뷰 아이디 값 받아주기
        review_id = request.POST['review_id']

        # 해당 아이디에 맞는 데이터 추출
        review_date = LectureCategories.objects.get(review_id = review_id)
        review_star = request.POST['review_star']

        #만약 리뷰 내용이 있는 경우.
        if 'review_contents' in request.POST:
            review_date.review_contents = request.POST['review_contents']
            review_date.review_star = review_star

        #리뷰 내용이 없는 경우.
        else:
            review_date.review_star = review_star
        review_date.save()
        return JsonResponse({'message':"작성 완료."})



#리뷰 삭제
def delete_review(request):
    if request.method == 'POST':
        # 리뷰 아이디 값 받아주기
        review_id = request.POST['review_id']
        # 해당 아이디에 맞는 데이터 추출
        review_date = LectureCategories.objects.get(review_id = review_id)
        review_date.delete()

#리뷰 정렬
def sort_reivew(request):
    if request.method == 'POST':
        pass
    #(티어, 카테고리, 작성, 찜한 글, 찜한 강의) 반환