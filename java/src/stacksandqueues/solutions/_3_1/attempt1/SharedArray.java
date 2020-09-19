package stacksandqueues.solutions._3_1.attempt1;

import stacksandqueues.datastructs.LinkedListStack;

import java.util.Arrays;
import java.util.Collections;
import java.util.stream.IntStream;

public class SharedArray<T> {
    private final static int DEFAULT_CAPACITY = 10;
    private final static int RESIZE_FACTOR = 2;
    private final LinkedListStack<Integer> nextIdxStack;
    private int size;
    private Pair<T>[] globalArray;

    @SuppressWarnings("unchecked")
    public SharedArray() {
        this.globalArray = (Pair<T>[]) new Pair[DEFAULT_CAPACITY];
        this.nextIdxStack = new LinkedListStack<>();
        this.size = 0;
        //init the empty indices
        IntStream.range(0, this.globalArray.length)
                 .boxed()
                 .sorted(Collections.reverseOrder())
                 .forEach(nextIdxStack::push);
    }

    public int popNextIdx() {
        return this.nextIdxStack.pop();
    }

    public void pushNextIdx(int idx) {
        this.nextIdxStack.push(idx);
    }

    public void insertPair(Pair<T> pair) {
        this.globalArray[pair.getIdx()] = pair;
        size++;
    }

    public Pair<T> pullPair(int idx) {
        Pair<T> toReturn =  this.globalArray[idx];
        this.globalArray[idx] = null;
        size--;
        return toReturn;
    }

    public boolean isFull() {
        return this.size == this.globalArray.length;
    }

    public void ensureSize() {
        if (this.isFull()) {
            int newCapacity = this.globalArray.length * 2;
            this.globalArray = Arrays.copyOf(this.globalArray, newCapacity);
        }
    }
}
