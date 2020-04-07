from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('test/', views.test, name='test'),
    path('terms/', views.terms, name='terms'),
    path('contacts/', views.contacts, name='contacts'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
