import java.util.Arrays;
import java.util.LinkedList;

public class l2_구명보트 {
    public static void main(String[] args){
        int[] testPeople = {70,50,80,50};
        int testLimit = 100;
        int testAnswer = solution(testPeople, testLimit);
    }

    public static int solution(int[] people, int limit){
        // LinkedList와 Deque 비교
        // 둘다 맨앞/맨뒤 넣고빼고 O(1) 가능인데
        // LinkedList는 index로 값 가져오고, remove로 값 지우기 가능
        // deque는 불가능.. 근데 왜 쓰지?
        // https://chucoding.tistory.com/52
        Arrays.sort(people);
        LinkedList<Integer> linkedList = new LinkedList<>();
        for(int man : people){
            linkedList.push(man);
            System.out.println(man + " " + linkedList);
        }
        System.out.println(people);
        System.out.println(linkedList);
        int answer =  0;
        while (!linkedList.isEmpty()){
            int big = linkedList.pollFirst();
            answer ++;

            if(!linkedList.isEmpty() && big + linkedList.peekLast() <=limit)
                linkedList.pollLast();
//            for (int i=linkedList.size()-1; i>=0; i--){
////                int big = linkedList.get(i);
//                if (small + linkedList.get(i) <=limit){
////                    linkedList.remove()
//                    linkedList.remove(i);
//                    break;
//                }
//            }
        }
        System.out.println(answer);

        return answer;
    }
}
