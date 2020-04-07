from django.urls import path

from app import views

urlpatterns = [
path('', views.DataList.as_view(), name='data_list'),
    path('', views.DataList.as_view(), name='data_list'),
    path('view/<int:pk>', views.DataView.as_view(), name='data_view'),
    path('new', views.DataCreate.as_view(), name='data_new'),
    path('view/<int:pk>', views.DataView.as_view(), name='data_view'),
    path('edit/<int:pk>', views.DataUpdate.as_view(), name='data_edit'),
    path('delete/<int:pk>', views.DataDelete.as_view(), name='data_delete'),
]

