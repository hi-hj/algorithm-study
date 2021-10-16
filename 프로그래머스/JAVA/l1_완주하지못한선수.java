import java.util.*;

class l1_완주하지못한선수 {
    public static void main(String[] args){
        String[] participant = {"leo","kiki","eden"};
        String[] completion = {"eden","kiki"};
        String test = solution(participant, completion);
    }
    
    public static String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> hm = new HashMap<>();
        for(String player : participant) hm.put(player, hm.getOrDefault(player,0)+1);
        for(String player : completion) hm.put(player, hm.get(player)-1);

        for (String key : hm.keySet()){
            if(hm.get(key)!=0){
                answer = key;
            }
        }
        return answer;
//        LinkedList<String> partici = new LinkedList<>();
//        HashSet<String> comple = new HashSet<>();
//
//        for (String p : participant){
//            partici.add(p);
//        }
//        for (String c : completion){
//            comple.add(c);
//        }
//        System.out.println(partici);
//        System.out.println(comple);
//
//
//        for (String c : comple){
//            partici.remove(c);
//        }
//        System.out.println(partici);
//
//        return partici.get(0);

    }
}

