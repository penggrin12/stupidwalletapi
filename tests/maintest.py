import stupidwalletapi
import asyncio


async def testing_all():
    test_password = "123testтест!./:"
    test_comment = "123testтест!:/.;"
    test_return_url = "https://t.me/penggrin"
    test_amount = 1
    swapi = stupidwalletapi.StupidWalletAPI(input("token: "))

    cheque1 = await swapi.create_cheque(stupidwalletapi.WAV_COIN, test_amount, test_password, test_comment)

    assert (cheque1.amount == test_amount)
    assert (cheque1.coin_amount == cheque1.amount)
    assert (cheque1.coin_id == stupidwalletapi.WAV_COIN)
    assert (cheque1.cheque_id == cheque1.id)
    assert (cheque1.comment == test_comment)
    assert (cheque1.is_activated == False)

    cheque2 = await swapi.claim_cheque(cheque1.id, test_password)

    assert (cheque2.id == cheque1.id)
    assert (cheque2.is_activated == True)

    invoice1 = await swapi.create_invoice(stupidwalletapi.WAV_COIN, test_amount, comment=test_comment,
                                          return_url=test_return_url)
    assert (invoice1.amount == test_amount)
    assert (invoice1.coin_amount == invoice1.amount)
    assert (invoice1.coin_id == stupidwalletapi.WAV_COIN)
    assert (invoice1.invoice_unique_hash == invoice1.id)
    assert (invoice1.invoice_unique_hash == invoice1.invoice_id)
    assert (invoice1.comment == test_comment)
    assert (invoice1.return_url == test_return_url)
    assert (len(invoice1.pay_history) == 0)

    invoice2 = await swapi.pay_invoice(invoice1.id)
    assert (invoice1.id == invoice2.id)
    assert (len(invoice2.pay_history) == 1)

    await swapi.delete_invoice(invoice1.id)


asyncio.run(testing_all())
