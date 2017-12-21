def main():
    dot_num = int(input())
    arr = []

    for i in range(0, dot_num):
        x, y = input().split()
        arr.append([int(x),int(y)])

    if len(arr) == 1:
        print(arr[0][0], arr[0][1])
        return

    
    
if __name__ == "__main__":
    main()
