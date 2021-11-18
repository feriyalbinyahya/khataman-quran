from django.urls import path

from . import views

app_name = 'kloter'

urlpatterns = [
    path('<int:kloter>', views.render_kloter, name="kloter"),
    path('', views.index, name='index'),
    path('kloter/', views.list_kloter, name="list_kloter"),
    path('addkloter/', views.addkloter, name="addkloter"),
    path('addperson/', views.addperson, name="addperson"),
    path('selesai/<int:id>', views.selesai, name="selesai"),
    path('belumselesai/<int:id>', views.belumselesai, name="belumselesai"),
    path('resetjuz/<int:kloter>', views.resetjuz, name="resetjuz"),
    path('resetputaran/<int:kloter>', views.resetputaran, name="resetputaran"),
    path('formperson/', views.formperson, name="formperson"),
    path('newjuz/<str:kloter>', views.new_juz, name="newjuz"),
    path('delete/<int:id>', views.deleteperson, name="deleteperson"),
]