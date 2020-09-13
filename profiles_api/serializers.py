from rest_framework import serializers

'''same as forms.py'''
class HelloSerializer(serializers.Serializer):
    """ Serializes a name field for testing an APIview"""
    name = serializers.CharField(max_length=10)
    




##
