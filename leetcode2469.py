class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        arr = []
        arr.append(celsius + 273.15) 
        arr.append(celsius * 1.80 + 32.00)
        return arr

a = Solution()
print(a.convertTemperature(celsius = 36.50))
print(a.convertTemperature(celsius = 122.11))
        
