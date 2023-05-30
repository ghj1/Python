# 파일 입출력과 예외처리
import os 

p = os.getcwd()
print(p)

# # 1 파일 쓰기 
# f = open("/Users/gimhyeonjeong/Documents/python/pyhton_100/종목1.txt", mode = "wt", encoding = "utf-8")
# f.write("005930\n")
# f.write("005380\n")
# f.write("035420")

# f = open("/Users/gimhyeonjeong/Documents/python/pyhton_100/종목2.txt", mode = "wt", encoding = "utf-8")
# f.write("005930 삼성전자\n")
# f.write("005380 현대차\n")
# f.write("035420 NAVER")

# # 2 csv 파일 쓰기 
# import csv
# f = open("매수종목.csv", mode="wt", encoding="utf-8", newline ='')
# writer = csv.writer(f)
# writer.writerow(["종목명", "종목코드", "PER"])
# writer.writerow(["삼성전자", "005930", 15.59])
# writer.writerow(["NAVER", "035420", 55.82])
# f.close()

# # 3 파일 읽어서 list에 저장 
# file = "/Users/gimhyeonjeong/Documents/python/pyhton_100/종목1.txt"
# f = open(file, mode="r", encoding="utf-8")
# li = []
# read = f.readlines()
# for i in read:
#     co = i.strip("\n")
#     li.append(co)
# print(li)

# f.close()


# # 4 파일 읽어서 dict에 저장
# file = "/Users/gimhyeonjeong/Documents/python/pyhton_100/종목2.txt"
# f = open(file, mode="r", encoding="utf-8")
# dic = {}
# li = []
# re = f.readlines()

# for i in re:
#     co = i.strip("\n")
#     cod = co.split(" ")
#     li.append(cod)
    
# for j in li:
#     dic[j[1]] = j [0]
    
# print(dic)
# f.close()

# # another results
# data = {}
# for line in lines:
#     line = line.strip()     # '\n' 제거
#     k, v = line.split()
#     #print(k, v)
#     data[k] = v

# print(data)
# f.close()
    
# 5