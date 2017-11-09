from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^itens/$', views.ItemList.as_view()),
    url(r'^item/(?P<pk>\d+)$', views.ItemDetail.as_view()),
    url(r'^shopping-lists/$', views.ShoppingListList.as_view()),
    url(r'^itens-in-list/$', views.ItemInListList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)