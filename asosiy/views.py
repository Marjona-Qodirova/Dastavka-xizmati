from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *


class SuvlarAPI(APIView):
    def get(self, request):
        suvlar=Suv.objects.all()
        ser=SuvSerializer(suvlar, many=True)
        return Response(ser.data)
    def post(self, request):
        suv=request.data()
        ser=SuvSerializer(suv)
        if ser.is_valid():
            ser.save()
            return Response({"xabar:":"Malumot qo'shildi",  "malumot": ser.data})
        return Response({"xabar:": "Malumot qo'shilmadi"})
class SuvAPI(APIView):
    def get(self, request, pk):
        suv = Suv.objects.get(id=pk)
        ser = SuvSerializer(suv)
        return Response(ser.data)

    def put(self, request, pk):
        suv = Suv.objects.get(id=pk)
        ser = SuvSerializer(suv, request.data)
        if ser.is_valid():
            ser.save()
            return Response({"xabar": "Ma'lumot ozgardi", "malumot": ser.data})
        return Response({"xabar": "Ma'lumot ozgarmadi"})





class MijozlarAPI(APIView):
    def get(self, request):
        mijozlar=Mijoz.objects.all()
        ser=MijozSerializer(mijozlar, many=True)
        return Response(ser.data)
    def post(self, request):
        mijoz=request.data()
        ser=MijozSerializer(mijoz)
        if ser.is_valid():
            ser.save()
            return Response({"xabar:":"Malumot qo'shildi" }, ser.data)
        return Response({"xabar:": "Malumot qo'shilmadi"})


class MijozAPI(APIView):
    def get(self, request, pk):
        mijoz = Mijoz.objects.get(id=pk)
        ser = MijozSerializer(mijoz)
        return Response(ser.data)

    def put(self, request, pk):
        mijoz= Mijoz.objects.get(id=pk)
        ser = SuvSerializer(mijoz, request.data)
        if ser.is_valid():
            ser.save()
            return Response({"xabar": "Ma'lumot ozgardi", "malumot": ser.data})
        return Response({"xabar": "Ma'lumot ozgarmadi"})


class BuyurtmalarAPI(APIView):
    def get(self, request):
        buyurtmalar=Buyurtma.objects.all()
        ser=BuyurtmaSerializer(buyurtmalar, many=True)
        return Response(ser.data)
    def post(self, request):
        buyurtma=request.data()
        ser=BuyurtmaSerializer(buyurtma)
        if ser.is_valid():
            ser.save()
            return Response({"xabar:":"Malumot qo'shildi" }, ser.data)
        return Response({"xabar:": "Malumot qo'shilmadi"})











class HaydovchilarViewSet(ModelViewSet):
    serializer_class = HaydovchiSerializer
    permission_classes = [IsAuthenticated, ]
    @action(methods=['GET'], detail=True)



class AdminlarViewSet(ModelViewSet):
    serializer_class = AdminSerializer
    permission_classes = [IsAuthenticated, ]
