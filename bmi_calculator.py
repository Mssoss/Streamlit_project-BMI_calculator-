import streamlit as st  # type: ignore[import-not-found]
st.title("welcome to the calculator")

weight=st.number_input("Enter Your weight (in kgs)")

status=st.radio("Select your height format:",('cms','m','feet'))

bmi = None
if(status=='cms'):
  height=st.number_input("Enter your height (in cms)")
  try:
    bmi=weight/((height/100)**2)
  except ZeroDivisionError:
    st.text("Height cannot be zero. Please enter a valid height.")
  except TypeError:
    st.text("Please enter a valid height.")
  except Exception as e:
    st.text(f"An unexpected error occurred: {e}")
elif(status=='m'):
  height=st.number_input("Enter your height (in m)")
  try:
    bmi=weight/(height**2)
  except ZeroDivisionError:
    st.text("Height cannot be zero. Please enter a valid height.")
  except TypeError:
    st.text("Please enter a valid height.")
  except Exception as e:
    st.text(f"An unexpected error occurred: {e}")
else: 
  height=st.number_input('Enter your height (in feet)')
  try:
    bmi=weight/(((height/3.28))**2)
  except ZeroDivisionError:
    st.text("Height cannot be zero. Please enter a valid height.")
  except TypeError:
    st.text("Please enter a valid height.")
  except Exception as e:
    st.text(f"An unexpected error occurred: {e}")

if(st.button("Calculate BMI")):
  if bmi is not None and bmi > 0: 
      st.text(f"Your BMI is {bmi:.2f}")

      if(bmi<16):
        st.text("You are very underweight")
      elif(bmi>=16 and bmi<18.5):
        st.text("You are underweight")
      elif(bmi>=18.5 and bmi<25):
        st.text("You are Healthy")
      elif(bmi>=25 and bmi<30):
        st.text("You are overweight")
      elif(bmi>=30): # Corrected to be part of the elif chain
        st.text("You are suffering from obesity")
  else:
      st.text("Please enter valid weight and height to calculate BMI.")



      #for running this program
      #python -m streamlit run bmi_calculator.py