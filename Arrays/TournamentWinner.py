def tournamentWinner(competitions, results):
    dic = {}
    win = ""
    points = 0
    for i in range(len(results)):
        currCompetition = competitions[i]
        winner = results[i]
        if winner == 0:
            if currCompetition[1] in dic:
                dic[currCompetition[1]] += 3
            else:
                dic[currCompetition[1]] = 3
            if dic[currCompetition[1]] > points:
                win = currCompetition[1]
                points = dic[currCompetition[1]]

        if winner == 1:
            if currCompetition[0] in dic:
                dic[currCompetition[0]] += 3
            else:
                dic[currCompetition[0]] = 3

            if dic[currCompetition[0]] > points:
                win = currCompetition[0]
                points = dic[currCompetition[0]]
    return win

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
        results = [0, 0, 1]
        expected = "Python"
        actual = tournamentWinner(competitions, results)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()