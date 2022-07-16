money = int(input("Введите сумму:"))

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
tkb = money / 100 * per_cent['ТКБ']
skb = money / 100 * per_cent['СКБ']
vtb = money / 100 * per_cent['ВТБ']
sber = money / 100 * per_cent['СБЕР']
tkb, skb, vtb, sber = int(tkb), int(skb), int(vtb), int(sber)
result = [tkb, skb, vtb, sber]
print(result)
print("Максимальная сумма, которую вы можете заработать за год -", max(result))

