from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView
from system.serializers import UserSerializer,TicketSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions,authentication
from system.permissions import OwnerOnly
from system.models import Ticket
# Create your views here.
class Register(CreateAPIView):
    serializer_class=UserSerializer

class Logout(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def post(self,request):
        request.auth.delete()

        return Response({"msg":"Logout SuccessFull"})
    
class TicketCreateList(ListCreateAPIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[OwnerOnly]

    serializer_class=TicketSerializer

    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user)

    queryset=Ticket.objects.all()

class TicketUpdateDeleteRetrieve(RetrieveUpdateDestroyAPIView):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[OwnerOnly]

    serializer_class=TicketSerializer

    queryset=Ticket.objects.all()

class TicketSummary(APIView):
    def get(self,request):
        
        
        open=Ticket.objects.filter(status='open').count()
        progres=Ticket.objects.filter(status='in_progress').count()
        resolved=Ticket.objects.filter(status='resolved').count()
        total=open+progres+resolved


        return Response({"Open":open,"in_progress":progres,"Resolved":resolved,"total":total})
