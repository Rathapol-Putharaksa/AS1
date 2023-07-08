from rest_framework import serializers
from .models import Todo


class TodoListSerializer(serializers.ModelSerializer):


    class Meta:
        model = Todo
        fields = ('id','title', 'description','start_date','due_date','complete')