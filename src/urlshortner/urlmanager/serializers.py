from rest_framework import serializers
import random
from .models import UrlModel

class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlModel
        fields = '__all__'

    def generate_short_url(self, url , length = 6):
        string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        return "".join(random.choice(string) for i in range(length))

    def create(self, validated_data):
        print(validated_data['url'])
        try:
            urls = validated_data['url']
            short_url = self.generate_short_url(urls)
            validated_data['short_url'] = short_url
            return UrlModel.objects.create(**validated_data)
        except Exception as e:
            return e