from django.shortcuts import render

# Create your views here.

def regist(request):            #통합 계좌 페이지
    if request.method == 'GET':
        return render(request, 'home.html')
    if request.method == 'GET':
        return render(request, 'home.html')