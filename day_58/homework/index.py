 1.
#include <iostream>
    using namespace std;
    
    // ფუნქცია Towers of Hanoi-ს ამოხსნაზე
    void towers_of_hanoi(int n, char source, char target, char auxiliary) {
        // ბაზის შემთხვევა: როდესაც დარჩა მხოლოდ ერთი დისკი
        if (n == 1) {
            cout  "Move disk 1 from "  source  " to "  target  endl;
            return;
        }
        
        // გადაადგილე n-1 დისკი საწყისი ღერძიდან auxiliary ღერძზე
        towers_of_hanoi(n - 1, source, auxiliary, target);
        
        // გადატანე ყველაზე დიდი დისკი საწყისი ღერძიდან მიზნობრივ ღერძზე
        cout "Move disk " n " from " source  " to "  target  endl;
        
        // გადაადგილე n-1 დისკი auxiliary ღერძიდან მიზნობრივ ღერძზე
        towers_of_hanoi(n - 1, auxiliary, target, source);
    }
    
    int main() {
        int n = 3; // დისკების რაოდენობა
        towers_of_hanoi(n, 'A', 'C', 'B'); // A - საწყისი, C - მიზნობრივი, B - დამხმარე ღერძი
        return 0;
    }
    2.
    def check_values_below_limit(arr, limit):
    return all(value <= limit for value in arr)
3.
import math

def minimal_people(handshakes):
    # Calculate the minimum number of people using the formula
    n = (1 + math.sqrt(1 + 8 * handshakes)) / 2
    return math.ceil(n)  # Round up to the nearest whole number
4.
def count_barcodes_with_double_digits(ndigit):
    # Define the range of numbers for ndigit barcodes
    start = 10**(ndigit - 1)
    end = 10**ndigit - 1

    # Counter for barcodes with double digits
    count = 0

    # Iterate through all numbers in the range
    for barcode in range(start, end + 1):
        barcode_str = str(barcode)
        # Check for any double digits
        if any(barcode_str[i] == barcode_str[i + 1] for i in range(len(barcode_str) - 1)):
            count += 1

    return count
5.
def arrayDiff(a, b):
    return [item for item in a if item not in b]
print(arrayDiff([1, 2], [1]))          # Output: [2]
print(arrayDiff([1, 2, 2, 2, 3], [2])) # Output: [1, 3]
print(arrayDiff([1, 2, 3], []))        # Output: [1, 2, 3]
print(arrayDiff([], [1, 2]))           # Output: []
def arrayDiff(a, b):
    b_set = set(b)
    return [item for item in a if item not in b_set]
