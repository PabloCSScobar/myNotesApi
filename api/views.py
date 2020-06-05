from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from api.models import Note
from api.serializers import UserSerializer, NoteSerializer
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    @action(detail=False, methods=['GET'])
    def get_user_info(self, request):
        # username = None
        # if request.user.is_authenticated:
        user = request.user.username
        return Response({'user': user}, status=status.HTTP_200_OK)

class NoteViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (IsAuthenticated, )


    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Note.objects.filter(owner=user)


    def create(self, request, *args, **kwargs):
        try:
            usr = request.user
            note = Note.objects.create(owner=usr, title=request.data['title'], body=request.data['body'])
            ser = NoteSerializer(note, many=False)
            response = {'message': 'New note created', 'result': ser.data}
            return Response(response, status=status.HTTP_200_OK)
        except:
            response = {'message': 'Something went wrong' }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
