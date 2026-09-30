class Solution:


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        newList = []
        for i in range(len(strs)):
            lst = sorted(strs[i])
            help = "".join(lst)
            if help not in hashMap:
                hashMap[help] = [i]
            else:
                hashMap[help].append(i)
        for k in hashMap:
            newList2 = []
            for index in hashMap[k]:
                newList2.append(strs[index])
            newList.append(newList2)
        return newList
