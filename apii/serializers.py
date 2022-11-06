from rest_framework import serializers
from apii.models import book



#create serializers here
class bookSerializer(serializers.HyperlinkedModelSerializer):
    book_id=serializers.ReadOnlyField()
    class Meta:
        model=book
        fields="__all__"
        
        
        
