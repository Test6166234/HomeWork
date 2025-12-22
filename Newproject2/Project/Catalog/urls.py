from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from Catalog.views import DoctorViewSet, PatientViewSet, BranchViewSet, AppointmentViewSet, UserViewSet, hospital_dashboard
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'branches', BranchViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'users', UserViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Safe.clinic API",
        default_version='v1',
        description="Backend API for Safe.clinic",
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/stats/', hospital_dashboard),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0)),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0)),
]
