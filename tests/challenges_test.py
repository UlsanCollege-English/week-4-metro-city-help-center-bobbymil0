"""
Tests for Metro City Help Center — Weekly Coding #4
"""

import pytest

pytestmark = pytest.mark.task(taskno=1)

from src.challenges import (
    ActionStack,
    RequestQueue,
    is_note_balanced,
    process_request_line,
    undo_recent_actions,
)


# ── ActionStack ───────────────────────────────────────────────

class TestActionStack:

    def test_push_and_pop_normal(self):
        stack = ActionStack()
        stack.push("open ticket")
        stack.push("assign worker")
        assert stack.pop() == "assign worker"
        assert stack.pop() == "open ticket"

    def test_pop_returns_lifo_order(self):
        stack = ActionStack()
        stack.push("a")
        stack.push("b")
        stack.push("c")
        assert stack.pop() == "c"

    def test_pop_empty_returns_none(self):
        stack = ActionStack()
        assert stack.pop() is None

    def test_peek_returns_top_without_removing(self):
        stack = ActionStack()
        stack.push("open ticket")
        assert stack.peek() == "open ticket"
        assert stack.peek() == "open ticket"  # still there

    def test_peek_empty_returns_none(self):
        stack = ActionStack()
        assert stack.peek() is None

    def test_is_empty_true_on_new_stack(self):
        stack = ActionStack()
        assert stack.is_empty() is True

    def test_is_empty_false_after_push(self):
        stack = ActionStack()
        stack.push("open ticket")
        assert stack.is_empty() is False

    def test_is_empty_true_after_all_popped(self):
        stack = ActionStack()
        stack.push("open ticket")
        stack.pop()
        assert stack.is_empty() is True


# ── RequestQueue ──────────────────────────────────────────────

class TestRequestQueue:

    def test_enqueue_and_dequeue_normal(self):
        queue = RequestQueue()
        queue.enqueue("Mina")
        queue.enqueue("Jay")
        assert queue.dequeue() == "Mina"
        assert queue.dequeue() == "Jay"

    def test_dequeue_returns_fifo_order(self):
        queue = RequestQueue()
        queue.enqueue("first")
        queue.enqueue("second")
        assert queue.dequeue() == "first"

    def test_dequeue_empty_returns_none(self):
        queue = RequestQueue()
        assert queue.dequeue() is None

    def test_peek_returns_front_without_removing(self):
        queue = RequestQueue()
        queue.enqueue("Mina")
        assert queue.peek() == "Mina"
        assert queue.peek() == "Mina"  # still there

    def test_peek_empty_returns_none(self):
        queue = RequestQueue()
        assert queue.peek() is None

    def test_is_empty_true_on_new_queue(self):
        queue = RequestQueue()
        assert queue.is_empty() is True

    def test_is_empty_false_after_enqueue(self):
        queue = RequestQueue()
        queue.enqueue("Mina")
        assert queue.is_empty() is False

    def test_is_empty_true_after_all_dequeued(self):
        queue = RequestQueue()
        queue.enqueue("Mina")
        queue.dequeue()
        assert queue.is_empty() is True


# ── is_note_balanced ──────────────────────────────────────────

class TestIsNoteBalanced:

    def test_parentheses_balanced(self):
        assert is_note_balanced("Call back (urgent)") is True

    def test_square_brackets_balanced(self):
        assert is_note_balanced("Repair request [building A]") is True

    def test_curly_and_square_balanced(self):
        assert is_note_balanced("Issue details: {network}[floor 2]") is True

    def test_mismatched_brackets(self):
        assert is_note_balanced("(]") is False

    def test_unclosed_bracket(self):
        assert is_note_balanced("(()") is False

    def test_empty_string(self):
        assert is_note_balanced("") is True

    def test_no_brackets(self):
        assert is_note_balanced("No brackets here at all") is True

    def test_nested_balanced(self):
        assert is_note_balanced("{[()]}") is True

    def test_wrong_close_order(self):
        assert is_note_balanced("{(})") is False


# ── process_request_line ──────────────────────────────────────

class TestProcessRequestLine:

    def test_normal_order_preserved(self):
        result = process_request_line(["Mina", "Jay", "Omar"])
        assert result == ["Mina", "Jay", "Omar"]

    def test_single_citizen(self):
        assert process_request_line(["Mina"]) == ["Mina"]

    def test_empty_list_returns_empty(self):
        assert process_request_line([]) == []


# ── undo_recent_actions (stretch) ─────────────────────────────

class TestUndoRecentActions:

    def test_undo_two(self):
        result = undo_recent_actions(["open ticket", "assign worker", "close ticket"], 2)
        assert result == ["open ticket"]

    def test_undo_zero(self):
        result = undo_recent_actions(["open ticket", "assign worker"], 0)
        assert result == ["open ticket", "assign worker"]

    def test_undo_more_than_available(self):
        result = undo_recent_actions(["open ticket"], 5)
        assert result == []

    def test_undo_empty_list(self):
        result = undo_recent_actions([], 3)
        assert result == []
