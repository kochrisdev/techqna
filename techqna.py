import streamlit as st
import pandas as pd

# Initialize session state to store form data if not already present
if 'form_data' not in st.session_state:
    st.session_state.form_data = {
        "name": "",
        "position": "",
        "department": "",
        "contact_email": "",
        "sol_arch_q1": "",
        "sol_arch_q2": "",
        "sol_arch_q3": "",
        "sol_arch_q4": "",
        "sol_arch_q5": "",
        "sol_arch_q6": "",
        "sol_arch_q7": "",
        "sol_arch_q8": "",
        "sol_arch_q9": "",
        "sol_arch_q10": "",
        "infra_q1": "",
        "infra_q2": "",
        "infra_q3": "",
        "infra_q4": "",
        "infra_q5": "",
        "infra_q6": "",
        "infra_q7": "",
        "infra_q8": "",
        "infra_q9": "",
        "infra_q10": "",
        "dev_team_q1": "",
        "dev_team_q2": "",
        "dev_team_q3": "",
        "dev_team_q4": "",
        "dev_team_q5": "",
        "dev_team_q6": "",
        "dev_team_q7": "",
        "dev_team_q8": "",
        "dev_team_q9": "",
        "dev_team_q10": "",
        "biz_tech_q1": "",
        "biz_tech_q2": "",
        "biz_tech_q3": "",
        "biz_tech_q4": "",
        "biz_tech_q5": "",
        "biz_tech_q6": "",
        "biz_tech_q7": "",
        "biz_tech_q8": "",
        "biz_tech_q9": "",
        "biz_tech_q10": ""
    }

# Function to clear all fields
def clear_all_fields():
    for key in st.session_state.form_data.keys():
        st.session_state.form_data[key] = ""

# Title of the app
st.title("Consulting Feedback Data Collection")

# Introduction
st.write("This app helps collect feedback on solution architecture, technology-stack review, infrastructure readiness, "
         "development team performance, and business-technology alignment. Sample answers are provided for guidance.")

# Basic information
st.subheader("Basic Information")
name = st.text_input("Name", value=st.session_state.form_data["name"])
position = st.text_input("Position", value=st.session_state.form_data["position"])
department = st.text_input("Department", value=st.session_state.form_data["department"])
contact_email = st.text_input("Contact Email", value=st.session_state.form_data["contact_email"])

# Solution Architecture and Technology-Stack Review with sample answers
st.subheader("Solution Architecture and Technology-Stack Review (Sample answers provided)")
sol_arch_q1 = st.text_area("1. Can you walk me through the current solution architecture, including key components and integrations?", 
                           value=st.session_state.form_data["sol_arch_q1"])
sol_arch_q2 = st.text_area("2. Why was the current technology stack chosen, and how well does it serve your current business needs?", 
                           value=st.session_state.form_data["sol_arch_q2"])
sol_arch_q3 = st.text_area("3. How modular is the architecture? Can you easily add or replace components without major overhauls?", 
                           value=st.session_state.form_data["sol_arch_q3"])
sol_arch_q4 = st.text_area("4. How smoothly do systems integrate with each other? Are there any significant challenges in data flow or API management?", 
                           value=st.session_state.form_data["sol_arch_q4"])
sol_arch_q5 = st.text_area("5. How is data managed across the system, including storage, transformation, and retrieval? Is the architecture optimized for large-scale data?", 
                           value=st.session_state.form_data["sol_arch_q5"])
sol_arch_q6 = st.text_area("6. Have you encountered any performance issues? What are the most common performance bottlenecks in the current architecture?", 
                           value=st.session_state.form_data["sol_arch_q6"])
sol_arch_q7 = st.text_area("7. How does the architecture handle growth in user numbers, transactions, or data volume? Is the architecture future-proof for scaling?", 
                           value=st.session_state.form_data["sol_arch_q7"])
sol_arch_q8 = st.text_area("8. Are there any parts of the technology stack that are outdated or have become hard to maintain?", 
                           value=st.session_state.form_data["sol_arch_q8"])
sol_arch_q9 = st.text_area("9. Are there any significant limitations in the current architecture that restrict new features or faster time-to-market?", 
                           value=st.session_state.form_data["sol_arch_q9"])
sol_arch_q10 = st.text_area("10. How easily can your current architecture accommodate new technologies, such as AI, blockchain, or IoT?", 
                            value=st.session_state.form_data["sol_arch_q10"])

# Scalable and Resilient Infrastructure Readiness Review with sample answers
st.subheader("Scalable and Resilient Infrastructure Readiness Review (Sample answers provided)")
infra_q1 = st.text_area("1. What mechanisms are in place to scale infrastructure based on demand, such as autoscaling or load balancing?", 
                        value=st.session_state.form_data["infra_q1"])
infra_q2 = st.text_area("2. Are you leveraging cloud services? If so, how are you using them to manage workloads, scalability, and cost?", 
                        value=st.session_state.form_data["infra_q2"])
infra_q3 = st.text_area("3. What is your disaster recovery strategy? How often are backups tested, and do you have geographically distributed redundancy?", 
                        value=st.session_state.form_data["infra_q3"])
infra_q4 = st.text_area("4. Are there any single points of failure in the infrastructure, and what redundancies exist to handle critical failures?", 
                        value=st.session_state.form_data["infra_q4"])
infra_q5 = st.text_area("5. Have you faced issues with high latency, downtime, or availability? How are these monitored and mitigated?", 
                        value=st.session_state.form_data["infra_q5"])
infra_q6 = st.text_area("6. How are security policies implemented at the infrastructure level (e.g., firewalls, encryption, access controls)? How often is security audited?", 
                        value=st.session_state.form_data["infra_q6"])
infra_q7 = st.text_area("7. Are you using infrastructure-as-code tools like Terraform or Ansible to automate infrastructure provisioning and management?", 
                        value=st.session_state.form_data["infra_q7"])
infra_q8 = st.text_area("8. How do you manage and optimize infrastructure costs, especially in cloud environments?", 
                        value=st.session_state.form_data["infra_q8"])
infra_q9 = st.text_area("9. What tools are you using to monitor infrastructure health, capacity, and performance? How proactive is your monitoring?", 
                        value=st.session_state.form_data["infra_q9"])
infra_q10 = st.text_area("10. Are there any regulatory requirements or compliance standards your infrastructure must adhere to, and how is this being managed?", 
                         value=st.session_state.form_data["infra_q10"])

# Development Team and Performance Review with sample answers
st.subheader("Development Team and Performance Review (Sample answers provided)")
dev_team_q1 = st.text_area("1. Can you describe the structure of the development team, including roles, responsibilities, and areas of expertise?", 
                           value=st.session_state.form_data["dev_team_q1"])
dev_team_q2 = st.text_area("2. Do you feel that the team has all the necessary skills to manage current and future projects? Where do you see skill gaps?", 
                           value=st.session_state.form_data["dev_team_q2"])
dev_team_q3 = st.text_area("3. What development methodologies do you follow (e.g., Agile, Scrum, Kanban)? How consistently are these methodologies applied?", 
                           value=st.session_state.form_data["dev_team_q3"])
dev_team_q4 = st.text_area("4. Do you have a continuous integration and delivery pipeline in place? If yes, how well is it working?", 
                           value=st.session_state.form_data["dev_team_q4"])
dev_team_q5 = st.text_area("5. How do you ensure code quality? Do you have processes like code reviews, static analysis, or automated testing?", 
                           value=st.session_state.form_data["dev_team_q5"])
dev_team_q6 = st.text_area("6. How do you measure development team productivity? What are the key metrics used?", 
                           value=st.session_state.form_data["dev_team_q6"])
dev_team_q7 = st.text_area("7. What tools do you use for team collaboration and communication? Are they effective?", 
                           value=st.session_state.form_data["dev_team_q7"])
dev_team_q8 = st.text_area("8. How do you gather and act on feedback from the development team? Are there any current pain points?", 
                           value=st.session_state.form_data["dev_team_q8"])
dev_team_q9 = st.text_area("9. What opportunities exist for team members to upskill, either through internal programs or external training?", 
                           value=st.session_state.form_data["dev_team_q9"])
dev_team_q10 = st.text_area("10. What are the biggest bottlenecks or challenges in the development process?", 
                            value=st.session_state.form_data["dev_team_q10"])

# Business and Technology Alignment Review with sample answers
st.subheader("Business and Technology Alignment Review (Sample answers provided)")
biz_tech_q1 = st.text_area("1. What are the core business objectives for the next 12-24 months, and how do you see technology contributing to achieving them?", 
                           value=st.session_state.form_data["biz_tech_q1"])
biz_tech_q2 = st.text_area("2. How well does the current technology support customer needs, and how are customer feedback and technology decisions aligned?", 
                           value=st.session_state.form_data["biz_tech_q2"])
biz_tech_q3 = st.text_area("3. How do you measure the return on investment (ROI) for technology projects? Are there any specific metrics or KPIs?", 
                           value=st.session_state.form_data["biz_tech_q3"])
biz_tech_q4 = st.text_area("4. How does your technology enable or constrain innovation, particularly in product development or market responsiveness?", 
                           value=st.session_state.form_data["biz_tech_q4"])
biz_tech_q5 = st.text_area("5. What market challenges are you facing that could be addressed or exacerbated by technology?", 
                           value=st.session_state.form_data["biz_tech_q5"])
biz_tech_q6 = st.text_area("6. How closely aligned are your technology and business strategies?", 
                           value=st.session_state.form_data["biz_tech_q6"])
biz_tech_q7 = st.text_area("7. How quickly can the business deliver new products or features to market? Does technology enable or slow this process?", 
                           value=st.session_state.form_data["biz_tech_q7"])
biz_tech_q8 = st.text_area("8. How do you decide on technology investments, and is there alignment between business priorities and the technology budget?", 
                           value=st.session_state.form_data["biz_tech_q8"])
biz_tech_q9 = st.text_area("9. What are the main business risks associated with technology, and how are these being managed?", 
                           value=st.session_state.form_data["biz_tech_q9"])
biz_tech_q10 = st.text_area("10. How do you view your technology in terms of competitive advantage?", 
                            value=st.session_state.form_data["biz_tech_q10"])

# Save the form data in session state
st.session_state.form_data["name"] = name
st.session_state.form_data["position"] = position
st.session_state.form_data["department"] = department
st.session_state.form_data["contact_email"] = contact_email
st.session_state.form_data["sol_arch_q1"] = sol_arch_q1
st.session_state.form_data["sol_arch_q2"] = sol_arch_q2
st.session_state.form_data["sol_arch_q3"] = sol_arch_q3
st.session_state.form_data["sol_arch_q4"] = sol_arch_q4
st.session_state.form_data["sol_arch_q5"] = sol_arch_q5
st.session_state.form_data["sol_arch_q6"] = sol_arch_q6
st.session_state.form_data["sol_arch_q7"] = sol_arch_q7
st.session_state.form_data["sol_arch_q8"] = sol_arch_q8
st.session_state.form_data["sol_arch_q9"] = sol_arch_q9
st.session_state.form_data["sol_arch_q10"] = sol_arch_q10
st.session_state.form_data["infra_q1"] = infra_q1
st.session_state.form_data["infra_q2"] = infra_q2
st.session_state.form_data["infra_q3"] = infra_q3
st.session_state.form_data["infra_q4"] = infra_q4
st.session_state.form_data["infra_q5"] = infra_q5
st.session_state.form_data["infra_q6"] = infra_q6
st.session_state.form_data["infra_q7"] = infra_q7
st.session_state.form_data["infra_q8"] = infra_q8
st.session_state.form_data["infra_q9"] = infra_q9
st.session_state.form_data["infra_q10"] = infra_q10
st.session_state.form_data["dev_team_q1"] = dev_team_q1
st.session_state.form_data["dev_team_q2"] = dev_team_q2
st.session_state.form_data["dev_team_q3"] = dev_team_q3
st.session_state.form_data["dev_team_q4"] = dev_team_q4
st.session_state.form_data["dev_team_q5"] = dev_team_q5
st.session_state.form_data["dev_team_q6"] = dev_team_q6
st.session_state.form_data["dev_team_q7"] = dev_team_q7
st.session_state.form_data["dev_team_q8"] = dev_team_q8
st.session_state.form_data["dev_team_q9"] = dev_team_q9
st.session_state.form_data["dev_team_q10"] = dev_team_q10
st.session_state.form_data["biz_tech_q1"] = biz_tech_q1
st.session_state.form_data["biz_tech_q2"] = biz_tech_q2
st.session_state.form_data["biz_tech_q3"] = biz_tech_q3
st.session_state.form_data["biz_tech_q4"] = biz_tech_q4
st.session_state.form_data["biz_tech_q5"] = biz_tech_q5
st.session_state.form_data["biz_tech_q6"] = biz_tech_q6
st.session_state.form_data["biz_tech_q7"] = biz_tech_q7
st.session_state.form_data["biz_tech_q8"] = biz_tech_q8
st.session_state.form_data["biz_tech_q9"] = biz_tech_q9
st.session_state.form_data["biz_tech_q10"] = biz_tech_q10

# Button to save the data as a CSV
if st.button("Save Data as CSV"):
    df = pd.DataFrame([st.session_state.form_data])
    df.to_csv("client_feedback_data_with_questions.csv", index=False)  # Save in the current directory
    st.success("Data saved successfully! You can download it below.")
    st.download_button(label="Download CSV", data=df.to_csv(), mime="text/csv", file_name="client_feedback_data_with_questions.csv")

# Button to clear all fields
if st.button("Clear All Answers"):
    clear_all_fields()
