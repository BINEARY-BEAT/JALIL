from . import views
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet


router=DefaultRouter()
router.register(r'books',BookViewSet,basename='book')

urlpatterns = [
    path('login/',views.user_login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('fuck/',views.fuck,name='fuck'),
    path('',include(router.urls))
]

