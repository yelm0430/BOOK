# blog/urls.py

from django.urls import path
from . import views

app_name='blog'

urlpatterns = [
    path('create/',views.create_posting,name='create_posting'),
    path('',views.index_posting,name='index_posting'),

    path('<int:posting_pk>/',views.detail_posting,name='detail_posting'),
    path('<int:posting_pk>/',views.update_posting,name='update_posting'),
    path('<int:posting_pk>/',views.delete_posting,name='delete_posting'),

    path('<int:posting_pk>/replies/create/',views.create_reply,name='create_reply'),
    path('<int:posting_pk>/replies/delete/',views.delete_reply,name='delete_reply'),
]
