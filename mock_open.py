def mock_open(content):
    mock_content = content
    class Opener:
        """Mock open function for dependency injection

        Attributes:
            filename: Mock file name if the open function
            mode: Mock mode of the open funcition
        """
        def __init__(self, filename, mode=""):
            self.mode = mode

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            return self        

        def __iter__(self):
            return iter(mock_content)

        def writer(self):
            pass
        def reader(self):
            pass
    return Opener
