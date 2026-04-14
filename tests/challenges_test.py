"""
Tests for Metro City Help Center — Weekly Coding #4
"""

import pytest
from src.challenges import (
    ActionStack,
    RequestQueue,
    is_note_balanced,
    process_request_line,
    undo_recent_actions,
)

pytestmark = pytest.mark.task(taskno=1)


# ── ActionStack ───────────────────────────────────────────────

class TestActionStack:

    def test_push_and_pop(self):
        stack = ActionStack()
        stack.push("open ticket")
        stack.push("assign worker")
        assert stack.pop() == "assign worker"
        assert stack.pop() == "open ticket"

    def test_pop_empty(self):
        stack = ActionStack()
        assert stack.pop() is None

    def test_peek(self):
        stack = ActionStack()
        stack.push("open ticket")
        assert stack.peek() == "open ticket"
        assert stack.peek() == "open ticket"

    def test_peek_empty(self):
        stack = ActionStack()
        assert stack.peek() is None

    def test_is_empty(self):
        stack = ActionStack()
        assert stack.is_empty()
        stack.push("x")
        assert not stack.is_empty()


# ── RequestQueue ──────────────────────────────────────────────

class TestRequestQueue:

    def test_enqueue_dequeue(self):
        queue = RequestQueue()
        queue.enqueue("Mina")
        queue.enqueue("Jay")
        assert queue.dequeue() == "Mina"
        assert queue.dequeue() == "Jay"

    def test_dequeue_empty(self):
        queue = RequestQueue()
        assert queue.dequeue() is None

    def test_peek(self):
        queue = RequestQueue()
        queue.enqueue("Mina")
        assert queue.peek() == "Mina"
        assert queue.peek() == "Mina"

    def test_peek_empty(self):
        queue = RequestQueue()
        assert queue.peek() is None

    def test_is_empty(self):
        queue = RequestQueue()
        assert queue.is_empty()
        queue.enqueue("x")
        assert not queue.is_empty()


# ── is_note_balanced ──────────────────────────────────────────

class TestIsNoteBalanced:

    def test_balanced_cases(self):
        assert is_note_balanced("Call back (urgent)")
        assert is_note_balanced("Repair request [building A]")
        assert is_note_balanced("Issue details: {network}[floor 2]")
        assert is_note_balanced("{[()]}")

    def test_unbalanced_cases(self):
        assert not is_note_balanced("(]")
        assert not is_note_balanced("(()")
        assert not is_note_balanced("{(})")

    def test_edge_cases(self):
        assert is_note_balanced("")
        assert is_note_balanced("No brackets here")


# ── process_request_line ──────────────────────────────────────

class TestProcessRequestLine:

    def test_normal(self):
        assert process_request_line(["Mina", "Jay", "Omar"]) == ["Mina", "Jay", "Omar"]

    def test_empty(self):
        assert process_request_line([]) == []


# ── undo_recent_actions ───────────────────────────────────────

class TestUndoRecentActions:

    def test_normal(self):
        assert undo_recent_actions(
            ["open ticket", "assign worker", "close ticket"], 2
        ) == ["open ticket"]

    def test_zero(self):
        assert undo_recent_actions(["a", "b"], 0) == ["a", "b"]

    def test_more_than_length(self):
        assert undo_recent_actions(["a"], 5) == []

    def test_empty(self):
        assert undo_recent_actions([], 3) == []