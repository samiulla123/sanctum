from rest_framework import serializers
from .models import NetworkStatus,Clients,ClientInfo,CpuTap,DiskTap,MemoryTap,NetworkTap

class NetworkStatusSerializer(serializers.ModelSerializer):
	class Meta:
		model=NetworkStatus
		fields=("time_stamp","Hostname","HostIpAddress")

class ClientsSerializer(serializers.ModelSerializer):
	class Meta:
		model=Clients
		fields=("c_id","c_name","c_inet","c_mac","c_token")

class ClientInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model=ClientInfo
		fields=("c_id","c_name","c_arch","c_platform","c_cpu","c_rom","c_ram_total","c_cpu_cores","c_cpu_freq")



class MemSerializer(serializers.ModelSerializer):
	class Meta:
		model=MemoryTap
		fields=('c_id','m_total','m_used','m_free','m_active','m_inactive','m_shared','m_cached','m_buffers')

class CPUSerializer(serializers.ModelSerializer):
	class Meta:
		model=CpuTap
		fields=('c_id','cpu_curr_freq','cpu_min_freq','cpu_max_freq','cpu_usage','cpu_curr_temp','cpu_high_temp','cpu_crit_temp')

class DiskSerializer(serializers.ModelSerializer):
	class Meta:
		model=DiskTap
		fields=('c_id','d_used_perc','d_total','d_used','d_free')#

class NetSerializer(serializers.ModelSerializer):
	class Meta:
		model=NetworkTap
		fields=('c_id','n_up','n_down')
