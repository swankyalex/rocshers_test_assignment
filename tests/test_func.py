from src.runner import HttpRequester


def test_check_string_method():
    """Testing function of correct-links checking"""
    result_1 = HttpRequester.check_string('http://onliner.by')
    result_2 = HttpRequester.check_string('http://sss')
    result_3 = HttpRequester.check_string('onliner')
    assert result_1
    assert result_2
    assert result_3 == False


def test_reader_method(monkeypatch):
    """Testing function of reading from stdin"""
    responses = iter(['http://onliner.by', 'onliner.by', 'http://youtube.com', ''])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    reader = HttpRequester()
    reader.reader()
    assert reader.strings == ['http://onliner.by', 'http://youtube.com']


def test_send_request_method():
    """Testing function of sending HTTP requests"""
    requester = HttpRequester()
    requester.send_request("http://onliner.by")
    correct = {'http://onliner.by': {'DELETE': 301,
                                     'GET': 200,
                                     'HEAD': 200,
                                     'OPTIONS': 301,
                                     'PATCH': 301,
                                     'POST': 200,
                                     'PUT': 301}}
    assert requester.results == correct


def test_runner(capsys, monkeypatch):
    """Test main function"""
    responses = iter(['http://youtube.com', ''])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    requester = HttpRequester()
    requester.runner()
    captured = capsys.readouterr()
    correct = "{'http://youtube.com': {'CONNECT': 400,\n                        'GET': 200,\n                        'HEAD': 200,\n                        'POST': 400,\n                        'PUT': 400}}\n"
    assert captured.out == correct
