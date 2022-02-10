import streamlit as st
import pickle

# model="C:/Users/Sanika/sanika/saved_steps.pkl"
# dt= pickle.load(open(model, "rb")) 
def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

dt = load_model()

model_svm = dt["model"]
fatigue = dt["fatigue"]
malaise = dt["malaise"]
anorexia = dt["anorexia"]
liverBig = dt["liverBig"]
liverFirm = dt["liverFirm"]
ascites = dt["ascites"]
albu = dt["albu"]


def show_predict_page():
    st.title("Hepatitis Prediction")
    st.write("""#### ML Project on Hepatitis Prediction""")


    gender = (
        "Male",
        "Female",
        "Not to be Mention",
    )
    anorexia = ("None","Yes","No")
    ascites = ("None","Yes","No")
    fatigue = ("None","Yes","No")
    liverBig = ("None","Yes","No")
    liverFirm =("None","Yes","No")
    malaise =("None","Yes","No")

    gender = st.selectbox('Gender : ',gender)
    albu = st.text_input('Albu : ') 
    anorexia = st.selectbox("Anorexia : ",anorexia)
    ascites = st.selectbox("Ascites : ",ascites)
    fatigue = st.selectbox("Fatigue : ",fatigue)
    liverBig = st.selectbox("LiverBig",liverBig)
    liverFirm = st.selectbox("LiverFirm",liverFirm)
    malaise = st.selectbox("Malaise",malaise)
    age = st.slider("Age",1,100,1)

    fatigue = 2 if fatigue == 'Yes' else 1
    malaise = 2 if malaise == 'Yes' else 1
    anorexia = 2 if anorexia == 'Yes' else 1
    liverBig = 2 if liverBig == 'Yes' else 1
    liverFirm = 2 if liverFirm == 'Yes' else 1
    ascites = 2 if ascites == 'Yes' else 1
    albu = 2 if albu == 'Yes' else 1

    sub = st.button("Predict")
    if sub:
        target = model_svm.predict([[fatigue,malaise,anorexia,liverBig,liverFirm,ascites,albu]])
        #st.subheader(f"The Predicted Value is {target}")
        # st.subheader(f"{type(target)}")
        if target[0] == 2:
            target='Yes'
        else:
            target='No'
        
        st.subheader(f"Predicted Hepatitis as {target}")
