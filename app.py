import streamlit as st
import random
from datetime import datetime

def main():
    st.set_page_config(
        page_title="Professional Growth Mindset",
        page_icon="📈",
        layout="wide"
    )

    st.title("📈 Professional Growth Mindset Development")
    
    # Sidebar
    st.sidebar.header("Professional Journey")
    page = st.sidebar.radio("Navigate", ["Core Principles", "Self Evaluation", "Development Practice", "Success Cases"])

    if page == "Core Principles":
        show_basics()
    elif page == "Self Evaluation":
        show_assessment()
    elif page == "Development Practice":
        show_practice()
    elif page == "Success Cases":
        show_stories()

def show_basics():
    st.header("Core Principles of Professional Growth")
    
    st.write("""
    Professional excellence is built on continuous development. A growth-oriented mindset 
    enables you to view challenges as opportunities, feedback as guidance, and effort 
    as the path to mastery in your professional journey.
    """)

    # Key Concepts
    st.subheader("The Four Pillars of Professional Excellence:")
    cols = st.columns(4)
    
    with cols[0]:
        st.markdown("### 📊 Strategic Thinking")
        st.write("Transform challenges into opportunities for professional advancement.")
    
    with cols[1]:
        st.markdown("### 💼 Professional Resilience")
        st.write("Build strength through strategic persistence and adaptation.")
    
    with cols[2]:
        st.markdown("### 📚 Continuous Development")
        st.write("Pursue excellence through systematic learning and application.")
    
    with cols[3]:
        st.markdown("### 🎯 Results-Driven")
        st.write("Transform professional vision into measurable outcomes.")

    # Professional Quotes
    if st.button("Professional Insight"):
        quotes = [
            "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
            "Leadership and learning are indispensable to each other. - John F. Kennedy",
            "The capacity to learn is a gift; the ability to learn is a skill; the willingness to learn is a choice. - Brian Herbert",
            "Innovation distinguishes between a leader and a follower. - Steve Jobs",
            "The best way to predict the future is to create it. - Peter Drucker"
        ]
        st.info(random.choice(quotes))

def show_assessment():
    st.header("📋 Simple Self-Evaluation")
    
    with st.form("simple_assessment"):
        st.write("Rate your current professional standing (1 = Beginner, 5 = Expert):")
        
        # Simplified evaluation with clear categories
        technical = st.slider("Technical Skills", 1, 5, 3)
        leadership = st.slider("Leadership Abilities", 1, 5, 3)
        communication = st.slider("Communication Skills", 1, 5, 3)
        
        submitted = st.form_submit_button("Generate Results")
        if submitted:
            # Calculate overall score
            total_score = (technical + leadership + communication) / 3
            
            # Display results with visual elements
            st.subheader("Your Professional Profile")
            
            # Show individual scores with progress bars
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Technical", f"{technical}/5")
                st.progress(technical/5)
            with col2:
                st.metric("Leadership", f"{leadership}/5")
                st.progress(leadership/5)
            with col3:
                st.metric("Communication", f"{communication}/5")
                st.progress(communication/5)
            
            # Overall assessment
            st.metric("Overall Score", f"{total_score:.1f}/5")
            
            # Provide focused recommendations
            st.subheader("Development Recommendations")
            if total_score < 3:
                st.info("Focus Areas:")
                st.write("• Join professional training programs")
                st.write("• Find a mentor in your field")
                st.write("• Start with small team projects")
            else:
                st.success("Next Steps:")
                st.write("• Lead team initiatives")
                st.write("• Mentor junior colleagues")
                st.write("• Pursue advanced certifications")

def show_practice():
    st.header("💼 Development Practice")
    
    # Required Development Plan
    st.subheader("Create Your Development Plan")
    
    with st.form("development_plan"):
        # Required inputs with clear labels
        name = st.text_input("Full Name *", key="name")
        role = st.text_input("Current Role *", key="role")
        
        st.write("---")
        st.write("Select Your Focus Areas *")
        focus_areas = st.multiselect(
            "Choose up to 3 areas",
            ["Technical Skills", "Leadership", "Communication", "Project Management", 
             "Innovation", "Strategic Thinking", "Team Building"],
            max_selections=3
        )
        
        st.write("---")
        st.write("Development Timeline")
        timeline = st.radio(
            "Select your development timeline *",
            ["3 months", "6 months", "1 year"]
        )
        
        st.write("---")
        st.write("Action Items")
        goal_1 = st.text_area("Primary Goal *", key="goal1")
        action_1 = st.text_area("Action Steps for Primary Goal *", key="action1")
        
        # Optional secondary goal
        st.write("---")
        goal_2 = st.text_area("Secondary Goal (Optional)", key="goal2")
        action_2 = st.text_area("Action Steps for Secondary Goal", key="action2")
        
        submitted = st.form_submit_button("Create Development Plan")
        
        if submitted:
            if not (name and role and focus_areas and goal_1 and action_1):
                st.error("Please fill in all required fields marked with *")
            else:
                # Display the development plan
                st.success("Development Plan Created Successfully!")
                
                st.subheader("Your Professional Development Plan")
                
                # Profile Section
                st.write("---")
                col1, col2 = st.columns(2)
                with col1:
                    st.write("**Professional Profile**")
                    st.write(f"Name: {name}")
                    st.write(f"Role: {role}")
                
                with col2:
                    st.write("**Development Focus**")
                    for area in focus_areas:
                        st.write(f"• {area}")
                
                # Timeline and Goals
                st.write("---")
                st.write(f"**Timeline:** {timeline}")
                
                # Display Goals and Actions
                st.write("---")
                st.write("**Development Goals & Actions**")
                
                # Primary Goal
                st.markdown(f"""
                **Primary Goal:**
                ```
                {goal_1}
                ```
                **Action Steps:**
                ```
                {action_1}
                ```
                """)
                
                # Secondary Goal (if provided)
                if goal_2 and action_2:
                    st.markdown(f"""
                    **Secondary Goal:**
                    ```
                    {goal_2}
                    ```
                    **Action Steps:**
                    ```
                    {action_2}
                    ```
                    """)
                
                # Generate recommendations based on focus areas
                st.write("---")
                st.subheader("Recommended Resources")
                for area in focus_areas:
                    st.write(f"**For {area}:**")
                    if area == "Technical Skills":
                        st.write("• Online courses on Coursera or Udemy")
                        st.write("• Professional certification programs")
                    elif area == "Leadership":
                        st.write("• Leadership workshop series")
                        st.write("• Management training programs")
                    elif area == "Communication":
                        st.write("• Professional speaking workshops")
                        st.write("• Business writing courses")
                    elif area == "Project Management":
                        st.write("• PMP certification preparation")
                        st.write("• Agile methodology training")
                    elif area == "Innovation":
                        st.write("• Design thinking workshops")
                        st.write("• Innovation management courses")
                    elif area == "Strategic Thinking":
                        st.write("• Strategic planning workshops")
                        st.write("• Business strategy courses")
                    elif area == "Team Building":
                        st.write("• Team leadership training")
                        st.write("• Conflict resolution workshops")

def show_stories():
    st.header("📈 Professional Success Cases")
    
    st.write("""
    Examine documented cases of professional excellence achieved through 
    systematic application of growth mindset principles.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Strategic Leadership Development")
        st.write("""
        "Through systematic application of professional development principles,
        I transformed from a technical specialist to a strategic leader. 
        Key to this transition was the structured approach to learning and
        the consistent application of growth methodologies."
        
        - Dr. James Wilson, PhD
        Chief Strategy Officer
        """)
        
    with col2:
        st.subheader("Organizational Innovation Excellence")
        st.write("""
        "By implementing a structured approach to professional development,
        our team achieved a 300% increase in innovation output. This was
        accomplished through systematic application of growth principles
        and strategic capability development."
        
        - Sarah Chen, MBA
        Director of Innovation
        """)

    # Additional Resources
    st.subheader("📚 Professional Development Resources")
    with st.expander("View Resources"):
        st.markdown("""
        ### Recommended Reading
        - "Strategic Leadership Development" - Harvard Business Review
        - "Professional Excellence Through Growth Mindset" - MIT Press
        - "Measuring Professional Development Impact" - Stanford Review
        
        ### Professional Development Tools
        - Strategic Planning Templates
        - Professional Development Tracking System
        - Competency Assessment Framework
        
        ### Learning Opportunities
        - Executive Leadership Program
        - Strategic Management Certification
        - Professional Innovation Workshop
        """)

if __name__ == "__main__":
    main()