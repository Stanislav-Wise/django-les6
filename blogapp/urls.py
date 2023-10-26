from django.urls import path
from .views import index, author_read, fake_author_and_post, author_posts

urlpatterns = [
    path('', index, name='index'),
    path('author/', author_read, name='author'),
    path('fake_data/', fake_author_and_post, name='fake_data'),
    path('posts/<int:author_id>/', author_posts, name='author_posts'),

]
