from django.urls import path
from .views import create_review_flutter, get_reviews, see_review, get_reviews_by_id, get_user,post_review,delete_review
from .views import get_books_by_author, write_review, get_ranks, get_all_reviews, get_books_by_id
from .views import get_reviews_by_user, get_rating_ranks, get_one_review

app_name = 'review'

urlpatterns = [
    path('', get_reviews, name='get_reviews'),
    path('<int:id>/', see_review, name='see_review'),
    path('get_reviews/<int:id>', get_reviews_by_id, name="get_reviews_by_id"),
    path('get_user/<int:id>', get_user, name='get_user'),
    path('user/<int:user_id>', get_reviews_by_user, name='get_reviews_by_user'),
    path('post/<int:book_id>', post_review, name='post_review'),
    path('post-flutter/<int:book_id>', create_review_flutter, name='create_review_flutter'),
    path('delete/<int:review_id>', delete_review, name='delete_review'),
    path('write/<int:book_id>', write_review, name='write_review'),
    path('books/<int:book_id>', get_books_by_id, name='get_books_by_id'),
    path('books/<str:author>', get_books_by_author, name='get_books_by_author'),
    path('ranks/', get_ranks, name='get_ranks'),
    path('rating_ranks/', get_rating_ranks, name='get_rating_ranks'),
    path('all/', get_all_reviews, name='get_all_reviews'),
    path('get_review/<int:review_id>', get_one_review, name='get_one_review'),
]