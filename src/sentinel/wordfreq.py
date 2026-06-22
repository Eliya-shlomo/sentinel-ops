import re
from collections import Counter, defaultdict, deque


class TextAnalyzer:
    def __init__(self, history_max_size: int = 5) -> None:
        self.word_counts: Counter[str] = Counter()

        self.word_locations: defaultdict[str, list[int]] = defaultdict(list)

        self.recent_processed_words: deque[str] = deque(maxlen=history_max_size)

    def process_text(self, text: str, line_number: int) -> None:
        """
        Cleans the input text, updates global word frequencies,
        tracks line locations, and pushes words into a bounded history log.
        """
        words: list[str] = re.findall(r"\b\w+\b", text.lower())

        for word in words:
            self.word_counts[word] += 1
            self.word_locations[word].append(line_number)
            self.recent_processed_words.append(word)

    def get_top_words(self, n: int = 5) -> list[tuple[str, int]]:
        """Returns the 'n' most common words sorted by frequency."""
        return self.word_counts.most_common(n)

    def get_recent_history(self) -> list[str]:
        """Returns the current sliding window of recently processed words."""
        return list(self.recent_processed_words)


if __name__ == "__main__":
    analyzer = TextAnalyzer(history_max_size=4)

    print("--- Step 1: Processing Line 1 ---")
    analyzer.process_text("Python is fast. Python is elegant.", line_number=1)
    print("Top words:", analyzer.get_top_words(2))
    print("Recent history:", analyzer.get_recent_history())
    print()

    print("--- Step 2: Processing Line 2 (Eviction Triggered) ---")
    analyzer.process_text("Fast code is good code.", line_number=2)

    print("Full Counter mapping:")
    print(analyzer.word_counts)
    print()

    print("Line locations for 'python':", analyzer.word_locations["python"])
    print("Line locations for 'code':", analyzer.word_locations["code"])
    print()

    print("Recent history (Oldest words evicted automatically):")
    print(analyzer.get_recent_history())
