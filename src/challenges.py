"""Weekly Coding #4: Metro City Help Center stacks and queues."""

from __future__ import annotations

from collections import deque

BRACKET_MATCH = {")": "(", "]": "[", "}": "{"}
OPENING_BRACKETS = set(BRACKET_MATCH.values())


class ActionStack:
    """Track staff actions using stack (LIFO) behavior."""

    def __init__(self) -> None:
        self._data: list[str] = []

    def push(self, action: str) -> None:
        """Add an action to the top of the stack."""
        self._data.append(action)

    def pop(self) -> str | None:
        """Remove and return the latest action, or None when empty."""
        if self.is_empty():
            return None
        return self._data.pop()

    def peek(self) -> str | None:
        """Return the latest action without removing it, or None when empty."""
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        """Return True if no actions are stored."""
        return len(self._data) == 0


class RequestQueue:
    """Manage citizen requests using queue (FIFO) behavior."""

    def __init__(self) -> None:
        self._data: deque[str] = deque()

    def enqueue(self, name: str) -> None:
        """Add a citizen to the back of the queue."""
        self._data.append(name)

    def dequeue(self) -> str | None:
        """Remove and return the first citizen, or None when empty."""
        if self.is_empty():
            return None
        return self._data.popleft()

    def peek(self) -> str | None:
        """Return the first citizen without removing them, or None when empty."""
        if self.is_empty():
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        """Return True if no citizens are waiting."""
        return len(self._data) == 0


def is_note_balanced(note: str) -> bool:
    """Return True if every bracket in the note is balanced."""
    stack: list[str] = []

    for char in note:
        if char in OPENING_BRACKETS:
            stack.append(char)
            continue

        if char in BRACKET_MATCH:
            if not stack or stack[-1] != BRACKET_MATCH[char]:
                return False
            stack.pop()

    return len(stack) == 0


def process_request_line(citizens: list[str]) -> list[str]:
    """Return a new list showing the FIFO service order for citizens."""
    if not citizens:
        return []

    line = deque(citizens)
    served: list[str] = []
    while line:
        served.append(line.popleft())
    return served


def undo_recent_actions(actions: list[str], undo_count: int) -> list[str]:
    """Undo the most recent ``undo_count`` actions and return what remains."""
    cutoff = max(0, len(actions) - max(0, undo_count))
    return actions[:cutoff]
