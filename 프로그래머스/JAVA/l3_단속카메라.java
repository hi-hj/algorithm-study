import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class l3_단속카메라 {
    public static void main(String[] args){
        int[][] testRoutes = {{-20,15}, {-14,-5}, {-18,-13}, {-5,-3}};
        int testAnswer = solution(testRoutes);

    }
    public static int solution(int[][] routes){
        Arrays.sort(routes, (a,b) -> Integer.compare(a[1],b[1]));
        Queue<int[]> queue = new LinkedList();
        for (int[] route: routes){
            queue.add(route);
//            System.out.println(Arrays.toString(route));
        }
//        System.out.println(queue);
        int answer = 0;

        while(!queue.isEmpty()){
            int[] route = queue.poll();
            answer ++;
            int nowCamera = route[1];
            while(!queue.isEmpty()){
                int start = queue.peek()[0];
                int end = queue.peek()[1];
                if (start<=nowCamera && nowCamera<=end){
                    queue.poll();
                }
                else
                    break;
            }
        }
//        System.out.println(answer);
        return answer;
    }
}
