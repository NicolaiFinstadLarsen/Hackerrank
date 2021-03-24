if __name__ == '__main__':
    s = input()
    print(any(z.isalnum() for z in s))
    print(any(z.isalpha() for z in s))
    print(any(z.isdigit() for z in s))
    print(any(z.islower() for z in s))
    print(any(z.isupper() for z in s))
