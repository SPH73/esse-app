import uuid

def get_slug_suffix():
    suffix = str(uuid.uuid4())[:4].replace('-', '').lower()
    return suffix