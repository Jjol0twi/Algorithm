def main():
    angle = 1
    match angle:
        case 1..89:
            answer = 1
        case 90:
            answer = 2
        case 91:
            answer = 3
        case 180:
            answer = 4
        case _:
            answer = 0
    print(answer)


main()
