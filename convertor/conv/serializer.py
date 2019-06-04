import re

import requests
from requests.exceptions import MissingSchema, ConnectionError, RequestException
from rest_framework import serializers


class UrlSerializer(serializers.Serializer):
    url = serializers.CharField()

    def validate_url(self, url):
        regexp = r'^https?://'
        if not re.match(regexp, url):
            raise serializers.ValidationError("Request exception. Url should start with http(s)://.")
        try:
            response = requests.head(url)
        except RequestException:
            raise serializers.ValidationError("Request exception. Url is incorrect or unavailable.")
        if response.status_code >= 400:
            raise serializers.ValidationError("Url is unavailable. Response code {}".format(response.status_code))
        return url


class FileSerializer(serializers.Serializer):
    file = serializers.FileField()
