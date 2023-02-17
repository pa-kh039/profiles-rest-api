from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views 


router=DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,basename='hello-viewset') #a route has been registered, all the urls can be retrieved using the base_name using the url retrieval function provided by django

urlpatterns=[
    path('hello-view/',views.HelloApiView.as_view()), #routes directly inserted inside urlpatterns won't be displayed...routes registered with router and then inserted into urlpatterns will be displayed using defaultrouter, like the below path
    path('',include(router.urls)),
]

