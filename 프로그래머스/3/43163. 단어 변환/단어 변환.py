from collections import deque

def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    def oneword(word1, word2):
        diff_count = sum([1 for a, b in zip(word1, word2) if a != b])
        return diff_count == 1
    
    que = deque([(begin,0)])
    visited = set([begin])
    
    while que:
        nowWord, count = que.popleft()
        
        if nowWord == target:
            return count
        
        for word in words:
            if word not in visited and oneword(nowWord, word) :
                que.append((word,count+1))
                visited.add(word)
                
    return 0
    