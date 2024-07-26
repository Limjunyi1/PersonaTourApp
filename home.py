import streamlit as st
from streamlit_option_menu import option_menu
from statics import home_statics


def run_home():
    """
    This function creates the home page. Edit the html in statics.py to change urls.
    """
    # Getting statics
    videos, packages, html_code, css_code = home_statics()


    # SECTION 1 (Suggested packages)
    st.subheader('Suggested Packages')

    cols = st.columns(len(packages))

    for i, col in enumerate(cols):
        with col:
            try:
                title = packages[i][0]
                url = packages[i][1]
                image = packages[i][2]
            except KeyError as exc:
                st.error(f"'{exc}' property missing for link #{i}")
                continue

            col.markdown(f'''
                            **<span style='font-size: 18px;'>{ title }</span>**
                            <a href='{url}'>
                            <img src='{image}' width=100% style='border-radius: 10px;'/>
                            </a>''',
                         unsafe_allow_html=True)
    st.write('''''')  # Space between links & Youtube Videos

    # SECTION 2 (AI generated itineraries)
    st.subheader('Pre-generated Itineraries (Japan)')

    st.markdown(css_code, unsafe_allow_html=True)
    st.markdown(html_code, unsafe_allow_html=True)

    # SECTION 3 (Suggested Videos)
    st.subheader('Suggested Videos')

    cols = st.columns(len(videos))

    for i, col in enumerate(cols):
        with col:
            try:
                title = videos[i][0]
                url = videos[i][1]
                image = videos[i][2]
            except KeyError as exc:
                st.error(f"'{exc}' property missing for link #{i}")
                continue

            col.markdown(f'''
                            **<span style='font-size: 18px;'>{ title }</span>**
                            <a href='{url}'>
                            <img src='{image}' width=100% style='border-radius: 10px;'/>
                            </a>''',
                         unsafe_allow_html=True)
    st.write('''''')  # Space between links & Youtube Videos


if __name__ == "__main__":
    run_home()
