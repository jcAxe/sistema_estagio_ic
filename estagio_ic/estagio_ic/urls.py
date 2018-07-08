from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('base_structures.urls', namespace='base_structures')),
    url(r'^actions/', include('user_actions.urls', namespace='user_actions')),

    url(r'^admin/', admin.site.urls),
]
