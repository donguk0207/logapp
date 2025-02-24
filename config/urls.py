from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('log_app.urls')), #default 첫페이지 설정할때
    path("logapp/", include('log_app.urls')),
    path("log/", include('log.urls'))

]
