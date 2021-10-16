import java.util.*;

public class l2_프린터 {
    public static void main(String[] agrs){
        int[] properties = {2,1,3,2};
        int location =2;
        int answer = solution(properties, location);
    }
    public static int solution(int[] priorities, int location) {
        Deque<Integer> queue = new ArrayDeque<>();
        Deque<Integer> numbers = new ArrayDeque<>();
        ArrayList<Integer> answer = new ArrayList<>();

        for (int i=0; i<priorities.length; i++){
            queue.add(priorities[i]);
            numbers.add(i);
        }

        while (!queue.isEmpty()){
            int nowPriority = queue.pollFirst();
            int nowIndex = numbers.pollFirst();
            System.out.println(nowIndex + " " + nowPriority);
            System.out.println(queue +" " + numbers);
            for (int priority : queue){
                if (priority > nowPriority){
                    queue.addLast(nowPriority);
                    numbers.addLast(nowIndex);
                    nowIndex = -1;
                    break;
                }
            }
            if (nowIndex >=0)
                answer.add(nowIndex);

        }
        System.out.println(answer);
        System.out.println(answer.indexOf(location));

        return answer.indexOf(location)+1;
    }
}
