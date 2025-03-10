```markdown
# po-translate

A simple CLI tool that scans a codebase for translations and updates a given PO file. It automatically extracts the language from the PO file's name (for example, "ar.po" yields the language code "ar").

## Installation

Clone the repository and install with pip:

```bash
pip3 install .
```

## Usage

Run the tool by providing the full path to your PO file. You can also specify a codebase directory to scan and a list of directory names to exclude.

For help, run:

```bash
po-translate --help
```

### Command-Line Arguments

- **`po_file` (required):** Full path to the PO file you want to process.  
  *Example:* `/full/path/to/ar.po`
- **`--codebase`:** Directory of the codebase to scan for translations.  
  Defaults to the current working directory.
- **`--exclude`:** Comma-separated list of directory names to exclude from the scan.  
  *Example:* `"OpenUpgrade,odoo"`

### Example

```bash
po-translate /full/path/to/ar.po --codebase /path/to/codebase --exclude "OpenUpgrade,odoo"
```

## What It Does

The tool scans the specified codebase for PO files matching the derived language (e.g., "ar") and updates your provided PO file with any matching translations found.

## License

This project is licensed under the MIT License.
```
