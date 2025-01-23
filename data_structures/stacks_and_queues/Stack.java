package data_structures.stacks_and_queues;

class Node {
    String value;
    Node next;
    Node(String value) {
        this.value = value;
        this.next = null;
    }
}

class Stack {
    private Node top;
    private Node bottom;
    private int length;

    Stack() {
        this.top = null;
        this.bottom = null;
        this.length = 0;
    }

    public String peek() {
        return top != null ? top.value : null;
    }

    public void push(String value) {
        Node newNode = new Node(value);
        if (length == 0) {
            top = newNode;
            bottom = newNode;
        } else {
            Node holding = top;
            top = newNode;
            top.next = holding;
        }
        length++;
    }

    public void pop() {
        if (top == null) {
            return;
        }
        if (top == bottom) {
            bottom = null;
        }
        top = top.next;
        length--;
    }

    public String[] printList() {
        String[] result = new String[length];
        int index = 0;
        Node currentNode = top;
        while (currentNode != null) {
            result[index++] = currentNode.value;
            currentNode = currentNode.next;
        }
        return result;
    }

    // Returns a string representation of the queue for debugging purposes
    @Override
    public String toString() {
        StringBuilder result = new StringBuilder("{");
        result.append("\"top\": ").append(top != null ? top.value : "null").append(", ");
        result.append("\"bottom\": ").append(bottom != null ? bottom.value : "null").append(", ");
        result.append("\"length\": ").append(length);
        result.append("}");
        return result.toString();
    }

    public static void main(String[] args) {
        Stack stack = new Stack();
        stack.push("4");
        System.out.println(java.util.Arrays.toString(stack.printList()));
        stack.push("3");
        System.out.println(java.util.Arrays.toString(stack.printList()));
        stack.push("2");
        System.out.println(java.util.Arrays.toString(stack.printList()));
        stack.push("1");
        System.out.println(java.util.Arrays.toString(stack.printList()));
        stack.pop();
        System.out.println(java.util.Arrays.toString(stack.printList()));
        System.out.println("Peek: " + stack.peek());
        System.out.println("toString: " + stack.toString());
    }
}
