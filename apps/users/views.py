from rest_framework import status, permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from apps.users.models import Doctor, Nurse
from apps.users.serializers import DoctorSerializer, NurseSerializer
from apps.users.models import IsChiefDoctorOrAdmin, IsAdminOrReadOnly

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsChiefDoctorOrAdmin]

    @action(detail=False, methods=['post'], permission_classes=[IsAdminOrReadOnly])
    def register_chief_doctor(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(is_chief_doctor=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], permission_classes=[IsChiefDoctorOrAdmin])
    def register_doctor(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NurseViewSet(viewsets.ModelViewSet):
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer
    permission_classes = [IsChiefDoctorOrAdmin]

    @action(detail=False, methods=['post'], permission_classes=[IsChiefDoctorOrAdmin])
    def register_nurse(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
