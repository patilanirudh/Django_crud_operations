from django.contrib import admin
from django.urls import path
# add following line
from django.urls.conf import include
from employee import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('emp',views.emp) ,#add path for employee
    path('show',views.show),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.destroy),
]