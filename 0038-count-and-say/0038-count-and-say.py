class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case: the first sequence is always "1"
        result = "1"
        
        # Generate the sequence iteratively from 2 to n
        for _ in range(1, n):
            current = result  # Store the current sequence
            result = ""       # Reset result to build the next sequence
            count = 1         # Start counting from the first character
            
            # Traverse the current sequence to generate the next one
            for j in range(1, len(current)):
                if current[j] == current[j - 1]:
                    # If the current character is the same as the previous one, increase the count
                    count += 1
                else:
                    # Append the count and the previous character to result
                    result += str(count) + current[j - 1]
                    count = 1  # Reset count for the new character
            
            # Don't forget to append the last counted group after the loop
            result += str(count) + current[-1]
        
        return result

        