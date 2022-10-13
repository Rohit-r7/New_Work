
from django.urls import include, path
from . import views
app_name = 'services'
urlpatterns = [
   path('',views.index,name='book'),
   path('food',views.home,name='fud'),
   path('room',views.rom,name='rom'),
   path('pool',views.roh,name='son')
]