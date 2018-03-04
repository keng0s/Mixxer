from rest_framework import serializers
import json


class JSONField(serializers.Field):
    def to_representation(self, value):
        return json.loads(value)
