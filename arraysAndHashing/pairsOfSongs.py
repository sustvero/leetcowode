class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        # create dictionary
        durations = [0] * 60

        pairs = 0

        # populate dictionary
        for song in time:
            durations[song % 60] += 1

        # match normal pairs
        for i in range(1, 30):
            pairs += durations[i] * durations[60 - i]

        # match special pairs
        if durations[0] > 1:
            pairs += durations[0] * (durations[0] - 1) // 2
        if durations[30] > 1:
            pairs += durations[30] * (durations[30] - 1) // 2

        # return result
        return pairs
        