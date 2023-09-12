from . import views

from django.urls import path

urlpatterns = (
    path('', views.add, name='add'),
    # path('details',views.details,name='details')
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('lvhome/',views.Testlistview.as_view(),name='lvhome'),
    path('dvhome/<int:pk>/',views.Testdetailview.as_view(),name='dvhome'),
    path('udhome/<int:pk>/',views.Testupdateview.as_view(),name='udhome'),
    path('delhome/<int:pk>/',views.Testdeleteview.as_view(),name='delhome'),
)
