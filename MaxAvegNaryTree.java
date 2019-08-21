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

public class MaxAvegNaryTree {
	ComponentNode root;
	HashMap<Integer, AvgAtt> hm=new HashMap<Integer, AvgAtt>();

	AvgAtt calculateAvg(ComponentNode root) {		
		if (root.components.size()==0) {
			//hm.put(root.value, new AvgAtt(1,root.value));
			return new AvgAtt(1, root.value);
		}		
		else {
			AvgAtt retAtt;
			int sum=root.value;
			int count=root.components.size();
			for(ComponentNode node: root.components) {
				retAtt=calculateAvg(node);
				sum+=retAtt.sum;
				count+=retAtt.count;
			}
			hm.put(root.value, new AvgAtt(count, sum));
			return new AvgAtt(count, sum);
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
		tree.calculateAvg(tree.root);
		float max=0;
		int maxAvg=0;
		for(Map.Entry<Integer, AvgAtt> entry : tree.hm.entrySet()) {
			 if (max < (entry.getValue().sum/entry.getValue().count)) {
				 max = entry.getValue().sum/entry.getValue().count;
				 maxAvg=entry.getKey();
				 }
		}
		System.out.println(maxAvg);		
	}
}
