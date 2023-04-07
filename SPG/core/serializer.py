from rest_framework import serializers
from django.contrib.auth import get_user_model
from assitant.models import TA
from assitant.serializer import TAserializer
User=get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email','password',"first_name","last_name"]
        extra_kwargs={
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }
    def create(self,validated_data):
        user=User.objects.create_user(**validated_data)
        return user

class UserSerializer(serializers.ModelSerializer):
    ta=serializers.SerializerMethodField()
    class Meta:
        model=User
        exclude=['password']
    
    def get_ta(self,obj):
        ta=TA.objects.filter(created_by=obj)
        serializer=TAserializer(ta,many=True)
        return serializer.data