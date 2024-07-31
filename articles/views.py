from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }

    return render(request, 'index.html', context)

def create(request):
    # new/ => 빈 종이를 보여주는 기능
    # create/ => 사용자가 입력한 데이터 저장

    # ===== 오늘은 메소드별 차이로 기능 분리 (기능은 항상 2가지 - 하고자 하는 것 동일 구조만 변경)

    # GET create/ => 빈 종이를 보여주는 기능
    # POST create/ => 사용자가 입력한 데이터 저장

    if request.method == 'POST':
        form = ArticleForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('articles:index')

            # article = Article()
            # article.title = title
            # article.save()
            # 와 동일, 그러나 is_valid()로 검증 코드 추가 !

        # else: => 중복 없앤 최종 코드 ! (아래 겹치는 코드 shift + Tab으로 빼기)
            # form = ArticleForm(request.POST)
            # context = {
            #     'form': form,
            # }

            # return render(request, 'create.html', context)

    else:
        form = ArticleForm()

    context = {
        'form': form,
    }

    return render(request, 'form.html', context)
        
def delete(request, id):

    return redirect('articles:index')

def update(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)

        if form.is_valid():
            form.save()
            return redirect('articles:index')
    
    else:
        # article = Article.objects.get(id=id)

        form = ArticleForm(instance=article)

    context = {
        'form': form,
    }

    return render(request, 'form.html', context)