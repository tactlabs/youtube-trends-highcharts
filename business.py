import pandas as pd 

def get_data():

    # print(df['channel_title'].tolist())
    try:
        df2 = pd.read_csv('trends.csv')
    except pd.errors.EmptyDataError:
        print("No data in trends.csv !")
        df = pd.read_csv('CAYT.csv')
        Channels= df['channel_title'].tolist()
        count=df['channel_title'].value_counts(ascending=False).head(10)
        count.columns = ['channel', 'no']
        print("count",count)
        count.to_csv('trends.csv', index=True)
    df2 = pd.read_csv('trends.csv')
    df2.columns = ['channel', 'no']
    print("df2",df2)
    channels_name=df2['channel'].tolist()
    no=df2['no'].tolist()

    print("TEAMS TO LIST:",channels_name,"no of times in trending:",no)
    result_dict = {
        'channel'            : channels_name,
        'no'             : no
    }

    
    print(result_dict)

    return result_dict

def add_row(channels_name, no):

    df = pd.read_csv('trends.csv')
    df.columns = ['channel', 'no']
    new_row = {
         'channel': channels_name,
        'no': no
    }

    

    df = df.append(new_row, ignore_index=True)
    # df['no'] = df['no'].astype(int)
    print(df)
    # df.sort_values(by='no', ascending=False,ignore_index=True)

    df.to_csv('trends.csv',index=False)

if __name__ == "__main__":
    get_data()