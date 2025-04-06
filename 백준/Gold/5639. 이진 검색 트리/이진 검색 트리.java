import java.io.*;
import java.util.*;



class Node{
    Node right;
    Node left;
    int value;
    Node(int value){
        this.value = value;
    }
    void insert(int newValue){
        if(newValue < this.value){
            if(this.left  == null){
                this.left = new Node(newValue);
            }
            else{
                this.left.insert(newValue);
            }
        }
        else{
            if(this.right == null){
                this.right = new Node(newValue);
            }
            else{
                this.right.insert(newValue);
            }
        }
    }
}

public class Main {

    public static void main(String[] args) throws IOException {
        File file = new File("input.txt");
        BufferedReader br = file.exists()
                ? new BufferedReader(new FileReader(file))
                : new BufferedReader(new InputStreamReader(System.in));
        Node root = null;
        int rootValue = Integer.parseInt(br.readLine());
        root = new Node(rootValue);
        String line;
        while (true){
            line = br.readLine();
            if(line == null) break;
            root.insert(Integer.parseInt(line));
        }
        postOrder(root);
    }
    static void postOrder(Node node){
        if(node == null) return;
        postOrder(node.left);
        postOrder(node.right);
        System.out.println(node.value);
    }


}
