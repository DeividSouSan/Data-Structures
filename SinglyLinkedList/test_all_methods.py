from tests.test_delete_method import TestDeleteMethod
from tests.test_add_method import TestAddMethod
from tests.test_add_to_method import TestAddToMethod

if __name__ == "__main__":
    TestAddMethod().test_add_to_empty_list()
    TestAddMethod().test_add_to_not_empty_list()
    print("All tests passed")

    TestDeleteMethod().test_delete_from_empty_list()
    TestDeleteMethod().test_delete_first_node_from_list()
    TestDeleteMethod().test_delete_last_node_from_list()
    TestDeleteMethod().test_delete_node_from_list()
    TestDeleteMethod().test_delete_the_only_node_in_list()
    TestDeleteMethod().test_delete_node_that_doesnt_exist()
    TestDeleteMethod().test_delete_node_that_appear_twice()
    print("All tests passed")

    TestAddToMethod().test_add_to_first_pos_of_empty_list()
    print("All tests passed")
