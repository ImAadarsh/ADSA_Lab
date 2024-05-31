#include <iostream>
using namespace std;

class tree {
public:
    // Constructor to initialize the node with given data
    tree(int data) : data_(data), left_(nullptr), right_(nullptr) {}

    // Member function to access the data stored in the node
    int getData() const { return data_; }

    // Member function to access the left subtree
    tree* getLeft() const { return left_; }

    // Member function to access the right subtree
    tree* getRight() const { return right_; }

    // Setter function to set the left subtree
    void setLeft(tree* left) { left_ = left; }

    // Setter function to set the right subtree
    void setRight(tree* right) { right_ = right; }

private:
    // Data stored in the node
    int data_;

    // Pointers to the left and right subtrees
    tree* left_;
    tree* right_;
};

tree* constructTree() {
    int data;
    cout << "Enter data for the node (enter -1 for NULL): ";
    cin >> data;

    if (data == -1) {
        return nullptr;
    }

    tree* newNode = new tree(data);
    cout << "Enter left child of " << data << ":\n";
    newNode->setLeft(constructTree());
    cout << "Enter right child of " << data << ":\n";
    newNode->setRight(constructTree());

    return newNode;
}

void printInorder(tree* root) {
    if (root != nullptr) {
        printInorder(root->getLeft());
        cout << root->getData() << " ";
        printInorder(root->getRight());
    }
}

int main() {
    // Construct the binary tree based on user input
    cout << "Enter data for the root node:\n";
    tree* root = constructTree();

    // Print the binary tree in inorder traversal
    cout << "Inorder traversal of the binary tree:\n";
    printInorder(root);

    return 0;
}
