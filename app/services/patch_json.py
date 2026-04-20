def patch_json(original, update):
    for key, value in update.items():
        if key in original:
            if isinstance(value, dict) and isinstance(original[key], dict):
                patch_json(original[key], value)
            elif value is not None and value != [] and value != original[key] :
                original[key] = value
        else:
            if value is not None:
                original[key] = value
    return original