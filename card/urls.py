from .views import index, latest, latest2, latest3
# from rest_framework import routers
from django.urls import path

# router = routers.DefaultRouter()
# router.register("cardapi", CardApi)

urlpatterns = [
    path('index', index, name='index'),
    # path('', include(router.urls)),
    path('scrap', latest, name="latest"),
    path('scrap/2', latest2, name="data-portion.io"),
    path('scrap/3', latest3, name="data-myth.market"),
    

]
