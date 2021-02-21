class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s : return 
        index = 0
        stack = []
        
        while index < len(s):
            if s[index] == "(":
                stack.append([s[index],index])
            elif s[index] == ")" and stack:
                if stack[-1][0] == "(":
                    stack.pop()
                else:
                    stack.append([s[index],index])
            elif s[index] == ")":
                stack.append([s[index],index])
            index += 1

        index_to_change = set()
        while stack:
            element , id = stack.pop()
            index_to_change.add(id)
            
            
        # generate a new string 
        print(index_to_change)
        new_str = ""
        for i in range(len(s)):
            if i not in index_to_change:
                new_str += s[i]
            else:
                new_str += "#"
        
        # join the string 

        new_string = ""
        for i in range(len(s)):
            if new_str[i] != "#":
                new_string += s[i]
        # return the new string
        return new_string

        
        