from HTTP_response_codes import responses, HttpResponse
import random
from decorator import check_error

@check_error
def random_code(custom_note):
    print(f"This is a note: {custom_note}")
    code, description= random.choice(list(responses.items()))
    return HttpResponse(400, description)


result = random_code("Hello")
print(result)


