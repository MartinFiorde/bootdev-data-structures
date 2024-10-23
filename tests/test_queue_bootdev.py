import unittest

from src.queue import Queue


class TestQueue(unittest.TestCase):

    def test_queue_3_2(self):
        run_cases = [
            (
                [("push", "Rand"), ("push", "Mat"), ("pop", None), ("peek", None)],
                ["Rand", "Mat"],
            ),
            (
                [
                    ("push", "Egwene"),
                    ("push", "Nynaeve"),
                    ("size", None),
                    ("pop", None),
                    ("size", None),
                ],
                [2, "Egwene", 1],
            ),
        ]

        submit_cases = run_cases + [
            ([("pop", None), ("peek", None), ("size", None)], [None, None, 0]),
            (
                [
                    ("push", "Perrin"),
                    ("push", "Moiraine"),
                    ("push", "Lan"),
                    ("pop", None),
                    ("pop", None),
                    ("peek", None),
                ],
                ["Perrin", "Moiraine", "Lan"],
            ),
            (
                [("push", "Thom"), ("pop", None), ("push", "Loial"), ("peek", None)],
                ["Thom", "Loial"],
            ),
        ]

        def visualize_queue(queue):
            if not queue.items:
                return "Queue is empty"
            return "\n".join([f"- {item}" for item in reversed(queue.items)])

        def test(operations, expected_outputs):
            queue = Queue()
            outputs = []
            for op, value in operations:
                if op == "push":
                    queue.push(value)
                elif op == "pop":
                    result = queue.pop()
                    outputs.append(result)
                elif op == "peek":
                    result = queue.peek()
                    outputs.append(result)
                elif op == "size":
                    result = queue.size()
                    outputs.append(result)


            if outputs == expected_outputs:
                return True
            return False

        def main():
            passed = 0
            failed = 0
            for test_case in test_cases:
                correct = test(*test_case)
                if correct:
                    passed += 1
                else:
                    failed += 1
            print(f"3-2 task: {passed} passed, {failed} failed")
            self.assertEqual(failed, 0)

        test_cases = submit_cases

        main()


if __name__ == "__main__":
    unittest.main()
