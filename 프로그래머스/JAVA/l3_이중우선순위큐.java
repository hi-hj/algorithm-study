import java.util.Arrays;
import java.util.Collections;
import java.util.PriorityQueue;

public class l3_이중우선순위큐 {
    public static void main(String[] args){

        String[] operations = {"I 7","I 5","I -5","D -1"};
        int[] answer = solution(operations);
        System.out.println(Arrays.toString(answer));

    }

    public static int[] solution(String[] operations) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

        for(String operation:operations){
            String input[] = operation.split(" ");
            switch(input[0]) {
                case "I":
                    minHeap.add(Integer.parseInt(input[1]));
                    maxHeap.add(Integer.parseInt(input[1]));
                    break;
                case "D":
                    if (minHeap.size()>0){
                        if(Integer.parseInt(input[1]) ==1){
                            // 최대값 삭제
                            int max = maxHeap.poll();
                            minHeap.remove(max);
                        }else{
                            // 최소값 삭제
                            int min = minHeap.poll();
                            maxHeap.remove(min);
                        }
                    }
                    break;
            }
        }
        int[] answer = {0,0};

        if(minHeap.size()>=2){
            answer[0] = maxHeap.poll();
            answer[1] = minHeap.poll();
        }
        System.out.println(Arrays.toString(answer));
        return answer;

    }
}
