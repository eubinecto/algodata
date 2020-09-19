package stacksandqueues.solutions._3_1.attempt1;

import stacksandqueues.datastructs.Stack;

import java.util.Arrays;
import java.util.EmptyStackException;

public class SharedStack<T> implements Stack<T> {
    // reference to the global array
    private SharedArray<T> sharedArray;


    public SharedStack(SharedArray<T> sharedArray) {
        //get the global array on init
        this.sharedArray = sharedArray;
    }


    @Override
    public T pop() {
        if(this.isEmpty()) {
            throw new EmptyStackException();
        }

        // To-do: how?
        return null;
    }

    @Override
    public void push(T item) {
        //get next empty index. this maybe is maintained by a stack.
        int nextIdx = this.sharedArray.popNextIdx();
        Pair<T> toInsert = new Pair<>(item, nextIdx);
        this.sharedArray.insertPair(toInsert);
    }

    @Override
    public T peek() {
        return null;
    }


    @Override
    public boolean isEmpty() {
        return false;
    }
}
