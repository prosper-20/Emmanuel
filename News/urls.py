from django.urls import path
from .views import news_home_page, news_detail_page

urlpatterns = [
    path("", news_home_page.as_view(), name="home"),
    path("<slug:slug>/", news_detail_page.as_view(), name="detail")
]