from typing import List

def chunk_list(lst: List, size: int) -> List[List]:
    """
    Chunk a list into sublists of the specified size.

    Args:
        lst (List): The list to be chunked.
        size (int): The size of each chunk.

    Returns:
        List[List]: A new list containing sublists of the specified size.

    Examples:
        >>> chunk_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    return [lst[i:i+size] for i in range(0, len(lst), size)]
