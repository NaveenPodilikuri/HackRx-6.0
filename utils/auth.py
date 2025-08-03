def verify_token(auth_header: str) -> bool:
    try:
        scheme, token = auth_header.split()
        return scheme.lower() == "bearer" and token == "munny123"
    except:
        return False
