import streamlit as st
import pandas as pd
import plotly.express as px
import time

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Online Product Analysis Dashboard", layout="wide")

# ---- LOADING ----
with st.spinner("🚀 Loading Dashboard..."):
    time.sleep(1)

# ---- CSS ----
st.markdown("""
<style>
.stApp {background-color:#000; color:white;}

h1 {
    color:#E50914;
    text-align:center;
    font-size:50px;
    text-shadow:0px 0px 15px #E50914;
}

section[data-testid="stSidebar"] {
    background-color:#111;
}

/* Metrics */
[data-testid="metric-container"] {
    background: linear-gradient(145deg, #141414, #1c1c1c);
    border-radius: 15px;
    padding: 20px;
    box-shadow: 0px 0px 20px rgba(229,9,20,0.3);
    transition:0.3s;
}
[data-testid="metric-container"]:hover {
    transform:scale(1.05);
}

/* Section */
.section {
    background:#111;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 0px 15px rgba(229,9,20,0.2);
    margin-bottom:20px;
}
</style>
""", unsafe_allow_html=True)

# ---- TITLE ----
st.markdown("<h1> Online Product Analysis Dashboard</h1>", unsafe_allow_html=True)

# ---- LOAD DATA ----
df = pd.read_excel("output.xlsx")

# ---- CLEANING ----
df['discount'] = df['discount'].astype(str).str.replace('% off','',regex=False)
df['discount'] = pd.to_numeric(df['discount'], errors='coerce')

df['actual_price'] = pd.to_numeric(df['actual_price'].astype(str).str.replace(',',''), errors='coerce')
df['selling_price'] = pd.to_numeric(df['selling_price'].astype(str).str.replace(',',''), errors='coerce')

df['average_rating'] = pd.to_numeric(df['average_rating'], errors='coerce')

df.dropna(inplace=True)

df['discount_percent'] = ((df['actual_price'] - df['selling_price']) / df['actual_price']) * 100

df['price_category'] = pd.cut(df['selling_price'],
                             bins=[0,500,2000,10000],
                             labels=['Low','Medium','High'])

# ---- FILTER ----
category = st.sidebar.multiselect("Category", df['category'].unique(), default=df['category'].unique())

price_range = st.sidebar.slider("Price Range",
                               int(df['selling_price'].min()),
                               int(df['selling_price'].max()),
                               (100,5000))

search = st.sidebar.text_input("Search Product")

filtered_df = df[
    (df['category'].isin(category)) &
    (df['selling_price'] >= price_range[0]) &
    (df['selling_price'] <= price_range[1])
]

if search:
    filtered_df = filtered_df[
        filtered_df['title'].str.contains(search, case=False, na=False)
    ]

# ---- STYLE FUNCTION ----
def style_chart(fig):
    fig.update_layout(
        template="plotly_dark",
        plot_bgcolor="#0d0d0d",
        paper_bgcolor="#0d0d0d",

        font=dict(family="Arial Black", size=14, color="#FFFFFF"),

        xaxis=dict(
            title_font=dict(size=16, color="#00C6FF"),
            tickfont=dict(size=13, color="#CCCCCC"),
            tickangle=-30,
            showgrid=False
        ),

        yaxis=dict(
            title_font=dict(size=16, color="#00C6FF"),
            tickfont=dict(size=13, color="#CCCCCC"),
            gridcolor="#222"
        ),

        hoverlabel=dict(bgcolor="#E50914", font_size=14, font_color="white")
    )
    return fig

# ---- TABS ----
tab1, tab2, tab3 = st.tabs(["📊 Overview", "📂 Category", "🛍 Products"])

# ================= TAB 1 =================
with tab1:

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Products", len(filtered_df))
    col2.metric("Avg Price", f"₹ {round(filtered_df['selling_price'].mean(),2)}")
    col3.metric("Avg Rating", round(filtered_df['average_rating'].mean(),2))
    col4.metric("Avg Discount %", round(filtered_df['discount_percent'].mean(),2))

    st.markdown("### 💸 Price Distribution")
    fig1 = px.histogram(filtered_df, x="selling_price", color_discrete_sequence=["#FF3D00"])
    st.plotly_chart(style_chart(fig1), use_container_width=True)

    st.markdown("### ⭐ Rating vs Price")
    fig2 = px.scatter(filtered_df, x="selling_price", y="average_rating",
                      color="average_rating", color_continuous_scale="Turbo")
    st.plotly_chart(style_chart(fig2), use_container_width=True)

    st.markdown("### 🥧 Price Category")
    pie = filtered_df['price_category'].value_counts().reset_index()
    pie.columns=['category','count']
    fig3 = px.pie(pie, names='category', values='count', hole=0.4)
    st.plotly_chart(style_chart(fig3), use_container_width=True)

    st.markdown("### 🔥 Discount")
    fig4 = px.histogram(filtered_df, x="discount_percent", color_discrete_sequence=["#FF1744"])
    st.plotly_chart(style_chart(fig4), use_container_width=True)

# ================= TAB 2 =================
with tab2:

    st.markdown("### 📊 Avg Price by Category")
    fig5 = px.bar(df.groupby('category')['selling_price'].mean().reset_index(),
                  x='category', y='selling_price',
                  color='selling_price', text='selling_price')
    fig5.update_traces(textposition='outside')
    st.plotly_chart(style_chart(fig5), use_container_width=True)

    st.markdown("### ⭐ Avg Rating by Category")
    fig6 = px.bar(df.groupby('category')['average_rating'].mean().reset_index(),
                  x='category', y='average_rating',
                  color='average_rating', text='average_rating')
    fig6.update_traces(textposition='outside')
    st.plotly_chart(style_chart(fig6), use_container_width=True)

    st.markdown("### 📦 Category Distribution")
    cat = df['category'].value_counts().reset_index()
    cat.columns=['category','count']
    fig7 = px.pie(cat, names='category', values='count')
    st.plotly_chart(style_chart(fig7), use_container_width=True)

    st.markdown("### 📊 Price Variation")
    fig8 = px.box(df, x='category', y='selling_price')
    st.plotly_chart(style_chart(fig8), use_container_width=True)

# ================= TAB 3 =================
with tab3:

    st.markdown("### 🏷 Top Brands")
    brand = filtered_df['brand'].value_counts().head(10).reset_index()
    brand.columns=['brand','count']
    fig9 = px.bar(brand, x='brand', y='count',
                  color='count', text='count',
                  color_continuous_scale="Blues")
    fig9.update_traces(textposition='outside')
    st.plotly_chart(style_chart(fig9), use_container_width=True)

    st.markdown("### 💎 Expensive Products")
    fig10 = px.bar(df.sort_values(by='selling_price', ascending=False).head(10),
                   x='selling_price', y='title',
                   orientation='h', text='selling_price')
    st.plotly_chart(style_chart(fig10), use_container_width=True)

    st.markdown("### ⭐ Top Rated")
    fig11 = px.bar(df.sort_values(by='average_rating', ascending=False).head(10),
                   x='average_rating', y='title',
                   orientation='h', text='average_rating')
    st.plotly_chart(style_chart(fig11), use_container_width=True)

    st.markdown("### 🧩 Sub-category")
    fig12 = px.bar(df.groupby('sub_category')['selling_price'].mean().sort_values(ascending=False).head(10).reset_index(),
                   x='sub_category', y='selling_price',
                   text='selling_price')
    fig12.update_traces(textposition='outside')
    st.plotly_chart(style_chart(fig12), use_container_width=True)

# ---- TABLE ----
st.dataframe(filtered_df.head(50))