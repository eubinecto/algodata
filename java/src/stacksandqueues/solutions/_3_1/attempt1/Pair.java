package stacksandqueues.solutions._3_1.attempt1;

public class Pair<T> {
    private final T item;
    private final int idx;

    public Pair(T item, int idx) {
        this.item = item;
        this.idx = idx;
    }

    public T getItem() {
        return item;
    }

    public int getIdx() {
        return idx;
    }
}
