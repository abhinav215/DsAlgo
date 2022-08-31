class Solution:
    def isValid(self, txt: str) -> bool:
        lt = list(txt)
        # print(lt)
        stack = deque()
        ans = True
        start = ["[","(","{"]
        end = ["]",")","}"]
        for ele in lt:
            if ele=="[":
                stack.append("[")
            elif ele=="{":
                stack.append("{")
            elif ele=="(":
                stack.append("(")
            elif ele=="]":
                if len(stack)==0:
                        return False
                a = stack.pop()
                if a!="[":
                    ans = False
                    break
            elif ele=="}":
                if len(stack)==0:
                    return False
                a = stack.pop()
                if a!="{":
                    ans = False
                    break
            elif ele==")":
                if len(stack)==0:
                    return False
                a = stack.pop()
                if a!= "(":
                    ans = False
                    break
            if len(stack)!=0:
                return False
            return True