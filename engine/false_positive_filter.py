from typing import Any, Iterable, List, Mapping

MESSAGE_FALSE_POSITIVE_HINTS = ("test file", "example")


def filter_false_positives(issues: Iterable[Mapping[str, Any]]) -> List[Mapping[str, Any]]:
    filtered = []

    for issue in issues:
        message = str(issue.get("message", "")).lower()
        file_path = str(issue.get("file", "")).lower()

        if any(hint in message for hint in MESSAGE_FALSE_POSITIVE_HINTS):
            continue
        path_parts = [part for part in file_path.replace("\\", "/").split("/") if part]
        if "examples" in path_parts or "example" in path_parts:
            continue

        filtered.append(issue)

    return filtered
