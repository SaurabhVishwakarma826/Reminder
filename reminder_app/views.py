from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .serializers import ReminderSerializer, UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.generics import ListAPIView
from .models import Reminder

class RegisterUserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginUserAPIView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        return Response({"error": "Invalid credentials"}, status=401)

class ReminderAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def send_email_reminder(self, reminder):
        sender_email = "your_email@example.com"  # Enter your email address
        receiver_email = reminder.email
        message = MIMEText(reminder.message)
        message['Subject'] = "Reminder"
        message['From'] = sender_email
        message['To'] = receiver_email

        with smtplib.SMTP('smtp.example.com', 587) as server:  # Enter your SMTP server
            server.starttls()
            server.login(sender_email, "your_password")  # Enter your email password
            server.sendmail(sender_email, receiver_email, message.as_string())

    def post(self, request):
        serializer = ReminderSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            reminder = serializer.save(user=request.user)  # Associate the reminder with the authenticated user
            # Schedule email reminder
            # reminder_datetime = datetime.combine(reminder.date, reminder.time)
            # current_datetime = datetime.now()
            # time_difference_seconds = (reminder_datetime - current_datetime).total_seconds()
            # if time_difference_seconds > 0:
            #     threading.Timer(time_difference_seconds, self.send_email_reminder, args=[reminder]).start()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReminderListView(ListAPIView):
    serializer_class = ReminderSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return Reminder.objects.filter(user=user)