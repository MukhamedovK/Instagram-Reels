from django.urls import path

from .views import AllReelsView, RecommendationsView


urlpatterns = [
    path('reels/', AllReelsView.as_view()),
    path('recommendations/', RecommendationsView.as_view()),
]

