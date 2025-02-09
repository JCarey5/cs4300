def hello_world():
    print("Hello, World!")


def test_Hello_World(capsys):
    hello_world()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"

hello_world()