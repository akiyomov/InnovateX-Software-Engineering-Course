from django.urls import path
from .views import ChatView, ParaphraseView

urlpatterns = [
    path('chat/', ChatView.as_view(), name='chat'),
    path('paraphrase/', ParaphraseView.as_view(), name='paraphrase'),
]