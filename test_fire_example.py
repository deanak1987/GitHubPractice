from fire_example import DataProcessor

processor = DataProcessor()


def test_process_text():
    assert "OLLEH" == processor.process_text("Hello", uppercase=True, reverse=True)


def test_analyze_numbers():
    numbers = [1, 2]
    assert 1.5 == processor.analyze_numbers(numbers, "mean")
    assert 2 == processor.analyze_numbers(numbers, "max")
    assert 1 == processor.analyze_numbers(numbers, "min")
    assert 3 == processor.analyze_numbers(numbers, "sum")


def test_flip_coin():
    assert None == processor.flip_coins(0)
    assert "Heads" or "Tails" in processor.flip_coins(1)
