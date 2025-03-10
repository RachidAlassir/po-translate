import argparse
import logging
import os
import polib

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")


def search_po_files(directory, excluded_directories, lang):
    po_files = []
    po_file_name = f"{lang}.po"
    for root, dirs, files in os.walk(directory):
        root_dir = os.path.basename(root)
        if root_dir in excluded_directories:
            continue
        po_files.extend(
            os.path.join(root, file)
            for file in files if file.endswith(po_file_name)
        )
    return po_files


def translate(filename, original_po, entries, po_files):
    translated_entries = []
    for file_path in po_files:
        if os.path.exists(file_path):
            po = polib.pofile(file_path)
            translated_entries.extend(po.translated_entries())
    for entry in entries:
        entry_translations = {}
        for translated_entry in translated_entries:
            if translated_entry.msgstr and translated_entry.msgid == entry.msgid:
                entry_translations[translated_entry.msgstr] = (
                    entry_translations.get(translated_entry.msgstr, 0) + 1
                )
        if entry_translations:
            entry.msgstr = max(entry_translations, key=entry_translations.get)
            print(f"'{entry.msgid}' -> '{entry.msgstr}'")
    # Save changes once after processing all entries
    original_po.save(filename)


def process_file(filename, lang, codebase_directory, excluded_directories):
    logging.debug(f"Checking filename: {filename}")
    logging.debug(f"Codebase directory: {codebase_directory}")
    logging.debug(f"Derived language: {lang}")
    try:
        po_files = search_po_files(codebase_directory, excluded_directories, lang)
        po = polib.pofile(filename)
        translate(filename, po, po.untranslated_entries(), po_files)
        logging.info(f"Successfully processed PO file: {filename}")
    except Exception as e:
        logging.error(f"Error processing file: {filename}")
        logging.error(f"Exception: {str(e)}")
        raise


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Update a PO file by scanning a codebase for translations.",
        epilog="""Examples:
  pofiletranslate /full/path/to/ar.po 
  pofiletranslate /full/path/to/ar.po --codebase /path/to/codebase --exclude "repository1,repository2"
        """
    )
    parser.add_argument(
        "po_file",
        help="Full path to the PO file to process (e.g. /full/path/to/ar.po)"
    )
    parser.add_argument(
        "--codebase",
        default=os.getcwd(),
        help="Directory of the codebase to scan for translations (default: current directory)"
    )
    parser.add_argument(
        "--exclude",
        default="",
        help="Comma-separated list of directory names to exclude from the scan (default: none)"
    )
    parser.add_argument(
        "--depth",
        type=int,
        default=4,
        help="Optional backtracking depth (default: 4)"
    )
    args = parser.parse_args()

    filename = args.po_file

    # Derive the language code from the filename (e.g., "ar.po" -> "ar")
    base = os.path.basename(filename)
    lang = base[:-3] if base.endswith(".po") else ""

    # Convert comma-separated excluded directories into a list
    excluded_directories = [d.strip() for d in args.exclude.split(",") if d.strip()]

    # If --depth is provided, modify the codebase_directory accordingly.
    codebase_directory = args.codebase
    for _ in range(args.depth):
        codebase_directory = os.path.dirname(codebase_directory)

    process_file(filename, lang, codebase_directory, excluded_directories)
