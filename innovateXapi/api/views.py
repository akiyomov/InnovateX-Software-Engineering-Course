from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ChatSerializer,TextSerializer
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


class TranslateView(APIView):
    def post(self, request):
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            user_message = serializer.validated_data['message']
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role":"system","content":system},
                    {"role": "user", "content": user_message}
                    ]
            )
            return Response({'reply': response['choices'][0]['message']['content']})
        else:
            print("Serializer errors:", serializer.errors) 
        return Response(serializer.errors, status=400)
    
system = "You are helpful assisstant to translate any text that required from user with asked language"

class ParaphraseView(APIView):
    def post(self, request):
        print("Received data:", request.data)  # Debugging line
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            user_message = serializer.validated_data['message']
            print("Validated message:", user_message)  # Debugging line
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are helpful to paraphrase any text that required from user with asked language"},
                    {"role": "user", "content": user_message}
                ]
            )
            return Response({'reply': response['choices'][0]['message']['content']})
        else:
            print("Serializer errors:", serializer.errors)  
        return Response(serializer.errors, status=400)

class GrammarCheckView(APIView):
    def post(self, request):
        serializer = TextSerializer(data=request.data)
        if serializer.is_valid():
            text_to_check = serializer.validated_data['text']
            response = self.check_grammar_with_gpt4(text_to_check)
            return Response(response)
        else:
            print("Serializer errors:", serializer.errors) 
        return Response(serializer.errors, status=400)

    def check_grammar_with_gpt4(self, text):
        response = openai.ChatCompletion.create(
            model="gpt-4", 
            messages=[
                {"role": "system", "content": "You are a helpful assistant tasked with checking and correcting grammar."},
                {"role": "user", "content": text},
                {"role": "assistant", "content": ""},
            ],
            response_format="json"
        )
        json_response = json.loads(response.choices[0].message['content'])
        json_en = {"en": json_response}
        return json_en
