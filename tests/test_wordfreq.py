from sentinel.wordfreq import TextAnalyzer


def test_get_top_words_counts_and_ordering() -> None:
    """
    Asserts that get_top_words returns correct frequencies and
    is strictly ordered from highest to lowest.
    """
    analyzer = TextAnalyzer(history_max_size=10)
    analyzer.process_text("apple banana cherry apple banana apple", line_number=1)

    top_words = analyzer.get_top_words(n=2)

    assert len(top_words) == 2
    assert top_words[0] == ("apple", 3)
    assert top_words[1] == ("banana", 2)


def test_word_locations_tracks_across_multiple_calls() -> None:
    """
    Asserts that word_locations accumulates line numbers correctly
    across separate process_text invocations.
    """
    analyzer = TextAnalyzer(history_max_size=10)

    analyzer.process_text("Python is amazing", line_number=1)
    analyzer.process_text("Writing clean code in Python", line_number=2)
    analyzer.process_text("Python forces clarity", line_number=5)

    assert analyzer.word_locations["python"] == [1, 2, 5]
    assert analyzer.word_locations["amazing"] == [1]
    assert analyzer.word_locations["missing_word"] == []


def test_deque_eviction_boundary_precisely() -> None:
    """
    Asserts the exact maxlen boundary of the deque.
    Processing exactly history_max_size + 1 words must evict
    the oldest word and preserve the rest in order.
    """
    history_max_size = 3
    analyzer = TextAnalyzer(history_max_size=history_max_size)

    analyzer.process_text("one two three", line_number=1)
    assert analyzer.get_recent_history() == ["one", "two", "three"]

    analyzer.process_text("four", line_number=2)

    current_history = analyzer.get_recent_history()
    assert len(current_history) == history_max_size
    assert "one" not in current_history
    assert current_history == ["two", "three", "four"]
