from rest_framework import serializers
from patient.models import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name', 'identity_document_number', 'date_of_birth']