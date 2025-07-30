def patch():
    import erpnext.accounts.doctype.payment_entry.payment_entry as pe

    def patched_get_advance_payment_entries(*args, **kwargs):
        kwargs.pop("default_advance_account", None)
        return []

    pe.get_advance_payment_entries = patched_get_advance_payment_entries

patch()
