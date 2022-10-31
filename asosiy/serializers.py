from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from .models import *


class SuvSerializer(ModelSerializer):
    class Meta():
        model=Suv
        fields='__all__'

class MijozSerializer(ModelSerializer):
    class Meta():
        model=Mijoz
        fields='__all__'
    def validate_qarz(self, qiymat):
        if qiymat>500000:
            raise ValidationError("Qarzingiz juda ko'p")
        return qiymat

class AdminSerializer(ModelSerializer):
    class Meta():
        model=Admin
        fields='__all__'

class HaydovchiSerializer(ModelSerializer):
    class Meta():
        model=Haydovchi
        fields='__all__'

class BuyurtmaSerializer(ModelSerializer):
    class Meta():
        model=Buyurtma
        fields='__all__'

