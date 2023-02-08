def mock_open(content=["Juan Perez,1,0,1,0"]):
    mock_content = content
    class Opener:
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
