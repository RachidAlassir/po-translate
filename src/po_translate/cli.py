import argparse
from po_translate.translate import process_file


def main():
    parser = argparse.ArgumentParser(description="PO Auto Translate CLI")
    parser.add_argument("lang", help="Language to translate to")
    parser.add_argument("--depth", type=int, default=4, help="Backtrack depth")
    parser.add_argument("--po_file_path", default=None, help="Path to PO file")

    args = parser.parse_args()

    # Compute default po_file_path if not provided
    if args.po_file_path is None:
        import os
        current_path = os.getcwd()
        args.po_file_path = os.path.join(current_path, f"{args.lang}.po")

    # Compute codebase path based on depth
    codebase_dir = args.po_file_path
    for _ in range(args.depth):
        codebase_dir = os.path.dirname(codebase_dir)

    # Call the translation script
    process_file(args.po_file_path, args.lang, False, codebase_dir, [])

if __name__ == "__main__":
    main()
