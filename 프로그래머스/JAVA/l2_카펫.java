import java.util.ArrayList;
import java.util.Arrays;

public class l2_카펫 {
    public static void main(String[] args){
        int brown =8;
        int yellow =1;
        int[] answer = solution(brown ,yellow);
    }
    public static int[] solution(int brown, int yellow) {
        int square = brown + yellow;
        ArrayList<int[]> canMake = new ArrayList<>();

        for (int i=1; i<=Math.sqrt(square); i++){
            int b = square/i;
            int check = square%i;
            if (check==0)
                System.out.println(b+" "+i);
                canMake.add(new int[] {b, i});
        }
        int[] answer = {0,0};
        for(int[] numbers : canMake){
            if (2*(numbers[0]+numbers[1]-2)==brown){
                answer[0] = numbers[0];
                answer[1] = numbers[1];
            }

        }
        System.out.println(Arrays.toString(answer));
        return answer;
    }
}
