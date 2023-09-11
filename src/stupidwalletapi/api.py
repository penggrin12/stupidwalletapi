from .base import BaseAPI
from .models import Cheque, Invoice
from .const import WAV_COIN

from typing import List


class StupidWalletAPI(BaseAPI):
    def __init__(self, token: str):
        super().__init__(token, "https://sw.svat.dev")

    async def get_balance(self, coin_id: int = WAV_COIN) -> int:
        """<https://st.svat.dev/docs#/User%20interaction/get_balance_user_get_balance_get>"""
        response = await self._make_request("GET", "/user/get_balance", {"coin_id": coin_id})
        return response.get("coin_amount")

    async def test_apikey(self) -> bool:
        try:
            return (await self.get_balance(WAV_COIN)) is not None
        except Exception:
            return False

    # Cheques

    async def cheque_from_id(self, cheque_id: str) -> Cheque:
        result = Cheque.from_info_cheque(await self._make_request("GET", "/user/info_cheque", {"cheque_id": cheque_id}))
        result._cheque_id = cheque_id
        return result

    async def my_cheques(self) -> List[Cheque]:
        """<https://st.svat.dev/docs#/User%20interaction/my_cheques_user_my_cheques_get>"""
        response = await self._make_request("GET", "/user/my_cheques", {})
        return [Cheque(data) for data in response.get("data")]

    async def info_cheque(self, cheque_id: str) -> Cheque:
        """<https://st.svat.dev/docs#/User%20interaction/info_about_cheque_user_info_cheque_get>"""
        response = await self._make_request("GET", "/user/info_cheque", {"cheque_id": cheque_id})
        return Cheque.from_info_cheque(response)

    async def create_cheque(self, coin_id: int, coin_amount: int, password: str = None, comment: str = None) -> Cheque:
        """<https://st.svat.dev/docs#/User%20interaction/create_cheque_endpoint_user_create_cheque_post>"""
        response = await self._make_request(
            "POST",
            "/user/create_cheque",
            {"coin_id": coin_id, "coin_amount": coin_amount,
             "password": password or "", "comment": comment or ""}
        )
        return await self.cheque_from_id(response.get("cheque_id"))

    async def claim_cheque(self, cheque_id: str, password: str = None) -> Cheque:
        """<https://st.svat.dev/docs#/User%20interaction/claim_cheque_endpoint_user_claim_cheque_post>"""
        await self._make_request(
            "POST",
            "/user/claim_cheque",
            {"cheque_id": cheque_id, "password": password or ""}
        )
        return await self.cheque_from_id(cheque_id)

    # Invoices

    async def my_invoices(self) -> List[Invoice]:
        """<https://st.svat.dev/docs#/Invoice%20thing/get_my_invoices_invoice_my_invoices_get>"""
        response = await self._make_request("GET", "/invoice/my_invoices", {})
        return [Invoice(data) for data in response.get("data")]

    async def get_invoice_data(self, invoice_unique_hash: str) -> Invoice:
        """<https://st.svat.dev/docs#/Invoice%20thing/invoice_data_invoice_get_invoice_data_get>"""
        response = await self._make_request("GET", "/invoice/get_invoice_data",
                                            {"invoice_unique_hash": invoice_unique_hash})
        return Invoice(response)

    async def pay_invoice(self, invoice_unique_hash: str) -> Invoice:
        """<https://st.svat.dev/docs#/Invoice%20thing/pay_invoice_invoice_pay_invoice_post>"""
        await self._make_request(
            "POST",
            "/invoice/pay_invoice",
            {"invoice_unique_hash": invoice_unique_hash}
        )
        return await self.get_invoice_data(invoice_unique_hash)

    async def create_invoice(self, coin_id: int, coin_amount: int, expiration_time: int = None, comment: str = None,
                             return_url: str = None) -> Invoice:
        """
        <https://st.svat.dev/docs#/Invoice%20thing/create_new_invoice_invoice_create_invoice_post>
        expiration_time: in minutes (default: 500_000)
        """
        response = await self._make_request(
            "POST",
            "/invoice/create_invoice",
            {"coin_id": coin_id, "coin_amount": coin_amount, "expiration_time": expiration_time or 500_000,
             "comment": comment or "", "return_url": return_url or ""}
        )
        return await self.get_invoice_data(response.get("invoice_unique_hash"))

    async def delete_invoice(self, invoice_unique_hash: str):
        """<https://st.svat.dev/docs#/Invoice%20thing/delete_invoice_invoice_delete_invoice_delete>"""
        await self._make_request(
            "DELETE",
            "/invoice/delete_invoice",
            {"invoice_unique_hash": invoice_unique_hash}
        )

    # Custom methods
    async def create_cheques_on_all_coins(self, coin_id: int, coin_amount: int):
        for _ in range(int((await self.get_balance(coin_id)) / coin_amount)):
            await self.create_cheque(coin_id=coin_id, coin_amount=coin_amount)

    async def claim_all_cheques(self) -> int:
        claimed_cheques = 0

        while True:
            cheques = await self.my_cheques()

            if not cheques:
                break

            for cheque in cheques:
                await self.claim_cheque(cheque_id=cheque.id)
                claimed_cheques += 1

        return claimed_cheques
