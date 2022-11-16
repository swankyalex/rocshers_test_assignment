from src.runner import check_string, reader, send_request, main


def test_check_string():
    """Testing function of correct-links checking"""
    result_1 = check_string('http://onliner.by')
    result_2 = check_string('http://sss')
    result_3 = check_string('onliner')
    assert result_1
    assert result_2
    assert result_3 == False


def test_reader(monkeypatch):
    """Testing function of reading from stdin"""
    responses = iter(['http://onliner.by', 'onliner.by', 'http://youtube.com', ''])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    result = reader()
    assert result == ['http://onliner.by', 'http://youtube.com']


def test_send_request():
    """Testing function of sending HTTP requests"""
    results = {}
    send_request("http://onliner.by", results)
    correct = {'http://onliner.by': {'DELETE': 301,
                                     'GET': 200,
                                     'HEAD': 200,
                                     'OPTIONS': 301,
                                     'PATCH': 301,
                                     'POST': 200,
                                     'PUT': 301}}
    assert results == correct


def test_main(capsys, monkeypatch):
    """Test main function"""
    responses = iter(['http://youtube.com', ''])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    main()
    captured = capsys.readouterr()
    correct = "{'http://youtube.com': {'CONNECT': 400,\n                        'GET': 200,\n                        'HEAD': 200,\n                        'POST': 400,\n                        'PUT': 400}}\n"
    assert captured.out == correct
