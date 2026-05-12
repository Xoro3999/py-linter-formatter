def format_linter_report(linter_report: dict) -> list:
    formatted_files = [
        format_single_linter_file(file_path, errors)
        for file_path, errors in linter_report.items()
    ]

    return sorted(formatted_files, key=lambda x: x["path"])