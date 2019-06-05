from rest_framework import routers

from . import views


router = routers.SimpleRouter()

router.register(r'micro_url', views.URLServiceViewSet)

urlpatterns = router.urls