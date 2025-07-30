def get_advance_payment_entries(*args, **kwargs):
    # Remove unsupported argument if present
    kwargs.pop("default_advance_account", None)
    # Return dummy value (or call original function if needed)
    return []
