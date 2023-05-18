from django.db import models
from constant import ENGLISH_SPEAKER ,SEMESTER ,CLASS_ATTRIBUTE
from django.core.exceptions import ValidationError
import uuid
# Create your models here.
from django.contrib.auth import get_user_model

def validate_course_instructor(value):
    if value>25 or value<0:
        raise ValidationError('invalid course instructor')
def validate_course(value):
    if value>26 or value<0:
        raise ValidationError('invalid course')

User=get_user_model()
class TA(models.Model):
    ta_id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    native_english_speaker= models.CharField(choices=[(e.value, e.value) for e in ENGLISH_SPEAKER],max_length=50)

    course_instructor=models.IntegerField(validators=[validate_course_instructor])
    course=models.IntegerField(validators=[validate_course])
    semester=  models.CharField(choices=[(e.value, e.value) for e in SEMESTER],max_length=50)
    class_size=models.IntegerField()
    performance_score=models.CharField(choices=[(e.value, e.value) for e in CLASS_ATTRIBUTE],max_length=50)

    created_by=models.ForeignKey(User,on_delete=models.CASCADE,blank= True,null=True ,related_name='ta_created_by')

    created_at=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,blank=True,null=True)
    
