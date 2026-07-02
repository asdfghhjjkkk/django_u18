
from django.contrib import admin
from django.urls import path
from page.views import get_product, detail_product, create_product,update_product,delete_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_product, name='list'),
    path('create/', create_product, name='create'),
    path('update/<int:pk>/', update_product, name='update'),
    path('detail/<int:pk>/', detail_product, name='detail'),
    path('delete/<int:pk>/', delete_product, name='delete'),
]
