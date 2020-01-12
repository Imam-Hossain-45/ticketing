from django.core import serializers
import json


def json_formatter(data_obj=None, fields=None):
    if fields:
        data = json.loads(
            serializers.serialize('json', [data_obj], fields=fields)
        )[0]
        formatted_data = {field: data['fields'].get(field) for field in fields}
    else:
        data = json.loads(
            serializers.serialize('json', [data_obj])
        )[0]
        formatted_data = data
    return formatted_data
