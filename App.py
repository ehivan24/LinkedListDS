__author__ = 'edwingsantos'


from LinkedListDS.LinkedList import LinkedList

linkedList = LinkedList()
linkedList.insertEnd(12)
linkedList.insertEnd(122)
linkedList.insertEnd(3)
linkedList.insertEnd(33)
linkedList.insertEnd(13)
linkedList.insertEnd(33)
linkedList.insertEnd(10)

linkedList.traverseList()
print("-"*50)
linkedList.remove(12)
print("-"*50)
linkedList.traverseList()
linkedList.remove(33)
print("-"*50)
linkedList.traverseList()

print ("size : %d " % linkedList.size())
linkedList.insertStart(24)
linkedList.traverseList()
linkedList.insertEnd(24)
linkedList.traverseList()