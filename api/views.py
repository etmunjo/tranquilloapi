from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

import api
from .serializers import TaskSerializer
from .models import Task

@api_view(['GET'])

def getRoutes(request):
    routes = [
        {
            'Endpoint': '/Tasks/',
            'method': 'GET',
            'body': 'none',
            'description': 'Returns and Array of Notes'
        },
        {
            'Endpoint': '/Tasks/id',
            'method': 'GET',
            'body': 'none',
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/Tasks/id/create',
            'method': 'GET',
            'body': 'none',
            'description': 'Creates Note'
        },
        {
            'Endpoint': '/Tasks/id/update',
            'method': 'GET',
            'body': 'none',
            'description': 'Updates Note'
        },
        {
            'Endpoint': '/Tasks/id/delete',
            'method': 'GET',
            'body': 'none',
            'description': 'Deletes Note'
        },
        {
            'Endpoint': '/Profile/',
            'method': 'GET',
            'body': 'none',
            'description': 'returns an array of profiles',
        },
        {
            'Endpoint': '/Profile/id/',
            'method': 'GET',
            'body': 'none',
            'description': 'returns a single profile object',
        },
        {
            'Endpoint': '/Profile/id/create',
            'method': 'GET',
            'body': 'none',
            'description': 'creates profile',
        },
        {
            'Endpoint': '/Profile/id/update',
            'method': 'GET',
            'body': 'none',
            'description': 'updates profile',
        },
        {
            'Endpoint': '/Profile/id/delete',
            'method': 'GET',
            'body': 'none',
            'description': 'deletes profile',
        },
    ]
# Create your views here.
    return Response(routes)


@api_view(['GET'])
def getTasks (request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getTask (request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def createTask(request):
    data = request.data 
    task = Task.objects.create(
        body=data['body']
    )
    serializer = TaskSerializer(task, many = False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateTask(request, pk):
    data = request.data 
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response('Note was deleted.')