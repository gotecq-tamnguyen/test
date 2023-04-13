def check_error(func):
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        if response.code in (400, 401):
            raise Exception("LOIIIII")
        return response
    return wrapper