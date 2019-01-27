class StockSpanner {
    private List<Integer> prices;
    private List<Integer> history;
    
    public StockSpanner() {
        prices = new ArrayList<>();
        history = new ArrayList<>();
        history.add(1);
    }
    
    public int next(int price) {
        prices.add(price);
        int num = findConsecutiveLength(prices, price);
        history.add(num);
        return num;
    }
    
    private int findConsecutiveLength(List<Integer> prices, int num) {
        int length = prices.size();
        int i = length - 1;
        while (i > 0 ) {
            if (prices.get(i-1) <= num) {
                i -= history.get(i);
            } else {
                break;
            }
        }
        
        return length - i;
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner obj = new StockSpanner();
 * int param_1 = obj.next(price);
 */