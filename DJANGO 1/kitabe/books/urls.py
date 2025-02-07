from django.urls import path
from books import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update_data/<int:id>', views.update_data, name='update_data'),
    path('deletedata/<int:id>', views.deletedata, name='deletedata')
]