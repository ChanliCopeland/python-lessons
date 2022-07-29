def who_attended(*args):
    print("Who was at the Party?")
    for arg in args:
        print(f'{arg} was there!')



def role_call(**kwargs):
    print("Who is in class today?")
    for key, value in kwargs.items():
    # for kwarg in kwargs:
        print(f"{key} was {value}")
        # print(kwarg)

def party(*args, **kwargs):
    for arg in args:
        print(f'{arg} was there!')
    for key, value in kwargs.items():
    # for kwarg in kwargs:
        print(f"{key} was {value}")


if __name__ == "__main__":
  who_attended('john','mary')

