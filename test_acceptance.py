import approvaltests


def test_two_plus_two():
    approvaltests.verify(2 + 2)

def test_hello():
    approvaltests.verify("Hello")

# if __name__ == '__main__':
#      approvaltests.main()
