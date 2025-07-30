def patch_india_compliance_override():
    import india_compliance.gst_india.overrides.payment_entry as ic_payment_entry

    def patched_get_advance_payment_entries(*args, **kwargs):
        kwargs.pop("default_advance_account", None)
        return []

    ic_payment_entry.get_advance_payment_entries = patched_get_advance_payment_entries

patch_india_compliance_override()
