import java.util.Arrays;
import java.util.Comparator;

public class l2_가장큰수 {
    public static void main(String[] args){
        int[] numbers = {3,30,34,5,9};
        String answer = solution(numbers);
    }

    public static String solution(int[] numbers){
        String[] nums = new String[numbers.length];
        for(int i=0; i<numbers.length; i++){
            nums[i] = numbers[i] +"";
        }
        System.out.println(Arrays.toString(nums));

        Arrays.sort(nums, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return (o2+o1).compareTo(o1+o2);
            }
        });

        String answer = "";
        for (String num:nums){
            answer += num;
        }
        return answer.charAt(0) =='0'? "0" : answer;

    }
}
