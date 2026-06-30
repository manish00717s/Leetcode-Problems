from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0

        graph = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                graph[word[:i] + "*" + word[i+1:]].append(word)

        q = deque([(beginWord, 1)])
        seen = {beginWord}

        while q:
            word, steps = q.popleft()

            if word == endWord:
                return steps

            for i in range(len(word)):
                for nxt in graph[word[:i] + "*" + word[i+1:]]:
                    if nxt not in seen:
                        seen.add(nxt)
                        q.append((nxt, steps + 1))

        return 0