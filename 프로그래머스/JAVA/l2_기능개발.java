import java.util.ArrayList;
import java.util.Arrays;

public class l2_기능개발 {
    public static void main(String[] args){
        int[] progresses = {93,30,55};
        int[] speeds = {1,30,5};

        int[] answer = solution(progresses, speeds);
    }
    public static int[] solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> result = new ArrayList<>();

        int now = 0;
        int cnt = 0;

        while (now < progresses.length){
            cnt = 0;

            for (int i =0; i<progresses.length;i++){
                progresses[i] += speeds[i];
            }
            for (int i=now; i<progresses.length;i++){
                if (progresses[now]>=100){
                    cnt +=1;
                    now = i+1;
                }
            }
            if (cnt!=0){
                result.add(cnt);
            }
        }
        int[] answer = new int[result.size()];
        for (int i =0; i<result.size(); i++){
            answer[i] = result.get(i).intValue();
        }
        System.out.println(Arrays.toString(answer));
        return answer;
    }
}
