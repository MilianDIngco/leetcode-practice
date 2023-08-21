//#include <stdlib.h>
#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    ListNode* ans = new ListNode;
    ListNode* temp = ans;
    bool carry = false;
    while(l1 != nullptr && l2 != nullptr) {
        int val = (carry) ? l1->val + l2->val + 1 : l1->val + l2->val;
        temp->val = val % 10;
        carry = (val > 9);
        if(l1->next == nullptr && l2->next == nullptr) {
            if(carry) 
                temp->next = new ListNode(1);
            return ans;
        }
        temp->next = new ListNode;//(l1->next != nullptr && l2->next != nullptr) ? new ListNode : nullptr;
        temp = temp->next;
        l1 = l1->next;
        l2 = l2->next;
    }

    while(l1 != nullptr) {
        int val = (carry) ? l1->val + 1 + temp->val : l1->val + temp->val;
        temp->val += val % 10;
        carry = val > 9;
        if(l1->next != nullptr) {
            temp->next = new ListNode;
            temp = temp->next;
        }
        l1 = l1->next;
    }
    while(l2 != nullptr) {
        int val = (carry) ? l2->val + 1 + temp->val : l2->val + temp->val;
        temp->val += val % 10;
        carry = val > 9;
        if(l2->next != nullptr) {
            temp->next = new ListNode;
            temp = temp->next;
        }
        l2 = l2->next;
    }
    if(carry)
        temp->next = new ListNode(1);

    return ans;
}

/*
123 + 456 = 

4 + 4 = 8 no carry from previous, no carry to next
5 + 5 = 0 no carry from previous, carry +1 to next
4 + 4 (+ 1) = carry +1 from prev, no carry to next
5 + 4 (+ 1) = carry + 1  from prev, carry +1 to next
*/

void printList(ListNode* t) {
    while(t != nullptr) {
        cout << (t->val);
        t = t->next;
    }
}

ListNode* fillList(ListNode* a, int num) {
    while(num > 0) {
        a->val = num % 10;
        num /= 10;
        a->next = (num > 0) ? new ListNode : nullptr;
        a = a->next;
    }
    return a;
}

int main(int argc, char const *argv[])
{
    ListNode* a = new ListNode();
    ListNode* b = new ListNode();
    int one = 5;
    int two = 5;
    fillList(a, one);
    fillList(b, two);
    ListNode* ans = addTwoNumbers(a, b);
    printList(a);
    cout << "+";
    printList(b);
    cout << "=";
    printList(ans);
    return 0;
}
