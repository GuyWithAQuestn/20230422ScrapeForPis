from deepdiff import DeepDiff


def differences_between_lists(existing_item_list, list_of_items_available):
    difference_between_lists = (DeepDiff(existing_item_list, list_of_items_available))

    return difference_between_lists