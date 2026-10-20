from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from . serializers import UserSerializer
from rest_framework.decorators import api_view
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode


class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many = True)
        return Response(serializer.data)
        
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            activation_link = f"http://localhost:8000/api/users/activate/{user.id}/"
            subject = "Confirmez votre compte"
            message = f"""
            Bonjour {user.username},

            Merci de vous être inscrit. Veuillez cliquer sur le lien suivant pour activer votre compte :
            {activation_link}

            Merci !
            """
            # Envoi de l'email
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,  # Si l'email échoue, une exception est levée
            )
            return Response({"message": "Utilisateur créé. Vérifiez votre email pour activer votre compte."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
# Vue pour activer un compte utilisateur
@api_view(['GET'])
def ActivateUserView(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if user.is_active:
        return Response({
            "status": False,
            "message": "The account is already activated."
        })

    user.is_active = True
    user.save()

    return Response({
        "status": True,
        "message": "Your account has been successfully activated. You can now log in."
    })

# requete pour reinitialiser le mot de pass
@api_view(['POST'])
def RequestPassworReset(request):
    email = request.data.get("email")

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({
            "message": "If the email exists in our records, a password reset link will be sent."
        }, status=status.HTTP_200_OK)
        
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(str(user.pk).encode())

    reset_link = f"http://localhost:8000/api/users/reset/{uid}/{token}/"

    subject = "Password Reset Request"
    message = f"Click the link below to reset your password:\n\n{reset_link}"
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [email],
    )

    return Response({
        "message": "If the email exists in our records, a password reset link will be sent."
    }, status=status.HTTP_200_OK)
    

# reinitialiser le mot de pass
@api_view(['POST'])
def ResetPassword(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(id=uid)
    except (TypeError, ValueError, User.DoesNotExist):
        return Response({"message": "Invalid link or user"}, status=status.HTTP_400_BAD_REQUEST)

    if not default_token_generator.check_token(user, token):
        return Response({"message": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)

    new_password = request.data.get("new_password")
    if not new_password:
        return Response({"message": "Password is required"}, status=status.HTTP_400_BAD_REQUEST)

    user.set_password(new_password)
    user.save()

    return Response({
        "message": "Password has been reset successfully."
    }, status=status.HTTP_200_OK)