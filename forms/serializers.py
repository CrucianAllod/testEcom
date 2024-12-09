from rest_framework import serializers
from datetime import datetime
from phonenumbers import parse, is_valid_number
from email.utils import parseaddr


class FieldSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    value = serializers.CharField()

    def validate(self, data):
        field_value = data.get('value')
        field_name = data.get('name')

        field_type = self.determine_field_type(field_value)

        if field_type == 'date':
            if not self.validate_date(field_value):
                raise serializers.ValidationError(f"Поле {field_name} должно быть корректной датой.")
        elif field_type == 'phone':
            if not self.validate_phone(field_value):
                raise serializers.ValidationError(f"Поле {field_name} должно быть корректным номером телефона.")
        elif field_type == 'email':
            if not self.validate_email(field_value):
                raise serializers.ValidationError(f"Поле {field_name} должно быть корректным email.")

        return data

    @staticmethod
    def validate_date(value):
        try:
            datetime.strptime(value, '%d.%m.%Y')
            return True
        except ValueError:
            try:
                datetime.strptime(value, '%Y-%m-%d')
                return True
            except ValueError:
                return False

    @staticmethod
    def validate_phone(value):
        value = value.strip()
        try:
            return is_valid_number(parse(value, region='RU'))
        except Exception:
            return False

    @staticmethod
    def validate_email(value):
        name, addr = parseaddr(value)
        return addr and '@' in addr

    def determine_field_type(self, value):
        if isinstance(value, str):
            if self.validate_date(value):
                return 'date'
            elif self.validate_phone(value):
                return 'phone'
            elif self.validate_email(value):
                return 'email'
        return 'text'