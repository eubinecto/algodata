package stacksandqueues.datastructs;

// implementing a stack with an array

import java.util.ArrayList;
import java.util.Arrays;
import java.util.EmptyStackException;

public class ArrayStack<T> implements Stack<T> {
    private static final int DEFAULT_CAPACITY = 10;
    private static final int RESIZE_FACTOR = 2;
    // instance variables
    private int size; // current size of the stack (this is essentially a "pointer")
    private Object[] dataArray;


    public ArrayStack() {
        //init the data Array with the default size
        this.dataArray = new Object[DEFAULT_CAPACITY];
        // the size starts with zero
        size = 0;
    }

    // if the array is full, then increase the capacity of the array
    public void ensureSize() {
        if (size == this.dataArray.length) {
            int newLength = this.dataArray.length * RESIZE_FACTOR;
            //update with the new copy of the new size
            this.dataArray = Arrays.copyOf(this.dataArray, newLength);
        }
    }

    @Override
    public void push(T item) {
        // insert the index, and then increment the size
        this.ensureSize(); // ensure the size of the array then store the item
        dataArray[size++] = item;
    }

    //but why does it complain about this?
    @Override
    @SuppressWarnings("unchecked")
    public T pop() {
        if (this.isEmpty()) {
            throw new EmptyStackException();
        }
        // first decrement the size, and then get the last inserted element
        T toReturn =  (T) this.dataArray[--size];
        //clear the stored element
        this.dataArray[size] = null;
        return toReturn;
    } // pop

    @Override
    @SuppressWarnings("unchecked")
    public T peek() {
        if (this.isEmpty()) {
            throw new EmptyStackException();
        }
        // just return the last inserted element
        return (T) this.dataArray[(this.size - 1)];
    } // peek

    @Override
    public boolean isEmpty() {
        return this.size == 0;
    }
}
