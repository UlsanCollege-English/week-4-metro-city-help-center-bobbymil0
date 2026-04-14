# Weekly Coding #4 - Metro City Help Center

## Summary
This project implements two core data structures for a help center workflow: a stack for undoable staff actions (LIFO) and a queue for citizen requests (FIFO). It also includes bracket validation for notes and a queue-based request-line processor.

## Complexity

| Function / Method | Time | Reason |
|---|---|---|
| `ActionStack.pop` | `O(1)` | Removes from the end of a Python list |
| `RequestQueue.dequeue` | `O(1)` | `deque.popleft()` is constant time |
| `is_note_balanced` | `O(n)` | Scans each character once with stack operations |
| `process_request_line` | `O(n)` | Each citizen is dequeued exactly once |

## Edge-case Checklist

| Case | Behavior |
|---|---|
| Empty action stack (`pop`) | Returns `None` |
| Empty action stack (`peek`) | Returns `None` |
| Empty request queue (`dequeue`) | Returns `None` |
| Empty request queue (`peek`) | Returns `None` |
| Empty string in `is_note_balanced` | Returns `True` |
| Note with no brackets | Returns `True` |
| Empty citizen list in `process_request_line` | Returns `[]` |

## Assistance and Sources
- AI used: Yes
- How AI was used: Helped refine wording, test organization, and readability
- Outside sources: Python documentation for `collections.deque`

## Run Tests
```bash
python -m pytest -q
```
