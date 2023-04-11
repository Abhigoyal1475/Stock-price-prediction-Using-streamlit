@staticmethod
    def train_test_forecast_report(symb): 
        """Launch training and plot testing results and reports MAPE error, finally it plots forecasts up to the specified horizon"""
        if st.session_state.TRAIN_JOB or st.session_state.TRAINED:
            text=st.empty() # Because streamlit adds widgets sequentially, we have to reserve a place at the top (after the chart of part 1)
            bar=st.empty() # Reserve a place for a progess bar
            
            text.write('Training model ... ') 
            bar=st.progress(0)

            stock = Stock(symb) 
            bar.progress(10)
            TEST_INTERVAL_LENGTH=st.session_state.TEST_INTERVAL_LENGTH #Retrieve input from the user
            TRAIN_INTERVAL_LENGTH=st.session_state.TRAIN_INTERVAL_LENGTH

            stock.load_train_test_data(TEST_INTERVAL_LENGTH, TRAIN_INTERVAL_LENGTH) #load train test data into the stock object, it's using cache
            bar.progress(30)
            stock.train_prophet() #this is also using cache
            bar.progress(70)
            text.write('Plotting test results ...')
            fig = stock.plot_test()
            bar.progress(100)
            bar.empty() #Turn the progress bar object back to what it was before and empty container
            st.markdown(
                f"## {symb} stock forecasts on testing set, Testing error {round(stock.test_mape*100,2)}%"
            )
            st.plotly_chart(fig)
            text.write('Generating forecasts ... ')
            fig2=stock.plot_inference() #Generate forecasts and plot them (no cache but figures are not updated if their data didn't change)
            st.markdown(f'## Forecasts for the next {st.session_state.HORIZON} days')
            st.plotly_chart(fig2)
            text.empty()
            """The button click will trigger this code to run only once, 
               the following flag TRAINED will keep this block of code executing even after the click,
               it won't redo everything however because we are using cache. 
               this flag needs to be initialized to False in the session state in main.py before the button"""

            st.session_state.TRAINED=True 
        else:
            st.markdown('Setup training job and hit Train')