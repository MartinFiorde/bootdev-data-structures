import unittest


from src.red_black_tree import RBTree, RBNode
from src.tree_user import User, get_users


class TestRedBlackTree(unittest.TestCase):

    def test_rbstree_6_7(self):

        run_cases = [
            (4,"""\
    > Shipley#11 [black]
        > Williamson#8 [red]
> Mitch#7 [black]
    > Blake#0 [black]""",)
        ]

        submit_cases = run_cases + [
            (10,"""\
        > Vennett#29 [black]
    > Mitch#26 [red]
        > George#23 [black]
            > Ricky#20 [red]
> Brownfield#16 [black]
        > Shipley#11 [black]
    > Vennett#10 [red]
            > Mitch#7 [red]
        > John#5 [black]
            > Ricky#1 [red]""",)
        ]


        def test(num_users, result_expected):
            users: User = get_users(num_users)
            tree = RBTree()
            for user in users:
                tree.insert(user)
            # print("=====================================")
            # print("Expecting:")
            # print("-------------------------------------")
            # print(result_expected)
            # print("-------------------------------------\n")
            # print("Actual:")
            # print("-------------------------------------")
            # print(print_tree(tree))
            # print("-------------------------------------\n")

            if print_tree(tree) == result_expected:
                # print("Pass \n")
                return True
            # print("Fail \n")
            return False


        def print_tree(node: RBTree):
            lines = []
            format_tree_string(node.root, lines)
            return "\n".join(lines)


        def format_tree_string(node: RBNode, lines: list[any], level=0):
            if node.val is not None:
                format_tree_string(node.right, lines, level + 1)
                lines.append(
                    " " * 4 * level
                    + "> "
                    + str(node.val)
                    + " "
                    + ("[red]" if node.red else "[black]")
                )
                format_tree_string(node.left, lines, level + 1)


        def main():
            passed = 0
            failed = 0
            for test_case in test_cases:
                correct = test(*test_case)
                if correct:
                    passed += 1
                else:
                    failed += 1
            # if failed == 0:
            #     print("============= PASS ==============")
            # else:
            #     print("============= FAIL ==============")
            print(f"6-7 task: {passed} passed, {failed} failed")
            self.assertEqual(failed, 0)


        test_cases = submit_cases

        main()
