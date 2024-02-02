# In user_form/views.py

from django.http import JsonResponse
from rest_framework import status,generics
from rest_framework.response import Response
import subprocess
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer
from .tasks import send_form_submission_email, add_num



class RunCelery(APIView):
    def get(self, request, format=None):
        print("Celery started...........")
        command = ['celery', '-A', 'assignments', 'worker', '--loglevel=info']
        subprocess.run(command)
        print(f"Celery running.........")
        return JsonResponse({"status": True})

class UserFormAPIView(APIView):
    def post(self, request, format=None):
        email = request.data.get('email')
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() #signal is used to send meail
            send_form_submission_email.delay(email)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserFormListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    def get_queryset(self):
        return User.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response({
            'status': 'success',
            'message': 'Users retrieved successfully',
            'data': serializer.data
        }, status=status.HTTP_200_OK)