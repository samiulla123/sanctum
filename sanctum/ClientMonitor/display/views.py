from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import NetworkStatus,ClientInfo,Clients
from .serializers import NetworkStatusSerializer,ClientsSerializer,ClientInfoSerializer,MemSerializer,NetSerializer,DiskSerializer,CPUSerializer
from rest_framework.renderers import TemplateHTMLRenderer
import logging
from rest_framework.parsers import JSONParser
from uuid import uuid4
import uuid
def index(request):
        return HttpResponse('<h1>Hey!</h1>')


class NetworkStatusController(APIView):
        renderer_classes = [TemplateHTMLRenderer]
        template_name = 'test_display.html'
        def get(self,request):
                hns=NetworkStatus.objects.all()
                # sr=NetworkStatusSerializer(hns,many=True)
                return Response({'vals':hns})
                # return render(request,'test_display.html',dict(json.dumps(sr.data)))

        def post(self,request):
                sr=NetworkStatusSerializer(data=request.data)
                if sr.is_valid():
                        sr.save()
                        return Response(sr.data)

class ClientsAPIController(APIView):
        def get(self,request):
                hns=Clients.objects.all()
                sr=ClientsSerializer(hns,many=True)
                # return Response(sr.data)
                return JsonResponse({'vals':sr.data})


class ClientsController(APIView):
        renderer_classes = [TemplateHTMLRenderer]
        template_name = 'index.html'
        def get(self,request):
                hns=Clients.objects.all()
                sr=ClientsSerializer(hns,many=True)
                # return Response(sr.data)
                return Response({'vals':sr.data})


        def post(self,request):
                # logging.error(list(Clients.objects.all())[0])
                data=request.data
                sr=ClientsSerializer(data=data)
                logging.error(data)
                if sr.is_valid():
                        sr.save()
                        # logging.error(Clients.objects.all())
                        cid=Clients.objects.all().filter(c_mac=data['c_mac'])
                        logging.error(cid[0].c_mac)
                        # logging.error(type(cid[0]))
                        # return Response(cid[0].c_id.value(),status=200)
                        return JsonResponse({'id':cid[0].c_id})
                        return Response({'id':cid[0].c_id},status=200)
                return Response(status=400)

class ClientInfoController(APIView):
        renderer_classes = [TemplateHTMLRenderer]
        template_name = 'clientinfo.html'
        def get(self,request):
                hns=ClientInfo.objects.all()
                # sr=ClientInfoSerializer(hns,many=True)
                # return Response(sr.data)
                return Response({'vals':hns})

        def post(self,request):
                sr=ClientInfoSerializer(data=request.data)
                logging.error(request.data)
                logging.error(sr.is_valid())
                if sr.is_valid():
                        sr.save()
                        return Response(sr.data)
                return Response(status=400)

class SysStatController(APIView):
      
        #         data cid valid or not :
        #                 token valid;
        #                         dict(request.data)
        #                                 for k,v in dict:
        #                                         if k=meminfo:
        #                                                 MeminfSerializer(v)




        def post(self,request):
                import json
                # d=json.dumps()
                jsn=json.loads(request.body.decode())
                # logging.error(jsn)
                #add c_token later *****************************************dd.is_valid()
                if Clients.objects.all().filter(c_id=jsn['c_id']).exists():
                        js=jsn['payload']
                        mem=js['mem']
                        net=js['net']
                        disk=js['disk']
                        cpu=js['cpu']
                        mem['c_id']=jsn['c_id']
                        net['c_id']=jsn['c_id']
                        disk['c_id']=jsn['c_id']
                        cpu['c_id']=jsn['c_id']
                        logging.error(disk)
                        logging.error(mem)
                        logging.error(cpu)
                        logging.error(net)
                        nd=NetSerializer(data=net)
                        dd=DiskSerializer(data=disk)
                        cd=CPUSerializer(data=cpu)
                        md=MemSerializer(data=mem)
                        logging.error(nd.is_valid())
                        logging.error(dd.is_valid())
                        logging.error(cd.is_valid())
                        logging.error(md.is_valid())
                        if nd.is_valid() and dd.is_valid() and  cd.is_valid() and md.is_valid():
                                nd.save()
                                dd.save()
                                cd.save()
                                md.save()
                                return Response(status=200)

                return Response(status=400)
