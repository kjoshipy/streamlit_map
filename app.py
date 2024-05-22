import streamlit as st
import pandas as pd
import plotly.express as px

#Run
#docker container using bash docker_script.sh
# streamlit run app.py --server.port=8501 --server.address=0.0.0.0
#Open http://localhost:8501/


def read_csv(file_path):
    df = pd.read_csv(file_path,
                     usecols=['wlbWellboreName', 'wlbNsDecDeg', 'wlbEwDesDeg',
                              'wlbDrillingOperator','wlbPurpose', 'wlbContent',
                              'wlbTotalDepth','wlbCompletionYear'])
    col_dict = {'wlbWellboreName':'wellName', 'wlbNsDecDeg':'latitude', 'wlbEwDesDeg':'longitude',
                  'wlbDrillingOperator':'drillingOperator', 'wlbPurpose':'purpose', 'wlbContent':'content',
                  'wlbTotalDepth':'depth', 'wlbCompletionYear':'completionYear'}
    df.rename(columns=col_dict, inplace=True)
    return df

def st_map(df):
    st.map(df, latitude='latitude' , longitude= 'longitude' )
def main():
    df = read_csv('wellbore_exploration_all.csv')
    # st.dataframe(df)
    st_map(df)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tbp = main()
    # print(tbp)

