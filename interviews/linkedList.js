// class LinkedList {
//     constructor(value) {
//         this.head = {
//             value: value,
//             next: null
//         }
//         this.tail = this.head;
//         this.size = 1;
//     }

//     addNode(data) {
//         let newNode = {
//             value: data,
//             next: null
//         }
//         this.tail.next = newNode;
//         this.tail = newNode;
//         this.size++;
//     }
//     deleteNode(index) {
//         let i = 1;
//         if (index === 0) {
//             let newHead = this.head.next;
//             this.head = newHead;
//         } else if (index >= this.size) {
//             return "Error: index out of bounds."
//         }
//         else {
//             let previousNode = this.head;
//             while (i < this.size - 1) {
//                 let currentNode = previousNode.next;
//                 let nextNode = currentNode.next;
//                 if (i === index) {
//                     previousNode.next = nextNode;
//                     break;
//                 }
//                 previousNode = currentNode;
//                 currentNode = nextNode;
//                 i++;
//             }
//             this.size--;
//             return this.head;
//         }
//     }
// }


// function reverseList(linkedList) {
//     let prevNode = null;
//     let currentNode = linkedList.head;
//     let nextNode = null;

//     while (currentNode != null) {
//         nextNode = currentNode.next;
//         currentNode.next = prevNode;
//         prevNode = currentNode;
//         currentNode = nextNode;
//     }
//     linkedList.head = prevNode;
//     return linkedList;
// }



// let linkedList = new LinkedList(100);
// linkedList.addNode(200);
// linkedList.addNode(300);
// linkedList.addNode(400);
// linkedList.addNode(500);
// linkedList.addNode(600);
// linkedList.addNode(700);
// linkedList.addNode(800);
// console.log(linkedList)
// // console.log(reverseList(linkedList))
for (i = 1; i <= 5; i++) {
    let j = i;
    console.log(j);
}