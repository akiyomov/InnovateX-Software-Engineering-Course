from rest_framework import serializers

class ChatSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=2000)

class TextSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=10000) 
