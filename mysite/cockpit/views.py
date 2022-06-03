from django.shortcuts import render
import json

# Create your views here.
from django.http import HttpResponse, JsonResponse
from kubernetes import client, config
from rest_framework.decorators import api_view

# def index(request):
#     config.load_kube_config()
#     v1 = client.CoreV1Api()
#     print("Listing pods with their IPs:")
#     ret = v1.list_pod_for_all_namespaces(watch=False)
#     for i in ret.items:
#         demo=print("%s\t%s" % (i.metadata.namespace, i.metadata.name))
#         return HttpResponse(demo)

# Configs can be set in Configuration class directly or using helper utilitys
@api_view(['GET'])
def getpods(request):
    if request.method == 'GET':
        config.load_kube_config()
        v1 = client.CoreV1Api()
        ret = v1.list_pod_for_all_namespaces(watch=False)
        data={}
        data2=[]
        for i in ret.items:
            # data["name"] = i.metadata.name
            # data["namepsace"] = i.metadata.namespace
            data={
                "name": i.metadata.name,
                "namespace": i.metadata.namespace
            }
            data2.append(data)
            print(data2)
        return HttpResponse(json.dumps(data2, indent=4))



# [
#     {
#         "name": <name>,
#         "namespace"": <ns>
#     }
# ]