class StringUtils:
    """
    A class containing various string utility functions for manipulation and analysis.
    """

    @staticmethod
    def reverse_string(s):
        """
        Reverse the input string.
        
        Parameters:
        s (str): The string to reverse.
        
        Returns:
        str: The reversed string.
        """
        return s[::-1]

    @staticmethod
    def is_palindrome(s):
        """
        Check if the input string is a palindrome.
        
        Parameters:
        s (str): The string to check.
        
        Returns:
        bool: True if the string is a palindrome, False otherwise.
        """
        cleaned = ''.join(e for e in s if e.isalnum()).lower()
        return cleaned == cleaned[::-1]

    @staticmethod
    def count_vowels(s):
        """
        Count the number of vowels in the input string.
        
        Parameters:
        s (str): The string to analyze.
        
        Returns:
        int: The number of vowels in the string.
        """
        return sum(1 for char in s.lower() if char in 'aeiou')

    @staticmethod
    def count_consonants(s):
        """
        Count the number of consonants in the input string.
        
        Parameters:
        s (str): The string to analyze.
        
        Returns:
        int: The number of consonants in the string.
        """
        return sum(1 for char in s.lower() if char in 'bcdfghjklmnpqrstvwxyz')

    @staticmethod
    def to_uppercase(s):
        """
        Convert the input string to uppercase.
        
        Parameters:
        s (str): The string to convert.
        
        Returns:
        str: The string in uppercase.
        """
        return s.upper()

    @staticmethod
    def to_lowercase(s):
        """
        Convert the input string to lowercase.
        
        Parameters:
        s (str): The string to convert.
        
        Returns:
        str: The string in lowercase.
        """
        return s.lower()

    @staticmethod
    def capitalize_words(s):
        """
        Capitalize the first letter of each word in the input string.
        
        Parameters:
        s (str): The string to capitalize.
        
        Returns:
        str: The string with each word capitalized.
        """
        return ' '.join(word.capitalize() for word in s.split())

    @staticmethod
    def count_words(s):
        """
        Count the number of words in the input string.
        
        Parameters:
        s (str): The string to analyze.
        
        Returns:
        int: The number of words in the string.
        """
        return len(s.split())

    @staticmethod
    def remove_whitespace(s):
        """
        Remove all whitespace characters from the input string.
        
        Parameters:
        s (str): The string to process.
        
        Returns:
        str: The string with all whitespace removed.
        """
        return ''.join(s.split())

    @staticmethod
    def is_anagram(s1, s2):
        """
        Check if two strings are anagrams of each other.
        
        Parameters:
        s1 (str): The first string.
        s2 (str): The second string.
        
        Returns:
        bool: True if the strings are anagrams, False otherwise.
        """
        return sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower())

    @staticmethod
    def replace_substring(s, old, new):
        """
        Replace all occurrences of a substring with another substring in the input string.
        
        Parameters:
        s (str): The string to process.
        old (str): The substring to replace.
        new (str): The substring to replace with.
        Returns:
        str: The string with the replaced substrings.
        """
        return s.replace(old, new)

    @staticmethod
    def count_substring(s, sub):
        """
        Count the occurrences of a substring in the input string.
        
        Parameters:
        s (str): The string to search.
        sub (str): The substring to count.
        
        Returns:
        int: The number of occurrences of the substring.
        """
        return s.count(sub)

    @staticmethod
    def starts_with(s, prefix):
        """
        Check if the string starts with the given prefix.
        
        Parameters:
        s (str): The string to check.
        prefix (str): The prefix to look for.
        
        Returns:
        bool: True if the string starts with the prefix, False otherwise.
        """
        return s.startswith(prefix)

    @staticmethod
    def ends_with(s, suffix):
        """
        Check if the string ends with the given suffix.
        
        Parameters:
        s (str): The string to check.
        suffix (str): The suffix to look for.
        
        Returns:
        bool: True if the string ends with the suffix, False otherwise.
        """
        return s.endswith(suffix)

    @staticmethod
    def remove_punctuation(s):
        """
        Remove all punctuation from the input string.
        
        Parameters:
        s (str): The string to process.
        
        Returns:
        str: The string with all punctuation removed.
        """
        import string
        return s.translate(str.maketrans('', '', string.punctuation))

    @staticmethod
    def to_title_case(s):
        """
        Convert the input string to title case.
        
        Parameters:
        s (str): The string to convert.
        
        Returns:
        str: The string in title case.
        """
        return s.title()

    @staticmethod
    def swap_case(s):
        """
        Swap the case of all letters in the input string.
        
        Parameters:
        s (str): The string to process.
        
        Returns:
        str: The string with swapped case.
        """
        return s.swapcase()

    @staticmethod
    def remove_digits(s):
        """
        Remove all digits from the input string.
        
        Parameters:
        s (str): The string to process.
        
        Returns:
        str: The string with all digits removed.
        """
        return ''.join([i for i in s if not i.isdigit()])

    @staticmethod
    def contains_substring(s, sub):
        """
        Check if the string contains the given substring.
        
        Parameters:
        s (str): The string to check.
        sub (str): The substring to look for.
        
        Returns:
        bool: True if the string contains the substring, False otherwise.
        """
        return sub in s

    @staticmethod
    def split_string(s, delimiter=" "):
        """
        Split the string by the given delimiter.
        
        Parameters:
        s (str): The string to split.
        delimiter (str): The delimiter to use for splitting.
        
        Returns:
        list: A list of substrings.
        """
        return s.split(delimiter)
    
# Example usage:
#
#if name == "main":
#example_string = "Hello, world! This is a test string."
#utils = StringUtils()
#print(utils.reverse_string(example_string))
#print(utils.is_palindrome("A man a plan a canal Panama"))
#print(utils.count_vowels(example_string))
#print(utils.count_consonants(example_string))
#print(utils.to_uppercase(example_string))
#print(utils.to_lowercase(example_string))
#print(utils.capitalize_words(example_string))
#print(utils.count_words(example_string))
#print(utils.remove_whitespace(example_string))
#print(utils.is_anagram("listen", "silent"))
#print(utils.replace_substring(example_string, "world", "there"))
#print(utils.count_substring(example_string, "is"))
#print(utils.starts_with(example_string, "Hello"))
#print(utils.ends_with(example_string, "string."))
#print(utils.remove_punctuation(example_string))
#print(utils.to_title_case(example_string))
#print(utils.swap_case(example_string))
#print(utils.remove_digits("Th3 qu1ck br0wn f0x"))
#print(utils.contains_substring(example_string, "test"))
#print(utils.split_string(example_string)#)

### Explanation
#- **reverse_string**: Reverses the input string.
#- **is_palindrome**: Checks if the input string is a palindrome.
#- **count_vowels**: Counts the number of vowels in the input string.
#- **count_consonants**: Counts the number of consonants in the input string.
#- **to_uppercase**: Converts the input string to uppercase.
#- **to_lowercase**: Converts the input string to lowercase.
#- **capitalize_words**: Capitalizes the first letter of each word in the input string.
#- **count_words**: Counts the number of words in the input string.
#- **remove_whitespace**: Removes all whitespace characters from the input string.
#- **is_anagram**: Checks if two strings are anagrams of each other.
#- **replace_substring**: Replaces all occurrences of a substring with another substring in the input string.
#- **count_substring**: Counts the occurrences of a substring in the input string.
#- **starts_with**: Checks if the string starts with the given prefix.
#- **ends_with**: Checks if the string ends with the given suffix.
#- **remove_punctuation**: Removes all punctuation from the input string.
#- **to_title_case**: Converts the input string to title case.
#- **swap_case**: Swaps the case of all letters in the input string.
#- **remove_digits**: Removes all digits from the input string.
#- **contains_substring**: Checks if the string contains the given substring.
#- **split_string**: Splits the string by the given delimiter.