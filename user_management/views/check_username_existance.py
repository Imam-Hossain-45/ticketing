from rest_framework.views import APIView
from user_management.models import User
from user_management.serializers import VisitorRegistrationUsernameCheckSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT


class VisitorRegistrationUsernameCheckView(APIView):
    """
    Check Username already exists or not

    Url: /user/username-check/
    """

    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = VisitorRegistrationUsernameCheckSerializer

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        serializer = VisitorRegistrationUsernameCheckSerializer(data=data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            json_data = {'valid_form': 'valid'}
            if User.objects.filter(username=username).exists():
                json_data.update({'username': True})
                json_data.update({'message': 'Username already exist'})
                return Response(json_data, status=HTTP_409_CONFLICT)
            else:
                json_data.update({'username': False})
                json_data.update({'message': 'Username is allowed to proceed'})
                return Response(json_data, status=HTTP_200_OK)
        json_data = {'valid_form': 'invalid', 'username': False, 'message': 'Invalid form'}
        return Response(json_data, status=HTTP_400_BAD_REQUEST)
