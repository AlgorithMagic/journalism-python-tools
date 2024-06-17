class ArrayToCountedDict:
    """
    A class to convert an array into a dictionary where keys are unique elements
    and values are the counts of those elements in the array.
    """
    
    @staticmethod
    def array_to_counted_dict(arr):
        """
        Convert an array into a dictionary where keys are unique elements
        and values are the counts of those elements in the array.
        
        Parameters:
        arr (list): The input array to be converted.
        
        Returns:
        dict: A dictionary with unique elements as keys and their counts as values.
        """
        counted_dict = {}
        for item in arr:
            if item in counted_dict:
                counted_dict[item] += 1
            else:
                counted_dict[item] = 1
        return counted_dict

# Example usage:
#
#if __name__ == "__main__":
#    example_array = ["apple", "banana", "apple", "orange", "banana", "apple"]
#    converter = ArrayToCountedDict()
#    counted_dict = converter.array_to_counted_dict(example_array)
#    print(counted_dict)
    # Output: {'apple': 3, 'banana': 2, 'orange': 1}
