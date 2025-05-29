import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Set page title and icon
# Page configuration
st.set_page_config(
    page_title="UNP Sri Lanka Religious Engagement Strategy",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and introduction
st.title("UNP Sri Lanka Strategy Dashboard")
st.markdown("""
**Rebuilding Trust Through Faith-Sensitive District Engagement (2020-2030)**

This dashboard visualizes the UNP's comprehensive strategy to rebuild from their historic 2020 defeat by engaging with religious communities across all 25 districts of Sri Lanka.
""")

# Data preparation
districts_data = {
    # Western Province
    'Colombo': {'Province': 'Western', 'Buddhist': 70.66, 'Muslim': 11.76, 'Christian': 9.56, 'Hindu': 7.89},
    'Gampaha': {'Province': 'Western', 'Buddhist': 71.48, 'Christian': 21.19, 'Muslim': 5.01, 'Hindu': 2.28},
    'Kalutara': {'Province': 'Western', 'Buddhist': 83.52, 'Muslim': 9.40, 'Christian': 3.79, 'Hindu': 3.27},
    
    # Central Province
    'Kandy': {'Province': 'Central', 'Buddhist': 73.0, 'Muslim': 14.0, 'Hindu': 9.5, 'Christian': 2.5},
    'Matale': {'Province': 'Central', 'Buddhist': 85.0, 'Hindu': 8.0, 'Muslim': 5.0, 'Christian': 2.0},
    'Nuwara Eliya': {'Province': 'Central', 'Hindu': 51.04, 'Buddhist': 39.67, 'Christian': 6.55, 'Muslim': 2.71},
    
    # Southern Province
    'Galle': {'Province': 'Southern', 'Buddhist': 93.9, 'Muslim': 3.7, 'Hindu': 1.5, 'Christian': 0.9},
    'Matara': {'Province': 'Southern', 'Buddhist': 95.0, 'Muslim': 3.0, 'Hindu': 2.0, 'Christian': 0.7},
    'Hambantota': {'Province': 'Southern', 'Buddhist': 90.0, 'Muslim': 6.0, 'Hindu': 3.0, 'Christian': 1.0},
    
    # Eastern Province
    'Trincomalee': {'Province': 'Eastern', 'Muslim': 42.11, 'Buddhist': 26.12, 'Hindu': 25.95, 'Christian': 5.79},
    'Batticaloa': {'Province': 'Eastern', 'Hindu': 70.0, 'Muslim': 20.0, 'Buddhist': 8.0, 'Christian': 2.0},
    'Ampara': {'Province': 'Eastern', 'Muslim': 43.4, 'Buddhist': 38.7, 'Hindu': 15.8, 'Christian': 2.0},
    
    # North Central Province
    'Anuradhapura': {'Province': 'North Central', 'Buddhist': 90.0, 'Muslim': 8.4, 'Christian': 1.1, 'Hindu': 0.5},
    'Polonnaruwa': {'Province': 'North Central', 'Buddhist': 89.7, 'Muslim': 7.5, 'Hindu': 1.7, 'Christian': 1.0},
    
    # North Western Province
    'Kurunegala': {'Province': 'North Western', 'Buddhist': 92.5, 'Muslim': 7.7, 'Hindu': 0.95, 'Christian': 0.85},
    'Puttalam': {'Province': 'North Western', 'Buddhist': 40.0, 'Christian': 30.0, 'Muslim': 18.0, 'Hindu': 3.0},
    
    # Northern Province
    'Jaffna': {'Province': 'Northern', 'Hindu': 80.0, 'Christian': 15.0, 'Muslim': 3.0, 'Buddhist': 2.0},
    'Kilinochchi': {'Province': 'Northern', 'Hindu': 75.0, 'Christian': 20.0, 'Muslim': 3.0, 'Buddhist': 2.0},
    'Mannar': {'Province': 'Northern', 'Christian': 60.0, 'Hindu': 25.0, 'Muslim': 10.0, 'Buddhist': 5.0},
    'Vavuniya': {'Province': 'Northern', 'Hindu': 65.0, 'Christian': 20.0, 'Muslim': 10.0, 'Buddhist': 5.0},
    'Mullaitivu': {'Province': 'Northern', 'Hindu': 70.0, 'Christian': 20.0, 'Muslim': 5.0, 'Buddhist': 5.0},
    
    # Uva Province
    'Badulla': {'Province': 'Uva', 'Buddhist': 70.0, 'Hindu': 20.0, 'Muslim': 8.0, 'Christian': 2.0},
    'Monaragala': {'Province': 'Uva', 'Buddhist': 85.0, 'Hindu': 10.0, 'Muslim': 4.0, 'Christian': 1.0},
    
    # Sabaragamuwa Province
    'Ratnapura': {'Province': 'Sabaragamuwa', 'Buddhist': 80.0, 'Muslim': 12.0, 'Hindu': 6.0, 'Christian': 2.0},
    'Kegalle': {'Province': 'Sabaragamuwa', 'Buddhist': 85.0, 'Christian': 8.0, 'Muslim': 5.0, 'Hindu': 2.0}
}

# Strategies data
strategies_data = {
    'Colombo': [
        "Buddhist Service Hubs: Partner with Gangaramaya and Kelaniya temples on urban poverty clinics",
        "Interfaith Education Forum: Convene mosque, church, and temple leaders quarterly",
        "Youth Tech Incubators: Host 'NextGen Colombo' hackathons in temple grounds"
    ],
    'Gampaha': [
        "Church-Linked STEM Scholarships: Collaborate with Catholic and Protestant schools",
        "Buddhist Temple-Jobs Link: 'Sunday with the Sangha' vocational training",
        "Microfinance Clinics: Small-business loans for home-based entrepreneurs"
    ],
    'Kalutara': [
        "Fishers' Relief Fund: Co-create Muslim community council for cyclone-resilience grants",
        "Vesak Environmental Drive: Sponsor green lighting at Kalutara Bodhiya",
        "Rail Underpass Advocacy: Town halls with Buddhist clergy and farmers"
    ],
    'Kandy': [
        "Perahera Dialogues: Link Temple of the Tooth with youth entrepreneurship training",
        "Merchant Microgrants: Support Muslim small traders through mosque committees",
        "Hindu Temple Fairs: Sponsor logistics at Kataragama-style festivals"
    ],
    'Trincomalee': [
        "Interfaith Port Plans: Present UNP's northeast port-expansion vision",
        "Beach-Clean Initiatives: Multi-faith clean-ups at Koneswaram Temple",
        "Ramadan & Vesak Clinics: Mobile health units during religious observances"
    ],
    'Nuwara Eliya': [
        "Tea-Worker Welfare Boards: Joint committees with Tamil unions and Sinhala elders",
        "Poya-Day Clinics: Free clinics promoted through kovils, viharas, and churches",
        "Inter-Community Tea-Tours: Use factory tours for community dialogue"
    ],
    'Matale': [
        "Temple-Farmers Roundtables: Partner with kovils and viharas to support smallholder tea and vegetable farmers through knowledge exchanges",
        "Heritage Tourism Workshops: Interfaith tours of Aluvihare Rock Temple and Dutch Fort led by local religious guides",
        "Youth Sports Leagues: Cross-faith cricket and volleyball tournaments sponsored by temples, churches, mosques, and kovils"
    ],
    'Galle': [
        "Sea2Temple Clean-Ups: Multi-faith beach cleanup drives along Unawatuna and Galle beaches",
        "Fort Heritage Festivals: Annual interfaith cultural fair at Galle Fort hosted by Buddhist, Hindu, Muslim, and Christian groups",
        "Fisher Livelihood Grants: Microfinance for small-scale fishermen in partnership with local churches and mosques"
    ],
    'Matara': [
        "Nilwala River Health Camps: Mobile clinics promoted through temples, churches, and mosques along the river basin",
        "Teardrop Temple Tours: Inter-community tours of the Parevi Duwa temple and Matara Fort led by youth volunteers",
        "Women’s Vocational Training: Skill-building workshops at temples and churches for single mothers"
    ],
    'Hambantota': [
        "Port Community Dialogues: Quarterly town halls with Buddhist and Muslim leaders on port expansion benefits",
        "Wildlife Conservation Drives: Interfaith volunteer days at Bundala and Yala national parks",
        "Youth Coding Bootcamps: Hackathons hosted in local religious centres to build digital literacy"
    ],
    'Batticaloa': [
        "Tamil-Muslim Cultural Fairs: Joint celebrations of Hindu and Islamic festivals alongside church choirs",
        "Fisher Welfare Workshops: Vocational training for coastal fishermen via kovils and mosque committees",
        "Youth Peacebuilding Camps: Residential interfaith programs for Christian, Hindu, and Muslim youth"
    ],
    'Ampara': [
        "Agrarian Extension Clinics: Mobile agriculture advice via mosque, kovil, and church networks",
        "Ramadan & Poson Food Drives: Joint community meals distributed through temples and mosques",
        "Women’s Literacy Circles: Faith-based adult education classes run from churches and mosques"
    ],
    'Anuradhapura': [
        "Sacred Site Pilgrimages: Interfaith guided tours of Sri Maha Bodhi and ancient stupas",
        "Agricultural Microgrants: Support for paddy farmers via temple and mosque patronage",
        "Cultural Youth Camps: Camps teaching heritage traditions across Buddhism, Islam, Hinduism, and Christianity"
    ],
    'Polonnaruwa': [
        "Heritage Conservation Projects: Volunteer restoration days at Vatadage and kovils",
        "Temple-Mosque Dialogue Forums: Monthly interfaith dialogues inside the medieval city walls",
        "Youth Scholarship Awards: Cross-religion academic scholarships funded by local clergy"
    ],
    'Kurunegala': [
        "Faith & Farming Workshops: Sustainable agriculture training at temple and mosque grounds",
        "Buddhist-Church Youth Festivals: Annual festivals with music, dance and sports competitions",
        "Volunteer Health Camps: Mobile clinics rotating between kovils, viharas, and churches"
    ],
    'Puttalam': [
        "Saltworker Support Fund: Microfinance for salt-pan communities via mosque and church partnerships",
        "Interfaith Mangrove Clean-ups: Coastal restoration drives led by Hindu, Muslim, and Christian volunteers",
        "Youth Entrepreneurship Grants: Seed funding for interfaith youth-led social enterprises"
    ],
    'Jaffna': [
        "Temple & Church Heritage Tours: Joint cultural tours of Nallur Kandaswamy Kovil and Jaffna Cathedral",
        "Fisher Livelihood Training: Modern fishing techniques taught under mosque and kovil sponsorship",
        "Youth Debate Clubs: Interfaith public speaking competitions in schools and temples"
    ],
    'Kilinochchi': [
        "Post-War Healing Circles: Interfaith trauma support sessions hosted by churches and kovils",
        "Vocational Training Hubs: Skill centers at mosque and temple grounds for unemployed youth",
        "Cultural Music Festivals: Joint concerts of Hindu, Muslim, and Christian devotional music"
    ],
    'Mannar': [
        "Fisher Empowerment Forums: Community discussions with Tamil Catholic and Muslim fishing leaders",
        "Beach Safety Clinics: First-aid training at local kovils and churches",
        "Youth Film Workshops: Interfaith storytelling film camps supported by clergy"
    ],
    'Vavuniya': [
        "Reconciliation Seminars: Interfaith dialogue on post-conflict healing at churches and kovils",
        "Agricultural Co-ops: Joint farmer cooperatives supported by mosque and temple committees",
        "Sports for Peace: Mixed-faith sports tournaments in local community centers"
    ],
    'Mullaitivu': [
        "Island Fisher Microfinance: Low-interest loans for island fishing communities via mosque networks",
        "Trauma Counseling Centers: Faith-based counseling run by church and kovil volunteers",
        "Youth Arts Workshops: Cross-community art programs in schools and religious centers"
    ],
    'Badulla': [
        "Tea Estate Health Camps: Mobile clinics in plantation areas via temples and churches",
        "Poson Pilgrimage Support: Joint pilgrim transport services run by kovil and church committees",
        "Mountain Trail Clean-ups: Conservation days in the Knuckles range with multi-faith volunteers"
    ],
    'Monaragala': [
        "Rural Livelihood Training: Skill workshops at temples, kovils, and mosque grounds for subsistence farmers",
        "Interfaith Literacy Drives: Adult reading classes hosted by churches and viharas",
        "Youth Leadership Forums: Cross-faith leadership training for local high school students"
    ],
    'Ratnapura': [
        "Gem Mining Safety Clinics: Health and safety workshops for mine workers via Buddhist and Christian centers",
        "Rainforest Restoration Drives: Reforestation projects led by temple and church youth groups",
        "Scholarship Fairs: Cross-community education fairs sponsored by clergy"
    ],
    'Kegalle': [
        "Rubber Farmer Roundtables: Knowledge exchange sessions at kovils and viharas",
        "Temple-Mosque Food Banks: Joint food distribution programs in low-income areas",
        "Youth Heritage Projects: Community history mapping with multi-faith student teams"
    ]
}

# Create DataFrame
df = pd.DataFrame.from_dict(districts_data, orient='index').reset_index()
df.rename(columns={'index': 'District'}, inplace=True)

# Fill missing values
for col in ['Buddhist', 'Muslim', 'Christian', 'Hindu']:
    df[col] = df[col].fillna(0)

# Sidebar
# st.sidebar.header("🔍 Filters")

# # Province filter
# provinces = ['All'] + sorted(df['Province'].unique().tolist())
# selected_province = st.sidebar.selectbox("Select Province", provinces)

# # Religion filter
# religions = ['All', 'Buddhist', 'Muslim', 'Christian', 'Hindu']
# selected_religion = st.sidebar.selectbox("Highlight Religion", religions)

# Filter data
# filtered_df = df.copy()
# if selected_province != 'All':
#     filtered_df = filtered_df[filtered_df['Province'] == selected_province]

# Main content with tabs
tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "🗺️ District Analysis", "🤝 Strategies", "📈 Analytics"])

with tab1:
    st.header("Overview of Religious Demographics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Summary statistics
        st.subheader("National Religious Composition")
        avg_buddhist = df['Buddhist'].mean()
        avg_muslim = df['Muslim'].mean()
        avg_christian = df['Christian'].mean()
        avg_hindu = df['Hindu'].mean()
        
        summary_df = pd.DataFrame({
            'Religion': ['Buddhist', 'Muslim', 'Christian', 'Hindu'],
            'Average %': [avg_buddhist, avg_muslim, avg_christian, avg_hindu]
        })
        
        fig_pie = px.pie(summary_df, values='Average %', names='Religion', 
                        title="Average Religious Distribution Across Districts",
                        color_discrete_map={
                            'Buddhist': '#FF6B6B',
                            'Muslim': '#4ECDC4',
                            'Christian': '#45B7D1',
                            'Hindu': '#96CEB4'
                        })
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with col2:
        # Province-wise breakdown
        st.subheader("Religious Majority by Province")
        province_stats = []
        for province in df['Province'].unique():
            prov_data = df[df['Province'] == province]
            for _, row in prov_data.iterrows():
                majority_religion = max(['Buddhist', 'Muslim', 'Christian', 'Hindu'], 
                                      key=lambda x: row[x])
                province_stats.append({
                    'Province': province,
                    'District': row['District'],
                    'Majority Religion': majority_religion,
                    'Percentage': row[majority_religion]
                })
        
        province_df = pd.DataFrame(province_stats)
        fig_bar = px.bar(province_df, x='District', y='Percentage', 
                        color='Majority Religion',
                        title='Religious Majority by District',
                        color_discrete_map={
                            'Buddhist': '#FF6B6B',
                            'Muslim': '#4ECDC4',
                            'Christian': '#45B7D1',
                            'Hindu': '#96CEB4'
                        })
        fig_bar.update_xaxes(tickangle=45)
        st.plotly_chart(fig_bar, use_container_width=True)

with tab2:
    st.header("District-Level Religious Analysis")
    
    # District selector
    selected_district = st.selectbox("Select District for Detailed View", 
                                    ['All'] + sorted(df['District'].tolist()))
    
    if selected_district == 'All':
        # Heatmap of all districts
        st.subheader("Religious Composition Heatmap")
        
        heatmap_data = df.set_index('District')[['Buddhist', 'Muslim', 'Christian', 'Hindu']]
        
        fig_heatmap = px.imshow(heatmap_data.values,
                               labels=dict(x="Religion", y="District", color="Percentage"),
                               x=['Buddhist', 'Muslim', 'Christian', 'Hindu'],
                               y=heatmap_data.index,
                               color_continuous_scale='Viridis',
                               title='Religious Demographics Across All Districts')
        fig_heatmap.update_layout(height=800)
        st.plotly_chart(fig_heatmap, use_container_width=True)
        
    else:
        # Individual district analysis
        district_data = df[df['District'] == selected_district].iloc[0]
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader(f"{selected_district} District")
            st.write(f"**Province:** {district_data['Province']}")
            
            # Religion percentages
            religions_pct = {
                'Buddhist': district_data['Buddhist'],
                'Muslim': district_data['Muslim'],
                'Christian': district_data['Christian'],
                'Hindu': district_data['Hindu']
            }
            
            fig_district = px.bar(x=list(religions_pct.keys()), 
                                 y=list(religions_pct.values()),
                                 title=f"Religious Composition - {selected_district}",
                                 color=list(religions_pct.keys()),
                                 color_discrete_map={
                                     'Buddhist': '#FF6B6B',
                                     'Muslim': '#4ECDC4',
                                     'Christian': '#45B7D1',
                                     'Hindu': '#96CEB4'
                                 })
            fig_district.update_layout(showlegend=False)
            st.plotly_chart(fig_district, use_container_width=True)
        
        with col2:
            st.subheader("Key Statistics")
            majority_religion = max(religions_pct.keys(), key=lambda x: religions_pct[x])
            st.metric("Majority Religion", majority_religion, 
                     f"{religions_pct[majority_religion]:.1f}%")
            
            diversity_score = 1 - sum((p/100)**2 for p in religions_pct.values() if p > 0)
            st.metric("Religious Diversity Index", f"{diversity_score:.3f}", 
                     "Higher = More Diverse")
            
            total_minorities = 100 - religions_pct[majority_religion]
            st.metric("Minority Population", f"{total_minorities:.1f}%")

with tab3:
    st.header("Faith-Sensitive Engagement Strategies")
    
    # Strategy search
    strategy_district = st.selectbox("Select District for Strategy Details", 
                                   sorted([d for d in strategies_data.keys()]))
    
    if strategy_district:
        district_info = df[df['District'] == strategy_district].iloc[0]
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader(f"Strategies for {strategy_district} District")
            st.write(f"**Province:** {district_info['Province']}")
            
            # Display strategies
            if strategy_district in strategies_data:
                for i, strategy in enumerate(strategies_data[strategy_district], 1):
                    st.write(f"**{i}.** {strategy}")
            else:
                st.info("Detailed strategies for this district are being developed based on the generic provincial templates.")
        
        with col2:
            st.subheader("District Demographics")
            demo_data = {
                'Religion': ['Buddhist', 'Muslim', 'Christian', 'Hindu'],
                'Percentage': [district_info['Buddhist'], district_info['Muslim'], 
                              district_info['Christian'], district_info['Hindu']]
            }
            
            fig_demo = px.pie(pd.DataFrame(demo_data), values='Percentage', names='Religion',
                             color_discrete_map={
                                 'Buddhist': '#FF6B6B',
                                 'Muslim': '#4ECDC4',
                                 'Christian': '#45B7D1',
                                 'Hindu': '#96CEB4'
                             })
            fig_demo.update_layout(height=300, showlegend=True, 
                                  legend=dict(orientation="v", x=1.05, y=0.5))
            st.plotly_chart(fig_demo, use_container_width=True)
    
    # Strategy types overview
    st.subheader("Strategy Categories Across Districts")
    
    strategy_types = {
        'Temple/Religious Partnerships': ['Colombo', 'Gampaha', 'Kalutara', 'Kandy'],
        'Interfaith Dialogue': ['Colombo', 'Trincomalee', 'Nuwara Eliya'],
        'Economic Development': ['Gampaha', 'Kalutara', 'Kandy', 'Nuwara Eliya'],
        'Health & Social Services': ['Trincomalee', 'Nuwara Eliya'],
        'Youth & Education': ['Colombo', 'Gampaha', 'Kandy'],
        'Environmental Initiatives': ['Kalutara', 'Trincomalee']
    }
    
    strategy_counts = pd.DataFrame({
        'Strategy Type': list(strategy_types.keys()),
        'Districts': [len(districts) for districts in strategy_types.values()]
    })
    
    fig_strategies = px.bar(strategy_counts, x='Strategy Type', y='Districts',
                           title='Number of Districts by Strategy Type',
                           color='Districts',
                           color_continuous_scale='Blues')
    fig_strategies.update_xaxes(tickangle=45)
    st.plotly_chart(fig_strategies, use_container_width=True)

with tab4:
    st.header("📈 Strategic Analytics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Religious Diversity Analysis")
        
        # Calculate diversity scores
        diversity_scores = []
        for _, row in df.iterrows():
            religions = [row['Buddhist'], row['Muslim'], row['Christian'], row['Hindu']]
            # Simpson's Diversity Index
            diversity = 1 - sum((p/100)**2 for p in religions if p > 0)
            diversity_scores.append({
                'District': row['District'],
                'Province': row['Province'],
                'Diversity Score': diversity
            })
        
        diversity_df = pd.DataFrame(diversity_scores)
        
        fig_diversity = px.scatter(diversity_df, x='District', y='Diversity Score',
                                  color='Province', size='Diversity Score',
                                  title='Religious Diversity by District',
                                  hover_data=['Province'])
        fig_diversity.update_xaxes(tickangle=45)
        st.plotly_chart(fig_diversity, use_container_width=True)
        
        # Top diverse districts
        st.subheader("Most Religiously Diverse Districts")
        top_diverse = diversity_df.nlargest(5, 'Diversity Score')[['District', 'Diversity Score']]
        st.dataframe(top_diverse, use_container_width=True)
    
    with col2:
        st.subheader("Strategic Priority Matrix")
        
        # Create priority matrix based on diversity and strategies
        priority_data = []
        for _, row in df.iterrows():
            district = row['District']
            religions = [row['Buddhist'], row['Muslim'], row['Christian'], row['Hindu']]
            diversity = 1 - sum((p/100)**2 for p in religions if p > 0)
            
            has_strategy = district in strategies_data
            strategy_count = len(strategies_data.get(district, []))
            
            priority_data.append({
                'District': district,
                'Diversity Score': diversity,
                'Strategy Development': 'High' if has_strategy else 'Low',
                'Strategy Count': strategy_count
            })
        
        priority_df = pd.DataFrame(priority_data)
        
        fig_priority = px.scatter(priority_df, x='Diversity Score', y='Strategy Count',
                                 color='Strategy Development', size='Strategy Count',
                                 hover_name='District',
                                 title='Strategy Development vs Religious Diversity',
                                 labels={'Strategy Count': 'Number of Strategies'})
        st.plotly_chart(fig_priority, use_container_width=True)
        
        st.subheader("Provincial Summary")
        provincial_summary = df.groupby('Province').agg({
            'Buddhist': 'mean',
            'Muslim': 'mean',
            'Christian': 'mean',
            'Hindu': 'mean'
        }).round(1)
        st.dataframe(provincial_summary, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
**Data Source:** Department of Census and Statistics, Sri Lanka (2012)  
**Strategy Framework:** UNP Faith-Sensitive Engagement Plan 2020-2030  
**Objective:** Rebuild trust and electoral viability through authentic religious community engagement
""")

# Additional insights in expander
with st.expander("📋 Key Insights & Recommendations"):
    st.markdown("""
    ### Key Strategic Insights:
    
    1. **Religious Diversity Hotspots:**
       - Trincomalee, Puttalam, and Nuwara Eliya show highest religious diversity
       - These districts require the most nuanced interfaith approaches
    
    2. **Buddhist-Majority Strongholds:**
       - Southern and North Western provinces are predominantly Buddhist
       - Temple partnerships and Buddhist clergy engagement are crucial
    
    3. **Multi-Religious Provinces:**
       - Eastern Province requires balanced Muslim-Hindu-Buddhist outreach
       - Northern Province needs Hindu-Christian focused strategies
    
    4. **Strategic Priorities:**
       - Develop comprehensive strategies for all 25 districts
       - Focus on economic development and social services
       - Emphasize interfaith dialogue in diverse districts
       - Leverage religious festivals and observances for community engagement
    
    5. **Implementation Timeline:**
       - Phase 1 (2025-2026): Establish partnerships in key districts
       - Phase 2 (2027-2028): Scale successful models province-wide
       - Phase 3 (2029-2030): Comprehensive evaluation and electoral preparation
    """)