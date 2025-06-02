from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import WeekdayInputSerializer
from .weekday_real import date_to_day

class WeekdayAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = WeekdayInputSerializer(data=request.data)
        if serializer.is_valid():
            day = serializer.validated_data['day']
            month = serializer.validated_data['month']
            year = serializer.validated_data['year'].zfill(4)

            date = f'{year}-{month}-{day}'
            try:
                output = date_to_day(date)
            except Exception as e:
                return Response({'error': f'Invalid date or server error: {str(e)}'}, status=400)

            result = {
                "day_of_the_week": output[0],
                "current_year": output[1][0][0],
                "preceeding_years": output[1][0][1],
                "preceeding_years_odds": output[1][0][2],
                "preceeding_years_odds_short": output[1][0][3],
                "current_month": output[1][1][0],
                "preceeding_months_odds": output[1][1][1],
                "current_day": output[1][2][0],
                "odd_days_upto_current_day": output[1][2][1],
                "sum_of_odd_days": {
                    "total_odd_days": output[1][3][0],
                    "sum_of_odd_days": output[1][3][1],
                    "sum_odd_days": output[1][3][2],
                    "day_of_the_week": output[1][3][3],
                }
            }
            return Response(result, status=200)
        return Response(serializer.errors, status=400)
