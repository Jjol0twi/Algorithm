fun solution(num1: Int, num2: Int): Int {
    if (!(num1 in -50000..50000 && num2 in -50000..50000)) {
        return -1
    }
    return num1 + num2
}