class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& A) {
        int oddPoint = 0;
        for (int i = 0; i < A.size(); i++) {
            if (A[i]%2 == 0) {
                swap(&A[i], &A[oddPoint]);
                oddPoint += 1;
            }
        }
        return A;
    }
    
    void swap(int* a, int* b) {
        int tmp = *a;
        *a = *b;
        *b = tmp;
    }
};
