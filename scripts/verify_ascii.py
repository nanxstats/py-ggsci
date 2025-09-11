"""ASCII verifier.

Verifies whether all text files in the current directory contain only ASCII characters.
"""

import os
import sys
from typing import FrozenSet, List, Tuple


def is_text_file(path: str, n: int | None = None) -> bool:
    """
    Classify any file as text or binary.

    Algorithm adopted from "A Fast Method for Identifying Plain Text Files"
    in zlib (`doc/txtvsbin.txt`).

    Args:
        path: File path.
        n: Maximal number of bytes to read. Defaults to file size.

    Returns:
        True if the file is text, False if binary.
    """
    ALLOW: FrozenSet[int] = frozenset([9, 10, 13] + list(range(32, 256)))
    BLOCK: FrozenSet[int] = frozenset(list(range(0, 7)) + list(range(14, 32)))

    with open(path, "rb") as file:
        bytecode = bytes(file.read(n or os.path.getsize(path)))

    if not bytecode:
        return False

    cond1 = any(b in ALLOW for b in bytecode)
    cond2 = not any(b in BLOCK for b in bytecode)

    return cond1 and cond2


def find_non_ascii_lines(filepath: str) -> List[Tuple[int, str, List[int]]]:
    """
    Find lines containing non-ASCII characters in a text file.

    Args:
        filepath: Path to the text file.

    Returns:
        List of tuples (line_number, line_content, positions) where positions
        are the character indices of non-ASCII characters in the line.
    """
    non_ascii_lines = []

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line_num, line in enumerate(f, 1):
                non_ascii_positions = []
                for pos, char in enumerate(line):
                    if ord(char) > 127:
                        non_ascii_positions.append(pos)

                if non_ascii_positions:
                    non_ascii_lines.append(
                        (line_num, line.rstrip("\n"), non_ascii_positions)
                    )
    except (UnicodeDecodeError, OSError) as e:
        # File might not be UTF-8 encoded or readable
        print(f"Warning: Can't read {filepath}: {e}")

    return non_ascii_lines


def highlight_non_ascii(line: str, positions: List[int]) -> str:
    """
    Highlight non-ASCII characters in a line.

    Args:
        line: The line content.
        positions: Positions of non-ASCII characters.

    Returns:
        Line with highlighted non-ASCII characters.
    """
    result = []
    for i, char in enumerate(line):
        if i in positions:
            # Show the character and its Unicode code point
            result.append(f"[{repr(char)[1:-1]}:U+{ord(char):04X}]")
        else:
            result.append(char)
    return "".join(result)


def scan_directory(root_dir: str) -> None:
    """
    Scan directory recursively for text files with non-ASCII characters.

    Args:
        root_dir: Root directory to scan.
    """
    # Directories to skip
    skip_dirs = {
        ".git",
        "__pycache__",
        "build",
        "dist",
        "site",
        "wheels",
        ".venv",
        ".pytest_cache",
        ".egg-info",
    }

    files_with_non_ascii = []
    total_files_scanned = 0

    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip certain directories
        dirnames[:] = [
            d for d in dirnames if d not in skip_dirs and not d.endswith(".egg-info")
        ]

        for filename in filenames:
            filepath = os.path.join(dirpath, filename)

            # Check if it's a text file
            if not os.path.isfile(filepath):
                continue

            try:
                if is_text_file(filepath):
                    total_files_scanned += 1
                    non_ascii_lines = find_non_ascii_lines(filepath)

                    if non_ascii_lines:
                        # Use relative path for cleaner output
                        rel_path = os.path.relpath(filepath, root_dir)
                        files_with_non_ascii.append((rel_path, non_ascii_lines))
            except Exception as e:
                print(f"Warning: Could not process {filepath}: {e}")

    # Report results
    print("ASCII verification report")
    print("=" * 25)
    print(f"Scanned {total_files_scanned} text files in: {root_dir}")
    print()

    if not files_with_non_ascii:
        print("SUCCESS: All text files contain only ASCII characters!")
    else:
        print(f"FOUND: {len(files_with_non_ascii)} file(s) with non-ASCII characters:")
        print()

        for filepath, non_ascii_lines in files_with_non_ascii:
            print(f"File: {filepath}")
            print(f"  Lines with non-ASCII characters: {len(non_ascii_lines)}")

            # Show up to 5 example lines
            for line_num, line, positions in non_ascii_lines[:5]:
                print(
                    f"  Line {line_num}: {highlight_non_ascii(line[:100], positions)}"
                )
                if len(line) > 100:
                    print(f"           ... (truncated, {len(line)} chars total)")

            if len(non_ascii_lines) > 5:
                print(f"  ... and {len(non_ascii_lines) - 5} more line(s)")
            print()

        # Summary
        print("Summary:")
        print(f"  Files with non-ASCII: {len(files_with_non_ascii)}")
        total_lines = sum(len(lines) for _, lines in files_with_non_ascii)
        print(f"  Total lines affected: {total_lines}")


def main():
    # Use current directory if no argument provided
    if len(sys.argv) > 1:
        root_dir = sys.argv[1]
    else:
        root_dir = os.getcwd()

    if not os.path.isdir(root_dir):
        print(f"Error: {root_dir} is not a directory")
        sys.exit(1)

    scan_directory(root_dir)


if __name__ == "__main__":
    main()
