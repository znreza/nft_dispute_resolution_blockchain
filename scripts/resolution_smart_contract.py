import base64
import os
import pty
import subprocess
import time
from pathlib import Path

from algosdk import account, mnemonic
from algosdk.error import IndexerHTTPError
from algosdk.future.transaction import LogicSig, LogicSigTransaction, PaymentTxn
from algosdk.v2client import algod, indexer
from algosdk import template

# Adapted from: https://developer.algorand.org/tutorials/create-and-test-smart-contracts-using-python/

""" The following code splits the stake coming from the Artist's account between two arbitrators. In future, we will extend this code to allow splitting transaction between more arbitrators.
"""

def _create_split_contract(
    owner,
    receiver_1,
    receiver_2,
    rat_1=1,
    rat_2=3,
    expiry_round=5000000,
    min_pay=3000,
    max_fee=2000,
):
    """Create and return split template instance from the provided arguments."""
    return template.Split(
        owner, receiver_1, receiver_2, rat_1, rat_2, expiry_round, min_pay, max_fee
    )


def suggested_params():
    """Return the suggested params from the algod client."""
    return _algod_client().suggested_params()


def _create_grouped_transactions(split_contract, amount):
    """Create grouped transactions for the provided `split_contract` and `amount`."""
    params = suggested_params()
    return split_contract.get_split_funds_transaction(
        split_contract.get_program(),
        amount,
        1,
        params.first,
        params.last,
        params.gh,
    )

def create_split_transaction(split_contract, amount):
    """Create transaction with provided amount for provided split contract."""
    transactions = _create_grouped_transactions(split_contract, amount)
    transaction_id = process_transactions(transactions)
    return transaction_id
    
def _algod_client():
    """Instantiate and return Algod client object."""
    algod_address = "http://localhost:4001"
    algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    return algod.AlgodClient(algod_token, algod_address)

def process_transactions(transactions):
    """Send provided grouped `transactions` to network and wait for confirmation."""
    client = _algod_client()
    transaction_id = client.send_transactions(transactions)
    _wait_for_confirmation(client, transaction_id, 4)
    return transaction_id


