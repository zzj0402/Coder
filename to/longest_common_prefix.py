class Solution:
    def longestCommonPrefix(self, array_of_strings) -> str:
        output = ''
        index = 0
        while index < len(array_of_strings[0]):
            last_string_character = array_of_strings[0][index]
            for each_string in array_of_strings:
                if last_string_character != each_string[index]:
                    return output
            output += last_string_character
            index += 1
