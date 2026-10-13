from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('accounts.urls')),

    # Movies
    path('movies/', views.movie_details, name='movie'),

    # Articles
    path('', include('articles.urls')),

    path('about/', views.about),
    path('api/',views.movies_api,name="movie"),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )