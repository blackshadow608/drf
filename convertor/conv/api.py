from rest_framework import generics, status

from convertor.conv.serializer import UrlSerializer, FileSerializer
from convertor.conv.utils import pdf_converter, prepare_file_response


class ConverterUrlAPI(generics.GenericAPIView):
    serializer_class = UrlSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        pdf = pdf_converter(serializer.validated_data['url'], content_type='url')
        response = prepare_file_response(file=pdf)
        return response


class ConverterFileAPI(generics.GenericAPIView):
    serializer_class = FileSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file_obj = request.FILES['file']
        pdf = pdf_converter(file_obj.read().decode('utf-8'), content_type='string')
        response = prepare_file_response(file=pdf)

        return response
