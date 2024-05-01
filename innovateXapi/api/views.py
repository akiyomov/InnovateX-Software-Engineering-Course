from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ChatSerializer, TextSerializer
import openai
from django.conf import settings

# Set the API key for the OpenAI service
openai.api_key = settings.OPENAI_API_KEY

class ChatView(APIView):
    """
    API View to handle chat interactions using OpenAI's ChatCompletion.
    """
    def post(self, request):
        """
        Receives a POST request with a user message, processes it through the GPT-3.5-turbo model,
        and returns the AI-generated response.
        """
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
    """
    API View to handle requests to translate text using OpenAI's GPT-4 model.
    """
    def post(self, request):
        """
        Receives a POST request with text, translates it using the GPT-4 model, and returns the translation.
        """
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            user_message = serializer.validated_data['message']
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role":"system", "content": system},
                    {"role": "user", "content": user_message}
                ]
            )
            return Response({'reply': response['choices'][0]['message']['content']})
        else:
            print("Serializer errors:", serializer.errors) 
        return Response(serializer.errors, status=400)

system = "You are helpful assistant to translate any text that required from user with asked language"

class ParaphraseView(APIView):
    """
    API View to handle requests to paraphrase text using the GPT-3.5-turbo model.
    """
    def post(self, request):
        """
        Receives a POST request with text, paraphrases it using the GPT-3.5-turbo model, and returns the paraphrased text.
        """
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            user_message = serializer.validated_data['message']
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
    """
    API View to handle grammar checking requests using OpenAI's GPT-4 model.
    """
    def post(self, request):
        """
        Receives a POST request with text, checks and corrects grammar using the GPT-4 model,
        and returns the corrected text.
        """
        serializer = TextSerializer(data=request.data)
        if serializer.is_valid():
            text_to_check = serializer.validated_data['text']
            response = self.check_grammar_with_gpt4(text_to_check)
            return Response(response)
        else:
            print("Serializer errors:", serializer.errors) 
        return Response(serializer.errors, status=400)

    def check_grammar_with_gpt4(self, text):
        """
        Uses the GPT-4 model to check and correct grammar in the provided text.
        """
        response = openai.ChatCompletion.create(
            model="gpt-4", 
            messages=[
                {"role": "system", "content": "You are a helpful assistant tasked with checking and correcting grammar."},
                {"role": "user", "content": text},
                {"role": "assistant", "content": ""},
            ],
        )
        return response['choices'][0]['message']['content']
