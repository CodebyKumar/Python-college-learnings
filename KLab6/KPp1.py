from pathlib import Path
p=Path('spam.txt')
print(p.write_text('Hello, World'))
print(p.read_text())
