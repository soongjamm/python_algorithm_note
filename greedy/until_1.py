
## 1
n, k = map(int, input().split())
answer = 0

while n != 1 :
  if n%k == 0:
    n/=k
  else :
    n-=1
  answer+=1
print(answer)

# ## 2
# n, k = map(int, input().split())
# answer = 0

# while n >= k :
#   while n%k != 0:
#     n -= 1
#     answer += 1
#   n //= k
#   answer += 1

# # 나눈 몫이 k보다 작아졌을 경우
# while n > 1 :
#   n -= 1
#   answer += 1

# print(answer)

    
