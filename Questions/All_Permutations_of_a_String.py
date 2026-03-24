def find_permutations(s):
    res = []
    chars = list(s)
    used = [False] * len(chars)

    def backtrack(current_path):
        if len(current_path)==len(chars):
            res.append("".join(current_path))
            return
        
        for i in range(len(chars)):
            if used[i]:
                continue

            used[i] = True
            current_path.append(chars[i])

            backtrack(current_path)

            used[i] = False
            current_path.pop()

    backtrack([])
    return res

def find_permutations_with_dup(s):
    res = []
    chars = sorted(list(s))
    used = [False] * len(chars)

    def backtrack(current_path):
        if len(current_path)==len(chars):
            res.append("".join(current_path))
            return

        for i in range(len(chars)):
            if used[i]:
                continue

            if i>0 and chars[i]==chars[i-1] and not used[i-1]:
                continue

            used[i] = True
            current_path.append(chars[i])

            backtrack(current_path)

            used[i] =False
            current_path.pop()
    
    backtrack([])
    return res

if __name__=='__main__':
    print(find_permutations("abc"))
    print(find_permutations_with_dup("aab"))