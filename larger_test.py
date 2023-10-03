from larger import main


def test_first(capsys, monkeypatch):
    inputs = iter(['15', '-8'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert captured.out == 'Greater number is: 15\n'


def test_second(capsys, monkeypatch):
    inputs = iter(['21', '37'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert captured.out == 'Greater number is: 37\n'


def test_equal(capsys, monkeypatch):
    inputs = iter(['17', '17'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert captured.out == 'The numbers are equal!\n'
