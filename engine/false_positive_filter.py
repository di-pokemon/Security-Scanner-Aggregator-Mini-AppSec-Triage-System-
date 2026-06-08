from typing import Iterable, List, Mapping

MESSAGE_FALSE_POSITIVE_HINTS = ("test file", "example")
PATH_FALSE_POSITIVE_HINTS = ("example",)


def filter_false_positives(issues: Iterable[Mapping[str, str]]) -> List[Mapping[str, str]]:
    filtered = []

    for issue in issues:
        message = str(issue.get("message", "")).lower()
        file_path = str(issue.get("file", "")).lower()

        if any(hint in message for hint in MESSAGE_FALSE_POSITIVE_HINTS):
            continue
        if any(hint in file_path for hint in PATH_FALSE_POSITIVE_HINTS):
            continue

        filtered.append(issue)

    return filtered
