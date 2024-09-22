import streamlit as st
import pandas as pd

# Initialize session state to store form data if not already present
if 'form_data' not in st.session_state:
    st.session_state.form_data = {}

# Title of the app
st.title("Consulting Feedback Data Collection")

# Introduction
st.write("This app helps collect feedback on solution architecture, technology-stack review, infrastructure readiness, "
         "development team performance, and business-technology alignment. Sample answers are provided for guidance.")

# Function to clear all fields
def clear_all_fields():
    st.session_state.form_data = {}  # Reset all session state values to empty
    st.experimental_rerun()  # Rerun the app to reflect cleared state

# Basic information
st.subheader("Basic Information")
name = st.text_input("Name", value=st.session_state.form_data.get("name", ""))
position = st.text_input("Position", value=st.session_state.form_data.get("position", ""))
department = st.text_input("Department", value=st.session_state.form_data.get("department", ""))
contact_email = st.text_input("Contact Email", value=st.session_state.form_data.get("contact_email", ""))

# Solution Architecture and Technology-Stack Review with sample answers
st.subheader("Solution Architecture and Technology-Stack Review (Sample answers provided)")
sol_arch_q1 = st.text_area("1. Can you walk me through the current solution architecture, including key components and integrations?", 
                           value=st.session_state.form_data.get("sol_arch_q1", "The system is built using a microservices architecture, leveraging Docker containers for deployment. Each service communicates via REST APIs."))
sol_arch_q2 = st.text_area("2. Why was the current technology stack chosen, and how well does it serve your current business needs?", 
                           value=st.session_state.form_data.get("sol_arch_q2", "The stack (React, Node.js, PostgreSQL) was chosen for scalability and developer familiarity. It has worked well, but we are starting to see performance limitations."))
sol_arch_q3 = st.text_area("3. How modular is the architecture? Can you easily add or replace components without major overhauls?", 
                           value=st.session_state.form_data.get("sol_arch_q3", "The architecture is modular, but some older services are more monolithic, making them harder to upgrade."))
sol_arch_q4 = st.text_area("4. How smoothly do systems integrate with each other? Are there any significant challenges in data flow or API management?", 
                           value=st.session_state.form_data.get("sol_arch_q4", "Most integrations are seamless, but there are occasional issues with data sync between the order management and inventory systems."))
sol_arch_q5 = st.text_area("5. How is data managed across the system, including storage, transformation, and retrieval? Is the architecture optimized for large-scale data?", 
                           value=st.session_state.form_data.get("sol_arch_q5", "Data is stored in a centralized PostgreSQL database, with some services using Redis for caching."))
sol_arch_q6 = st.text_area("6. Have you encountered any performance issues? What are the most common performance bottlenecks in the current architecture?", 
                           value=st.session_state.form_data.get("sol_arch_q6", "The main bottlenecks are in the database during peak traffic hours, particularly with read-heavy operations."))
sol_arch_q7 = st.text_area("7. How does the architecture handle growth in user numbers, transactions, or data volume? Is the architecture future-proof for scaling?", 
                           value=st.session_state.form_data.get("sol_arch_q7", "We have auto-scaling set up for our cloud infrastructure, but our monolithic services are starting to hinder rapid scaling."))
sol_arch_q8 = st.text_area("8. Are there any parts of the technology stack that are outdated or have become hard to maintain?", 
                           value=st.session_state.form_data.get("sol_arch_q8", "Some older services still use AngularJS, which is no longer supported, making updates difficult."))
sol_arch_q9 = st.text_area("9. Are there any significant limitations in the current architecture that restrict new features or faster time-to-market?", 
                           value=st.session_state.form_data.get("sol_arch_q9", "Integration with legacy systems sometimes slows down the implementation of new features."))
sol_arch_q10 = st.text_area("10. How easily can your current architecture accommodate new technologies, such as AI, blockchain, or IoT?", 
                            value=st.session_state.form_data.get("sol_arch_q10", "Our current architecture could support AI integration via additional microservices, but blockchain and IoT would require significant changes."))

# Scalable and Resilient Infrastructure Readiness Review with sample answers
st.subheader("Scalable and Resilient Infrastructure Readiness Review (Sample answers provided)")
infra_q1 = st.text_area("1. What mechanisms are in place to scale infrastructure based on demand, such as autoscaling or load balancing?", 
                        value=st.session_state.form_data.get("infra_q1", "We use AWS autoscaling for our EC2 instances, and load balancing is managed by an Elastic Load Balancer."))
infra_q2 = st.text_area("2. Are you leveraging cloud services? If so, how are you using them to manage workloads, scalability, and cost?", 
                        value=st.session_state.form_data.get("infra_q2", "Yes, we are on AWS, using EC2 for compute, S3 for storage, and RDS for databases."))
infra_q3 = st.text_area("3. What is your disaster recovery strategy? How often are backups tested, and do you have geographically distributed redundancy?", 
                        value=st.session_state.form_data.get("infra_q3", "We perform daily backups stored in a different AWS region. We also test our failover process quarterly."))
infra_q4 = st.text_area("4. Are there any single points of failure in the infrastructure, and what redundancies exist to handle critical failures?", 
                        value=st.session_state.form_data.get("infra_q4", "Most components are redundant, but our main database still has a single point of failure."))
infra_q5 = st.text_area("5. Have you faced issues with high latency, downtime, or availability? How are these monitored and mitigated?", 
                        value=st.session_state.form_data.get("infra_q5", "We use CloudWatch to monitor latency and uptime. There were some downtime issues with our database during a recent spike in traffic."))
infra_q6 = st.text_area("6. How are security policies implemented at the infrastructure level (e.g., firewalls, encryption, access controls)? How often is security audited?", 
                        value=st.session_state.form_data.get("infra_q6", "Security is enforced through VPC firewalls, IAM roles, and encryption at rest for all sensitive data."))
infra_q7 = st.text_area("7. Are you using infrastructure-as-code tools like Terraform or Ansible to automate infrastructure provisioning and management?", 
                        value=st.session_state.form_data.get("infra_q7", "Yes, we use Terraform to manage our infrastructure as code, which has improved consistency and reduced manual errors."))
infra_q8 = st.text_area("8. How do you manage and optimize infrastructure costs, especially in cloud environments?", 
                        value=st.session_state.form_data.get("infra_q8", "We use AWS Cost Explorer to monitor our spending and have implemented cost-saving measures such as Reserved Instances."))
infra_q9 = st.text_area("9. What tools are you using to monitor infrastructure health, capacity, and performance? How proactive is your monitoring?", 
                        value=st.session_state.form_data.get("infra_q9", "We use CloudWatch and Prometheus for monitoring. Our monitoring setup is reactive, but we are moving towards a more proactive approach."))
infra_q10 = st.text_area("10. Are there any regulatory requirements or compliance standards your infrastructure must adhere to, and how is this being managed?", 
                         value=st.session_state.form_data.get("infra_q10", "We need to comply with GDPR, and data is managed accordingly through encryption and data protection policies."))

# Development Team and Performance Review with sample answers
st.subheader("Development Team and Performance Review (Sample answers provided)")
dev_team_q1 = st.text_area("1. Can you describe the structure of the development team, including roles, responsibilities, and areas of expertise?", 
                           value=st.session_state.form_data.get("dev_team_q1", "We have a cross-functional team structure with dedicated frontend, backend, and DevOps engineers, along with a product manager."))
dev_team_q2 = st.text_area("2. Do you feel that the team has all the necessary skills to manage current and future projects? Where do you see skill gaps?", 
                           value=st.session_state.form_data.get("dev_team_q2", "The team is technically strong, but we have a skill gap in AI and machine learning, which will be needed in future projects."))
dev_team_q3 = st.text_area("3. What development methodologies do you follow (e.g., Agile, Scrum, Kanban)? How consistently are these methodologies applied?", 
                           value=st.session_state.form_data.get("dev_team_q3", "We follow Scrum, but adherence is inconsistent, particularly with sprint planning and retrospectives."))
dev_team_q4 = st.text_area("4. Do you have a continuous integration and delivery pipeline in place? If yes, how well is it working?", 
                           value=st.session_state.form_data.get("dev_team_q4", "Yes, we use Jenkins for CI/CD, but deployments are often delayed due to manual approvals."))
dev_team_q5 = st.text_area("5. How do you ensure code quality? Do you have processes like code reviews, static analysis, or automated testing?", 
                           value=st.session_state.form_data.get("dev_team_q5", "We have code reviews and automated tests in place, but static analysis is not used consistently."))
dev_team_q6 = st.text_area("6. How do you measure development team productivity? What are the key metrics used?", 
                           value=st.session_state.form_data.get("dev_team_q6", "We track velocity and cycle time to measure team productivity."))
dev_team_q7 = st.text_area("7. What tools do you use for team collaboration and communication? Are they effective?", 
                           value=st.session_state.form_data.get("dev_team_q7", "We use Jira for task management and Slack for communication, and both have been effective overall."))
dev_team_q8 = st.text_area("8. How do you gather and act on feedback from the development team? Are there any current pain points?", 
                           value=st.session_state.form_data.get("dev_team_q8", "We hold regular retrospectives, but the feedback loop could be improved to address pain points more quickly."))
dev_team_q9 = st.text_area("9. What opportunities exist for team members to upskill, either through internal programs or external training?", 
                           value=st.session_state.form_data.get("dev_team_q9", "We have a budget for external training, but team members have limited time to take advantage of it."))
dev_team_q10 = st.text_area("10. What are the biggest bottlenecks or challenges in the development process?", 
                            value=st.session_state.form_data.get("dev_team_q10", "The biggest bottleneck is the manual code deployment process, which slows down delivery."))

# Business and Technology Alignment Review with sample answers
st.subheader("Business and Technology Alignment Review (Sample answers provided)")
biz_tech_q1 = st.text_area("1. What are the core business objectives for the next 12-24 months, and how do you see technology contributing to achieving them?", 
                           value=st.session_state.form_data.get("biz_tech_q1", "We aim to expand into new markets, and technology will play a key role by enabling faster product releases and improving customer experience."))
biz_tech_q2 = st.text_area("2. How well does the current technology support customer needs, and how are customer feedback and technology decisions aligned?", 
                           value=st.session_state.form_data.get("biz_tech_q2", "The current system supports most customer needs, but we have received feedback about performance issues during peak usage."))
biz_tech_q3 = st.text_area("3. How do you measure the return on investment (ROI) for technology projects? Are there any specific metrics or KPIs?", 
                           value=st.session_state.form_data.get("biz_tech_q3", "We track ROI by measuring customer satisfaction and revenue growth post-implementation."))
biz_tech_q4 = st.text_area("4. How does your technology enable or constrain innovation, particularly in product development or market responsiveness?", 
                           value=st.session_state.form_data.get("biz_tech_q4", "The current setup supports product development but limits innovation due to the technical debt in legacy systems."))
biz_tech_q5 = st.text_area("5. What market challenges are you facing that could be addressed or exacerbated by technology?", 
                           value=st.session_state.form_data.get("biz_tech_q5", "Competition is increasing, and we need technology to improve our time-to-market to stay competitive."))
biz_tech_q6 = st.text_area("6. How closely aligned are your technology and business strategies?", 
                           value=st.session_state.form_data.get("biz_tech_q6", "There is alignment, but sometimes technical debt forces us to delay business initiatives."))
biz_tech_q7 = st.text_area("7. How quickly can the business deliver new products or features to market? Does technology enable or slow this process?", 
                           value=st.session_state.form_data.get("biz_tech_q7", "We can deliver new products in 2-3 months, but older systems are slowing down the process."))
biz_tech_q8 = st.text_area("8. How do you decide on technology investments, and is there alignment between business priorities and the technology budget?", 
                           value=st.session_state.form_data.get("biz_tech_q8", "Technology investments are made based on business priorities, but occasionally, unforeseen technical issues lead to additional costs."))
biz_tech_q9 = st.text_area("9. What are the main business risks associated with technology, and how are these being managed?", 
                           value=st.session_state.form_data.get("biz_tech_q9", "Our main risks are downtime and security breaches, both of which we manage with regular reviews and audits."))
biz_tech_q10 = st.text_area("10. How do you view your technology in terms of competitive advantage?", 
                            value=st.session_state.form_data.get("biz_tech_q10", "Our technology is a competitive advantage in terms of customer experience, but we need to innovate faster to maintain this edge."))

# Save the form data in session state
st.session_state.form_data = {
    "name": name, "position": position, "department": department, "contact_email": contact_email,
    "sol_arch_q1": sol_arch_q1, "sol_arch_q2": sol_arch_q2, "sol_arch_q3": sol_arch_q3, "sol_arch_q4": sol_arch_q4,
    "sol_arch_q5": sol_arch_q5, "sol_arch_q6": sol_arch_q6, "sol_arch_q7": sol_arch_q7, "sol_arch_q8": sol_arch_q8,
    "sol_arch_q9": sol_arch_q9, "sol_arch_q10": sol_arch_q10,
    "infra_q1": infra_q1, "infra_q2": infra_q2, "infra_q3": infra_q3, "infra_q4": infra_q4, "infra_q5": infra_q5,
    "infra_q6": infra_q6, "infra_q7": infra_q7, "infra_q8": infra_q8, "infra_q9": infra_q9, "infra_q10": infra_q10,
    "dev_team_q1": dev_team_q1, "dev_team_q2": dev_team_q2, "dev_team_q3": dev_team_q3, "dev_team_q4": dev_team_q4,
    "dev_team_q5": dev_team_q5, "dev_team_q6": dev_team_q6, "dev_team_q7": dev_team_q7, "dev_team_q8": dev_team_q8,
    "dev_team_q9": dev_team_q9, "dev_team_q10": dev_team_q10,
    "biz_tech_q1": biz_tech_q1, "biz_tech_q2": biz_tech_q2, "biz_tech_q3": biz_tech_q3, "biz_tech_q4": biz_tech_q4,
    "biz_tech_q5": biz_tech_q5, "biz_tech_q6": biz_tech_q6, "biz_tech_q7": biz_tech_q7, "biz_tech_q8": biz_tech_q8,
    "biz_tech_q9": biz_tech_q9, "biz_tech_q10": biz_tech_q10
}

# Button to save the data as a CSV
if st.button("Save Data as CSV"):
    df = pd.DataFrame([st.session_state.form_data])
    df.to_csv("client_feedback_data_with_questions.csv", index=False)  # Save in the current directory
    st.success("Data saved successfully! You can download it below.")
    st.download_button(label="Download CSV", data=df.to_csv(), mime="text/csv", file_name="client_feedback_data_with_questions.csv")

# Button to clear all fields
if st.button("Clear All Answers"):
    clear_all_fields()
