import json
import time
import datetime
import threading
import requests

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from .models import Task, TaskHistory, Service

from .serializers import TaskSerializer, ServiceSerializer


def send_api_request(*kwargs):
    print("I am here in function")
    try:
        url = kwargs[1]
        if kwargs[0] == 2:
            time.sleep(
                datetime.datetime.strptime(kwargs[2], "%Y-%m-%d %H:%M:%S").timestamp() -
                datetime.datetime.now().timestamp())
            print(datetime.datetime.now().timestamp() -
                  datetime.datetime.strptime(kwargs[2], "%Y-%m-%d %H:%M:%S").timestamp())
            response = requests.post(url=url, json=kwargs[4])
            obj = Task.objects.get(id=kwargs[3])
            obj.task_status = 2
            obj.save(update_fields=['task_status'])
            obj1 = TaskHistory.objects.create(task=obj, response=str(response))
            obj1.save()
            print(response.json())
        elif kwargs[0] == 1:
            time.sleep(
                datetime.datetime.strptime(kwargs[2],
                                           "%Y-%m-%d %H:%M:%S").timestamp() - datetime.datetime.now().timestamp()
            )

            response = requests.get(url=url)
            obj = Task.objects.get(id=kwargs[3])
            obj.task_status = 2
            obj.save(update_fields=['task_status'])
            obj1 = TaskHistory.objects.create(task=obj, response=str(response))
            obj1.save()
            print(response.json())
    except Exception as e:
        print(e)
    print("function ended")


class TaskCreateAPIView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def post(self, request, *args, **kwargs):
        serializer = TaskSerializer(data=request.data)
        print(request.data)
        print("I am here in post")
        if serializer.is_valid():
            print("I am valid")
            serializer.save()

            if request.data.get('type') == 2:
                threaded = threading.Thread(target=send_api_request, args=(request.data.get('request_type'),
                                                                           request.data.get('request_url'),
                                                                           request.data.get('datatime'),
                                                                           serializer.data.get('id'),
                                                                           request.data.get('request_body')))

            else:
                threaded = threading.Thread(target=send_api_request, args=(request.data.get('request_type'),
                                                                           request.data.get('request_url'),
                                                                           request.data.get('datatime'),
                                                                           serializer.data.get('id')))
            threaded.start()
            print("started")

            return Response("ok", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        objects = Task.objects.all()
        serializer = TaskSerializer(objects, many=True)
        return Response(serializer.data)


class ServiceAPIView(ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def post(self, request, *args, **kwargs):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def get(self, request, *args, **kwargs):
        objects = Service.objects.all()
        serializer = ServiceSerializer(objects, many=True)
        return Response(serializer.data)
