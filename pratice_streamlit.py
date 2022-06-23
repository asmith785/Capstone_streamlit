import streamlit as st #web development
import pandas as pd #read csv & df manipulation
import matplotlib.pyplot as plt #charts
import plotly.express as px #charts
from PIL import Image #insert image

st.set_page_config(page_title="My webpage", page_icon=":tada:", layout = "wide")


header = st.container()
intro= st.container()
dataset_location = st.container()
software_location = st.container()
cyber_location = st.container()
se_skills = st.container()
cyber_skills = st.container()
data_skills = st.container()
insight = st.container()
conclusion = st.container()

with header:
    st.title("Analysis For Alumni's Pursuing Job Opportunities In Software Engineer, Data Analysis & Cybersecurity.")
    st.subheader("Antone Smith, Muees Adewunmi, Dylan Picart")
    image = Image.open('job-tips.jpeg')
    st.image(image)
    st.write("---")
    st.write("Our target demographic aims at students that have recently graduated from a bootcamp and are unsure of how to keep up to date with technology. It is crucial to continuously keep up with technology as the world continues to change and technology continues to advance. Relying on bootcamps alone won’t get you to the career discipline you are looking to go to. There are a variety of news related sources on the internet but one can become overwhelmed with the mass amount of news at their fingertips and some don’t know what exactly to search for. Our analysis seeks to provide Alumni with info of what skills are predominantly asked for on job application descriptions to give the user a better idea on how to up-skill.")
    
    st.write(''' According to a report from Career Karma, over 44K people have attended and graduated from a bootcamp in 2020. This number has grown since 2019 by about 30%. We can only expect this number to continue to grow as the world continues to be affected by Covid-19 in 2021.


         ''')
    st.write("Knowing what skills are needed will give Alumi’s an edge on the competition to potentially rise on the applicant list and achieve the job they are aiming for.")

    
with intro:
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Hypothesis")
        st.write("We believe that even technical skills contribute to Alumni being able to find jobs but what mainly attributes to the difficulty of finding employment is location. We believe there is limited employment outside of New York, California and Texas. Which may be attributing to Alumni having difficulty finding employment. We hope to test our hypothesis durning out this analysis.")
        st.write("We explore datasets containing job postings for software engineers, data analysis and cybersecurity professionals in order to discover the distribution of job locations, as well as the skills that are most relevant to their respective profession.")


    with right_column:
        image2 = Image.open('Magnifying-glass-by-Iconika-580x364.jpeg')
        st.image(image2)

with dataset_location:
    # st.header("Data Analyst Jobs Dataset")
    # st.text("https://www.kaggle.com/datasets/defrinogionaldo/glassdoor-jobs-data-analysis")

#imported data analysis job dataset
    
    dataset_url = "DataAnalyst.csv"

# read csv from a URL
    @st.experimental_memo
    def get_data() -> pd.DataFrame:
        return pd.read_csv(dataset_url)

    analyst_data = get_data()


    #analyst_data = pd.read_csv("/Users/antonesmtih/Desktop/streamlit/DataAnalyst.csv")
    # st.write(analyst_data.head())

    
# jobs per state code for data analyst data set
    analyst_data['job_state'] = analyst_data['Location'].apply(lambda x : x.split(',')[1])
    analyst_data['job_state'] = analyst_data['job_state'].replace('Arapahoe', 'CO', regex=True)
    
#below is plot of number of data analyst jobs per state
    left_column, right_column = st.columns(2)
    with right_column:
        data= analyst_data['job_state'].value_counts().sort_values()
        state_names = data.index
        state_counts = list(data)
        final_df =pd.DataFrame({"States":state_names, "Counts":state_counts})

        fig = px.bar(final_df,y="States", x= "Counts",title = "Data Analyst Jobs Posting in United States", orientation="h")
        st.plotly_chart(fig)    

    with left_column:
        st.subheader("""The top five job posting locations for Data Analyst related jobs are the following:

- California
- Texas
- New York
- Illinois
- Pennsylvania""")
    st.write("---")


#imported software engineer job dataset
with software_location:
    se_jobs_data = pd.read_csv("us-software-engineer-jobs-zenrows.csv")
    # st.write(se_jobs_data.head())
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("""According to the plot shown, we can see that the top five job posting locations for Software Engineers are :
        
- California
- Texas
- New York
- Massachusets 
- Virginia.""")

    with right_column:
        image3 = Image.open('software_location_graph.png')
        st.image(image3)
    st.write("---")

with cyber_location:
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader(""" Our top five Cybersecurity related job postings are the following:

- California
- Georgia
- Texas
- Washington
- New Jersey

 Something interesting of note is that there are more cybersecurity jobs in NJ than there are in NY, contrary to the sheer amount of tech job postings in NYC.""")

    with right_column:
        image4 = Image.open('cyber_location_graph.png')
        st.image(image4)
    st.write("---")


with se_skills:
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("""The top five Software Engineer skills are:

- Java
- Python
- AWS
- JavaScript
- SQL        
        """)

    with right_column:
        image6 = Image.open('software_skills_graph.png')
        st.image(image6)
    st.write("---")

with cyber_skills:
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("""The top five Cyber Security skills are:

- SQL
- Python
- Java
- Firewall
- AWS        
        """)

    with right_column:
        image7 = Image.open('cyber_skills_graph.png')
        st.image(image7)
    st.write("---")

with data_skills:
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("""The top five Data Analysis skills are:

- R
- SQL
- Excel
- Python
- Tableau
        """)

    with right_column:
        image5 = Image.open('data_skills_graph.png')
        st.image(image5)
    st.write("---")


with insight:
    st.header("Insights")



    st.subheader("Data vs Cyber vs Software Engineering")
    st.write("""
- California is the top state for all 3 career path job locations, & Texas is in the top 3 states for all 3 career paths.
- Python & SQL are priorities for all 3 career path skill sets, however Data has the least amount of skill sets in common relative to the other two.
- Georgia is in the top 3 amount of cyber security job postings, unlike software engineering and data analysis.""")

st.write("---")
with conclusion:
    st.header("Conclusion")
    st.write("Our findings confirmed our hypothesis that California, Texas  were among the top five job locations in Cybersecurity, Data, and Software Engineering. However, our hypothesis was shown to be false in its assumption of limited employment opportunities outside of these three states. In Cybersecurity, Georgia and Washington had more job vacancies as opposed to New York also important to note Cyber Security is the only profession where Washington was in the top 5 job locations. For Data, Illinois and Pennsylvania were among the top five states for career opportunities. For Software Engineering, Massachusetts and Virginia were among the top five. Our insights also indicated that the top overlapping skills between all three technology career paths were SQL and Python; however, it should be noted that Data had the most variety when it came to skills in general, whereas Software Engineering & Cybersecurity all had Python, Java, SQL, & AWS. While our findings were different than we expected, we are still able to communicate to alumni what the most sought out skills employers in their respective career paths are looking for, as well as provide insight as to the job vacancies within each respective state.")












#  # jobs per state code for data software data set

    # with right_column:
    #     se_jobs_data['location'].replace('California', 'California , CA', regex=True)
    #     se_jobs_data['location'].replace('Remote', ', Remote', regex=True)
    #     se_jobs_data['location'].replace('Texas', ', TX', regex=True)

    #     se_jobs_data['job_state'] = se_jobs_data['location'].apply(lambda x : x.split(',')[-1])

    #     statess = se_jobs_data[(se_jobs_data['job_state'].isin(['Wyoming','Texas', 'United States','California','North Carolina', 'Oregon','Washington State','Maryland','Vermont','Remote', 'West Virginia', 'Rhode Island', 'Nebraska','Connecticut', 'Louisiana', 'Oklahoma', 'Maine', 'Puerto Rico','Tennessee', 'Alabama', 'South Dakota', 'Alaska', 'Kansas','Kentucky', 'Ohio', 'New Hampshire', 'South Carolina', 'Arkansas','Idaho', 'New Jersey', 'Montana', 'North Dakota','Indiana','Minnesota', 'Florida','Iowa', 'Arizona','Oregon''North Carolina', 'Utah', 'Missouri', 'Virginia', 'Pennsylvania','Nevada', 'Michigan', 'Delaware', 'Colorado','New York State', 'Georgia', 'Massachusetts', 'Wisconsin','Illinois','New Mexico'])==False)]

    #     se_data= statess['job_state'].value_counts().sort_values()
    #     se_state_names = se_data.index
    #     se_state_counts = list(se_data)
    #     final_se_df =pd.DataFrame({"States":se_state_names, "Counts":se_state_counts})

    #     se_fig = px.bar(final_se_df,y="States", x= "Counts",title = "Data Software Engineer Jobs Posting in United States", orientation="h")
    #     se_fig.show()



