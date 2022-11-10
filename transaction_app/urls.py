from django.contrib import admin
from django.urls import path, include
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import TransactionListView

urlpatterns = [
    path('transaction/', TransactionListView.as_view()),
]