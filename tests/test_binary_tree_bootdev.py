import unittest


import random
from src.binary_tree import BSTNode
from src.tree_user import User, get_users


class TestBinaryTree(unittest.TestCase):

    def test_bstree_5_8(self):

        run_cases = [
            (6, 2, [User(0), User(9), User(16), User(17)]),
            (
                12,
                4,
                [
                    User(2),
                    User(10),
                    User(11),
                    User(17),
                    User(22),
                    User(27),
                    User(30),
                    User(33),
                ],
            ),
        ]

        submit_cases = run_cases + [
            (
                24,
                6,
                [
                    User(2),
                    User(3),
                    User(9),
                    User(10),
                    User(12),
                    User(16),
                    User(18),
                    User(19),
                    User(22),
                    User(23),
                    User(35),
                    User(39),
                    User(45),
                    User(51),
                    User(54),
                    User(68),
                    User(69),
                    User(70),
                ],
            ),
        ]

        def test(num_users, num_to_delete, expected):
            users = get_users(num_users)
            users_copy = users.copy()
            random.shuffle(users_copy)
            users_to_delete = users_copy[:num_to_delete]
            bst = BSTNode()
            for user in users:
                bst.insert(user)
            try:
                actual_bst = BSTNode()
                for user in users:
                    actual_bst.insert(user)
                for user in users_to_delete:
                    actual_bst = actual_bst.delete(user)
                actual = actual_bst.inorder()
                if expected == actual:
                    return True
                return False
            except Exception as e:
                print(e)
                return False

        def format_tree_string(bst_node, lines: list[str], level=0):
            if bst_node is not None:
                format_tree_string(bst_node.right, lines, level + 1)
                lines.append(" " * 4 * level + "> " + str(bst_node.val))
                format_tree_string(bst_node.left, lines, level + 1)

        def main():
            passed = 0
            failed = 0
            for test_case in test_cases:
                correct = test(*test_case)
                if correct:
                    passed += 1
                else:
                    failed += 1
            print(f"5-8 task: {passed} passed, {failed} failed")
            self.assertEqual(failed, 0)

        test_cases = submit_cases

        main()
