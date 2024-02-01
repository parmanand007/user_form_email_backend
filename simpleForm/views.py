# In user_form/views.py

from rest_framework import status,generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer
from .utils import send_form_submission_email

class UserFormAPIView(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            try:
                #we can use celery or run below function in asyncronus
                send_form_submission_email([serializer.validated_data['email']])            
            except Exception as e:
                return Response({"email":f"unsuccessful and reason is {e}","data":serializer.data},status=status.HTTP_201_CREATED)
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