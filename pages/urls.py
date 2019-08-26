from django.urls import path
from .views import HomePageViews


urlpatterns = [path('',HomePageView.as_view(),name='home')]