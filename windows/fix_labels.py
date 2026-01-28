from pathlib import Path

# pastas de labels
labels_dirs = [
    Path("./dataset/train/labels"),
    Path("./dataset/val/labels"),
]

for labels_path in labels_dirs:
    if not labels_path.exists():
        print(f"Pasta não encontrada: {labels_path}")
        continue

    for file in labels_path.glob("*.txt"):
        new_lines = []

        with open(file, "r") as f:
            for line in f:
                parts = line.strip().split()
                if not parts:
                    continue

                cls = int(parts[0]) - 1

                # se a classe for menor que 0, define como 3
                if cls < 0:
                    cls = 3

                parts[0] = str(cls)
                new_lines.append(" ".join(parts))

        with open(file, "w") as f:
            f.write("\n".join(new_lines))

    print(f"Processado: {labels_path}")