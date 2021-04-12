from django.urls import path

from temlink import views

urlpatterns = [
    path('generate_link/', views.GenerateLinkView.as_view()),
    path('<str:token>/', views.LinkView.as_view())
]
