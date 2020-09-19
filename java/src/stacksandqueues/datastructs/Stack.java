package stacksandqueues.datastructs;

// super class of all the stacks
// abstract class for the two classes (essentially an interface)
public interface Stack<T> {
    //abstract methods
    //public abstract is redundant, so they are omitted here.
    T pop();
    void push(T item);
    T peek();
    boolean isEmpty();
}
