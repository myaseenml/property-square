from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('telecalling', views.telecalling, name='telecalling'),
    path('admin', views.admin, name='admin'),
    path('agent', views.agent, name='agent'),
    path('manager', views.manager, name='manager'),
    path('sale_availability', views.sale_availability, name='sale_availability'),
    path('invoice_generation', views.invoice_generation, name='invoice_generation'),
    path('offer_letter', views.offer_letter, name='offer_letter'),
]
