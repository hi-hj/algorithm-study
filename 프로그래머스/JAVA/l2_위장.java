import java.util.HashMap;
import java.util.Iterator;

public class l2_위장 {
    public static void main(String[] args){
        String[][] clothes = {{"yellowhat", "headgear"}, {"bluesunglasses", "eyewear"}, {"green_turban", "headgear"}};
        int answer = solution(clothes);

    }
    public static int solution(String[][] clothes) {
        int answer = 1;

        HashMap<String, Integer> clothMap = new HashMap<>();

        for (String[] cloth : clothes){
            System.out.println(cloth[0]+" "+cloth[1]);

            clothMap.put(cloth[1], clothMap.getOrDefault(cloth[1],0)+1);
            System.out.println(clothMap);
        }
        Iterator<Integer> it = clothMap.values().iterator();

        while(it.hasNext()){
            answer *= it.next().intValue()+1;
        }
        return answer-1;
    }
}
