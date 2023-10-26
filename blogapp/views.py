# Доработаем задачу 4.
# Создай четыре функции для реализации CRUD в модели Django Article (статья).


from django.shortcuts import render
from .models import Author, Article
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
# Create your views here.


def author_read(request):
    author = Author.objects.all()
    return HttpResponse(author)


def index(request):
    context = {
        'title': 'Блог',
        'data': 'Какой-то текст',
    }
    return render(request, 'blogapp/index.html', context=context)


def fake_author_and_post(request):
    for i in range(10):
        author = Author(first_name=f'Author{i}',
                        last_name=f'Lastname{i}',
                        email='email{i}.gmail.com',
                        bio=f"{'какой-то текст ' * 10}",
                        b_data="2023-10-26"
                        )
        # author.save()

        for j in range(15):
            article = Article(
                title=f'Title_{j}',
                content=f"{'какой-то текст ' * 10 * j}",
                publication_date='2023-10-26',
                author=author,
                category=f'Category{j}'

            )
            # article.save()

# Доработаем задачи из прошлого семинара по созданию моделей автора, статьи и комментария.
# Создайте шаблон для вывода всех статей автора в виде списка заголовков.
# Если статья опубликована, заголовок должен быть ссылкой на статью.
# Если не опубликована, без ссылки.
# Не забываем про код представления с запросом к базе данных и маршруты.


def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    article = Article.objects.filter(author=author).order_by('-id')
    context = {
        "title": "Статьи автора",
        "author": author,
        "posts": article
    }
    return render(request, "blogapp/author_posts.html", context=context)

