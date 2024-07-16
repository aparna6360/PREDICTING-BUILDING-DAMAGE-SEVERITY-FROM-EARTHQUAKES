import pandas
import sklearn
import pickle
import streamlit as st
from PIL import Image
file1=open(r"C:\Users\USER\Downloads\eqproject.pkl",'rb')
dict1=pickle.load(file1)
print(dict1)
le_land_surface_condition=dict1['label_encoder']['land_surface_condition']
le_foundation_type=dict1['label_encoder']['foundation_type']
le_roof_type=dict1['label_encoder']['roof_type']
le_ground_floor_type=dict1['label_encoder']['ground_floor_type']
le_other_floor_type=dict1['label_encoder']['other_floor_type']
le_condition_post_eq=dict1['label_encoder']['condition_post_eq']
le_damage_grade=dict1['label_encoder']['damage_grade']
model=dict1['model']
scaling=dict1['scaler']

st.markdown(
    "<h1 style='color: darkblue;'>PREDICTING BUILDING DAMAGE SEVERITY FROM EARTHQUAKES</h1>",
    unsafe_allow_html=True
)
image = Image.open('2_noto-peninsula-earthquake-japan-24002056070583.png')
st.image(image, width=750)
age=st.text_input('Enter the Age of building:')
plinth_area=st.text_input('Enter the Plinth area square feet:')
height_pre=st.text_input('Enter the building height before earthquake:')
height_post=st.text_input('Enter the building height after earthquake:')
land_co=st.selectbox('land_surface_condition',('Flat','Moderate slope','Steep slope'))
fo_ty=st.selectbox('foundation_type',('Mud mortar-Stone/Brick','Bamboo/Timber','Cement-Stone/Brick','RC','Other'))
ro_ty=st.selectbox('roof_type',('Bamboo/Timber-Light roof','Bamboo/Timber-Heavy roof','RCC/RB/RBC'))
gr_fl_ty=st.selectbox('ground_floor_type',('Mud','RC','Brick/Stone','Timber','Other'))
oth_ty=st.selectbox('other_floor_type',('TImber/Bamboo-Mud','Timber-Planck','Not applicable','RCC/RB/RBC'))
has_superstructure_adobe_mud = st.checkbox("Has superstructure adobe mud")
adobe_mud = 1 if has_superstructure_adobe_mud else 0
st.write("has_superstructure_adobe_mud flag value:",adobe_mud)
has_superstructure_mud_mortar_stone=st.checkbox("Has superstructure mud mortar stone")
mud_mortar_stone=1 if has_superstructure_mud_mortar_stone else 0
has_superstructure_stone_flag=st.checkbox("Has superstructure stone flag")
stone_flag=1 if has_superstructure_stone_flag else 0
has_superstructure_cement_mortar_stone=st.checkbox("Has superstructure cement mortar stone")
cement_mortar_stone=1 if has_superstructure_cement_mortar_stone else 0
has_superstructure_mud_mortar_brick=st.checkbox("Has superstructure mud mortar brick")
mud_mortar_brick=1 if has_superstructure_mud_mortar_brick else 0
has_superstructure_cement_mortar_brick=st.checkbox("Has superstructure cement mortar brick")
cement_mortar_brick=1 if has_superstructure_cement_mortar_brick else 0
has_superstructure_timber=st.checkbox("Has superstructure timber")
timber=1 if has_superstructure_timber else 0
has_superstructure_bamboo=st.checkbox("Has superstructure bamboo")
bamboo=1 if has_superstructure_bamboo else 0
has_superstructure_rc_non_engineered=st.checkbox("Has superstructure rc non engineered")
rc_non_engineered=1 if has_superstructure_rc_non_engineered else 0
has_superstructure_rc_engineered=st.checkbox("Has superstructure rc engineered")
rc_engineered=1 if has_superstructure_rc_engineered else 0
has_superstructure_other=st.checkbox("Has superstructure other")
other=1 if has_superstructure_other else 0
con_post=st.selectbox('condition_post_eq',('Damaged-Not used','Damaged-Rubble unclear','Damaged-Used in risk','Damaged-Repaired and used','Damaged-Rubble clear','Not damaged','Damaged-Rubble Clear-New building built','Covered by landslide'))
pred=st.button('PREDICT')
def prediction(age_building,plinth_area_sq_ft,height_ft_pre_eq,height_ft_post_eq,land_surface_condition,foundation_type,roof_type,ground_floor_type,
       other_floor_type,has_superstructure_adobe_mud,has_superstructure_mud_mortar_stone,has_superstructure_stone_flag,has_superstructure_cement_mortar_stone,
       has_superstructure_mud_mortar_brick,has_superstructure_cement_mortar_brick,has_superstructure_timber,has_superstructure_bamboo,
       has_superstructure_rc_non_engineered,has_superstructure_rc_engineered,has_superstructure_other,condition_post_eq):
  land_surface_condition=le_land_surface_condition.transform([land_surface_condition])[0]
  foundation_type=le_foundation_type.transform([foundation_type])[0]
  roof_type=le_roof_type.transform([roof_type])[0]
  ground_floor_type=le_ground_floor_type.transform([ground_floor_type])[0]
  other_floor_type=le_other_floor_type.transform([other_floor_type])[0]
  condition_post_eq=le_condition_post_eq.transform([condition_post_eq])[0]
  input_data = [[age_building,plinth_area_sq_ft,height_ft_pre_eq,height_ft_post_eq,land_surface_condition,foundation_type,roof_type,ground_floor_type,
       other_floor_type,has_superstructure_adobe_mud,has_superstructure_mud_mortar_stone,has_superstructure_stone_flag,has_superstructure_cement_mortar_stone,
       has_superstructure_mud_mortar_brick,has_superstructure_cement_mortar_brick,has_superstructure_timber,has_superstructure_bamboo,
       has_superstructure_rc_non_engineered,has_superstructure_rc_engineered,has_superstructure_other,condition_post_eq]]
  input_data_scaled = scaling.transform(input_data)
  return model.predict(input_data_scaled)[0]

def display_prediction_result(result_text,text_color, background_color, border_color):
    st.markdown(
        f"""
        <div style="text-align: center; font-size: 34px; font-weight: bold; margin-top: 20px; color: {text_color};
                    background-color: {background_color};
                    border: 2px solid {border_color};
                    padding: 20px;
                    border-radius: 6px;">
            {result_text}
        </div>
        """,
        unsafe_allow_html=True
    )
predict = prediction(age,plinth_area,height_pre,height_post,land_co,fo_ty,ro_ty,gr_fl_ty,oth_ty,adobe_mud,mud_mortar_stone,stone_flag,cement_mortar_stone,mud_mortar_brick,
                     cement_mortar_brick,timber,bamboo,rc_non_engineered,rc_engineered,other,con_post)
if pred:
    predict = prediction(age,plinth_area,height_pre,height_post,land_co,fo_ty,ro_ty,gr_fl_ty,oth_ty,adobe_mud,mud_mortar_stone,stone_flag,cement_mortar_stone,mud_mortar_brick,
                     cement_mortar_brick,timber,bamboo,rc_non_engineered,rc_engineered,other,con_post)
    if predict == 0:
        display_prediction_result('GRADE 1',text_color='darkblue', background_color='lightblue', border_color='darkblue')
    elif predict == 1:
        display_prediction_result('GRADE 2',text_color='darkblue', background_color='lightblue', border_color='darkblue')
    else:
        display_prediction_result('GRADE 3',text_color='darkblue', background_color='lightblue', border_color='darkblue')
