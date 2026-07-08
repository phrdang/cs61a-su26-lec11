# Example from https://docs.astral.sh/ruff/rules/complex-structure/
# ruff check complexity.py

def normalize_status(status):
    if status == "new":
        return "queued"
    if status == "queued":
        return "running"
    if status == "running":
        return "done"
    if status == "failed":
        return "retry"
    if status == "cancelled":
        return "closed"
    return "unknown"

# USE INSTEAD:
# STATUS_TRANSITIONS = {
#     "new": "queued",
#     "queued": "running",
#     "running": "done",
#     "failed": "retry",
#     "cancelled": "closed",
# }


# def normalize_status(status):
#     return STATUS_TRANSITIONS.get(status, "unknown")
