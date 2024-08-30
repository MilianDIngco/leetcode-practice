class MinStack {

    /*
     * Used a Linked list since thats the only way to have O(1) insertion
     */
    public class Node {
        int value;
        Node prev = null;
        Node prevMin = null;

        Node() {

        }

        Node(int value) {
            this.value = value;
        }

        Node(int value, Node prev) {
            this(value);
            this.prev = prev;
        }
    }

    private Node top, minTop;
    private int length;

    public MinStack() {
        length = 0;
        top = null;
        minTop = null;
    }

    /*
     * @val int value added to the top of the stack
     */
    public void push(int val) {

        Node temp = new Node(val, top);
        if (top == null) {
            minTop = temp;
            top = temp;
        } else {
            temp.prev = top;
            top = temp;
            if (temp.value <= minTop.value) {
                temp.prevMin = minTop;
                minTop = temp;
            }
        }

    }

    /*
     * Removes the top most node from the stack
     */
    public void pop() {
        if (top == minTop)
            minTop = minTop.prevMin;
        top = top.prev;
    }

    /*
     * Returns value of the topmost node of the stack
     */
    public int top() {
        if (top != null)
            return top.value;
        else
            return -1;
    }

    /*
     * Returns the minimum value of the stack
     */
    public int getMin() {
        if (minTop != null)
            return minTop.value;
        else
            return -1;
    }

    public String toString() {
        Node temp = top;
        String stack = "";
        stack += "Stack: \n";
        while (temp != null) {
            stack += " " + temp.value + " ";
            temp = temp.prev;
        }
        stack += "\nMinStack: \n";
        temp = minTop;
        while (temp != null) {
            stack += " " + temp.value + " ";
            temp = temp.prevMin;
        }
        stack += "\n------------------------";

        return stack;
    }

    public static void main(String[] args) {
        MinStack ms = new MinStack();

        ms.push(-3);
        ms.push(-2);
        ms.push(-1);
        System.out.println("PUSHED\n" + ms.toString());
        ms.pop();
        System.out.println("POPPED\n" + ms.toString());
        ms.push(-2);
        ms.push(-3);
        System.out.println("PUSHED\n" + ms.toString());
        ms.pop();
        System.out.println("POPPED\n" + ms.toString());
        System.out.println("TOP\n" + ms.top());
        System.out.println("MIN\n" + ms.getMin());

    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */