import random
import string

def generate_verification_code(length=6) -> str:
    return ''.join(random.choices(string.digits, k=length))


if __name__ == "__main__":
    print (generate_verification_code ())