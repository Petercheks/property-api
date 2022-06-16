from rest_framework.routers import DefaultRouter

from users.views import RolViewSet, UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('roles', RolViewSet, basename='rol')

urlpatterns = router.urls