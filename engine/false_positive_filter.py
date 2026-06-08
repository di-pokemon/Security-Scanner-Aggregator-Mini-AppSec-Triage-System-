from typing import Iterable, List, Mapping


def filter_false_positives(issues: Iterable[Mapping[str, str]]) -> List[Mapping[str, str]]:
    filtered = []

    for issue in issues:
        message = str(issue.get("message", "")).lower()
        file_path = str(issue.get("file", "")).lower()

        if "test file" in message:
            continue
        if "example" in message or "example" in file_path:
            continue

        filtered.append(issue)

    return filtered
