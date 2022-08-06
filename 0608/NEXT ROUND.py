players = input("Кол-во участников, кол-во призовых мест, через пробел: ")
players = list(map(int, players.split()))
scores = input("Набранные очки, через прoбел: ")
scores = list(map(int, scores.split()))
scores = sorted(scores, reverse=True)
final = 0
sub = 0
for i in scores:
    if scores.index(i) <= players[1]:
        sub += 1
print(sub)
# http://codeforces.com/problemset/problem/158/A