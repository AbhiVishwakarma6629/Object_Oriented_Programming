public class RemoveVal {
    public static int removeElement(int[] nums, int val) {
        int k = 0;
        for (int num : nums) {
            if (num != val){
                nums[k] = num;
                k++;
            }
        }
    return k;
    }

    public static void main(String[] args) {
        int[] nums = {3,2,2,3};
        int val = 3;
        int newlength = removeElement(nums, val);
        System.out.println(newlength);
    }
}