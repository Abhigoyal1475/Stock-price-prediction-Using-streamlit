#----part-1--------------------------------Session state intializations---------------------------------------------------------------

if "TEST_INTERVAL_LENGTH" not in st.session_state:
    # set the initial default value of test interval
    st.session_state.TEST_INTERVAL_LENGTH = 60

if "TRAIN_INTERVAL_LENGTH" not in st.session_state:
    # set the initial default value of the training length widget
    st.session_state.TRAIN_INTERVAL_LENGTH = 500

if "HORIZON" not in st.session_state:
    # set the initial default value of horizon length widget
    st.session_state.HORIZON = 60

#---------------------------------------------------------Train_test_forecast_splits---------------------------------------------------
st.sidebar.markdown("## Forecasts")
train_test_forecast_c = st.sidebar.container()

train_test_forecast_c.markdown("## Select interval lengths")
HORIZON = train_test_forecast_c.number_input(
    "Inference horizon", min_value=7, max_value=200, key="HORIZON"
)
TEST_INTERVAL_LENGTH = train_test_forecast_c.number_input(
    "number of days to test on and visualize",   
    min_value=7,
    key="TEST_INTERVAL_LENGTH",
)

TRAIN_INTERVAL_LENGTH = train_test_forecast_c.number_input(
    "number of  day to use for training",
    min_value=60,
    key="TRAIN_INTERVAL_LENGTH",
)


train_test_forecast_c.button(
    label="Train",
    key='TRAIN_JOB'
)
"""
part-3
Calling a static method in the Stock class to create a stock object, train prophet,test , forecast and plot. 
It's behavior depends on the session_state variables  linked to the widgets above. 
"""
Stock.train_test_forecast_report(SYMB)