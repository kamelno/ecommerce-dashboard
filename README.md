📊 Real-Time E-commerce Analytics Dashboard
A professional, interactive, and real-time data analytics dashboard built for modern E-commerce tracking. This project demonstrates the integration of Data Engineering, OOP principles, and Live Data Visualization.

🚀 Key Features
Real-time KPI Tracking: Instant updates for Total Revenue, Order Count, and Average Order Value (AOV).

Live Sales Feed: A dynamic transaction table that updates as new "orders" are processed.

Categorical Analysis: Interactive Plotly charts showing sales distribution across different product categories.

Scalable Architecture: Built using Python Classes (OOP) to separate business logic from the UI layer.

🛠️ Technical Stack
Language: Python 3.13

Framework: Streamlit (For the Web Interface)

Visualization: Plotly Express (For interactive charts)

Data Handling: Pandas & NumPy

Deployment: Streamlit Cloud & GitHub

🏗️ Project Architecture (OOP Approach)
The project is structured into two main modules to ensure Clean Code and maintainability:

analytics.py: Contains the EcommerceAnalytics class, responsible for data generation, KPI calculations, and business logic.

app.py: Handles the frontend rendering, session state management, and real-time refresh loops.

📈 How to Run Locally
Clone the repository:

Bash
git clone https://github.com/YOUR_USERNAME/ecommerce-dashboard.git
Install dependencies:

Bash
pip install -r requirements.txt
Run the app:

Bash
streamlit run app.py
