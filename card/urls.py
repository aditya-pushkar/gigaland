from .views import latest, latest2, latest3, index
# from card import views


from django.urls import path


urlpatterns = [
    path('index', index.as_view(), name='index'),
    # path('', include(router.urls)),
    path('scrap', latest, name="latest"),
    path('scrap/2', latest2, name="data-portion.io"),
    path('scrap/3', latest3, name="data-myth.market"),
    

]
