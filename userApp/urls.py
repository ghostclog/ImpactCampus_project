from django.urls import path
from . import views

urlpatterns = [
    path('regist/', views.regist),  #회원가입
    path('login/', views.login),    #로그인
    path('emailSend/', views.email_send),   #인증 번호 보내기
    path('emailCHK/', views.email_chk),     #인증번호 확인
    path('idCHK/', views.id_chk),   #아이디 중복 확인
    path('findID/', views.find_id), #아이디 찾기
    path('CHpassword/', views.ch_password), #비밀번호 바꾸기
    path('RECHKpassword/', views.rechk_password),   #비밀번호 인증
    path('editCategory/', views.edit_category),     #카테고리 수정
    path('mypageInfo/', views.mypage_info), #마이페이지
]
