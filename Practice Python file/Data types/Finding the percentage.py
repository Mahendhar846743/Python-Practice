if __name__ == '__main__':
    n = int(input())
    print(n)
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    if query_name in student_marks.keys():
        x=student_marks.get(query_name)
        avg=sum(x)/len(scores)
        print("{:.2f}".format(avg))
    else:
        pass

# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika
#
# 56.00
