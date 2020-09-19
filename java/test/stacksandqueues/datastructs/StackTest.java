package stacksandqueues.datastructs;

import org.junit.Assert;
import org.junit.Test;

public class StackTest {

    @Test
    public void testPop() {
        // init a stack
        Stack<Integer> stack = new Stack<>();
        // to push
        int expected = 1;
        // push an element
        stack.push(expected);
        // asserts
        Assert.assertEquals(expected, (int) stack.pop());
        Assert.assertTrue(stack.isEmpty());

    }

    @Test
    public void testPush() {
        Stack<Integer> stack = new Stack<>();
        int expected = 1;
        Assert.assertTrue(stack.isEmpty());
        stack.push(expected);
        Assert.assertFalse(stack.isEmpty());
        Assert.assertEquals(expected, (int) stack.peek());
    }

    @Test
    public void testPeek() {
        Stack<Integer> stack = new Stack<>();
        int expected = 1;
        stack.push(expected);
        //asserts
        Assert.assertEquals(expected, (int) stack.peek());
        // peek does not pop the element
        Assert.assertEquals(expected, (int) stack.peek());
    }

    @Test
    public void isEmpty() {
        Stack<Integer> stack = new Stack<>();
        Assert.assertTrue(stack.isEmpty());
        stack.push(1);
        Assert.assertFalse(stack.isEmpty());
    }
}