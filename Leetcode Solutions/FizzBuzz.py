class Solution:
    def fizzBuzz(self, number: int) -> List[str]:
        lists = []
        for n in range(1, number + 1):
            if n % 3 == 0 and n % 5 == 0:
                lists.append("FizzBuzz")
            elif n % 3 == 0:
                lists.append("Fizz")
            elif n % 5 == 0:
                lists.append("Buzz")
            else:
                lists.append(str(n))
        return(lists)