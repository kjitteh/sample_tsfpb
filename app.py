import streamlit as st
import pandas as pd
# import other packages


st.write("""
    # TSFPB Isolated Bridge Structural Response Predictor
    **Developed by:** Hanzlah Akhlaq 
    **Email:** hanzlahakhlaq@tongji.edu.cn""")


col1, col2 = st.columns(2)
with col1:
    c1, c2 = col1.columns([2, 3])
    c1.markdown('$\mu _l$')
    c1.markdown('$\mu _u$')
    c1.markdown('$R_m (mm)$')
    c1.markdown('$D_{th} (mm)$')
    c1.markdown('$K_p (kN/mm)$')
    c1.markdown('$S1 (g)$')
    c1.markdown('$S3 (g)$')
    c1.markdown('$S5 (g)$')
    ul = c2.number_input("$\mu l$", key='ul', label_visibility='collapsed')
    uu = c2.number_input("ga", key='uu', label_visibility='collapsed')
    rm = c2.number_input("$\mu l$", key='rm', label_visibility='collapsed')
    dt = c2.number_input("$\mu l$", key='dt', label_visibility='collapsed')
    kp = c2.number_input("$\mu l$", key='kp', label_visibility='collapsed')
    s1 = c2.number_input("$\mu l$", key='s1', label_visibility='collapsed')
    s3 = c2.number_input("a", key='s3', label_visibility='collapsed')
    s5 = c2.number_input("$\mu l$", key='s5', label_visibility='collapsed')

with col2:
    c3, c4 = col2.columns([2,3])
    c3.markdown('$\mu _m$')
    c3.markdown('$R_l (mm)$')
    c3.markdown('$R_u (mm)$')
    c3.markdown('$M_p (T)$')
    c3.markdown('$M_g (T)$')
    c3.markdown('$S2 (g)$')
    c3.markdown('$S4 (g)$')
    um = c4.number_input("$\mu m$", key='um', label_visibility='collapsed')
    rl = c4.number_input("$Rl (mm)$", key='rl', label_visibility='collapsed')
    ru = c4.number_input("$Ru (mm)$", key='ru', label_visibility='collapsed')
    mp = c4.number_input("$Mp (T)$", key='mp', label_visibility='collapsed')
    mg = c4.number_input("$Mg (T)$", key='mg', label_visibility='collapsed')
    s2 = c4.number_input("$S2 (g)$", key='s2', label_visibility='collapsed')
    s4 = c4.number_input("$S4 (g)$", key='s4', label_visibility='collapsed')


def clear():
    print('clearing')

st.write("""<h3 style="text-align:center">Prediction Results</h3>""", unsafe_allow_html=True)
_, result_left, result_right, _ = st.columns([1,3,2,1])
with result_left:
    st.markdown("Pier Force (kN):")
    st.markdown("<span style='text-align:right'>Pier Displacement (mm):<span>", unsafe_allow_html=True)
    st.markdown("Bearing Force (kN):")
    st.markdown("Bearing Displacement (mm):")

def predict():
    inputs_df = pd.DataFrame({'ul':ul,'um':um,'rl':rl,'rm':rm,'ru':ru,'dt':dt,'mp':mp,
        'kp':kp,'mg':mg,'s1':s1,'s2':s2,'s3':s3,'s4':s4,'s5':s5}, index=[0])
    # can add checks if inputs are proper e.g not equal to 0
    # results_df = model.predict(inputs_df)
    results_df = pd.DataFrame({'PF':23,'PD':0.32,'BF':12,'BD':1.4}, index=[0])
    with result_right:
        st.markdown(results_df['PF'][0])
        st.markdown(results_df['PD'][0])
        st.markdown(results_df['BF'][0])
        st.markdown(results_df['BD'][0])

_, left, right, _ = st.columns(4)
predict_btn = left.button('Predict', type='primary', use_container_width=True, on_click=predict)
clear_btn = right.button('Clear', use_container_width=True)


# adjust labels to be inline with input boxes
st.markdown("""
<style>
    [data-testid="stNumberInputContainer"], [data-testid="stMarkdownContainer"]>p {
        height: 2rem;
        line-height: 2rem;
    }
</style>
""", unsafe_allow_html=True)


