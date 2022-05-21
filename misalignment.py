file1=open("output_file_ibm2.out")


line_number="1"

dict={}
for i in file1:
    new_line=i.split()
    if(int(new_line[0]) in dict):
        dict[int(new_line[0])].append((int(new_line[1]),int(new_line[2])))
    else:
        dict[int(new_line[0])]=[(int(new_line[1]),int(new_line[2]))]


file11=open("dev.key")
dict1={}
for i in file11:
    new_line=i.split()
    if(int(new_line[0]) in dict1):
        dict1[int(new_line[0])].append((int(new_line[1]),int(new_line[2])))
    else:
        dict1[int(new_line[0])]=[(int(new_line[1]),int(new_line[2]))]

match=[]
not_match=[]
for i in dict:
    dev_line=dict1[i]
    my_line=dict[i]
    out_scores=0
    for j in range(len(dev_line)):
        if(dev_line[j] in my_line):
            out_scores=out_scores+1
    threshold_gen=out_scores/len(dev_line)
    if(threshold_gen>0.95):
        match.append(i)
    if(threshold_gen<0.2):
        not_match.append(i)
# print(not_match)
# print(match)
print(dict1[196])
print(dict[196])

# t_myfile=[]
# t_dev_key=[]

# for i in dict:
#     print(i,dict[i])
#     if(i==line_number):
#         t_myfile.append(dict1[i])
# print(t_myfile)