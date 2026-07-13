from rest_framework.serializers import ModelSerializer
from testapp.models import Criminal, Case, Evidence, Officer, Witness



# CriminalSerializer
class CriminalSerializer(ModelSerializer):
    class Meta:
        model = Criminal
        fields = '__all__'


#  CaseSerializer    
class CaseSerializer(ModelSerializer):
    class Meta:
        model = Case
        fields = '__all__'


# EvidenceSerializer
class EvidenceSerializer(ModelSerializer):
    class Meta:
        model = Evidence
        fields = '__all__'



# OfficerSerializer
class OfficerSerializer(ModelSerializer):
    class Meta:
        model = Officer
        fields = '__all__'



# WitnessSerializer
class WitnessSerializer(ModelSerializer):
    class Meta:
        model = Witness
        fields = '__all__'
