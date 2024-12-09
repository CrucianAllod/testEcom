from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from forms.models import FormsTemplate
from forms.serializers import FieldSerializer

class SendFormAPI(APIView):
    @swagger_auto_schema(
        request_body=FieldSerializer(many=True),
        responses={201: openapi.Response('Created'), 400: openapi.Response('Bad Request')}
    )
    def post(self, request):
        fields_data = request.data
        validated_fields = []

        for field_data in fields_data:
            serializer = FieldSerializer(data=field_data)
            if serializer.is_valid():
                validated_fields.append(serializer.validated_data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        fields_dict = {field['name']: field['value'] for field in validated_fields}
        templates = FormsTemplate.objects.all()
        matched_template = None

        for template in templates:
            template_fields = template.fields

            if all(field in fields_dict and self.validate_field_type(fields_dict[field], template_fields[field]) for field in template_fields):
                matched_template = template.name
                break

        if matched_template:
            return Response({'template_name': matched_template}, status=status.HTTP_200_OK)

        field_types = {key: self.determine_field_type(value) for key, value in fields_dict.items()}
        return Response(field_types, status=status.HTTP_200_OK)

    def validate_field_type(self, value, field_type):
        if field_type == 'date':
            return FieldSerializer.validate_date(value)
        elif field_type == 'phone':
            return FieldSerializer.validate_phone(value)
        elif field_type == 'email':
            return FieldSerializer.validate_email(value)
        return True

    def determine_field_type(self, value):
        if isinstance(value, str):
            if FieldSerializer.validate_date(value):
                return 'date'
            elif FieldSerializer.validate_phone(value):
                return 'phone'
            elif FieldSerializer.validate_email(value):
                return 'email'
        return 'text'