import re

class StringToArray:
    """
    A class to convert a string into an array of words and punctuation in the same order as in the string.

    Attributes:
    -----------
    input_string : str
        The string to be converted.
    word_array : list
        An array where each element is a word or punctuation mark from the input string in the same order.
    """

    def __init__(self, input_string):
        """
        Initializes the StringToArray class with an input string.

        Parameters:
        -----------
        input_string : str
            The string to be converted into an array.
        """
        self.input_string = input_string
        self.word_array = self._string_to_array()

    def _string_to_array(self):
        """
        Converts the input string into an array of words and punctuation marks.

        The method separates words and punctuation and maintains their order.

        Returns:
        --------
        list
            An array of words and punctuation marks in the same order as they appear in the input string.
        """
        # Define a regex pattern to match words and punctuation
        pattern = re.compile(r'\b\w+\b|[.,!?:;(){}\[\]"\']')

        # Find all matches in the input string
        matches = pattern.findall(self.input_string)

        # Convert words to lowercase, keeping punctuation as is
        matches = [match.lower() if match.isalpha() else match for match in matches]
        
        return matches

    def get_word_array(self):
        """
        Returns the array of words and punctuation marks.

        Returns:
        --------
        list
            An array where each element is a word or punctuation mark from the input string.
        """
        return self.word_array

# Example usage:
#
#if __name__ == "__main__":
#    input_string = "Hello world! Hello, world."
#    string_to_array = StringToArray(input_string)
#    print(string_to_array.get_word_array())
