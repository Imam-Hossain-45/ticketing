from rest_framework.views import APIView
from dh_test.models import AndroidTestUser, AndroidTestScanLog
from dh_test.serializers import ScanQRSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from datetime import datetime
from django.conf import settings


class ScanQRView(APIView):
    """
    Scan QR code
    Url: /api/test/android/get-user-info/
    """

    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = ScanQRSerializer

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        serializer = ScanQRSerializer(data=data)

        if serializer.is_valid():
            ticket_id = serializer.validated_data['ticket_id']
            if AndroidTestUser.objects.filter(ticket_id=ticket_id).exists():
                validity = 'valid'
                json_data = {'ticket_validity': validity}
                user = AndroidTestUser.objects.get(ticket_id=ticket_id)
                json_data.update({
                    'name': user.name,
                    'email': user.email,
                    'phone': user.phone,
                    'date_of_birth': user.date_of_birth,
                })
                if user.profile_picture in ['', None]:
                    json_data['profile_picture'] = None
                else:
                    json_data['profile_picture'] = settings.MEDIA_URL_HEADER + str(user.profile_picture)
                status = HTTP_200_OK

            else:
                validity = 'invalid'
                json_data = {'ticket_validity': validity}
                status = HTTP_404_NOT_FOUND

            AndroidTestScanLog.objects.create(
                ticket_id=ticket_id, scan_date=datetime.today(), scan_time=datetime.now().time(), status=validity
            )

        else:
            json_data = {'ticket_validity': 'invalid'}
            status = HTTP_400_BAD_REQUEST

        return Response(json_data, status=status)


class ScanLogListView(APIView):
    """
        Scan QR code
        Url: /api/test/android/scan-log/
    """

    permission_classes = [AllowAny]

    def get(self, request, format=None, **kwargs):
        data_list = []
        print(AndroidTestScanLog.objects.all().count())
        if AndroidTestScanLog.objects.all().count() > 0:
            logs = AndroidTestScanLog.objects.all().order_by('-scan_date', '-scan_time')
            print(logs)
            for log in logs:
                print(log)
                # data_list.append(
                #     {
                #         'ticket_id': log.ticket_id,
                #         'scan_date': log.scan_date,
                #         'scan_time': log.scan_time,
                #         'status': log.status,
                #     }
                # )

        return Response(data_list, status=HTTP_200_OK)

