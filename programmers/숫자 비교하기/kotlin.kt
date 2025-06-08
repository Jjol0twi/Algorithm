class Solution {
    fun solution(num1: Int, num2: Int): Int {
        return if (num1 in -50000..50000 && num2 in -50000..50000) {
            if (num1 == num2){
                1
            } else {
                -1
            }
        } else {
            0
        }
    }
}