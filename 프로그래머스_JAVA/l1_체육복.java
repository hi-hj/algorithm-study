import java.util.HashSet;

public class l1_체육복 {

    public static void main(String[] args){
        int a = 5;
        int[] b = {2,4};
        int[] c = {1,3,5};
        int d = solution(a,b,c);
    }
    public static int solution(int n, int[] lost, int[] reserve) {
        int answer = n -lost.length;
        HashSet<Integer> realReserve = new HashSet<Integer>();
        for (int r:reserve){
            realReserve.add(r);
        }
        for(int i=0; i<lost.length; i++){
            if(realReserve.contains(lost[i])) {
                answer++;
                realReserve.remove(lost[i]);
                lost[i] = -1;
            }
        }
        for (int i=0; i<lost.length;i++){
            if(realReserve.contains(lost[i]-1)){
                answer++;
                realReserve.remove(lost[i]-1);
            }else if(realReserve.contains(lost[i]+1)){
                answer++;
                realReserve.remove(lost[i]+1);
            }
        }

        return answer;
    }
}
