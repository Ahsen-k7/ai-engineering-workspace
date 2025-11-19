from bank_account import BankAccount
import pytest

def test_initial_balance():
    account = BankAccount("Ahsen", 100)
    assert account.balance == 100

def test_deposit():
    account = BankAccount("Ahsen", 100)
    account.deposit(50)
    assert account.balance == 150

def test_deposit_invalid():
    account = BankAccount("Ahsen", 100)
    with pytest.raises(ValueError):
        account.deposit(0)

def test_withdraw():
    account = BankAccount("Ahsen", 100)
    account.withdraw(40)
    assert account.balance == 60

def test_withdraw_insufficient():
    account = BankAccount("Ahsen", 50)
    with pytest.raises(ValueError):
        account.withdraw(100)

def test_get_balance():
    account = BankAccount("Ahsen", 200)
    assert account.get_balance() == 200
