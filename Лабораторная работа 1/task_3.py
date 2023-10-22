#Разделение игроков на две команды
players = ["Рафаэль", "Эмма", "Габриэль", "Люка", "Луиза", "Мишель"]
total = len(players)
sr_ind = int(total // 2)
team_1 = players[:sr_ind]
team_2 = players[sr_ind:]
print("Общее число игроков:", total)
print("Первая команда: ", team_1)
print("Вторая команда: ", team_2)
