
from rest_framework import permissions, viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Transaction, Account
from .serializer import TransactionSerializer, AccountSerializer


class TransactionListView(APIView, mixins.DestroyModelMixin,
                          mixins.ListModelMixin,
                          mixins.CreateModelMixin,
                          mixins.UpdateModelMixin):
    permission_classes = [permissions.IsAuthenticated] # Разрешения только авторизованным
    """Вывод транзакции"""
    def get(self, request):
        transaction = Transaction.objects.get()
        serializer = TransactionSerializer(transaction, many=False)
        return Response(serializer.data)


class AccountViewSet(viewsets.GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin):
    serializer_class = AccountSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    queryset = Account.objects.all()

    def perfom_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_query_set(self):
        return self.queryset.filter(user=self.request.user)


