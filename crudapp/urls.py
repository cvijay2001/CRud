from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from crudapp import urls
from . import views

urlpatterns = [

    path('emp', views.emp,name='emp'),  
    path('',views.show,name='show'),  
    path('edit/<int:eid>/',views.edit, name='edit'),
    path('delete/<int:eid>', views.destroy, name='delete'),  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()