import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from vis1 import Vis
import plotly.express as px
from pathlib import Path
import seaborn as sns
st.set_page_config(layout="wide")
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
print(Path(__file__).parent)
config = current_dir / '.streamlit' / 'config.toml'
with open(config, 'r'):
    pass
tab1, tab2, tab3, tab4 = st.tabs(["Power Bi", "Tableau", "Plotly", "Stats"])
with tab1:
    # components.html(r"""
    # <iframe title="Result" width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=464567ca-3427-4fc9-b9d0-32973b7ff055&autoAuth=true&ctid=d547ebda-f80d-409a-9fd2-d6381f024ee9" frameborder="0" allowFullScreen="true"></iframe>
    # """,height=None,width=None)

    st.write("""<iframe title="Result" width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=464567ca-3427-4fc9-b9d0-32973b7ff055&autoAuth=true&ctid=d547ebda-f80d-409a-9fd2-d6381f024ee9" frameborder="0" allowFullScreen="true"></iframe>""", unsafe_allow_html=True)

with tab2:
    components.html(r"""
<div class='tableauPlaceholder' id='viz1692202381894' style='position: relative'><noscript><a href='https:&#47;&#47;www.visualpathos.com&#47;home&#47;100-years-of-july-heat'><img alt='100 Years of July Heat ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;5Z&#47;5ZTNNTGM4&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='shared&#47;5ZTNNTGM4' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;5Z&#47;5ZTNNTGM4&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1692202381894');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='1274px';vizElement.style.height='845px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>    """,
                    height=800,width=1500)


with tab3:

    current_dir = Path(__file__).parent
    df_path = current_dir / 'Salesstore2.csv'

    df = pd.read_csv(df_path, encoding="ISO-8859-1", low_memory=False)
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    data = st.columns(2)
    with data[0]:
        Vis.visualize1(df)
    with data[1]:
        fig = px.scatter(df, x="Sales", y="Profit", animation_frame=df['Order Date'].dt.month, animation_group="Region",
                         size="Order_Quantity", color="Ship_Mode",
                     log_x=True, size_max=55, )
        fig.update_layout(
            title_text="Highlight Clusters",
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=False),
            plot_bgcolor='rgba(0, 0, 0, 0)',
            paper_bgcolor='rgba(0, 0, 0, 0)',
        )

        st.plotly_chart(fig)

   # x = st.slider('as')

with tab4:
    current_dir = Path(__file__).parent
    df_path = current_dir / 'Salesstore2.csv'
    df = pd.read_csv(df_path, encoding="ISO-8859-1", low_memory=False)
    df1 = pd.DataFrame(df.head(5))
    st.dataframe(df1)
    st.title('Order Priority Dist')
    figs = sns.countplot(df, x='Order_Priority')

    st.pyplot(figs.get_figure())

