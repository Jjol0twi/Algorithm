class Solution {
    fun solution(angle: Int): Int {
        return when (angle) {
//            in 1..91 -> 1
            in 1 until 90 -> 1
            90 -> 2
//            in 91..179 -> 3
            in 91 until 180 -> 3
            180 -> 4
            else -> 0
        }
        /*
        return if (angle > 0 && angle < 90) {
            1
        } else if (angle == 90) {
            2
        } else if (angle > 90 && angle < 180) {
            3
        } else if (angle == 180) {
            4
        } else {
            0
        }
        */
    }
}