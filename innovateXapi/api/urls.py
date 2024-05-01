from django.urls import path
from .views import ChatView, TranslateView, ParaphraseView

urlpatterns = [
    path('chat/', ChatView.as_view(), name='chat'),
    path('translate/',TranslateView.as_view(),name='translate'),
    path('paraphrase/', ParaphraseView.as_view(), name='paraphrase'),
]