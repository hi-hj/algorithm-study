import java.util.Arrays;
import java.util.stream.IntStream;

public class l2_조이스틱 {

    public static void main(String[] args){
        String testName = "JAZ";
        int testAnswer = solution(testName);
    }
    public static int solution(String name) {
        char[] getName = name.toCharArray();
        int[] target = new int[getName.length];
        for(int i =0; i<target.length; i++){
            target[i] = Math.min(getName[i] -'A', 'Z'-getName[i]+1);
        }
        System.out.println(Arrays.toString(target));
        int nowIndex = 0;
        int count = 0;
        while(true){
//        while (IntStream.of(target).sum()!=0){
//            System.out.println(nowIndex + " "+Arrays.toString(target)+" "+count);
            if (target[nowIndex]!=0){
                count += target[nowIndex];
                target[nowIndex] = 0;
            }
            if (IntStream.of(target).sum()==0){
                break;
            }

                int leftCnt =0, rightCnt = 0;
                for(int i=0; i<target.length; i++){
                    leftCnt++;
                    if(target[(nowIndex-leftCnt+target.length)%target.length]!=0) break;
                }
                for(int i=0; i<target.length;i++){
                    rightCnt++;
                    if(target[(nowIndex+rightCnt+target.length)%target.length]!=0) break;
                }

                if (leftCnt<rightCnt){
                    nowIndex = (nowIndex-leftCnt+target.length)%target.length;
                    count += leftCnt;
                } else{
                    nowIndex = (nowIndex+rightCnt+target.length)%target.length;
                    count += rightCnt;
                }



        }
        System.out.println(count);
        return count;
    }
}
