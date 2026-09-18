# Part 1: Count & Length

def seq_count(rawdata: list) -> int:
    """Counts Sequences in rawdata."""
    return len(rawdata)


def seq_length(rawdata: list) -> list:
    """Counts length of each sequence and gives back tuples."""
    lengths = []
    for index, seq in enumerate(rawdata, start=1):
        lengths.append((f"Sequence_{index}", len(seq)))
    return lengths

def analyze_sequences(rawdata: list) -> dict:
    """Counts sequences and calculates their lengths in a single pass."""
    total_count = len(rawdata)
    lengths = [(f"Sequence_{index}", len(seq)) for index, seq in enumerate(rawdata, start=1)]

    return {
        "count": total_count,
        "lengths": lengths,
    }
