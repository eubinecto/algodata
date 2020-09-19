package stacksandqueues.datastructs;

import org.junit.Assert;
import org.junit.Test;

import java.util.Collections;
import java.util.stream.IntStream;

import static org.junit.Assert.*;

public class ArrayStackTest {

    @Test
    public void testEnsureSize() {
        // the default size is 10.
        ArrayStack<Integer> arrayStack = new ArrayStack<>();
        //Java's equivalent of python's range() function
        // https://stackoverflow.com/questions/3790142/java-equivalent-of-pythons-rangeint-int
        // using method reference for this.
        IntStream.range(0, 100)
                .forEach(arrayStack::push);
        // pop it, and assert it in reverse.
        // you would have to sort the stream in reversed order
        // https://www.techiedelight.com/generate-intstream-decreasing-order-java/
        IntStream.range(0, 100)
                .boxed()
                .sorted(Collections.reverseOrder())
                .forEach(
                        // action for for each expressed in lambda
                        num -> assertEquals(num, arrayStack.pop())
                );

    }

    @Test
    public void testPush() {
        ArrayStack<Integer> arrayStack = new ArrayStack<>();
        int expected = 1;
        Assert.assertTrue(arrayStack.isEmpty());
        arrayStack.push(expected);
        assertFalse(arrayStack.isEmpty());
        assertEquals(expected, (int) arrayStack.peek());
    }

    @Test
    public void testPop() {
        // init a stack
        ArrayStack<Integer> arrayStack = new ArrayStack<>();
        // to push
        int expected = 1;
        // push an element
        arrayStack.push(expected);
        // asserts
        assertEquals(expected, (int) arrayStack.pop());
        assertTrue(arrayStack.isEmpty());
    }

    @Test
    public void testPeek() {
        ArrayStack<Integer> arrayStack = new ArrayStack<>();
        int expected = 1;
        arrayStack.push(expected);
        //asserts
        assertEquals(expected, (int) arrayStack.peek());
        // peek does not pop the element
        assertEquals(expected, (int) arrayStack.peek());
    }

    @Test
    public void testIsEmpty() {
        ArrayStack<Integer> arrayStack = new ArrayStack<>();
        assertTrue(arrayStack.isEmpty());
        arrayStack.push(1);
        assertFalse(arrayStack.isEmpty());
    }
}