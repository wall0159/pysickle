# test the main program

def quality_filter_errors_on_nonnumeric_input():
    numeric_quality_score = list([1, 2, 'A'])
    window_width = 20
    assert not filter_on_quality(numeric_quality_score, window_width)

