from typing import List

#Bu tarz "in-place" dizilim soruları, programlama dünyasında 
# her zaman İki İşaretçi (Two Pointers) adı verilen bir teknikle çözülür.

#Mantık şudur: Yeni bir liste açmak yerine, orijinal listenin içine iki tane ok (işaretçi) yerleştiririz.
#Sağ İşaretçi (R): Dizideki elemanları tek tek gezen bir kâşiftir. "Farklı" bir sayı bulana kadar ilerler.
#Sol İşaretçi (L): Kâşif farklı bir sayı bulduğunda, 
#o sayının orijinal dizide tam olarak nereye yerleştirileceğini (yedekleneceğini) gösteren konumdur.

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        L = 1
        for R in range(1, len(nums)):
            if nums[R] != nums[R - 1]:
                nums[L] = nums[R]
                L += 1
                
        return L

if __name__ == "__main__":
    cozum = Solution()
    
    ornek_nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    
    print(f"Orijinal Liste: {ornek_nums}")
    
    k = cozum.removeDuplicates(ornek_nums)
    
    print(f"Benzersiz Eleman Sayısı (k): {k}")
    print(f"Düzenlenmiş Liste: {ornek_nums[:k]}")

    