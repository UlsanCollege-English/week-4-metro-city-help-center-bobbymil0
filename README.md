# Weekly Coding #4 — Metro City Help Center

## Summary

This project builds small parts of a support system for Metro City Help Center. Staff actions are tracked with a stack so the most recent can be undone first, and waiting citizens are managed with a queue so they are served in arrival order. The assignment focuses on choosing the right data structure — stack (LIFO) or queue (FIFO) — for each real-world need.

---

## Complexity

| Function / Method | Time Complexity | Reason |
|---|---|---|
| `ActionStack.pop` | O(1) | `list.pop()` from the end is constant time |
| `RequestQueue.dequeue` | O(1) | `deque.popleft()` is constant time; this is why `deque` is used instead of a plain list |
| `is_note_balanced` | O(n) | Each character in the note is visited exactly once |
| `process_request_line` | O(n) | Each citizen is enqueued and dequeued exactly once |

---

## Edge-case checklist

| Case | How the code handles it |
|---|---|
| Empty action stack — `pop` | Returns `None` immediately via `is_empty()` check |
| Empty action stack — `peek` | Returns `None` immediately via `is_empty()` check |
| Empty request queue — `dequeue` | Returns `None` immediately via `is_empty()` check |
| Empty request queue — `peek` | Returns `None` immediately via `is_empty()` check |
| Empty string for `is_note_balanced` | The loop never runs; the stack stays empty; returns `True` |
| Note with no brackets | Non-bracket characters are ignored; returns `True` |
| Empty citizen list for `process_request_line` | Caught by `if not citizens` guard; returns `[]` immediately |

---

## Assistance & sources

- **AI used:** Yes
- **What it helped with:** Structuring the docstrings and README table formatting
- **Outside sources:** Python docs for `collections.deque` — https://docs.python.org/3/library/collections.html#collections.deques