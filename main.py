import streamlit as st
from streamlit_option_menu import option_menu

import login,new

st.set_page_config(
    page_title="Login Page",
    layout="centered"
)

class MultiApp:
    def __init__(self):
        self.apps = []
    def add_app(self,title,function):
        self.spps.append({
            "title": title, 
            "function": function
        })
    def run():
        with st.sidebar:
            selected_app = option_menu(
                menu_title='Menu',
                options=['Login','Main Page'],
                icons=[None, None], # optional
                menu_icon=None, # optional
                default_index=1,
                styles={
                    "Conatainer":{"padding":"5px"},
                    "Option": {"width": "200px"}
                }
            )
              