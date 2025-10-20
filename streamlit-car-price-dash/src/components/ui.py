from streamlit import st

def styled_button(label, key=None):
    return st.button(label, key=key, help="Click to " + label)

def styled_input(label, placeholder="", key=None):
    return st.text_input(label, placeholder=placeholder, key=key)

def styled_number_input(label, min_value=None, max_value=None, step=None, key=None):
    return st.number_input(label, min_value=min_value, max_value=max_value, step=step, key=key)

def styled_radio(label, options, key=None):
    return st.radio(label, options, key=key)

def styled_selectbox(label, options, key=None):
    return st.selectbox(label, options, key=key)

def styled_multiselect(label, options, key=None):
    return st.multiselect(label, options, key=key)

def styled_info(message):
    st.info(message)

def styled_subheader(label):
    st.subheader(label)