import streamlit as st 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from streamlit_player import st_player

# ## -- Define the Page Config -- ##

## make a title 
st.title('Lunch \'n Learn')

## display some random metrics in 3 columns 
st.write('## Metrics')
col1, col2, col3 = st.columns(3)
col1.metric('Simplicity', '100%', '9999%')
col2.metric('Learning Curve', '0.1%', '-95.23%')
col3.metric('Time to learn', '1 Day', '-50.00%')

## create a set of 4 buttons in 4 columns
st.write('#### Buttons')
col1, col2, col3, col4 = st.columns(4)
bt1 = col1.button('This', key='button1')
bt2 = col2.button('is', key='button2')
bt3 = col3.button('very', key='button3')
bt4 = col4.button('Easy', key='button4')

## if button4 (bt4) is clicked, display a message with balloons 
if bt4:
    with st.expander("We can even hide stuff in containers!"):
        st.write('## Balloons')
        st.success('This is a success message!')
        st.balloons()

## create a set of 4 checkboxes in 4 columns
st.write('#### Checkboxes')
col1, col2, col3, col4 = st.columns(4)
cb1 = col1.checkbox('Customize', key='checkbox1')
cb2 = col2.checkbox('all', key='checkbox2')
cb3 = col3.checkbox('the', key='checkbox3')
cb4 = col4.checkbox('interactions', key='checkbox4')

## if all 4 checkboxes are checked, display an error message
if cb1 and cb2 and cb3 and cb4:
    with st.expander("There seems to be something here!"):
        st.error('You checked all the boxes! - Bold Move Cotton!')
        URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        # Embed a youtube video
        options = {
            "playing":True,
            "muted":False,
            "light":False,
            "loop":True,
            "controls":False,
        }

        event = st_player(URL, **options, key="youtube_player")


## make a header
st.header('Catching Title')

## make a subheader
st.subheader('Informative Subheader')


## make a latex markdown with an equation 
st.write("We can even have math equations:")
st.latex(r'''\alpha^2 + \beta^2 = \gamma^2''')
st.latex(r'''e^{i\pi} + 1 = 0''')

## put in a separator 
st.write('---')

## make a header
st.header('Generating Random Data')

## create three columns: min_range, max_range, and number of columns 
st.write('## Customize the data')
col1, col2, col3 = st.columns(3)
min_range = col1.number_input('Min Range', value=0, step=1)
max_range = col2.number_input('Max Range', value=100, step=1)
## slider for the number of columns 
num_cols = col3.slider('Number of Columns', min_value=1, max_value=100, value=3, step=1)

## create a dataframe with values filled with min_range, max_range, and the number of columns 
df = pd.DataFrame(np.random.randint(min_range, max_range, size=(100, num_cols)), columns=[str(x) for x in range(num_cols)])

## show the dataframe 
if st.button("Show Dataframe"): 
    st.dataframe(df)

## show some random graphs 
st.write('## Visualizations!!')

## 3 columns for 3 different graphs: line, bar, map 
col1, col2, col3 = st.columns(3)
line_graph = col1.button('Line Graph')
bar_graph = col2.button('Bar Graph')
map_graph = col3.button('Map')

if line_graph: 
    st.line_chart(df)

if bar_graph:
    st.bar_chart(df)


if map_graph:
    map_data = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])
    st.map(map_data)



## separator 
st.write('---')

## header for download buttons 
st.header('Download Data')

## make 3 columns: download data (csv), download data (json)
col1, col2 = st.columns(2)
# csv_download = col1.button('Download Data (CSV)')

## if csv_download is clicked, download the dataframe as a csv

col1.download_button(
    label="Download CSV",
    data=df.to_csv().encode('utf-8'),
    file_name='data.csv',
    mime='text/csv',
)

## if json_download is clicked, download the dataframe as a json
col2.download_button(
    label="Download JSON",
    data=df.to_json().encode('utf-8'),
    file_name='data.json',
    mime='text/json',
)
