# Создайте модель Автор. Модель должна содержать следующие поля:
# ●	имя до 100 символов
# ●	фамилия до 100 символов
# ●	почта
# ●	биография
# ●	день рождения
# Дополнительно создай пользовательское поле “полное имя”, которое возвращает имя и фамилию.

from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    b_data = models.DateField()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'


# Создайте модель Статья (публикация). Авторы из прошлой задачи могут писать статьи.
# У статьи может быть только один автор. У статьи должны быть следующие обязательные поля:
# ●	заголовок статьи с максимальной длиной 200 символов
# ●	содержание статьи
# ●	дата публикации статьи
# ●	автор статьи с удалением связанных объектов при удалении автора
# ●	категория статьи с максимальной длиной 100 символов
# ●	количество просмотров статьи со значением по умолчанию 0
# ●	флаг, указывающий, опубликована ли статья со значением по умолчанию False


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views_count = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
