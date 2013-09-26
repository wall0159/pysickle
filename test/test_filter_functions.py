import filter

def quality_filter_errors_on_nonnumeric_input():
    numeric_quality_score = list([1, 2, 'A'])
    window_width = 20
    assert not filter_on_quality(numeric_quality_score, window_width)
    
def quality_filter_errors_on_inappropriate_window_width():
    numeric_quality_score = range(1,19)
    window_width = 22 #window too long for quality sequence
    assert not filter_on_quality(numeric_quality_score, window_width)   
    
def quality_filter_returns_sequence_of_same_length():
    numeric_quality_score = range(1,100) % 20
    window_width = 20 #window too long for quality sequence
    filtered_quality_score = filter_on_quality(numeric_quality_score, window_width) 
    assert len(filtered) == len(numeric_quality_score)
