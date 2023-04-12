from rest_framework import serializers
from .models import User, TipoDeNota, Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'user', 'title','text']
