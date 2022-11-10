from django.db import models, transaction

from manager_for_pay import settings


class Category(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Transaction(models.Model):

    """Транзакция должна содержать в себе: сумму\*, время\*, категорию\*, организацию\*, описание. """
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    summa = models.DecimalField(default=0, max_digits=12, decimal_places=2, verbose_name='summa', null=True)
    time = models.DateTimeField(auto_now=True, verbose_name='time', null=True)
    org = models.CharField(max_length=100, verbose_name='org', null=True)
    description = models.CharField(max_length=200, verbose_name='description', null=True)


    @classmethod
    def make_transaction(cls, amount, account, user_id):
        if account.balance < amount:
            raise(ValueError('Не хватает денежных средств'))
        with transaction.atomic():
            account.balance -= amount
            account.save()
            trans = cls.objects.create(amount=amount, account=account, user_id=user_id)
        return account, trans


class Account(models.Model):
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.name}'


class Action(models.Model):
    amount = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    date = models.DateTimeField(auto_now_add=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='actions')

    def __str__(self):
        return self.account


class Transfer(models.Model):
    from_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='from_account')
    to_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='to_account')
    amount = models.DecimalField(max_digits=12, decimal_places=2, null=True)










