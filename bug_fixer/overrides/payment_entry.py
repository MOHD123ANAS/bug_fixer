# your_app/overrides/payment_entry.py

from erpnext.accounts.doctype.payment_entry.payment_entry import get_advance_payment_entries as original_fn

def get_advance_payment_entries(*args, **kwargs):
    kwargs.pop("default_advance_account", None)  # remove unsupported kwarg
    return original_fn(*args, **kwargs)
