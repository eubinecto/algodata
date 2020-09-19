package stacksandqueues.datastructs;

import org.junit.Assert;
import org.junit.Test;

public class LinkedListStackTest {

    @Test
    public void testPop() {
        // init a stack
        LinkedListStack<Integer> linkedListStack = new LinkedListStack<>();
        // to push
        int expected = 1;
        // push an element
        linkedListStack.push(expected);
        // asserts
        Assert.assertEquals(expected, (int) linkedListStack.pop());
        Assert.assertTrue(linkedListStack.isEmpty());

    }

    @Test
    public void testPush() {
        LinkedListStack<Integer> linkedListStack = new LinkedListStack<>();
        int expected = 1;
        Assert.assertTrue(linkedListStack.isEmpty());
        linkedListStack.push(expected);
        Assert.assertFalse(linkedListStack.isEmpty());
        Assert.assertEquals(expected, (int) linkedListStack.peek());
    }

    @Test
    public void testPeek() {
        LinkedListStack<Integer> linkedListStack = new LinkedListStack<>();
        int expected = 1;
        linkedListStack.push(expected);
        //asserts
        Assert.assertEquals(expected, (int) linkedListStack.peek());
        // peek does not pop the element
        Assert.assertEquals(expected, (int) linkedListStack.peek());
    }

    @Test
    public void isEmpty() {
        LinkedListStack<Integer> linkedListStack = new LinkedListStack<>();
        Assert.assertTrue(linkedListStack.isEmpty());
        linkedListStack.push(1);
        Assert.assertFalse(linkedListStack.isEmpty());
    }
}