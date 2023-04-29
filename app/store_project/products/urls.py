from django.urls import path

from .views import BookDetailView
from .views import BookListView
from .views import ProgramDetailView
from .views import ProgramListView
from .views import StoreView

app_name = "products"
urlpatterns = [
    path("store/", StoreView.as_view(), name="store"),
    path("books/<str:slug>/", BookDetailView.as_view(), name="book_detail"),
    path("books/", BookListView.as_view(), name="book_list"),
    path("programs/<str:slug>/", ProgramDetailView.as_view(), name="program_detail"),
    path("programs/", ProgramListView.as_view(), name="program_list"),
]
