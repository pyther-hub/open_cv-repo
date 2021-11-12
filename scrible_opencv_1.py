import pickle
a = {2: 'g', 3: 'n'}
data1 = pickle.load(open('image_data_1.dat', 'rb'))
data2 = pickle.load(open('image_data.dat', 'rb'))
numb = len(data1)
data1_keys = list(data1.keys())
data1_val = list(data1.values())
data2_keys = list(data2.keys())
data2_val = list(data2.values())
print(numb)
for i in range(0, numb):
    if (data1_keys[i] == data2_keys[i]) and (data1_val[i] == data2_val[i]):
        if i % 100 == 0:
            print('yep')
        continue
    print(data1_keys[i], data1_val[i])
    print(data2_keys[i], data1_val[i])
