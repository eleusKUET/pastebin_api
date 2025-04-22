from django.urls import path

from .views import ContentCreateView, ContentRetrieveView, ContentUpdateView, ContentDeleteView, RUDView

app_name = "content"
urlpatterns = [
    path('create/', ContentCreateView.as_view(), name='create'),
    path('retrieve/<str:token>/', ContentRetrieveView.as_view(), name='read'),
    path('update/<str:token>/', ContentUpdateView.as_view(), name='update'),
    path('delete/<str:token>/', ContentDeleteView.as_view(), name='delete'),
    path('<str:token>/', RUDView.as_view(), name='read-update-delete')
]
