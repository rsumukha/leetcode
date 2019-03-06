package interview_prep;
import java.util.*;

 class ComponentNode{
	int value;
	ArrayList<ComponentNode> components=new ArrayList<ComponentNode>();
	ComponentNode(){}
	ComponentNode(int noLines){
		this.value=noLines;
	}
 }
 
 class AvgAtt{
	 int sum;
	 int count;
	 AvgAtt(){}
	 AvgAtt(int c, int sum){
		 this.sum=sum;
		 this.count=c;
	 }
 }
 class count{
	 int ct=0;
 }

public class MaxAvegNaryTree {
	ComponentNode root;
	HashMap<Integer, AvgAtt> hm=new HashMap<Integer, AvgAtt>();
	count c=new count();
	
	
	double calculateAvg(ComponentNode root) {
		
		if (root.components.size()==0) {
			hm.put(root.value, new AvgAtt(1,root.value));
			return root.value;
		}
		
		else {
			int sum=root.value;
			for(ComponentNode node: root.components) {
				sum+=calculateAvg(node);
			}
			hm.put(root.value, new AvgAtt(root.components.size(),sum));
			return sum;
		}
	}

	public static void main(String[] args) {
		MaxAvegNaryTree tree=new MaxAvegNaryTree();
		tree.root = new ComponentNode(200);
		ComponentNode n2=new ComponentNode(120);
		ComponentNode n3=new ComponentNode(100);
		
		ComponentNode n4 =new ComponentNode(80);
		ComponentNode n5=new ComponentNode(60);
		
		n2.components.add(n4);
		n3.components.add(n5);
		tree.root.components.add(n2);
		tree.root.components.add(n3);
		tree.c=new count();
		double sum = tree.calculateAvg(tree.root);
		System.out.println("end");
		for(Map.Entry<Integer, AvgAtt> entry : tree.hm.entrySet()) {
			System.out.println(entry.getKey() + ":"+ entry.getValue().sum+"&"+ entry.getValue().count);
		}
		
		
	}

}
