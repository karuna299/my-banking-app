import pytest
from mybank import BankAccount

def test_deposit():

    account = BankAccount(balance=150)

    account.deposit(50)

    assert account.balance == 200

def test_withdrawal_sufficent_amount():

    account = BankAccount(balance=150)

    account.withdrawal(30)

    assert account.balance == 120

def test_withdrawal_insufficent_amount():

    account = BankAccount(balance=150)

    with pytest.raises(ValueError, match="Insufficent Funds")
      account.withdrawal(200)
