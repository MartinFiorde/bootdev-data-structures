import unittest

from src.stack import Stack


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
        if "__RUN__" in globals():
            test_cases = run_cases

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
        ]

        def visualize_stack(stack):
            if not stack:
                return "- (empty)"
            return "\n".join(
                [
                    f"    - {item['name']}: {list(item.values())[1]}"
                    for item in reversed(stack)
                ]
            )

        def test(operations, expected_outputs):
            print("---------------------------------")
            stack = Stack()
            actual_outputs = []

            for i, (op, value) in enumerate(operations):
                print(f"Operation {i + 1}:")
                if op == "push":
                    print(f"  Push: {value}")
                    actual_outputs.append(stack.push(value))
                elif op == "pop":
                    result = stack.pop()
                    print(f"  Pop: {result}")
                    actual_outputs.append(result)
                elif op == "peek":
                    result = stack.peek()
                    print(f"  Peek: {result}")
                    actual_outputs.append(result)
                elif op == "size":
                    result = stack.size()
                    print(f"  Size: {result}")
                    actual_outputs.append(result)

                print(f"  Stack:\n{visualize_stack(stack.items)}")
                print()

            print(f"Expected outputs: {expected_outputs}")
            print(f"Actual outputs: {actual_outputs}")
            if actual_outputs == expected_outputs:
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
            print(f"{passed} passed, {failed} failed")
            self.assertEqual(failed, 0)

        test_cases = submit_cases
        if "__RUN__" in globals():
            test_cases = run_cases

        main()


if __name__ == "__main__":
    unittest.main()
