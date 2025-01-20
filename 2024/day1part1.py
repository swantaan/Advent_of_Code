def calculate_total_distance(file_path):
    with open(file_path, 'r') as f:
        left = []
        right = []
        
        lines = f.readlines()
        for line in lines:
            temp = line.split("   ")
            left.append(temp[0])
            right.append(temp[1])

    left.sort()
    right.sort()

    total_dist = 0
    for i in range(len(left)):
        dist = abs(int(left[i]) - int(right[i]))
        total_dist += dist

    return total_dist

if __name__ == "__main__":
    file_path = "input.txt"
    total_dist = calculate_total_distance(file_path)
    print(total_dist)
