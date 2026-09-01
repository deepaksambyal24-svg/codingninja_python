# Given DataFrame as a dictionary
data = {
    "Math": [78, 82, 91, 65, 89],
    "Physics": [85, 79, 92, 88, 76],
    "Chemistry": [89, 94, 78, 88, 84],
    "Biology": [81, 85, 80, 77, 90]
}

# Write your code here


for key, value in data.items():
    sorted_value = sorted(value)
    min_value = (min(value))
    max_value = (max(value))
    mean_value = (sum(value) / len(value))

    l = len(sorted_value)
    istquartile_pos = l // 4

    ist_qur = sorted_value[int(istquartile_pos)]

    iind_quartile_pos = l // 2
    iind_qur = sorted_value[int(iind_quartile_pos)]

    iird_quartile_pos = (3 * l) // 4

    iird_qur = sorted_value[int(iird_quartile_pos)]

    print(f'Statistics for {key}:', end='\n')
    print(f'Min: {min_value}')
    print(f'Max: {max_value}')
    print(f'Mean: {mean_value:.2f}')
    print(f'25th Percentile: {ist_qur}')
    print(f'50th Percentile: {iind_qur}')
    print(f'75th Percentile: {iird_qur}')
    print()