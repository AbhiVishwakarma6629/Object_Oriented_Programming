public class RemoveDuplicates {
    public static int removeElement(int[] nums) {
        int k = 1;
        for (int i=1; i<nums.length;i++) {
            if (nums[i] != nums[i-1]) {
                nums[k] = nums[i];
                k++;
            }
        }
    return k;
    }
    public static void main(String[] args) {
        int[] nums = {1,1,2};
        System.out.println(removeElement(nums));
    }
}
