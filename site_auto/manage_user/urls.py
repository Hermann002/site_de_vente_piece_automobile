from django.urls import include, path
from rest_framework import routers

from manage_user import views

router = routers.DefaultRouter()
router.register(r'registredusers', views.RegistredUser)
router.register(r'updatedusers', views.UpdatedUser)
router.register(r'deletedusers', views.DeletedUser)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += router.urls