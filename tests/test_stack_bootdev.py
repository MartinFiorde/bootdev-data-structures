import unittest

from src.stack import Stack
from src.stack_usecase import is_balanced


class TestStack(unittest.TestCase):

    def test_stack_2_1(self):
        run_cases = [
            (
                [
                    ("push", {"name": "Alice", "role": "Developer"}),
                    ("push", {"name": "Bob", "title": "CTO"}),
                    ("size", None),
                ],
                2,
            ),
            (
                [
                    ("push", {"name": "Charlie", "company": "TechCorp"}),
                    ("push", {"name": "Diana", "skills": "Python"}),
                    ("push", {"name": "Ethan", "role": "Manager"}),
                    ("size", None),
                ],
                3,
            ),
        ]

        submit_cases = run_cases + [
            (
                [
                    ("size", None),
                ],
                0,
            ),
            (
                [
                    ("push", {"name": "Frank", "experience": "5 years"}),
                    ("push", {"name": "Grace", "education": "MBA"}),
                    ("push", {"name": "Henry", "location": "New York"}),
                    ("push", {"name": "Ivy", "industry": "Finance"}),
                    ("size", None),
                ],
                4,
            ),
            (
                [
                    ("push", {"name": "Jack", "connections": 500}),
                    ("size", None),
                    ("push", {"name": "Kelly", "endorsements": 50}),
                    ("size", None),
                ],
                2,
            ),
        ]

        def test(operations, expected_output):
            stack = Stack()
            result = None
            for op, value in operations:
                if op == "push":
                    stack.push(value)
                elif op == "size":
                    result = stack.size()

            if result == expected_output:
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
            print(f"2-1 task: {passed} passed, {failed} failed")
            self.assertEqual(failed, 0)

        test_cases = submit_cases

        main()

    def test_stack_2_4(self):
        run_cases = [
            (
                [
                    ("push", {"name": "Alice", "role": "Developer"}),
                    ("push", {"name": "Bob", "role": "Designer"}),
                    ("size", None),
                    ("peek", None),
                    ("pop", None),
                    ("size", None),
                ],
                [
                    None,
                    None,
                    2,
                    {"name": "Bob", "role": "Designer"},
                    {"name": "Bob", "role": "Designer"},
                    1,
                ],
            ),
            (
                [
                    ("push", {"name": "Charlie", "company": "TechCorp"}),
                    ("push", {"name": "David", "skills": ["Python", "JavaScript"]}),
                    ("pop", None),
                    ("pop", None),
                    ("pop", None),
                ],
                [
                    None,
                    None,
                    {"name": "David", "skills": ["Python", "JavaScript"]},
                    {"name": "Charlie", "company": "TechCorp"},
                    None,
                ],
            ),
        ]

        submit_cases = run_cases + [
            (
                [
                    ("push", {"name": "Eve", "role": "Manager", "years": 5}),
                    ("peek", None),
                    ("push", {"name": "Frank", "role": "DevOps"}),
                    ("size", None),
                    ("pop", None),
                    ("pop", None),
                    ("pop", None),
                ],
                [
                    None,
                    {"name": "Eve", "role": "Manager", "years": 5},
                    None,
                    2,
                    {"name": "Frank", "role": "DevOps"},
                    {"name": "Eve", "role": "Manager", "years": 5},
                    None,
                ],
            ),
            (
                [
                    ("peek", None),
                ],
                [
                    None,
                ],
            ),
        ]

        def test(operations, expected_outputs):
            stack = Stack()
            actual_outputs = []

            for i, (op, value) in enumerate(operations):
                if op == "push":
                    actual_outputs.append(stack.push(value))
                elif op == "pop":
                    result = stack.pop()
                    actual_outputs.append(result)
                elif op == "peek":
                    result = stack.peek()
                    actual_outputs.append(result)
                elif op == "size":
                    result = stack.size()
                    actual_outputs.append(result)

            if actual_outputs == expected_outputs:
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
            print(f"2_4 task: {passed} passed, {failed} failed")
            self.assertEqual(failed, 0)

        test_cases = submit_cases

        main()

    def test_stack_2_7(self):
        run_cases = [
            ("(", False),
            ("()", True),
            ("(())", True),
        ]

        submit_cases = run_cases + [
            ("()()", True),
            ("(()))", False),
            ("((())())", True),
            ("(()(()", False),
            (")(", False),
            (")()(()", False),
        ]

        def test(input1, expected_output):
            print("---------------------------------")
            print(f"Input: {input1}")
            print(f"Expecting: {expected_output}")
            result = is_balanced(input1)
            print(f"Actual: {result}")
            if result == expected_output:
                print("Pass")
                return True
            print("Fail")
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
            if failed == 0:
                print("============= PASS ==============")
            else:
                print("============= FAIL ==============")
            print(f"2-7 task: {passed} passed, {failed} failed")
            self.assertEqual(failed, 0)

        test_cases = submit_cases
        if "__RUN__" in globals():
            test_cases = run_cases

        main()


if __name__ == "__main__":
    unittest.main()
