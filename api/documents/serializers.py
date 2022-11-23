from rest_framework import serializers
from .models import Users, Documents, Repositories


class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'email', 'date_joined')
        read_only_fields = ('date_joined',)


class DocumentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = ('id', 'name', 'data', 'rep_id', 'added_at')
        read_only_fields = ('added_at', 'id',)


class RepositoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Repositories
        fields = ('id', 'name', 'created_at', 'owner')
        read_only_fields = ('created_at', 'id',)
