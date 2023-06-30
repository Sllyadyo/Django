from django.urls import path
from django.views.decorators.cache import cache_page

from app_news.views import CreateNews, NewsDetail, UpdateNews, NewsByCategory

urlpatterns = [
    # Страница создания новости (кэширование на 1 час)
    path('create_news/', cache_page(3600)(CreateNews.as_view()), name='create_news'),
    
    # Подробности новости по её идентификатору
    path('<int:pk>/', NewsDetail.as_view(), name='news_detail'),
    
    # Обновление существующей новости по её идентификатору
    path('update_news/<int:pk>/', UpdateNews.as_view(), name='update_news'),
    
    # Новости по заданной категории по её идентификатору
    path('category/<int:category_id>', NewsByCategory.as_view(), name='news_by_category')
]
