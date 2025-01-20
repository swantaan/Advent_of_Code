def calculate_similarity(file_path):
    with open(file_path, 'r') as f:
        left = []
        right = []
        
        lines = f.readlines()
        for line in lines:
            temp = line.split("   ")
            left.append(temp[0])
            right.append(temp[1])

    total_similarity = 0
    for i in range(len(left)):
        similarity = int(left[i]) * right.count(left[i] + "\n")
        total_similarity += similarity

    return total_similarity

if __name__ == "__main__":
    file_path = "input.txt"
    similarity = calculate_similarity(file_path)
    print(similarity)
