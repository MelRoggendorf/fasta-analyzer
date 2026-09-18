from Bio import SeqIO
from parts import part1, part2, part3
from reportlab.pdfgen import canvas

sequences = [str(record.seq).upper()
             for record in SeqIO.parse("dna.fasta", "fasta")]

lengths = part1(sequences)
gc = part2(sequences)
short = part3(sequences, 100)

pdf = canvas.Canvas("summary_report.pdf")
pdf.drawString(50, 800, "DNA Summary Report")
pdf.drawString(50, 780, f"Number of sequences: {len(sequences)}")

for i in range(len(sequences)):
    pdf.drawString(
        50, 750 - i * 20,
        f"Sequence {i+1}: length={lengths[i]}, GC={gc[i]:.1f}%, short={short[i]}"
    )

pdf.save()