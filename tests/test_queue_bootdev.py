import unittest

from src.queue_imperfect import QueueImperfect, QueueMatchmaking
from src.queue_imperfect_usecase import matchmake


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


        def test(operations, expected_outputs):
            queue = QueueImperfect()
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
        
    def test_queue_3_C1(self):
        run_cases = [
            [("Ted", "join"), (["Ted"], "No match found")],
            [("Barney", "join"), (["Barney", "Ted"], "No match found")],
            [("Marshall", "join"), (["Marshall", "Barney", "Ted"], "No match found")],
            [("Lily", "join"), (["Lily", "Marshall"], "Ted matched Barney!")],
            [("Robin", "join"), (["Robin", "Lily", "Marshall"], "No match found")],
            [("Carl", "join"), (["Carl", "Robin"], "Marshall matched Lily!")],
            [("Carl", "leave"), (["Robin"], "No match found")],
            [("Robin", "leave"), ([], "No match found")],
        ]

        submit_cases = run_cases + [
            [("Ranjit", "join"), (["Ranjit"], "No match found")],
            [("Ranjit", "leave"), ([], "No match found")],
            [("Victoria", "join"), (["Victoria"], "No match found")],
            [("Quinn", "join"), (["Quinn", "Victoria"], "No match found")],
            [("Zoey", "join"), (["Zoey", "Quinn", "Victoria"], "No match found")],
            [("Stella", "join"), (["Stella", "Zoey"], "Victoria matched Quinn!")],
        ]


        def test(queue: QueueImperfect, user, expected_state):
            try:
                result = matchmake(queue, user)
            except Exception as e:
                result = f"Error: {e}"
            if result == expected_state[1] and queue.items == expected_state[0]:
                return True
            return False


        def main():
            passed = 0
            failed = 0
            queue = QueueMatchmaking()
            for test_case in test_cases:
                correct = test(queue, *test_case)
                if correct:
                    passed += 1
                else:
                    failed += 1
            print(f"3-C1 task: {passed} passed, {failed} failed")
            self.assertEqual(failed, 0)


        test_cases = submit_cases

        main()



if __name__ == "__main__":
    unittest.main()
