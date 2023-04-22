from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('show/',views.show,name='show'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('log_page/',views.log_page,name='log_page'),
    path('page/',views.page,name='page'),
    

]
