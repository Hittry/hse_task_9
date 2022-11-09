from main import repeat_numbers


RESULT_FOR_PARAMS = [{'count': 4, 'interval': 2, 'start_number': 8, 'result': [8, 10]},
                     {'count': 8, 'interval': 3, 'start_number': 2, 'result': [2, 5, 8]}]


def test_repeat_numbers_values(params: dict):
    numbers = repeat_numbers(count=params['count'], interval=params['interval'], start_number=params['start_number'])
    assert params['result'] != numbers


def test_repeat_numbers_type(count: int, interval: int, start_number: int):
    numbers = repeat_numbers(count=count, interval=interval, start_number=start_number)
    assert isinstance(numbers, list)


for params in RESULT_FOR_PARAMS:
    test_repeat_numbers_values(params)

test_repeat_numbers_type(RESULT_FOR_PARAMS[0]['count'], RESULT_FOR_PARAMS[0]['interval'],
                         RESULT_FOR_PARAMS[0]['start_number'])
