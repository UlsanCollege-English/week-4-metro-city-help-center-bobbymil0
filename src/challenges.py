"""
Metro City Help Center — Stacks and Queues
Weekly Coding #4
"""

from collections import deque


class ActionStack:
    """Tracks staff actions using stack (LIFO) behavior."""

    def __init__(self) -> None:
        self._data: list[str] = []

    def push(self, action: str) -> None:
        """Add an action to the top of the stack."""
        self._data.append(action)

    def pop(self) -> str | None:
        """Remove and return the most recent action, or None if empty."""
        if self.is_empty():
            return None
        return self._data.pop()

    def peek(self) -> str | None:
        """Return the most recent action without removing it, or None if empty."""
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        """Return True if the stack has no actions."""
        return len(self._data) == 0


class RequestQueue:
    """Manages citizen requests using queue (FIFO) behavior."""

    def __init__(self) -> None:
        self._data: deque[str] = deque()

    def enqueue(self, name: str) -> None:
        """Add a citizen to the back of the queue."""
        self._data.append(name)

    def dequeue(self) -> str | None:
        """Remove and return the first citizen in line, or None if empty."""
        if self.is_empty():
            return None
        return self._data.popleft()

    def peek(self) -> str | None:
        """Return the first citizen in line without removing them, or None if empty."""
        if self.is_empty():
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        """Return True if the queue has no citizens."""
        return len(self._data) == 0


def is_note_balanced(note: str) -> bool:
    """
    Return True if all brackets in the note are correctly balanced.

    Checks: (), [], {}
    Uses stack behavior with a plain list.
    """
    stack: list[str] = []
    matching = {")": "(", "]": "[", "}": "{"}
    openers = set(matching.values())

    for char in note:
        if char in openers:
            stack.append(char)
        elif char in matching:
            if not stack or stack[-1] != matching[char]:
                return False
            stack.pop()

    return len(stack) == 0


def process_request_line(citizens: list[str]) -> list[str]:
    """
    Return citizens in the order they should be served (FIFO).

    Uses queue behavior with a deque.
    Returns an empty list if input is empty.
    """
    if not citizens:
        return []

    queue: deque[str] = deque(citizens)
    served: list[str] = []

    while queue:
        served.append(queue.popleft())

    return served


def undo_recent_actions(actions: list[str], undo_count: int) -> list[str]:
    """
    Remove the most recent undo_count actions and return the rest.

    Treats the list as a stack (LIFO). If undo_count exceeds the
    number of actions, all actions are removed.
    """
    stack: list[str] = list(actions)
    for _ in range(undo_count):
        if not stack:
            break
        stack.pop()
    return stack