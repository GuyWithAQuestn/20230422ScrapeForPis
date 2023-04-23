from deepdiff import DeepDiff


def differences_between_lists(existing_item_list, list_of_items_available):
#    difference_between_lists = (DeepDiff(existing_item_list, list_of_items_available))

    # print("existing_item_list")
    # print(existing_item_list)
    #
    # print("list_of_items_available")
    # print(list_of_items_available)

    difference_between_lists = [] #empty list
    for i in list_of_items_available:
        if i not in existing_item_list:
            difference_between_lists.append(i)

    # print("difference_between_lists")
    # print(difference_between_lists)

    return difference_between_lists