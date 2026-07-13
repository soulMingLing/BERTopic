flag_year=[]
for i in range(15):
    flag_year.append(0)
with open('师德师风切词.txt','r',encoding='utf8') as file:
    words_lines=file.readlines()
flag=0
for words_line in words_lines:
    flag=flag+1
    words_line=words_line.strip()
    if words_line=='二零一二年':
        flag_year[0]=flag
    elif words_line=='二零一三年':
        flag_year[1]=flag
    elif words_line=='二零一四年':
        flag_year[2]=flag
    elif words_line=='二零一五年':
        flag_year[3]=flag
    elif words_line=='二零一六年':
        flag_year[4]=flag
    elif words_line=='二零一七年':
        flag_year[5]=flag
    elif words_line=='二零一八年':
        flag_year[6]=flag
    elif words_line=='二零一九年':
        flag_year[7]=flag
    elif words_line=='二零二零年':
        flag_year[8]=flag
    elif words_line=='二零二一年':
        flag_year[9]=flag
    elif words_line=='二零二二年':
        flag_year[10]=flag
    elif words_line=='二零二三年':
        flag_year[11]=flag
    elif words_line=='二零二四年':
        flag_year[12]=flag
    elif words_line=='二零二五年':
        flag_year[13]=flag
    elif words_line=='二零二六年':
        flag_year[14]=flag
# for i in range(11):
#     print(flag_year[i])
time_years=[0,0,0,0,0,0,10,76,322,477,1576,279,270,20,0] #2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026
for i in range(14):
    time_years[i]=flag_year[i+1]-flag_year[i]
    if flag_year[i+1]==1 and flag_year[i]==0:
        time_years[i]=0
    if time_years[i]<0:
        print("该年份存在错误，请手动调整："+str(2012+i)+","+str(2012+i+1))
#print(len(words_lines))
time_years[14]=len(words_lines)-flag_year[14]+1
#print(time_years[10])
if flag_year[14]==0:
    print("该年份存在错误，请手动调整：2026")
lines=[]
year=2012
sum_num=0
for time_year in time_years:
    sum_num=sum_num+time_year
    for i in range(time_year):
        lines.append(str(year))
    year = year + 1
print(sum_num)
with open('师德师风时间.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(lines))