import unittest


from src.graph import Graph


class TestGraph(unittest.TestCase):

    def test_graph_10_C1(self):

        run_cases = [
            (
                [
                    ("Oslo", "Bergen"),
                    ("Oslo", "Trondheim"),
                    ("Bergen", "Trondheim"),
                    ("Edinburgh", "London"),
                    ("Edinburgh", "Bristol"),
                    ("London", "Bristol"),
                ],
                "Oslo",
                "Edinburgh",
                None,
            ),
            (
                [
                    ("New York", "London"),
                    ("New York", "Cairo"),
                    ("New York", "Tokyo"),
                    ("London", "Dubai"),
                    ("Cairo", "Kyiv"),
                    ("Cairo", "Madrid"),
                    ("London", "Madrid"),
                    ("Buenos Aires", "New York"),
                    ("Tokyo", "Buenos Aires"),
                    ("Kyiv", "San Francisco"),
                ],
                "Cairo",
                "San Francisco",
                ["Cairo", "Kyiv", "San Francisco"],
            ),
        ]
        submit_cases = run_cases + [
            (
                [
                    ("Los Angeles", "Istanbul"),
                    ("Los Angeles", "Shanghai"),
                    ("Paris", "Singapore"),
                    ("Istanbul", "Rome"),
                    ("Paris", "Rome"),
                    ("Rome", "Seattle"),
                    ("Sydney", "Los Angeles"),
                    ("Shanghai", "Sydney"),
                    ("Sydney", "Cairo"),
                    ("Cairo", "Seattle"),
                    ("Seattle", "Tokyo"),
                    ("Tokyo", "Shanghai"),
                    ("Istanbul", "Cairo"),
                    ("Rome", "Berlin"),
                    ("Berlin", "Paris"),
                    ("Singapore", "Sydney"),
                    ("Cairo", "Istanbul"),
                    ("Berlin", "Tokyo"),
                ],
                "Los Angeles",
                "Berlin",
                ["Los Angeles", "Istanbul", "Rome", "Berlin"],
            ),
        ]

        def test(edges_to_add, from_vertex, to_vertex, expected_path):
            print("=================================")
            graph = Graph()
            for edge in edges_to_add:
                graph.add_edge(edge[0], edge[1])
                print(f"Added edge: {edge}")
            print("---------------------------------")
            try:
                print(f"Path from {from_vertex} to {to_vertex}")
                path = graph.bfs_path(from_vertex, to_vertex)
                print(f" - Expecting: {expected_path}")
                print(f" - Actual: {path}")

                if path == expected_path:
                    print("Pass")
                    return True
                print("Fail")
                return False
            except Exception as e:
                print(f"Error: {e}")
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
            print(f"10-C1 task: {passed} passed, {failed} failed")
            self.assertEqual(failed, 0)

        test_cases = submit_cases
        if "__RUN__" in globals():
            test_cases = run_cases

        main()