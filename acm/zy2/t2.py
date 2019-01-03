class Node(object):
    def __init__(self, value, next=None):
        self.value = value;
        self.next = next;


class Queue(object):
    # 链队列的数据结构
    # 队列中存在两个指针，一个头指针，一个尾指针，但是在这里就省去了，只留了一个尾指针

    def __init__(self):
        self.head = None

    def init_queue(self, data):

        self.head = Node(data[0])
        p = self.head
        for i in data[1:]:
            p.next = Node(i)
            p = p.next

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if (head is None) or (head.next is None):
            return 'true'

        middleNode = self.middleNode(head)
        slow = self.reverseList(middleNode)
        while slow is not None:
            if head.value != slow.value:
                return 'false'
            head = head.next
            slow = slow.next
        return 'true'

    def reverseList(self, head):
        if head is None:
            return None
        present = head
        new_head = None
        while present is not None:
            cur = present.next
            present.next = new_head
            new_head = present
            present = cur
        return new_head

    def middleNode(self, head):
        fast = head
        slow = head
        while (fast is not None) and (slow is not None):
            if fast.next is None:
                return slow
            elif (fast.next is not None) and (fast.next.next is None):
                return slow.next
            else:
                fast = fast.next.next
                slow = slow.next


if __name__ == '__main__':
    try:
        while True:
            arr = list(map(str, input().split()))
            arr = arr[1:]
            q = Queue()
            q.init_queue(arr)
            print(q.isPalindrome(q.head))
    except:
        exit(0)