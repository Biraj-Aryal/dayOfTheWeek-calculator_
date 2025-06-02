# weekday/serializers.py
from rest_framework import serializers

class WeekdayInputSerializer(serializers.Serializer):
    day = serializers.IntegerField(min_value=1, max_value=31)
    month = serializers.IntegerField(min_value=1, max_value=12)
    year = serializers.CharField(max_length=4)  # String because you zfill it
