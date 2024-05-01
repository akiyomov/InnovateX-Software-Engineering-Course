from django.urls import path
from .views import ChatView, TranslateView, ParaphraseView, GrammarCheckView

urlpatterns = [
    path('chat/', ChatView.as_view(), name='chat'),
    path('translate/',TranslateView.as_view(),name='translate'),
    path('paraphrase/', ParaphraseView.as_view(), name='paraphrase'),
    path('grammar-check/', GrammarCheckView.as_view(), name='grammar-check'),
]
