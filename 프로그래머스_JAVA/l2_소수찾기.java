import java.util.HashSet;

public class l2_소수찾기 {
    public static void main(String[] args){
        String numbers = "17";
        int answer = solution(numbers);

    }

    public static int solution(String numbers){
        HashSet<Integer> set = new HashSet<>();
        permutation("", numbers, set);
        int count= 0;
        while(set.iterator().hasNext()){
            int a = set.iterator().next();
            set.remove(a);
            if(a==2) count++;
            if(a%2!=0 && isPrime(a)) count++;

        }

        return count;
    }

    public static boolean isPrime(int n ){
        if(n==0 || n==1) return false;
        for(int i=3; i<=(int)Math.sqrt(n); i++){
            if(n%i==0) return false;
        }
        return true;
    }

    public static void permutation(String prefix, String str, HashSet<Integer> set){
        int n = str.length();

        if(!prefix.equals("")) set.add(Integer.valueOf(prefix));
        for (int i =0; i<n; i++){
            permutation(prefix + str.charAt(i), str.substring(0,i)+str.substring(i+1,n), set);
        }
    }
}
