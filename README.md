# File Organizer (Python)

A simple Python script that automatically organizes files in a folder by type.

## Features

- Organizes files into folders:
  - Images
  - Documents
  - Audio
  - Video
  - Archives
  - Code
  - Other

- Verbose output:
  - Shows what is happening while running

- Dry-run mode:
  - Preview what will happen without moving files

---

## How to use

### Normal mode (moves files)

```bash
python organizer.py <folder_path>
```

Example:

```bash
python organizer.py test
```

---

### Dry-run mode (no changes)

```bash
python organizer.py <folder_path> --dry-run
```

Example:

```bash
python organizer.py test --dry-run
```

---

## Example output

```
Moving photo.jpg → Images
Moving report.pdf → Documents
```

Dry-run:

```
Would move photo.jpg → Images
Would move report.pdf → Documents
```

---

## Technologies

- Python
- pathlib
- shutil
- sys