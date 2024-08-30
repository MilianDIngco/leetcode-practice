#include <algorithm>
#include <iostream>

using namespace std;

struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {

  ListNode* temp1 = (list1->val <= list2->val) ? list1 : list2;
  ListNode* temp2 = (temp1 == list1) ? list2 : list1;
  ListNode* hold = temp2->next;
 
  while(temp1->next != nullptr && temp2->next != nullptr) {
    if(temp2->val <= temp1->next->val && temp1->val < temp2->val) {
      temp2->next = temp1->next;
      temp1->next = temp2;
      temp2 = hold;
      hold = temp2->next;
    } else {
      temp1 = temp1->next;
    }
  }

  if(temp1->next == nullptr) {
    temp1->next = temp2;
  } 

  

  return temp1;

}

void printList(ListNode* list) {
  ListNode* temp = list;
  while(temp != nullptr) {
    temp = temp->next;
  }

}

void deleteList(ListNode* list) {
  ListNode* temp = list->next;
  while(temp != nullptr) {
    delete list;
    list = temp;
    temp = temp->next;
  }
  delete list;
}

void addElement(ListNode* list, int val) {
  ListNode* temp = new ListNode(val);
  ListNode* a = list;

  while(a->next != nullptr) 
    a = a->next;
  
  a->next = temp;

}

int main (int argc, char *argv[]) {
  
  ListNode* a = new ListNode(1);
  addElement(a, 2);
  addElement(a, 4);

  ListNode* b = new ListNode(1);
  addElement(b, 3);
  addElement(b, 4);

  printList( mergeTwoLists(a,b) );

  deleteList(a);
  return 0;
  
}
