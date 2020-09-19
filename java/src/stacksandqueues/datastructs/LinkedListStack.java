package stacksandqueues.datastructs;

import java.util.EmptyStackException;

// using generic
/*
 * Stack is a LIFO data structure.
 * Last In First Out.
 * parameterised type T.
 */

// you must specify the parameterised type of the interface that this class implements
// https://stackoverflow.com/questions/15442508/interface-and-a-class-name-clash-same-erasure-yet-neither-overrides-other
public class LinkedListStack<T> implements Stack<T> {
    // inner data class for stack
    // houses data with the same generic data type T
    private static class LinkedList<T> {
        private final T data; // data is final
        private LinkedList<T> next; // but next node should not be final
        public LinkedList(T data) {
            this.data = data;
            // if not assigned, the value will be null.
            // here, next node is not assigned,so the value of it
            // is null
        } // constructor for stack node
    } // Stack Node
    //the stack node maintains this.
    //this initially points to null
    private LinkedList<T> top;


    /*
        TO-DO
        implement the following ADT interface for the stack
        pop()
        push(item)
        peek()
        isEmpty()
         */
    public T pop() {
        if (this.isEmpty()) {
            // Ha! so there is an exception class like this.
            throw new EmptyStackException();
        }
        T poppedData = this.top.data;
        this.top = this.top.next;
        return poppedData;
    }

    public void push(T item) {
        LinkedList<T> newNode = new LinkedList<>(item);
        newNode.next = this.top; // the top is the next one to the new node
        this.top = newNode; // newNode is now at the top
    }

    public T peek() {
        if (this.isEmpty()) {
            throw new EmptyStackException();
        }
        // just return the data
        return this.top.data;
    }

    public boolean isEmpty() {
        // how do I check if the stack is empty?
        // just check this out
        return this.top == null;
    }

}
