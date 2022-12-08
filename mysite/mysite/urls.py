from django.contrib import admin
from django.urls import path, include
from . views import *

# untuk media
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', index, name='index'),
    path('resep', resep, name='resep'),
    path('resep/detil/<str:key>', resep_detil, name='resep_detil'),
    path('tempatmakan', tempatmakan, name='tempatmakan'),
    path('kontak', kontak, name='kontak'),
        
    # apps 
    path('dashboard/', include('resep.urls')),
    
    # login & logout
    path('login/', login, name='login'), 
    path('logout/', logout_view, name='logout'),   
        

]

# untuk media
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)