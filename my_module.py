print("Importing my module...........")

def find_index(from_search,to_search):
    """
    :param from_search:
    :param to_search:
    :return: index of str to find otherwise returns -1
    """
    to_search = to_search.strip().capitalize()

    for index,word in enumerate(from_search):
        if word == to_search:
            return index

    return -1


