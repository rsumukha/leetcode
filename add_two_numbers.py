# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
        self.val = x
        self.next = None

def printlist(node):
	i=0
	temp=node
	while node!=None:
		i+=1
		node=node.next

	for e in range(0,i):
		print(temp.val)
		temp=temp.next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        list1=[]
        list2=[]
        while l1!=None or l2!=None:        	
        	if l1!=None:
        		list1.append(str(l1.val))
        		l1=l1.next
        	if l2!=None:
        		list2.append(str(l2.val))
        		l2=l2.next
        list1.reverse()
        list2.reverse()
        ret_num=int(''.join(list1))+int(''.join(list2))
        ret_list=[int(i) for i in str(ret_num)]
        temp=ListNode(None)
        for num in ret_list:
        	newnode=ListNode(num)
        	newnode.next=temp.next
        	temp.next=newnode

        return temp.next

temp1=ListNode(None)
temp1.next=None
temp2=ListNode(None)
temp2.next=None


n=raw_input("enter n1")
for num in range(0,int(n)):
	val=raw_input("enter the nums")
	l=ListNode(int(val))
	l.next=temp1.next
	temp1.next=l
m= raw_input("enter n2")
for num2 in range(0,int(m)):
	val2=raw_input("enter the nums")
	l2=ListNode(int(val2))
	l2.next=temp2.next
	temp2.next=l2

obj=Solution()
#printlist(temp1.next)
#printlist(temp2.next)

x=obj.addTwoNumbers(temp1.next,temp2.next)
printlist(x)




