sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]

duplicate={}

for item in sample_list:
    duplicate[item] = duplicate.get(item, 0) + 1
    
result = [item for item, count in duplicate.items() if count > 1]

print(result)