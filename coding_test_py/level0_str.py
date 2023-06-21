# 문자열 str이 주어질 때, str을 출력하는 코드를 작성해 보세요.
# 제한
# 1 ≤ str의 길이 ≤ 1,000,000
# str에는 공백이 없으며, 첫째 줄에 한 줄로만 주어집니다.

str = input()
ln_str = len(str)
re = str.replace(" ", "")

if ln_str < 1:
    print("한 자 이상 입력해주세요.")
    str = input()

elif ln_str > 1000000:
    print("1000000자 이하로 입력해주세요.")
    str = input()

else:
    print(str)
    
    
# another result
str = input()
while True:
    if len(str) >= 1 and len(str) <= 10000000 and str != ' ':

        print(str)
        break
    else:
        continue

