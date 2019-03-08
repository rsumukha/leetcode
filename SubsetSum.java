package interview_prep;
import java.util.*;

public class SubsetSum {
	int[] al={10, 15, 25, 5, 3, 27, 22, 2, 28};
	static int sum_;
	ArrayList<ArrayList<Integer>> ans=new ArrayList<ArrayList<Integer>>();
	SubsetSum(int s){
		SubsetSum.sum_=s;
	}
	
	void subsetsum_b(int[] list, ArrayList<Integer> alreadyin) {
		int alreadyinSum=0;
		for (int j:alreadyin) {
			alreadyinSum+=j;
		}
		if (alreadyinSum==sum_) {
			ans.add(alreadyin);
			return;
		}
		if (list.length==0 || alreadyinSum>sum_) {
			return;
		}		
		ArrayList<Integer> temp=new ArrayList<Integer>(alreadyin); 
		alreadyin.add(list[0]);
		subsetsum_b(Arrays.copyOfRange(list, 1, list.length), alreadyin);
		subsetsum_b(Arrays.copyOfRange(list, 1, list.length), temp);

	}
	void subsetsum_dp() {		
	}

	public static void main(String[] args) {
		SubsetSum ss=new SubsetSum(30);
		ArrayList<Integer> temp=new ArrayList<Integer>();
		ss.subsetsum_b(ss.al, temp);
		ss.subsetsum_dp();	
		for (ArrayList<Integer> ll: ss.ans) {
			System.out.println(ll);
		}

	}

}
