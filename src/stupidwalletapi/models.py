from typing import Optional, Self, List, Union
from datetime import datetime


class PayHistoryItem:
    def __init__(self, raw: dict):
        self._user_id = raw.get("user_id")
        self._pay_time = raw.get("pay_time")
        self._pay_hash = raw.get("pay_hash")

    def __str__(self) -> str:
        return f"<PayHistory Item by {self._user_id}, at {self._pay_time}>"

    def __repr__(self) -> str:
        return self.__str__()

    @property
    def user_id(self) -> int:
        return self._user_id

    @property
    def pay_time(self) -> datetime:
        return datetime.fromisoformat(self._pay_time)

    @property
    def pay_hash(self) -> str:
        return self._pay_hash


class Cheque:
    def __init__(self, raw: dict):
        self._cheque_id = raw.get("cheque_id")
        self._is_activated = raw.get("is_activated")
        self._coin_id = raw.get("coin_id")
        self._coin_amount = raw.get("coin_amount")
        self._password = raw.get("password")
        self._comment = raw.get("comment")

    def __str__(self) -> str:
        return f"<Cheque #{self._cheque_id}, {self._coin_id}: {self._coin_amount}>"

    def __repr__(self) -> str:
        return self.__str__()

    @staticmethod
    def from_my_cheques(raw: dict) -> Self:
        return Cheque(raw)

    @staticmethod
    def from_info_cheque(raw: dict) -> Self:
        return Cheque(raw)

    @property
    def cheque_id(self) -> str:
        return self._cheque_id

    @property
    def id(self) -> str:
        """Alias for cheque_id"""
        return self._cheque_id

    @property
    def is_activated(self) -> Optional[bool]:
        """Only works when cheque is found with info_cheque"""
        return self._is_activated

    @property
    def coin_id(self) -> int:
        return self._coin_id

    @property
    def coin_amount(self) -> int:
        return self._coin_amount

    @property
    def amount(self) -> int:
        """Alias for coin_amount"""
        return self._coin_amount

    @property
    def password(self) -> Optional[str]:
        return self._password

    @property
    def comment(self) -> Optional[str]:
        return self._comment


class Invoice:
    def __init__(self, raw: dict):
        self._creator_id = raw.get("creator_id")
        self._invoice_unique_hash = raw.get("invoice_unique_hash")
        self._coin_id = raw.get("coin_id")
        self._coin_amount = raw.get("coin_amount")
        self._comment = raw.get("comment")
        self._expiration_time = raw.get("expiration_time")
        self._creation_time = raw.get("creation_time")
        self._return_url = raw.get("return_url")
        self._pay_history = raw.get("pay_history")

    def __str__(self) -> str:
        return f"<Invoice #{self._invoice_unique_hash}, {self._coin_id}: {self._coin_amount}>"

    def __repr__(self) -> str:
        return self.__str__()

    @property
    def creator_id(self) -> int:
        return self._creator_id

    @property
    def invoice_unique_hash(self) -> str:
        return self._invoice_unique_hash

    @property
    def invoice_id(self) -> str:
        """Alias for invoice_unique_hash"""
        return self._invoice_unique_hash

    @property
    def id(self) -> str:
        """Alias for invoice_unique_hash"""
        return self.invoice_unique_hash

    @property
    def coin_id(self) -> int:
        return self._coin_id

    @property
    def coin_amount(self) -> int:
        return self._coin_amount

    @property
    def amount(self) -> int:
        """Alias for coin_amount"""
        return self._coin_amount

    @property
    def comment(self) -> Optional[str]:
        return self._comment

    @property
    def expiration_time(self) -> datetime:
        return datetime.fromisoformat(self._expiration_time)

    @property
    def expiration(self) -> datetime:
        """Alias for expiration_time"""
        return self.expiration_time

    @property
    def creation_time(self) -> datetime:
        return datetime.fromisoformat(self._creation_time)

    @property
    def creation(self) -> datetime:
        """Alias for creation_time"""
        return self.creation_time

    @property
    def return_url(self) -> str:
        return self._return_url

    @property
    def pay_history(self) -> Union[List[PayHistoryItem], List]:
        """Only works when cheque is found with get_invoice_data"""
        return [PayHistoryItem(data) for data in self._pay_history] if self._pay_history else []
