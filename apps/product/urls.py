from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^api/', include(([
        url(r'^$', views.ProductList.as_view(), name='list'),
        url(r'^bill/$', views.product_list, name='bill'),
        url(r'^(?P<pk>[0-9]+)/$', views.ProductDetail.as_view(), name='detail'),
    ], 'api'), namespace='api')),
]
