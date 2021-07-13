

public class l2_주식가격 {
    static class Stock{
        int index;
        int price;
        public Stock(int index, int price){
            this.index = index;
            this.price = price;
        }
    }

    public static void main(String[] args){
        int[] prices = {1,2,3,2,3};
        int[] answer = solution(prices);
    }

    public static int[] solution(int[] prices){
        int len = prices.length;
        int[] answer = new int[len];
        int i, j;
        for (i = 0; i < len; i++) {
            for (j = i + 1; j < len; j++) {
                answer[i]++;
                if (prices[i] > prices[j])
                    break;
            }
        }
        return answer;


//        Stack<Stock> stack = new Stack<>();
//        int[] answer = new int[prices.length];
//
//        for (int i =0; i<prices.length; i++){
////            System.out.println("now "+ i +" "+ prices[i]);
////            System.out.print("stack ");
////            for (Stock test : stack){
////                System.out.print("("+test.price + "," + test.index +") ");
////            }
////            System.out.println();
//
//
//
//            if (stack.isEmpty() || stack.peek().price <= prices[i])
//                stack.push(new Stock(i, prices[i]));
//            else {
//                while (stack.peek().price > prices[i]) {
//                    Stock now = stack.pop();
//                    int nowIndex = now.index;
//                    int nowPrice = now.price;
//                    answer[nowIndex] = i - nowIndex;
//                }
//                stack.push(new Stock(i, prices[i]));
//            }
//        }
////        for (Stock test : stack){
////            System.out.print("("+test.price + "," + test.index +") ");
////        }
//        while (!stack.isEmpty()){
//            Stock now = stack.pop();
//            answer[now.index] = prices.length - now.index-1;
//        }
////        System.out.println(Arrays.toString(answer));
//        return answer;
    }
}
