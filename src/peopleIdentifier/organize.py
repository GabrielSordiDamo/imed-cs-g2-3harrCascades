import os
i = 1
for file_type in ['negatives']:

    for file_name in os.listdir(file_type):
        line = f'{file_type}/{file_name}\n'
        i += 1
        with open(f'{file_type}.txt', 'a') as appender:
            appender.write(line)
    print(i)
