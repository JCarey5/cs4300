def count_words_in_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    words = len(content.split())
    return words


count = count_words_in_file("task6_read_me.txt")
print(count)


test_files = ["task6_read_me.txt"]
expected_word_counts = {
    "task6_read_me.txt": 104
}


def pytest_generate_tests(metafunc):
    if "filename" in metafunc.fixturenames:
        metafunc.parametrize("filename", test_files)


for filename in test_files:
    def create_test_function(filename):
        def test_word_count():
            assert count_words_in_file(filename) == expected_word_counts.get(filename, -1)
        test_word_count.__name__ = f"test_word_count_{filename.replace('.', '_')}"  
        globals()[test_word_count.__name__] = test_word_count  

    create_test_function(filename)