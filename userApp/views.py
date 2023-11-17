from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
import random



from .models import UserData
from Favorites.models import FavoriteCategories as FavorCategory
from annouceApp.models import ForEmailChk

#회원가입(인증이 다 완료된 상태)
def regist(request):
    if request.method == 'POST':
        # request에 들어있을 유저 정보 받아주기
        user_id = request.POST['user_id']
        user_pass = request.POST['user_pass']
        user_email = request.POST['user_email']
        user_tier = 10
        # UserData 객체 생성
        user = UserData(user_id=user_id, user_pass=user_pass, user_email=user_email, user_tier = user_tier)
        # 유저 정보를 데이터베이스에 저장 / 해싱도 같이 해줌
        user.save()  

        # 유저의 즐겨찾기 카테고리 저장 알고리즘
        user_category = request.POST['user_category']
        # one(유저id) to many(카테고리id) 구조의 데이터베이스라서, 반복문을 통한 데이터 저장.
        # + 지금와서 생각하는 부분이지만, 유저 즐겨찾기와 같은 데이터는 firebase와같인 비정형. 혹은 json형식이 더 저장 및 관리하기 편하다는 생각이 들었음.
        for cateogry in user_category:
            user_categories = FavorCategory(user_id = user_id,category_id = cateogry)
            user_categories.save()

        return JsonResponse({'return_message':'회원가입 성공.'})
    
#로그인
def login(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user_pass = request.POST['user_pass']

        try:
            # 사용자가 입력한 아이디에 맞는 컬럼을 user라는 변수에 넣음. 만약 없는 경우 에러가 발생함으로, except으로 넘어감
            user = UserData.objects.get(user_id=user_id)
            # 아이디 존재시, model에 정의해둔 check_password 메소드를 통하여 비밀번호를 체크함.
            if user.check_password(user_pass):
                return JsonResponse({'return_message':'로그인 성공.'})
            else:
                return JsonResponse({'return_message':'비밀번호가 틀렸습니다.'})
        except:
            return JsonResponse({'return_message':'아이디가 틀렸습니다.'})
        
#이메일 보내기    
def email_send(request):
    if request.method == 'POST':
        # 사용자 이메일 정보 획득
        user_email = request.POST['user_email']
        
        # 만약 사용자가 입력한 이메일이 이미 가입된 이메일인 경우
        if UserData.objects.filter(user_email = user_email).exists():
            return JsonResponse({'return_message':'이미 존재하는 이메일입니다.'})
        
        # 우선 6자리 랜덤 인증 번호를 생성함. 6자리를 채우주기 위해 빈부분은 '0'으로 채움
        rand_num = random.random()
        num = int(rand_num*1000000)
        chk_num = str(num).zfill(6)

        # 사용자 이메일 정보와 인증 번호를 ForEmailChk라는 데이터베이스에 저장함.
        email_data = ForEmailChk(chk_num = chk_num, user_email = user_email)
        email_data.save()

        # 사용자 이메일로 인증번호를 발송
        html_mail = render_to_string("send_email.html", {'chk_num': chk_num})
        send_mail(
                    'Studinfo에서 온 이메일 인증번호입니다.',        #메일 제목
                    '1',                #메일 내용(html파일에 의해 실제로 메일에 표현되지 않음)
                    'lldp0506@naver.com',       #발신인 / 팀장 '김덕윤'의 이메일임.
                    [user_email],               #수신인
                    fail_silently=False,
                    html_message=html_mail      #html내용
                )
        return JsonResponse({'return_message':'인증 번호를 전송했습니다.'})

#이메일 인증(메일 전송 후)
def email_chk(request):
    if request.method == 'POST':
        # 사용자 이메일과 사용자가 입력한 인증 번호 정보를 받아줌.
        user_email = request.POST['user_email']
        chk_num = request.POST['chk_num']
        
        # 사용자의 이메일과 인증번호가 일치하는 컬럼 존재시, 인증 성공. 아니면 인증 실패
        if ForEmailChk.objects.filter(user_email=user_email, chk_num=chk_num).exists():
            return JsonResponse({'return_message':'인증 성공'})
        return JsonResponse({'return_message':'인증 실패'})

#아이디 중복 확인
def id_chk(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        # 중복 아이디 입력시 에러가 없음. 중복 아이디가 아닌 경우 에러 발생.
        try: 
            UserData.objects.get(user_id=user_id)
            return JsonResponse({'return_message':'사용 할 수 없는 아이디입니다.'})
        except:
            return JsonResponse({'return_message':'사용 가능한 아이디입니다.'})

        # 기존에 생각했던 코드. 근데, 'chk = UserData.objects.all()'를 사용하고, 그 다음 'chk.filter(user_id = user_id).exists()'를 사용하면,
        # 속도가 너무 느려질거같다는 생각이 들어서 코드를 수정함.
        '''
        chk = UserData.objects.all()
        if chk.filter(user_id = user_id).exists():
            return JsonResponse({'chk_message':'아이디 중복입니다.'})
        return JsonResponse({'chk_message':'아이디 중복이 아닙니다.'})    
        '''

#아이디 찾기
def find_id(request):
    if request.method == 'POST':
        user_email = request.POST['user_email']

        try: 
            user_data = UserData.objects.get(user_email = user_email)
            user_id = user_data.user_id
            return JsonResponse({'chk_message':user_id})
        except:
            return JsonResponse({'chk_message':'해당 이메일과 연결된 아이디를 찾을 수 없습니다.'}) 

        # 기존에 만들어놨던 코드. 위에 코드로 조금 더 간결하게 만들었음.
        '''
        chk = UserData.objects.all()
        if chk.filter(user_email = user_email).exists():
            user_id = chk.filter(user_email = user_email).values('user_id')
            return JsonResponse({'chk_message':'이것이 당신의 아이디.'})
        return JsonResponse({'chk_message':'당신의 아이디. 존재하지 않는다.'})  
        '''

#비밀번호 수정
def ch_password(request):
    if request.method == 'POST':
        # 유저 정보 받기
        user_id = request.POST['user_id']
        user_pass = request.POST['user_pass']

        # 비밀번호 수정 부분 / get을 사용했기에 혹시나하는 오류에 대비하여 try-except을 넣어둠
        try:
            user = UserData.objects.get(user_id=user_id)
            user.user_pass = user_pass
            user.save()
            return JsonResponse({'return_message':'수정 완료.'})
        except:
            return JsonResponse({'return_message':'잘못된 접근입니다.'})

#비밀번호 수정 전, 비밀번호 인증
def rechk_password(request):
    if request.method == 'POST':
        # 유저 정보 받기
        user_id = request.POST['user_id']
        user_pass = request.POST['user_pass']

        # 비밀번호 인증 부분 / get을 사용했기에 혹시나하는 오류에 대비하여 try-except을 넣어둠
        try:
            user = UserData.objects.get(user_id=user_id)
            if user.check_password(user_pass):
                return JsonResponse({'return_message':'인증 성공.'})
            else:
                return JsonResponse({'return_message':'비밀번호가 틀렸습니다.'})
        except:
            return JsonResponse({'return_message':'잘못된 접근입니다.'})

#사용자 카테고리 수정
def edit_category(request):
    if request.method == 'GET':
        user_id = request.POST['user_id']
        user_category = FavorCategory.objects.filter(user_id = user_id).values("category_id")
        return JsonResponse({'return_message':user_category})
        
    if request.method == 'POST':
        # 유저 정보 받기
        user_id = request.POST['user_id']
        user_category = request.POST['user_category']

        # 기존의 유저 카테고리 삭제.
        FavorCategory.objects.filter(user_id = user_id).delete()
        # 그리고 새롭게 카테고리 업데이트

        #테스트용 코드
        new_categories = [FavorCategory(user_id=user_id, category_id=category) for category in user_category]
        FavorCategory.objects.bulk_create(new_categories)
        return JsonResponse({'return_message':'수정 완료.'})
        #기존 코드
        for cateogry in user_category:
            user_categories = FavorCategory(user_id = user_id,category_id = cateogry)
            user_categories.save()



#마이페이지 정보
def mypage_info(request):
    if request.method == 'POST':
        pass
    #(티어, 카테고리, 작성, 찜한 글, 찜한 강의) 반환