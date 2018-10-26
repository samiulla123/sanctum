from django.db import models 
import hashlib
from django.contrib.auth.models import User
from uuid import uuid4

class NetworkStatus(models.Model):
	time_stamp=models.CharField(max_length=20,null=False)
	Hostname=models.CharField(max_length=20,null=False)
	HostIpAddress=models.CharField(max_length=20,null=False)

	def __str__(self):
                return "Time:{} \n Hostname: {} \n Ip address: {}".format(self.time_stamp, self.Hostname,self.HostIpAddress)

class Clients(models.Model):
	c_name=models.CharField(max_length=20)
	c_id = models.AutoField(primary_key=True)
	c_inet=models.CharField(max_length=15,null=False,unique=True)
	c_mac=models.CharField(max_length=17,unique=True)
	@property
	def c_token(self):
		hash_object = hashlib.sha1((self.c_inet+self.c_mac).encode('utf-8'))
		hex_dig = hash_object.hexdigest()		
		return str(hex_dig)

	def __str__(self):
		return "c_id:{} inet:{}\nmac:{}\n".format(self.c_id,self.c_inet,self.c_mac)

class ClientInfo(models.Model):
	c_id=models.ForeignKey(Clients,on_delete=models.CASCADE)
	time_stamp = models.DateTimeField(auto_now_add=True)
	c_name=models.CharField(max_length=20,null=False)#
	c_arch=models.CharField(max_length=5)#
	c_platform=models.CharField(max_length=20)#
	c_cpu=models.CharField(max_length=40)#
	c_rom=models.IntegerField()#
	c_ram_total=models.IntegerField()#
	c_cpu_cores=models.IntegerField()#
	c_cpu_freq=models.CharField(max_length=10)#


class MemoryTap(models.Model):
	c_id=models.ForeignKey(Clients,on_delete=models.CASCADE)
	time_stamp = models.DateTimeField(auto_now_add=True)
	m_total=models.IntegerField()
	m_used=models.IntegerField()
	m_free=models.IntegerField()
	m_active=models.IntegerField(blank=True,null=True)
	m_inactive=models.IntegerField(blank=True,null=True)
	m_shared=models.IntegerField(blank=True,null=True)
	m_cached=models.IntegerField(blank=True,null=True)
	m_buffers=models.IntegerField(blank=True,null=True)


class DiskTap(models.Model):
	c_id=models.ForeignKey(Clients,on_delete=models.CASCADE)
	time_stamp = models.DateTimeField(auto_now_add=True)
	d_total=models.IntegerField()
	d_used=models.IntegerField()
	d_free=models.IntegerField()
	d_used_perc=models.IntegerField()#d_used_perc


class NetworkTap(models.Model):
	c_id=models.ForeignKey(Clients,on_delete=models.CASCADE)
	time_stamp = models.DateTimeField(auto_now_add=True)
	n_up=models.IntegerField()
	n_down=models.IntegerField()

class CpuTap(models.Model):
	c_id=models.ForeignKey(Clients,on_delete=models.CASCADE)
	time_stamp = models.DateTimeField(auto_now_add=True)
	cpu_usage=models.DecimalField(decimal_places=2,max_digits=5)
	cpu_curr_freq=models.IntegerField()
	cpu_min_freq=models.IntegerField()
	cpu_max_freq=models.IntegerField()
	cpu_curr_temp=models.DecimalField(decimal_places=5,max_digits=10)
	cpu_high_temp=models.DecimalField(decimal_places=5,max_digits=10)
	cpu_crit_temp=models.DecimalField(decimal_places=5,max_digits=10)
