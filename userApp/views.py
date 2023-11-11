from django.shortcuts import render
from django.http import HttpResponse
from .models import UserData

#회원가입
def regist(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user_pass = request.POST['user_pass']
        user_email = request.POST['user_email']
        user_tier = 10

        user = UserData(user_id=user_id, user_pass=user_pass, user_email=user_email, user_tier = user_tier)  # UserData 객체 생성
        user.save()  # 데이터베이스에 저장 / 해싱도 같이 해줌
        return render(request, 'home.html')
    
#로그인
def login(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user_pass = request.POST['user_pass']
        try:
            user = UserData.objects.get(user_id=user_id)
            if user.check_password(user_pass):
                return HttpResponse('로그인 성공!')
            else:
                return HttpResponse('비번이 틀림')
        except:
            return HttpResponse('해당하는 아이디가 없음')