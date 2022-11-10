from rest_framework import serializers

from .models import Transaction, Category, Account, Action


class TransactionSerializer(serializers.ModelSerializer):
    '''Список трансзаций в формате JSON'''

    class Meta:

        model = Transaction
        fields = '__all__'


# class UserSerializer(serializers.ModelSerializer):
#     '''Список users в формате JSON'''
#
#     class Meta:
#         model = User
#         fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    '''Список category в формате JSON'''

    class Meta:
        model = Category
        fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):
    '''Список Account в формате JSON'''

    class Meta:
        model = Account
        fields = '__all__'


class ActionSerializer(serializers.ModelSerializer):
    '''Список Action в формате JSON'''

    class Meta:
        model = Action
        fields = '__all__'


class TransferSerializer(serializers.ModelSerializer):
    '''Список Transfer в формате JSON'''

    class Meta:
        model = Action
        fields = '__all__'