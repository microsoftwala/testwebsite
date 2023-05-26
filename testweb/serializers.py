from rest_framework import serializers
from testweb.models import Test

# create serailizers here
class TestSerializer(serializers.HyperlinkedModelSerializer):
    qno = serializers.ReadOnlyField()
    class Meta:
        model = Test
        fields = '__all__'