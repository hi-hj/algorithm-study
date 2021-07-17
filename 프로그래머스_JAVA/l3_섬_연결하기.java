import java.util.Arrays;
import java.util.HashSet;

public class l3_섬_연결하기 {
    public static void main(String[] args){
        int[][] testCosts = {{0,1,1},{0,2,2},{1,2,5},{1,3,1},{2,3,8}};
        int testN = 4;
        int testAnswer = solution(testN, testCosts);

    }

    public static int solution(int n, int[][] costs){
        Arrays.sort(costs, (a,b) -> Integer.compare(a[2],b[2]));
//        Arrays.sort(costs, new Comparator<int[]>() {
//            @Override
//            public int compare(int[] o1, int[] o2) {
//                return o1[2]- o2[2];
//            }
//        });
        HashSet<Integer> visited = new HashSet<>();
        visited.add(costs[0][0]);
        int answer = 0;
        while (visited.size() < n){
            for(int i=0; i<costs.length; i++){
                if (visited.contains(costs[i][0]) && visited.contains(costs[i][1]))
                    continue;
                if (visited.contains(costs[i][0]) || visited.contains(costs[i][1])){
                    visited.add(costs[i][0]);
                    visited.add(costs[i][1]);
                    answer += costs[i][2];
                    costs[i] = new int[] {-1,-1,-1};
                    break;
                }
            }
        }
        System.out.println(answer);
//        for(int[] cost:costs){
//            System.out.println(Arrays.toString(cost));
//        }
//        System.out.println(Arrays.toString(costs));
//        int answer =. 0;
        return answer;
    }
}
