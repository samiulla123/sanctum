from django.conf.urls import url
from .views import NetworkStatusController,ClientInfoController,ClientsController,ClientsAPIController,SysStatController

urlpatterns=[
        url(r'^$',NetworkStatusController.as_view(), name='network_status'),
        url(r'^clients/datain/',SysStatController.as_view(), name='clients_list_api_datain'),
        url(r'^clients/api/',ClientsAPIController.as_view(), name='clients_list_api'),
        url(r'^clients/',ClientsController.as_view(), name='clients_list'),
        url(r'^clientinfo/',ClientInfoController.as_view(), name='clients_info'),]
        

