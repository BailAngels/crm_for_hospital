from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from apps.users.models import Doctor, Nurse
from apps.users.serializers import DoctorSerializer, NurseSerializer, ChiefDoctorRegistrationSerializer, DoctorRegistrationSerializer, NurseRegistrationSerializer
from apps.users.models import IsChiefDoctorOrReadOnly, IsAdminOrReadOnly

class ChiefDoctorRegistrationView(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def post(self, request):
        serializer = ChiefDoctorRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DoctorRegistrationView(APIView):
    permission_classes = [IsChiefDoctorOrReadOnly]

    def post(self, request):
        serializer = DoctorRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NurseRegistrationView(APIView):
    permission_classes = [IsChiefDoctorOrReadOnly]

    def post(self, request):
        serializer = NurseRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    # permission_classes = [IsChiefDoctorOrReadOnly]

class NurseViewSet(viewsets.ModelViewSet):
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer
    permission_classes = [IsChiefDoctorOrReadOnly]
