import java.util.Stack;

public class l2_큰_수_만들기 {
    public static void main(String[] args) {
        String testNumber = "4177252841";
        int testK = 4;
//        String testAnswer = solution(testNumber, testK);
        String testAnswer = solution2(testNumber, testK);
    }

    public static String solution2(String number, int k) {
        char[] result = new char[number.length() - k];
        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < number.length(); i++) {
            char c = number.charAt(i);
            while (!stack.isEmpty() && stack.peek() < c && k-- > 0) {
                stack.pop();
            }
            stack.push(c);
        }
        for (int i =0; i<result.length; i++){
            result[i] = stack.get(i);
        }


        return new String(result);
    }
}


//    public static String solution(String number, int k) {
//
//        StringBuilder answer = new StringBuilder();
//
//        for(int i =0; i<number.length();i++){
////            System.out.println(number.charAt(i));
//            while (k>0){
//                if (answer.length()>0 && number.charAt(i) > answer.charAt(answer.length()-1)){
//                    answer.deleteCharAt(answer.length()-1);
//                    k -=1;
//                }
//                else
//                    break;
//            }
//            answer.append(number.charAt(i));
//        }
//        System.out.println(answer);
//        int answerLength = answer.length();
//
//        String stringAnswer = answer.toString();
//
//        if (k>0)
//            stringAnswer = answer.substring(0,answerLength-k);
//        System.out.println(stringAnswer);
//        return stringAnswer;
//    }

//}
