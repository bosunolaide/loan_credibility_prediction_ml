import pickle
import streamlit as st
 
# loading the trained model
pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome,  LoanAmount, Credit_History, Property_Area):   
 
    # Pre-processing user input    
    if Gender == "Female":
        Gender = 0
    else:
        Gender = 1
 
    if Married == "Unmarried":
        Married = 0
    else:
        Married = 1
        
    if Dependents == "0":
        Dependents = 0
    elif Dependents == "1":
        Dependents = 1
    elif Dependents == "2":
        Dependents = 2
    else:
        Dependents = 3
 
    if Education == "Undergraduate":
        Education = 0
    else:
        Education = 1
        
    if Self_Employed == "Not Self Employed":
        Self_Employed = 0
    else:
        Self_Employed = 1
        
    if Property_Area == "Rural Area":
        Property_Area = 0
    elif Property_Area == "Semi-Urban Area":
        Property_Area = 1
    else:
        Property_Area = 2
        
    if Credit_History == "Uncleared Debts":
        Credit_History = 0
    else:
        Credit_History = 1  
 
    # Making predictions 
    prediction = classifier.predict( 
        [[Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome,  LoanAmount, Credit_History, Property_Area]])
     
    if prediction == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:purple;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Loan Credibility Prediction App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    Gender = st.selectbox('Gender',("Male","Female"))
    Married = st.selectbox('Marital Status',("Unmarried","Married")) 
    Dependents = st.selectbox('Number of Dependents',("0","1","2","3+"))
    Education = st.selectbox('Education',("Undergraduate","Graduate")) 
    Self_Employed = st.selectbox('Employment Status',("Not Self Employed","Self Employed")) 
    ApplicantIncome = st.number_input("Applicant's Monthly income") 
    CoapplicantIncome = st.number_input("Co-Applicant's Monthly Income")
    LoanAmount = st.number_input("Total Loan Amount")
    Credit_History = st.selectbox('Credit_History',("Uncleared Debts","No Uncleared Debts"))
    Property_Area = st.selectbox('Property Location Area',("Rural Area","Semi-Urban Area", "Urban Area")) 
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome,  LoanAmount, Credit_History, Property_Area) 
        st.success('Your loan is {}'.format(result))
        print(LoanAmount)
     
if __name__=='__main__': 
    main()