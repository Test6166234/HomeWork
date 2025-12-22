
from rest_framework.routers import DefaultRouter


from .views import PostViewSet, AAAViewSet, BookViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'AAA', AAAViewSet)
router.register(r'books', BookViewSet)


urlpatterns = router.urls

