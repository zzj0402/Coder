class Solution:
    def longestCommonPrefix(self, array_of_strings) -> str:
        output = ''
        index = 0
        if len(array_of_strings) == 0 or array_of_strings[0] == '':
            return output
        if len(array_of_strings) == 1:
            return array_of_strings[0]
        while index < len(array_of_strings[0]):
            last_string_character = array_of_strings[0][index]
            for each_string in array_of_strings:
                if index < len(each_string):
                    if last_string_character != each_string[index]:
                        return output
                else:
                    return output
            output += last_string_character
            index += 1
        return output
