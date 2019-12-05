# https://www.hackerrank.com/challenges/python-lists/problem
if __name__ == '__main__':
    N = int(input())
    our_list = []
    for i in range(N):
        command = input()
        command = command.split()
        if command[0] == 'insert':
            our_list.insert(int(command[1]), int(command[2]))
        elif command[0] == 'print':
            print(our_list)
        elif command[0] == 'remove':
            our_list.remove(int(command[1]))
        elif command[0] == 'append':
            our_list.append(int(command[1]))
        elif command[0] == 'sort':
            our_list.sort()
        elif command[0] == 'pop':
            our_list.pop()
        else:
            our_list.reverse()

