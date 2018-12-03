
from indy import IndyError
from indy import wallet
from indy.error import ErrorCode

import json

import time

from indy import anoncreds, crypto, did, ledger, pool, wallet, non_secrets

import json
import logging
from typing import Optional

from indy.error import ErrorCode, IndyError

import asyncio


async def run():

    steward_wallet_config = json.dumps({"id": "sovrin_steward_wallet"})
    steward_wallet_credentials = json.dumps({"key": "steward_wallet_key"})

    try:
        await wallet.delete_wallet(steward_wallet_config, steward_wallet_credentials)
    except:
        pass
    try:
        await wallet.create_wallet(steward_wallet_config, steward_wallet_credentials)
    except:
        pass

    wallet_handle = await wallet.open_wallet(steward_wallet_config, steward_wallet_credentials)

    # insert a record
    res = await non_secrets.add_wallet_record(wallet_handle,"custom", "phone", "604-568-7891", "{}")


    # get the record
    phone = await non_secrets.get_wallet_record(wallet_handle, "custom", "phone", "{}")
    print("phone: " + phone)

    # delete the record
    #await non_secrets.delete_wallet_record(wallet_handle, "custom", "phone")

    # get the record again
    try:
        phone = await non_secrets.get_wallet_record(wallet_handle, "custom", "phone", "{}")
        print("phone: " + phone)
    except:
        print("wallet item not found")

    
    steward_did_info = {'seed': '000000000000000000000000Steward1'}
    res = await did.create_and_store_my_did(wallet_handle, json.dumps(steward_did_info))

    a = 1


def run_coroutine(coroutine, loop=None):
    if loop is None:
        loop = asyncio.get_event_loop()
    loop.run_until_complete(coroutine())


if __name__ == '__main__':
    run_coroutine(run)
    time.sleep(1)  # FIXME waiting for libindy thread complete
