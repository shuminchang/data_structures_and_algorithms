package data_structures.stacks_and_queues;

class Node {
    String value;
    Node next;
    Node(String value) {
        this.value = value;
        this.next = null;
    }
}

class Queue {
    private Node first;
    private Node last;
    private int length;

    Queue() {
        this.first = null;
        this.last = null;
        this.length = 0;
    }

    public String peek() {
        return first != null ? first.value : null;
    }

    public void enqueue(String value) {
        Node newNode = new Node(value);
        if (length == 0) {
            first = newNode;
            last = newNode;
        } else {
            last.next = newNode;
            last = newNode;
        }
        length++;
    }

    public void dequeue() {
        if (first == null) {
            return;
        }
        if (first == last) {
            last = null;
        }
        first = first.next;
        length--;
    }

    public String[] printList() {
        String[] result = new String[length];
        int index = 0;
        Node currentNode = first;
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
        result.append("\"first\": ").append(first != null ? first.value : "null").append(", ");
        result.append("\"last\": ").append(last != null ? last.value : "null").append(", ");
        result.append("\"length\": ").append(length);
        result.append("}");
        return result.toString();
    }

    public static void main(String[] args) {
        Queue queue = new Queue();
        queue.enqueue("David");
        System.out.println(java.util.Arrays.toString(queue.printList()));
        queue.enqueue("Jimmy");
        System.out.println(java.util.Arrays.toString(queue.printList()));
        queue.enqueue("Mary");
        System.out.println(java.util.Arrays.toString(queue.printList()));
        queue.dequeue();
        System.out.println(java.util.Arrays.toString(queue.printList()));
        System.out.println("Peek: " + queue.peek());
        System.out.println("toString: " + queue.toString());
    }
}
