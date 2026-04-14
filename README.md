# Weekly Coding #4 — Metro City Help Center

## Summary
This project simulates a support system for the Metro City Help Center. It uses a stack to track recent staff actions (LIFO) and a queue to manage citizen requests (FIFO). It also includes a function to check balanced brackets in notes and a queue-based system to process citizens in order.

---

## Complexity

| Function / Method       | Time Complexity | Reason |
|------------------------|----------------|--------|
| `ActionStack.pop`      | O(1)           | Removing from the end of a list is constant time |
| `RequestQueue.dequeue` | O(1)           | `deque.popleft()` runs in constant time |
| `is_note_balanced`     | O(n)           | Each character is processed once |
| `process_request_line` | O(n)           | Each citizen is processed once |

---

## Edge-case Checklist

| Case                                   | Behavior |
|----------------------------------------|----------|
| Empty action stack (`pop`)             | Returns `None` |
| Empty action stack (`peek`)            | Returns `None` |
| Empty request queue (`dequeue`)        | Returns `None` |
| Empty request queue (`peek`)           | Returns `None` |
| Empty string in `is_note_balanced`     | Returns `True` |
| Note with no brackets                  | Returns `True` |
| Empty citizen list                     | Returns `[]` |

---

## Assistance & Sources

- **AI used:** Yes  
- **How it was used:** Helped improve structure, readability, and formatting  
- **Other sources:** Python documentation for `collections.deque`  

---

## Run Tests

```bash
python -m pytest -q