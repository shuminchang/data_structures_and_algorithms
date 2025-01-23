

class Node {
    int value;
    Node next;

    Node(int value) {
        this.value = value;
        this.next = null;
    }
}

class LinkedList {
    private Node head;
    private Node tail;
    private int length;

    LinkedList() {
        this.head = null;
        this.tail = null;
        this.length = 0;
    }

    @Override
    public String toString() {
        StringBuilder result = new StringBuilder();
        Node current = head;
        while (current != null) {
            result.append(current.value).append(" -> ");
            current = current.next;
        }
        return result.length() > 0 ? result.substring(0, result.length() - 4) : "";
    }

    public void add(int value) {
        Node newNode = new Node(value);
        if (head == null) {
            head = newNode;
            tail = newNode;
        } else {
            tail.next = newNode;
            tail = newNode;
        }
        length++;
    }

    public void prepend(int value) {
        Node newNode = new Node(value);
        if (length == 0) {
            head = newNode;
            tail = newNode;
        } else {
            newNode.next = head;
            head = newNode;
        }
        length++;
    }

    public void insert(int index, int value) {
        if (index >= length) {
            add(value);
            return;
        }
        if (index == 0) {
            prepend(value);
            return;
        }
        Node newNode = new Node(value);
        Node leading = traverseToIndex(index - 1);
        Node holding = leading.next;
        leading.next = newNode;
        newNode.next = holding;
        length++;
    }

    public void remove(int index) {
        if (index < 0 || index >= length) {
            throw new IndexOutOfBoundsException("Index out of bounds");
        }
        if (index == 0) {
            head = head.next;
            if (length == 1) {
                tail = null;
            }
        } else {
            Node leading = traverseToIndex(index - 1);
            Node unwanted = leading.next;
            leading.next = unwanted.next;
            if (index == length - 1) {
                tail = leading;
            }
        }
        length--;
    }

    public void reverse() {
        Node prev = null;
        Node currentNode = head;
        tail = head;

        while (currentNode != null) {
            Node next = currentNode.next;
            currentNode.next = prev;
            prev = currentNode;
            currentNode = next;
        }
        head = prev;
    }

    private Node traverseToIndex(int index) {
        int count = 0;
        Node currentNode = head;
        while (count != index) {
            currentNode = currentNode.next;
            count++;
        }
        return currentNode;
    }

    public int[] printList() {
        int[] result = new int[length];
        int index = 0;
        Node currentNode = head;
        while (currentNode != null) {
            result[index++] = currentNode.value;
            currentNode = currentNode.next;
        }
        return result;
    }

    public static void main(String[] args) {
        LinkedList myList = new LinkedList();
        myList.prepend(888);
        myList.add(1);
        myList.add(2);
        myList.add(3);
        myList.prepend(99);
        myList.insert(99, 88);
        myList.insert(0, 88);
        myList.insert(4, 88);

        System.out.println(java.util.Arrays.toString(myList.printList()));
        
        // Removing the element at index 88 will throw an error
        // Uncomment to see the exception:
        // myList.remove(88); 

        myList.remove(0);
        System.out.println(java.util.Arrays.toString(myList.printList()));

        myList.remove(3);
        System.out.println(java.util.Arrays.toString(myList.printList()));

        myList.reverse();
        System.out.println(java.util.Arrays.toString(myList.printList()));
        System.out.println("toString: " + myList.toString());
    }
}
