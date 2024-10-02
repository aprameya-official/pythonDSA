class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if(n==0):
            return True
        planted=0
        for i in range(len(flowerbed)):
            is_leftempty=(i==0)or(flowerbed[i-1]==0)
            is_rightempty=(i==len(flowerbed)-1) or (flowerbed[i+1]==0)
            
            if(flowerbed[i]==0 and is_leftempty and is_rightempty):
                flowerbed[i]=1
                planted+=1

                if(planted==n):
                    return True
        return False