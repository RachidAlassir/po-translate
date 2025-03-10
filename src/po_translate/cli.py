import argparse
import os
from src.po_translate.translate import process_file

def main():
    parser = argparse.ArgumentParser(description="PO Auto Translate CLI")
    parser.add_argument("po_file_path", help="Path to PO file")
    parser.add_argument("--depth", type=int, default=4, help="Backtrack depth")

    args = parser.parse_args()

    # Compute the full absolute path for the PO file
    po_file_path = os.path.abspath(args.po_file_path)

    # Compute lang from the file name (e.g., 'ar.po' -> 'ar')
    lang = os.path.splitext(os.path.basename(po_file_path))[0]

    # Compute codebase path based on depth
    codebase_dir = po_file_path
    for _ in range(args.depth):
        codebase_dir = os.path.dirname(codebase_dir)

    # Call the translation script
    process_file(po_file_path, lang, codebase_dir, [])

if __name__ == "__main__":
    main()
