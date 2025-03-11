### PO files translator from local codebases

A simple CLI tool that scans a codebase for translations and updates a given PO file with the most likely translations.
It automatically extracts the language from the PO file's name (for example, "ar.po" yields the language code "ar").

## Installation

```bash
pip3 install pofiletranslate
```

## Usage

To run the tool, you can provide either the full path or the relative path to the .po file, 
depending on where you're located in the terminal.
Example, Browse your translation folder (e.g., `i18n`), open the terminal, and run:
```bash
 pofiletranslate fr.po
```
For help, run:

```bash
pofiletranslate --help
```

### Command-Line Arguments

- **`po_file_path` (required):** Path to the PO file you want to process.  
  *Example:* `/full/path/to/ar.po`
  
- **`--depth` (optional):** Backtrack depth for computing the codebase directory. Defaults to `4`.  
  *Example:* `--depth 3`

- **`--exclude` (optional):** Comma-separated list of directory names to exclude from the scan. 
Defaults to an empty string, meaning no directories are excluded.  
  *Example:* `--exclude "dir1,dir2"`
  - This will exclude the directories `dir1` and `dir2` from the translation scan.

### Example usage:

```bash
pofiletranslate /full/path/to/ar.po --depth 3 --exclude "dir1,dir2"
```
This example will process the `ar.po` file with a depth of `3` and will exclude 
the directories `dir1` and `dir2` from the scan.

## What It Does

The tool scans the specified codebase for PO files matching the derived language (e.g., "fr") 
and updates your provided PO file with the most likely translation.
If for example state == 'statut' is found with 70% confidence and state == 'état' is found with 30% confidence, 
the tool will select 'statut'.
