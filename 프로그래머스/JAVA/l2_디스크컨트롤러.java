import java.util.PriorityQueue;

public class l2_디스크컨트롤러 {
    public static void main(String[] args){
        int[][] jobs = {{0,3}, {1,9}, {2,6}};
        int answer = solution(jobs);
    }
    public static class Disk implements Comparable<Disk>{
        int getTime;
        int howLong;
        Disk(int getTime, int howLong){
            this.getTime = getTime;
            this.howLong = howLong;
        }

        @Override
        public int compareTo(Disk o) {
            return this.howLong - o.howLong;
        }

    }
    public static int solution(int[][] jobs) {
        int answer =0, now =0, index = 0;
        int start = -1;
        PriorityQueue<Disk> queue = new PriorityQueue<>();

        while (index < jobs.length){
            for(int[] job : jobs){
                if (start<job[0] && job[0]<=now)
                    queue.add(new Disk(job[0],job[1]));
            }

            if (queue.size() >0){
                Disk current = queue.poll();
                start = now;
                now += current.howLong;
                answer += (now-current.getTime);
                index +=1;
            }
            else
                now+=1;
        }
        return answer/jobs.length;

    }
}
