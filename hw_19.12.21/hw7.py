import json

companies = {}
pos_counr, pos_sum = 0, 0
with open('фирма.txt') as file:
    file_lines = file.readlines()
    for line in file_lines:
        data = line.split()
        profit = float(data[2]) - float(data[3])
        companies.update({data[0]: profit})
        if profit > 0:
            pos_counr += 1
            pos_sum += profit

average_profit = pos_sum / pos_counr
result = [companies, {'average_profit': average_profit}]

with open("result.json", 'w') as file:
    json.dump(result, file)
