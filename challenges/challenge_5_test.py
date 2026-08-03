from challenge_5_quiz import get_results

def test_get_result():
    assert get_results(['A']) == 'You missed: A'
    assert get_results(['A', 'B']) == 'You missed: A, B'
    assert get_results([]) == 'Great Job!'