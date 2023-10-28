from django.db import models

# Create your models here.



'''
# 유틸리티 모음 앱(anounceApp)
  문의사항 테이블
    - 테이블 기본키(PK): IntegerField
    - 제목: CharField
    - 내용: TextField
    - 작성자ID: CharField
    - 공개여부: BooleanField

  이메일 인증 사용 테이블
    - 이메일(이걸 기본키로): EmailField
    - 인증번호: CharField

  공지사항 앱
    - 테이블 기본키(PK): IntegerField
    - 제목: CharField
    - 내용: TextField
'''