import java.util.Arrays;

public class l2_Hindex {
    public static void main(String[] args){
        int[] citations = {3,0,6,1,5};
        int answer = solution(citations);
    }

    public static int solution(int[] citations){
        // Array 내림차순에 너무 집착
        // 파이썬 스타일대로 굳이 할 필요 없다.
        Arrays.sort(citations);
        int h = citations.length;
        while (h>=0){
            int cnt = 0;
            for (int i = citations.length-1; i>=0; i--){
                if (citations[i]>=h)
                    cnt ++;
                else
                    break;
            }

            System.out.println(h+" "+cnt);
            if (cnt>=h)
                break;
            h--;
        }
        return h;
    }
}
