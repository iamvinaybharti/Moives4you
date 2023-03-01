from django.contrib import admin
from django.urls import path
from moviemanager import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('book/', views.book, name="book"),
    path('terms/', views.terms, name="terms"),
    path('about/', views.about, name="about"),
    path('checkout/', views.checkout),
    path('<int:movie_id>/', views.detail, name = "detail"),

] + static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
