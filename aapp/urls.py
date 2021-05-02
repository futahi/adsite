from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('islaminspb/', views.islaminspb, name='islaminspb'),
    path('family/', views.family, name='family'),
    path('articles/', views.articles, name='articles'),
    path('quran/', views.quran, name='quran'),

    
    #Detils pages
    path('details/<int:post_id>/', views.post_details, name='details'),
    path('sura_details/<int:sura_id>/', views.sura_details, name='sura_details'),
    path('islam_details/<int:islam_id>/', views.islam_details, name='islam_details'),
    path('family_details/<int:family_id>/', views.family_details, name='family_details'),
    path('article_details/<int:article_id>/', views.article_details, name='article_details'),


 ]