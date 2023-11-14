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
        return HttpResponse('회원가입 완료')
    
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
        
#이메일 보내기    
def email_send(request):
    if request.method == 'POST':
        pass
    #프론트에서 인증하고자하는 이메일을 보낼 경우,
    #해당 이메일에 인증 번호를 발송함.
    #그리고, 해당 이메일과 인증 번호를 데이터베이스에 저장

#이메일 인증
def email_chk(request):
    if request.method == 'POST':
        pass
    #프론트에서 이메일과 인증 번호 발송시
    #데이터베이스에 저장된 이메일과 인증번호 값을 체크
    #존재한다면 true/아니면 false

#아이디 중복 확인
def id_chk(request):
    if request.method == 'POST':
        pass
    #만약 프론트에서 쏴준 아이디가 데이터베이스에 존재하는지 확인

#아이디 찾기
def find_id(request):
    if request.method == 'POST':
        pass
    #?? 어캐 할지 아직 모름

#비밀번호 수정
def ch_password(request):
    if request.method == 'POST':
        pass
    #프론트에서 아이디와 비번을 주면, 해당 아이디에 맞는 비번 컬럼값을 수정

#비밀번호 수정 전, 비밀번호 인증
def rechk_password(request):
    if request.method == 'POST':
        pass
    #비밀번호 체크를 사용.

#사용자 카테고리 수정
def edit_category(request):
    if request.method == 'POST':
        pass
    #???

#마이페이지 정보
def mypage_info(request):
    if request.method == 'POST':
        pass
    #(티어, 카테고리, 작성, 찜한 글, 찜한 강의) 반환