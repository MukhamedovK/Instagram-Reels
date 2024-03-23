from django.urls import path

from instagram.views import AllReelsView, RecommendationsView, home_page


urlpatterns = [
    path('', home_page, name='home'),
    path('reels/', AllReelsView.as_view()),
    path('recommendations/', RecommendationsView.as_view()),
]

