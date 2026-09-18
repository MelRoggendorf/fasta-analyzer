# Subtask: Flag sequences shorter than a threshold

threshold = 100

for seq_id, seq in sequences.items():
    if len(seq) < threshold:
        print(seq_id, "is SHORT")
    else:
        print(seq_id, "is OK")