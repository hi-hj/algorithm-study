import java.util.*;

public class l2_다리를지나는트럭 {
    public static void main(String[] args){
        int bridge_length = 2;
        int weight = 10;
        int[] truck_weights = {7,4,5,6};

        int answer = solution(bridge_length, weight, truck_weights);
    }


    public static int solution(int bridge_length, int weight, int[] truck_weights) {
        Deque<Integer> bridge = new ArrayDeque<>();
        for(int i=0; i<bridge_length; i++){
            bridge.add(0);
        }

        int time = 0;
        int nowWeight = 0;
        Deque<Integer> waitTruck = new ArrayDeque<Integer>();
        for (int truck:truck_weights)
            waitTruck.add(truck);

        while (!waitTruck.isEmpty()){
            // MOVE
            int downTruck = bridge.pollLast();
            bridge.addFirst(0);

            if (downTruck!=0)
                nowWeight -= downTruck;

            if (nowWeight + waitTruck.peekFirst() <= weight){
                int truck = waitTruck.pollFirst();
                nowWeight += truck;
                bridge.pollFirst();
                bridge.addFirst(truck);
            }
            time +=1;
        }
        while (!bridge.isEmpty()){
            bridge.pollLast();
            time+=1;
        }
        System.out.println(time);
        return time;

    }
}
