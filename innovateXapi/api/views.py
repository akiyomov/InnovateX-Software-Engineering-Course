from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ChatSerializer
import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

class ChatView(APIView):
    def post(self, request):
        print("Received data:", request.data)  # Debugging line
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            user_message = serializer.validated_data['message']
            print("Validated message:", user_message)  # Debugging line
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_message}]
            )
            return Response({'reply': response['choices'][0]['message']['content']})
        else:
            print("Serializer errors:", serializer.errors)  # Debugging line
        return Response(serializer.errors, status=400)

