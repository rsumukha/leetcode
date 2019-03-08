package interview_prep;

class Node {
	int value;
	Node left, right;
	Node (int v) {
		value=v;
		left=right=null;
	}
}	
	class count{
		int count=0;
	}

	class sum{
		int sum=0;
	}
public class AverageTree {
	Node root;
	count c=new count();
	sum s=new sum();
		
		
		void calAverage(Node node,sum s, count c) {
			if (node==null) {
				return ;
			}
			calAverage(node.left, s, c);
			s.sum = s.sum + node.value;
			c.count++;
			calAverage(node.right, s, c);
		}
		
		
	

	public static void main(String[] args) {
		AverageTree at=new AverageTree();
		at.root= new Node(1);
		at.root.left=new Node(2);
		at.root.right=new Node(3);
		at.root.left.right=new Node(4);
		at.calAverage(at.root, at.s, at.c);
		System.out.println(at.s.sum);
		// TODO Auto-generated method stub

	}

}
