from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
import random



from .models import UserData
from Favorites.models import FavoriteCategories as FavorCategory
from annouceApp import ForEmailChk

#회원가입
def regist(request):
    if request.method == 'POST':
        #유저 정보
        user_id = request.POST['user_id']
        user_pass = request.POST['user_pass']
        user_email = request.POST['user_email']
        user_tier = 10
        user = UserData(user_id=user_id, user_pass=user_pass, user_email=user_email, user_tier = user_tier)  # UserData 객체 생성
        user.save()  # 유저 정보를 데이터베이스에 저장 / 해싱도 같이 해줌

        #유저의 즐겨찾기 카테고리
        user_category = request.POST['user_category']
        for cateogry in user_category:
            user_categories = FavorCategory(user_id = user_id,category_id = cateogry)
            user_categories.save()

        return JsonResponse({'return_message':'회원가입 성공'})
    
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

        rand_num = random.random()      # random 라이브러리 가져오기
        num = int(rand_num*1000000)     # 6자리 랜덤 수 생성
        chk_num = str(num).zfill(6)     # 만약 비어있는 부분 존재시 0으로 채워주기
        user_email = request.POST['user_email'] # 사용자 이메일 정보 획득

        email_data = ForEmailChk(chk_num = chk_num, user_email = user_email)   #추후 데이터 체크를 위해 테이블에 저장
        email_data.save()

        html_mail = render_to_string("send_email.html", {'chk_num': chk_num})    # 발신 이메일 양식에 사용자가 사용할 인증 번호 넣기
        send_mail(
                    'Studinfo에서 비밀번호 변경에 대한 인증번호입니다.',        #메일 제목
                    '1',                #메일 내용(html파일에 의해 실제로 메일에 표현되지 않음)
                    'lldp0506@naver.com',       #발신인
                    [user_email],               #수신인
                    fail_silently=False,
                    html_message=html_mail      #html내용
                )

#이메일 인증
def email_chk(request):
    if request.method == 'POST':
        user_email = request.POST['user_email']     # 사용자 이메일 정보 획득
        chk_num = request.POST['chk_num']           # 사용자 이메일 정보 획득
        if ForEmailChk.objects.filter(user_email=user_email, chk_num=chk_num).exists(): #프론트에서 보내준 이메일과 그에 맞는 인증 번호 존재시
            return JsonResponse({'return_message':'인증 성공'})
        return JsonResponse({'return_message':'인증 실패'})


#아이디 중복 확인
def id_chk(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        chk = UserData.objects.all()                    # 유저 테이블의 모든 객체를 가져옴
        if chk.filter(user_id = user_id).exists():      # 아이디 중복 체크
            return JsonResponse({'chk_message':'아이디 중복입니다.'})
        return JsonResponse({'chk_message':'아이디 중복이 아닙니다.'})



#아이디 찾기
def find_id(request):
    if request.method == 'POST':
        user_email = request.POST['user_email']
        chk = UserData.objects.all()
        if chk.filter(user_email = user_email).exists():
            user_id = chk.filter(user_email = user_email).values('user_id')
            return JsonResponse({'chk_message':'이것이 당신의 아이디.'})
        return JsonResponse({'chk_message':'당신의 아이디. 존재하지 않는다.'})
        
    #이메일 입력하면 해당 이메일이 등록? 기록된? 아이디값 반환해주기

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