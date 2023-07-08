from django.shortcuts import render
from todo.models import Todo
from todo.serializers import TodoListSerializer
from rest_framework import generics,status  
from rest_framework.response import Response  
from django.shortcuts import get_object_or_404  

from rest_framework.decorators import api_view





@api_view(["POST"])
def post(request):  
    serializer = TodoListSerializer(data=request.data)  
    if serializer.is_valid():  
        serializer.save()  
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
    else:  
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
@api_view(["GET"])
def get(request):  
    result = Todo.objects.all()  
    serializers = TodoListSerializer(result,many=True)  
    return Response({'status': 'success', "data":serializers.data}, status=200)

@api_view(['PUT'])
def update(request, id):
    newData = Todo.objects.get(id=id)
    serializers = TodoListSerializer(instance=newData, data=request.data,partial=True)

    if serializers.is_valid():
        serializers.save()
        return Response({"status": "success", "data": serializer.data})

    else:
        return Response({"status": "error", "data": serializer.errors})


@api_view(['DELETE'])
def delete(request, id):

    deleteData = get_object_or_404(Todo,id=id)
    deleteData.delete()
    return Response({"status": "success", "data": "Record Deleted"}) 




  
  
  

       




