import streamlit as st
import random
import datetime
import qrcode
from PIL import Image, ImageDraw, ImageFont
import os
import re

st.title("ID CARD ")

d_date = datetime.datetime.now()
reg_format_date = d_date.strftime("%d-%m-%Y  ID CARD Generator  %I:%M:%S %p")

st.write(reg_format_date)

company = st.text_input('Enter School Name:')
name = st.text_input('Enter Your Full Name:')
gender = st.text_input('Enter Your Gender:')
age = st.number_input('Enter Your Age:', min_value=0, value=0)
dob = st.date_input('Enter Your Date Of Birth:')
blood_group = st.text_input('Enter Your Blood Group:')
No = st.text_input('Enter Your Mobile Number:')
address = st.text_input('Enter Your Address:')

# Validation functions
def validate_name(name):
    if not re.match(r"^[a-zA-Z\s]+$", name):
        st.warning("Invalid name. Name should only contain letters and spaces.")
        return False
    return True

def validate_phone_number(phone_number):
    if not re.match(r"^\d{10}$", phone_number):
        st.warning("Invalid phone number. Please enter a 10-digit number.")
        return False
    return True

def validate_blood_group(blood_group):
    if not re.match(r"^(A|B|AB|O)[+-]$", blood_group.upper()):
        st.warning("Invalid blood group. Please enter a valid blood group (e.g., A+, B-, AB+, O-).")
        return False
    return True

def validate_dob(dob):
    current_date = datetime.date.today()
    if dob > current_date:
        st.warning("Invalid Date of Birth. Date of Birth cannot be in the future.")
        return False
    return True

if st.button('Generate ID Card'):
    if not (validate_name(name) and validate_phone_number(No) and validate_blood_group(blood_group) and validate_dob(dob)):
        st.warning("Please correct the input errors and try again.")
    else:
        idno = random.randint(10000000, 90000000)  # Generate idno here

        image = Image.new('RGB', (1000, 900), (255, 255, 255))
        draw = ImageDraw.Draw(image)

        font = ImageFont.truetype('arial.ttf', size=45)

        os.system("")

        (x, y) = (50, 50)
        color = 'rgb(0, 0, 0)'  # black color
        font = ImageFont.truetype('arial.ttf', size=80)
        draw.text((x, y), company, fill=color, font=font)

        # Rest of your code for generating the ID card

        image.save(f'{name}.png')

        QR = qrcode.make(f'{company}\n{name}\n{idno}')
        QR.save(f'{idno}.bmp')

        ID = Image.open(f'{name}.png')
        QR = Image.open(f'{idno}.bmp')
        ID.paste(QR, (650, 350))

        ID.save(f'{name}.png')

        st.image(f'{name}.png')
