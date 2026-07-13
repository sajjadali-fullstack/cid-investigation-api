from django.shortcuts import render
from rest_framework import generics
from testapp.models import *
from testapp.serializers import *



# Create your views / business logic here 👇.


# CriminalListView
class CriminalListView(generics.ListAPIView):
    queryset = Criminal.objects.all()
    serializer_class = CriminalSerializer
    # Filter
    search_fields = ('name','alias', 'age', 'gender', 'criminal_history',) 
    ordering_fields = ('age',)



# CaseListView
class CaseListView(generics.ListAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    search_fields = ('title', 'case_number', 'description', 'location', 'officer__name',)


# EvidenceListView
class EvidenceListView(generics.ListAPIView):
    queryset = Evidence.objects.all()
    serializer_class = EvidenceSerializer

    # def get_queryset(self):
    #     qs = Evidence.objects.all()
    #     evidence = self.request.GET.get('evidence_type')

    #     if evidence is not None:
    #         qs = qs.filter(name__icontains=evidence)
    #     return qs
        # search like this : http://localhost:8000/evidences-api/?evidence=RDX Explosive Residue
    search_fields = ('evidence_type',)


# OfficerListView
class OfficerListView(generics.ListAPIView):
    queryset = Officer.objects.all()
    serializer_class = OfficerSerializer

    # def get_queryset(self):
    #     qs = Officer.objects.all()
    #     officer_name = self.request.GET.get('name')

    #     if officer_name is not None:
    #         qs = qs.filter(name__icontains=officer_name)
    #     return qs
        # search like this : http://localhost:8000/officers-api/?name=Abhijeet
    search_fields = ('name','rank', )
    



# WitnessListView
class WitnessListView(generics.ListAPIView):
    queryset = Witness.objects.all()
    serializer_class = WitnessSerializer
    search_fields = ('name', 'phone', 'statement',)


def home(request):
     context = {

        "officers": Officer.objects.count(),

        "criminals": Criminal.objects.count(),

        "cases": Case.objects.count(),

        "evidences": Evidence.objects.count(),

        "witnesses": Witness.objects.count(),

    }
     return render(request, 'testapp/home.html', context)