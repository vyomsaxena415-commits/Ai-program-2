"""Count the most common words in a text file (or a built-in sample)."""
import re
import sys
from collections import Counter

text = open(sys.argv[1], encoding="utf-8").read() if len(sys.argv) > 1 else (
    "The quick brown fox jumps over the lazy dog. The dog barks, "
    "and the fox runs away. A quick fox is a happy fox.")
if len(sys.argv) < 2:
    print("No file given, using sample text.\n")

stop = {"the", "a", "an", "and", "is", "of", "to", "in", "it", "over"}
counts = Counter(w for w in re.findall(r"[a-z']+", text.lower()) if w not in stop)

print(f"Unique words: {len(counts)}\nTop 10:")
for word, n in counts.most_common(10):
    print(f"  {word:<15} {'#' * n} ({n})")
