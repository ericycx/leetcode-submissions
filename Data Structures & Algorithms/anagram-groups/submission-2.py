class Solution:


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output_list = []
        anagram_dict = {}
        # hashmap {anagram} -> [index]
        for i in range(len(strs)):
            # want to go through once, and categorize each anagram
            sortt = sorted(strs[i])
            sorted_word = "".join(sortt)
            if sorted_word not in anagram_dict:
                anagram_dict[sorted_word] = [strs[i]]
            else:
                anagram_dict[sorted_word].append(strs[i])
        for k in anagram_dict:
            output_list.append(anagram_dict[k])
        return output_list
            