# 🎬 Online Product Analysis Dashboard

An interactive and visually appealing **Streamlit dashboard** for analyzing online product prices, categories, ratings, and discounts.

---

## 🚀 Features

* 📊 Interactive data visualizations (Plotly)
* 🔍 Advanced filtering (category, price range, search)
* 🏷 Brand-wise analysis
* 📈 Category-wise insights
* 💸 Price & discount distribution
* ⭐ Rating vs Price comparison
* 📥 Download filtered dataset

---

## 🧠 Tech Stack

* Python
* Streamlit
* Pandas
* Plotly

---

# 📊 Dashboard Walkthrough

## 🔹 1. Overview Dashboard

👉 Shows key KPIs like total products, average price, rating, and discount with visual insights.

![Overview](Images/overview%201.jpeg)
![Overview](Images/overview%202.jpeg)

👉 Includes:

* Price Distribution Histogram
* Rating vs Price Scatter Plot
* Price Category Pie Chart

![Overview](Images/overview%203.jpeg)
![Overview](Images/overview%204.jpeg)

---

## 📂 2. Category Analysis

👉 Helps understand how different product categories perform.

![Category](Images/category%201.jpeg)
![Category](Images/category%202.jpeg)

👉 Includes:

* Avg Price by Category
* Avg Rating by Category

![Category](Images/category%203.jpeg)
![Category](Images/category%204.jpeg)

👉 Also includes:

* Category Distribution
* Price Variation (Box Plot)

---

## 🛍️ 3. Product Insights

👉 Focuses on brand performance and product-level trends.

![Products](Images/products%201.jpeg)
![Products](Images/products%202.jpeg)

👉 Includes:

* Top Brands Analysis
* Discount Distribution

![Products](Images/products%203.jpeg)
![Products](Images/products%204.jpeg)

👉 Also includes:

* Top Expensive Products
* Top Rated Products
* Sub-category Analysis

---

## ⚙️ Installation & Setup

1. Clone the repository:

```bash id="1a2b3c"
git clone https://github.com/TheTarunkumar/Online-Product-analysis.git
cd Online-Product-analysis
```

2. Install dependencies:

```bash id="4d5e6f"
pip install -r requirements.txt
```

3. Run the app:

```bash id="7g8h9i"
streamlit run app.py
```

---

## 📁 Project Structure

```id="j1k2l3"
Online-Product-analysis/
│── Images
│── Data.xlsx
│── README.md
│── app.py
│── online product price analysis.ipynb
```

---

## 🎯 Key Insights

* Mid-range products dominate the dataset
* High discounts don’t always mean high ratings
* Some brands consistently perform better
* Pricing varies significantly across categories

---

## 💡 Future Improvements

* 🌐 Deploy dashboard online
* 🤖 Add ML-based predictions
* 📊 Real-time API integration
* 📱 Mobile-friendly UI


