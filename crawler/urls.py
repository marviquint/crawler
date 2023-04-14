from django.urls import path
from . import views

urlpatterns = [
    path('crawl-website/', views.download_pdf, name='download_pdf'),
]





# from django.urls import path
# from . import views

# urlpatterns = [
#     path('crawl_books/', views.crawl_books, name='crawl_books'),
#     #path('book_data/', views.book_data, name='book_data'),  # add this line
# ]
