
from django.contrib import admin
from django.urls import path
from donations import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name='home'),
    path('donate/', views.donate_view, name='donate'),
    path('thank-you/', views.thank_you_view, name='thank_you'),
    path('export/csv/', views.export_donations_csv, name='export_donations_csv'),
]
