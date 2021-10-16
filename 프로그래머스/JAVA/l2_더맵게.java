import java.util.PriorityQueue;

public class l2_더맵게 {
    public static void main(String[] args){
        int[] scoville = {1,2,3,9,10,12};
        int K = 7;
        int answer = solution(scoville, K);
    }


    public static int solution(int[] scoville, int K){
        int count = 0;
        PriorityQueue<Integer> queue = new PriorityQueue<>();
        for (int food : scoville){
            queue.add(food);
        }

        while (queue.peek() <K){
            if (queue.size() ==1)
                return -1;
            count ++;
            int first = queue.poll();
            int second = queue.poll();

            int newFood = first + second*2;
            queue.add(newFood);
            // System.out.println(count+" "+newFood);
        }


        return count;
    }
}
