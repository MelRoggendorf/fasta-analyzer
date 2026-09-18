file_path = (
    r"C:\Users\mehar\DNA\fasta-analyzer\Nucleotide_Sequence_01.fasta"
)
sequence = ""
with open(file_path, "r") as f:
  for line in f:
    if not line.startswith(">"):
      sequence += line.strip().upper()

# Calculate GC content
g_count = sequence.count("G")
c_count = sequence.count("C")
total_bases = len(sequence)

if total_bases > 0:
  gc_content = ((g_count + c_count) / total_bases) * 100
  print(f"Total Bases: {total_bases}")
  print(f"GC Content: {gc_content:.2f}%")
else:
  print("No sequence found.")